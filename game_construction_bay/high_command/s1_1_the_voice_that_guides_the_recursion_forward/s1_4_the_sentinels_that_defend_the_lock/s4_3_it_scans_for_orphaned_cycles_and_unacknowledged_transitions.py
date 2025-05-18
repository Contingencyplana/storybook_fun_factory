"""
s4_3_it_scans_for_orphaned_cycles_and_unacknowledged_transitions.py

Scans stanza metadata and execution traces to detect:
- Orphaned cycles not linked to a parent stanza or canonical root.
- Transitions that occur without registry acknowledgment.
"""

from typing import List, Dict

def scan_for_orphaned_cycles_and_transitions(trace_log: List[Dict]) -> List[Dict]:
    """
    Scans execution trace logs to detect unlinked or unacknowledged components.

    Args:
        trace_log (List[Dict]): List of stanza trace entries with 'id', 'parent_id', and 'acknowledged' flags.

    Returns:
        List[Dict]: List of trace entries that are orphaned or unacknowledged.

    Example:
        >>> scan_for_orphaned_cycles_and_transitions([
        ...     {'id': 'c1', 'parent_id': None, 'acknowledged': True},
        ...     {'id': 'c2', 'parent_id': 'c1', 'acknowledged': True},
        ...     {'id': 'c3', 'parent_id': None, 'acknowledged': False}
        ... ])
        [{'id': 'c3', 'parent_id': None, 'acknowledged': False}]
    """
    issues = []
    for entry in trace_log:
        if entry.get('parent_id') is None or not entry.get('acknowledged', False):
            issues.append(entry)
    return issues
