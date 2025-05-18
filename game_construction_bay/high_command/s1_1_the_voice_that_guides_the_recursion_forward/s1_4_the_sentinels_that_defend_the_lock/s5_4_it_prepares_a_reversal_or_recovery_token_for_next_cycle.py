"""
s5_4_it_prepares_a_reversal_or_recovery_token_for_next_cycle.py

Generates recovery tokens used by Cycle 3: lockdown_reversion_and_repair/.
These tokens define the rollback, re-entry point, and memory hints for recursive repair.
"""

from typing import Dict, Any
import uuid
from datetime import datetime, timezone

def prepare_recovery_token(anomaly_id: str, stanza_id: str, strategy: str = "rollback") -> Dict[str, Any]:
    """
    Prepares a structured token used for recovery in the next Cycle.

    Args:
        anomaly_id (str): The ID of the anomaly this token responds to.
        stanza_id (str): The stanza that will be subject to rollback or repair.
        strategy (str): Strategy type ("rollback", "rebuild", or "pause").

    Returns:
        Dict[str, Any]: A token object with metadata for recovery action.

    Example:
        >>> prepare_recovery_token("anom123", "s4_1")
        {'token_id': '...', 'anomaly_id': 'anom123', 'stanza_id': 's4_1', 'strategy': 'rollback', ...}
    """
    if strategy not in {"rollback", "rebuild", "pause"}:
        raise ValueError(f"Invalid recovery strategy: {strategy}")

    return {
        "token_id": str(uuid.uuid4()),
        "anomaly_id": anomaly_id,
        "stanza_id": stanza_id,
        "strategy": strategy,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "next_cycle": "lockdown_reversion_and_repair"
    }
