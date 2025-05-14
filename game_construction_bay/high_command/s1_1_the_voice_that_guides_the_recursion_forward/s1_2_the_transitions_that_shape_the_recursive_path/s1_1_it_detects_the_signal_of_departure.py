"""
Filename: s1_1_it_detects_the_signal_of_departure.py

Detects the signal that a stanza, component, or Cycle is about to yield control or transition its logic.
This module serves as the first checkpoint in the recursive handover protocol.

Usage Example:
>>> signal = detect_departure_signal({'status': 'ready_to_depart', 'trace_id': 'abc123'})
>>> assert signal is True
"""

from typing import Dict

def detect_departure_signal(context: Dict) -> bool:
    """
    Detects whether a recursive zone is ready to initiate a handoff.
    Looks for specific status keys and handoff markers.

    Args:
        context (Dict): The context dictionary containing current stanza/component state.

    Returns:
        bool: True if a departure signal is detected, False otherwise.
    """
    return context.get("status") == "ready_to_depart" and "trace_id" in context
