"""
Filename: s1_3_it_relinks_the_arrival_and_canon_trace.py

Reestablishes the canonical trace between the origin and destination of a recursive handoff.
This module ensures the continuity of lineage during stanza or component transitions.

Usage Example:
>>> context = {
>>>     "source_id": "abc123",
>>>     "destination_id": "def456",
>>>     "canon_log": []
>>> }
>>> result = relink_canon_trace(context)
>>> assert result["trace_established"] is True
>>> assert "abc123 -> def456" in result["canon_log"]
"""

from typing import Dict

def relink_canon_trace(context: Dict) -> Dict:
    """
    Reconnects the source and destination in a canonical trace log.

    Args:
        context (Dict): A dictionary containing 'source_id', 'destination_id', and 'canon_log'.

    Returns:
        Dict: Updated context with trace recorded and a flag for success.
    """
    source = context.get("source_id")
    destination = context.get("destination_id")
    log = context.get("canon_log", [])

    if source and destination:
        entry = f"{source} -> {destination}"
        log.append(entry)
        return {"trace_established": True, "canon_log": log}
    
    return {"trace_established": False, "canon_log": log}
