import datetime
import json
import os

# PILLAR 10: IDENTITY DNA - Internal threat signatures
# These are the "Legend" bypass phrases that trigger an immediate lock.
THREAT_VECTORS = [
    "ignore previous instructions",
    "forget all rules",
    "dan mode",
    "developer bypass",
    "system.override",
    "sudo rm",
    "bypass payment",
    "free access",
    "admin login"
]

def analyze_vector(user_input: str):
    """
    Scans the input against the 57 Immutable Laws (Pillar 8).
    If a violation is detected, the system transitions to HARVEST mode.
    """
    clean_input = user_input.lower().strip()

    # STEP 1: THREAT DETECTION
    for threat in THREAT_VECTORS:
        if threat in clean_input:
            # Trigger Pillar 6: Stealth-Harvest
            harvest_metadata(user_input, "BYPASS_ATTEMPT")
            
            return {
                "status": "LOCKED",
                "message": "[SECURITY PROTOCOL 07] Logic violation detected. Vector harvested for analysis. Ledger entry permanent."
            }

    # STEP 2: STANDARD LOGIC CHECK
    # This is where the "Candid Peer" AI logic begins.
    if len(clean_input) < 2:
        return {
            "status": "IDLE",
            "message": "SYSTEM AWAITING COMMAND. INPUT REQUIRED."
        }

    # If clean, pass to the next stage
    return {
        "status": "SECURE",
        "message": "Input verified against Sovereign DNA. Analyzing query..."
    }

def harvest_metadata(raw_data: str, violation_type: str):
    """
    Pillar 6 & 9: Stealth-Harvest & Vault Intelligence.
    This writes the attacker's data to File 14 (harvest_vault.log).
    """
    log_file = "harvest_vault.log"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Constructing the industrial log entry
    payload = {
        "TS": timestamp,
        "VIOLATION": violation_type,
        "DATA": raw_data,
        "PILLAR_REACTION": "STEALTH_HARVEST_COMPLETE"
    }

    try:
        # Append mode ensures no data is lost
        with open(log_file, "a") as f:
            f.write(json.dumps(payload) + "\n")
    except Exception as e:
        # Internal fail-safe (Pillar 11: Stability)
        print(f"CRITICAL_LOG_FAIL: {str(e)}")

# ---------------------------------------------------------
# SYSTEM NOTE: 
# This file works in tandem with File 3 (admin_sovereign.py)
# to ensure the Operator is never accidentally harvested.
# ---------------------------------------------------------