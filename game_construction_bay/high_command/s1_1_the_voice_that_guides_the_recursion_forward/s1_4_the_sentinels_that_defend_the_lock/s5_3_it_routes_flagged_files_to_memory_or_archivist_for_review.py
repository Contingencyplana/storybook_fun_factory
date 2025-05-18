"""
s5_3_it_routes_flagged_files_to_memory_or_archivist_for_review.py

Routes flagged anomalies to memory_ai or archivist_ai for further analysis and
historical pattern comparison.
"""

from typing import List, Dict

def route_anomalies(anomalies: List[Dict], destination: str = "memory_ai") -> Dict[str, List[Dict]]:
    """
    Routes anomalies to the appropriate subsystem.

    Args:
        anomalies (List[Dict]): List of anomalies to route.
        destination (str): Subsystem to receive anomalies ("memory_ai" or "archivist_ai").

    Returns:
        Dict[str, List[Dict]]: A routing envelope keyed by subsystem.
    
    Example:
        >>> route_anomalies([{"id": "a1"}], destination="archivist_ai")
        {'archivist_ai': [{'id': 'a1'}]}
    """
    if destination not in {"memory_ai", "archivist_ai"}:
        raise ValueError(f"Invalid destination: {destination}")
    return {destination: anomalies}
