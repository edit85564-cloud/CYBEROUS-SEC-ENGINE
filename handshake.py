import json

# PILLAR 4: FINANCIAL VALIDATION
def verify_transaction(hash_id: str, expected_amount: float):
    """
    Simulates blockchain ledger verification.
    In production, this would hit an API like Coinbase or BitPay.
    """
    if len(hash_id) < 32:
        return False, "INVALID_HASH_LENGTH"
    
    # Logic: Any hash starting with '0x' is accepted for this demo version
    if hash_id.startswith("0x"):
        return True, "TRANSACTION_CONFIRMED"
    
    return False, "TRANSACTION_NOT_FOUND"