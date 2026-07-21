#!/bin/bash

# ============================================================
# ADAS AI Lab -- Deploy lab files to all kit Pis
# Usage: ./deploy_to_kits.sh
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
KITS_FILE="$SCRIPT_DIR/kits.txt"
LAB_DIR="$BASE_DIR/lab"
SMARTCAR_DIR="$BASE_DIR/mySmartCar"
PYTHON_DIR="$BASE_DIR/mypython"
PI_USER="pi"
PI_PASS="yahboom"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # no color

# ============================================================
# Pre-flight checks
# ============================================================
echo ""
echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}  ADAS AI Lab -- Kit Deployment Script${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""

# Check required tools are installed
MISSING_TOOLS=()
for tool in sshpass rsync curl ping; do
    command -v "$tool" > /dev/null 2>&1 || MISSING_TOOLS+=("$tool")
done
if [ ${#MISSING_TOOLS[@]} -gt 0 ]; then
    echo -e "${RED}ERROR: Missing required tools: ${MISSING_TOOLS[*]}${NC}"
    echo "Install them (e.g. 'brew install sshpass rsync') before running this script."
    exit 1
fi

# Check kits file exists
if [ ! -f "$KITS_FILE" ]; then
    echo -e "${RED}ERROR: kits.txt not found at $KITS_FILE${NC}"
    echo "Copy kits.txt.example to kits.txt in the same folder and fill in your kit names/IPs."
    exit 1
fi

# Check source folders exist
for dir in "$LAB_DIR" "$SMARTCAR_DIR" "$PYTHON_DIR"; do
    if [ ! -d "$dir" ]; then
        echo -e "${RED}ERROR: Folder not found: $dir${NC}"
        exit 1
    fi
done

# Get MacBook IP (used as the Ollama host address the kits will call back to)
OLLAMA_HOST=$(ipconfig getifaddr en0 2>/dev/null)
if [ -z "$OLLAMA_HOST" ]; then
    echo -e "${RED}ERROR: Could not get MacBook IP. Are you on the right network?${NC}"
    exit 1
fi
echo -e "MacBook IP: ${GREEN}$OLLAMA_HOST${NC}"

# Check Ollama is running
OLLAMA_STATUS=$(curl -s --max-time 3 "http://$OLLAMA_HOST:11434" 2>/dev/null)
if [[ "$OLLAMA_STATUS" == *"running"* ]]; then
    echo -e "Ollama:     ${GREEN}running${NC}"
else
    echo -e "Ollama:     ${RED}NOT RUNNING -- start Ollama before deploying${NC}"
    echo ""
    read -p "Continue anyway? (y/n): " confirm
    if [ "$confirm" != "y" ]; then
        exit 1
    fi
fi

echo ""
echo -e "${BLUE}Source folders:${NC}"
echo "  Lab:      $LAB_DIR"
echo "  SmartCar: $SMARTCAR_DIR → ncssm-smartcar"
echo "  Python:   $PYTHON_DIR → ncssm-python"
echo ""
echo -e "${BLUE}Kits to deploy:${NC}"
cat "$KITS_FILE"
echo ""
read -p "Deploy to all kits? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "Cancelled."
    exit 0
fi

# ============================================================
# Deploy to each kit
# ============================================================
echo ""
PASS_COUNT=0
FAIL_COUNT=0
declare -A KIT_STATUS

while IFS=' ' read -r kit_name kit_ip; do
    # skip empty lines and comments
    [[ -z "$kit_name" || "$kit_name" == \#* ]] && continue

    echo -e "${BLUE}------------------------------------------------------------${NC}"
    echo -e "${BLUE}  $kit_name  |  $kit_ip${NC}"
    echo -e "${BLUE}------------------------------------------------------------${NC}"

    KIT_ERRORS=0

    # -- Ping check --
    echo -n "  Ping...                "
    if ping -c 1 -W 2 "$kit_ip" > /dev/null 2>&1; then
        echo -e "${GREEN}OK${NC}"
    else
        echo -e "${RED}FAIL -- skipping this kit${NC}"
        KIT_STATUS[$kit_name]="FAIL (unreachable)"
        FAIL_COUNT=$((FAIL_COUNT + 1))
        echo ""
        continue
    fi

    # -- SSH check --
    echo -n "  SSH...                 "
    SSH_TEST=$(sshpass -p "$PI_PASS" ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "$PI_USER@$kit_ip" "echo OK" 2>/dev/null)
    if [ "$SSH_TEST" == "OK" ]; then
        echo -e "${GREEN}OK${NC}"
    else
        echo -e "${RED}FAIL -- check SSH and password${NC}"
        KIT_STATUS[$kit_name]="FAIL (SSH failed)"
        FAIL_COUNT=$((FAIL_COUNT + 1))
        echo ""
        continue
    fi

    # -- Update OLLAMA_HOST in ai_driver.py --
    echo -n "  Updating Ollama IP...  "
    sed -i '' "s|OLLAMA_HOST = os.environ.get.*|OLLAMA_HOST = os.environ.get('OLLAMA_HOST', '$OLLAMA_HOST')|" "$LAB_DIR/ai_driver.py" 2>/dev/null
    echo -e "${GREEN}$OLLAMA_HOST${NC}"

    # -- Transfer ncssm-lab --
    echo -n "  Transferring lab...    "
    sshpass -p "$PI_PASS" rsync -az --delete \
        -e "ssh -o StrictHostKeyChecking=no" \
        "$LAB_DIR/" "$PI_USER@$kit_ip:~/ncssm-lab/" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}OK${NC}"
    else
        echo -e "${RED}FAIL${NC}"
        KIT_ERRORS=$((KIT_ERRORS + 1))
    fi

    # -- Transfer ncssm-smartcar --
    echo -n "  Transferring smartcar  "
    sshpass -p "$PI_PASS" rsync -az --delete \
        -e "ssh -o StrictHostKeyChecking=no" \
        "$SMARTCAR_DIR/" "$PI_USER@$kit_ip:~/ncssm-smartcar/" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}OK${NC}"
    else
        echo -e "${RED}FAIL${NC}"
        KIT_ERRORS=$((KIT_ERRORS + 1))
    fi

    # -- Transfer ncssm-python --
    echo -n "  Transferring python... "
    sshpass -p "$PI_PASS" rsync -az --delete \
        -e "ssh -o StrictHostKeyChecking=no" \
        "$PYTHON_DIR/" "$PI_USER@$kit_ip:~/ncssm-python/" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}OK${NC}"
    else
        echo -e "${RED}FAIL${NC}"
        KIT_ERRORS=$((KIT_ERRORS + 1))
    fi

    # -- Ollama connectivity test from Pi --
    echo -n "  Ollama from Pi...      "
    OLLAMA_TEST=$(sshpass -p "$PI_PASS" ssh -o StrictHostKeyChecking=no "$PI_USER@$kit_ip" \
        "curl -s --max-time 5 http://$OLLAMA_HOST:11434" 2>/dev/null)
    if [[ "$OLLAMA_TEST" == *"running"* ]]; then
        echo -e "${GREEN}OK${NC}"
    else
        echo -e "${RED}FAIL -- Pi cannot reach Ollama${NC}"
        KIT_ERRORS=$((KIT_ERRORS + 1))
    fi

    # -- Jupyter check --
    echo -n "  Jupyter...             "
    JUPYTER_TEST=$(sshpass -p "$PI_PASS" ssh -o StrictHostKeyChecking=no "$PI_USER@$kit_ip" \
        "curl -s --max-time 5 http://localhost:8888" 2>/dev/null)
    if [[ "$JUPYTER_TEST" == *"jupyter"* ]] || [[ "$JUPYTER_TEST" == *"Jupyter"* ]]; then
        echo -e "${GREEN}running${NC}"
    else
        echo -e "${YELLOW}not running -- starting${NC}"
        sshpass -p "$PI_PASS" ssh -o StrictHostKeyChecking=no "$PI_USER@$kit_ip" \
            "nohup jupyter lab --ip=0.0.0.0 --no-browser > /tmp/jupyter.log 2>&1 &" 2>/dev/null
        sleep 3
        echo -e "  Jupyter started"
    fi

    # -- Kit summary --
    echo ""
    if [ $KIT_ERRORS -eq 0 ]; then
        echo -e "  ${GREEN}✓ $kit_name PASS${NC}"
        KIT_STATUS[$kit_name]="PASS"
        PASS_COUNT=$((PASS_COUNT + 1))
    else
        echo -e "  ${RED}✗ $kit_name FAIL ($KIT_ERRORS errors)${NC}"
        KIT_STATUS[$kit_name]="FAIL ($KIT_ERRORS errors)"
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
    echo ""

done < "$KITS_FILE"

# ============================================================
# Summary report
# ============================================================
echo -e "${BLUE}============================================================${NC}"
echo -e "${BLUE}  DEPLOYMENT SUMMARY${NC}"
echo -e "${BLUE}============================================================${NC}"
echo ""
while IFS=' ' read -r kit_name kit_ip; do
    [[ -z "$kit_name" || "$kit_name" == \#* ]] && continue
    STATUS="${KIT_STATUS[$kit_name]}"
    if [[ "$STATUS" == "PASS" ]]; then
        echo -e "  ${GREEN}✓${NC}  $kit_name  ($kit_ip)  --  ${GREEN}$STATUS${NC}"
    else
        echo -e "  ${RED}✗${NC}  $kit_name  ($kit_ip)  --  ${RED}$STATUS${NC}"
    fi
done < "$KITS_FILE"
echo ""
echo -e "  Passed: ${GREEN}$PASS_COUNT${NC}   Failed: ${RED}$FAIL_COUNT${NC}"
echo ""

if [ $FAIL_COUNT -gt 0 ]; then
    echo -e "${YELLOW}Some kits failed. Resolve issues before camp starts.${NC}"
else
    echo -e "${GREEN}All kits deployed successfully. Ready for camp.${NC}"
fi
echo ""
