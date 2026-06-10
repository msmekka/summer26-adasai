import requests
import json

# ═══════════════════════════════════════
#   SET THIS TO INSTRUCTOR PROVIDED IP
OLLAMA_HOST = "192.168.4.xx"   # change to instructor provided IP
OLLAMA_PORT = 11434
MODEL       = "phi3:mini"
# ═══════════════════════════════════════

def ask(prompt, host=OLLAMA_HOST):
    """Send a prompt to Ollama and return the response text."""
    try:
        response = requests.post(
            f"http://{host}:{OLLAMA_PORT}/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=10
        )
        return response.json()["response"]
    except Exception as e:
        return f"ERROR: Could not reach AI server -- {str(e)}"

def decide(observation):
    """Given an observation about what the robot sees, get a driving decision."""
    prompt = f"""You are the AI brain of a small robot car in a classroom.
    
The robot's camera reports: {observation}

Respond with ONLY one of these exact words: FORWARD, LEFT, RIGHT, STOP
No explanation, just the single word decision."""
    
    return ask(prompt).strip().upper 
