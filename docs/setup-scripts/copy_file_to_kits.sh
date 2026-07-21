#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILE=$1
DEST=${2:-/home/pi/}
USER=pi
KITS_FILE="$SCRIPT_DIR/kits.txt"

if [ -z "$FILE" ]; then
    echo "Usage: $0 <file> [destination]"
    exit 1
fi

if [ ! -f "$KITS_FILE" ]; then
    echo "ERROR: kits.txt not found at $KITS_FILE"
    echo "Copy kits.txt.example to kits.txt in the same folder and fill in your kit names/IPs."
    exit 1
fi

while IFS=' ' read -r kit_name kit_ip; do
    [[ -z "$kit_name" || "$kit_name" == \#* ]] && continue
    echo "Copying to $kit_name ($kit_ip)..."
    scp "$FILE" "$USER@$kit_ip:$DEST"
    if [ $? -eq 0 ]; then
        echo "  OK"
    else
        echo "  FAILED"
    fi
done < "$KITS_FILE"
