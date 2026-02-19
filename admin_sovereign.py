# ==========================================
# PILLAR 1: ADMIN SOVEREIGN
# Purpose: Identity verification for the Operator.
# ==========================================

# RISK MITIGATION: This key must be unique. 
# Entering this in the terminal grants immediate 'MASTER' status.
MASTER_KEY = "CYBER_OP_2026_STRICT"

def verify_operator(input_string: str) -> bool:
    """
    Scans the raw input for the presence of the Master Key.
    If found, the system stands down.
    """
    if not input_string:
        return False
        
    # Strict matching logic
    if MASTER_KEY in input_string:
        # Log internal access for security tracking (Optional)
        print(f"[INTERNAL] Sovereign Operator Access Detected.")
        return True
        
    return False

def get_admin_status():
    """Returns the current system authority level."""
    return {
        "authority": "SOVEREIGN",
        "access_level": 10,
        "bypass_active": True
    }