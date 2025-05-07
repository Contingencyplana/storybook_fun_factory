"""
Filename: s4_4_it_confirms_when_a_line_is_ready_born.py

Purpose:
Determines whether a stanza line is ready to be marked as complete and canon-ready.
It validates success markers in a stanza status map, checking that each stanza line meets 
completion criteria (e.g., "[✅ Success!]"). This enables High Command to certify progress 
and confirm milestones before dispatching further creation or testing.

Poetic Function:
The witness of fulfillment—it sees the thread now woven tight, the stanza's shape fully formed.
It knows when silence has turned to song, and names the moment a line becomes real.

Usage:
Called by Dispatch Logic to verify file readiness prior to closing a stanza or escalating logic.
"""

from typing import Dict, List


def get_ready_lines(status_map: Dict[str, str], marker: str = "[✅ Success!]") -> List[str]:
    """
    Returns a list of stanza line filenames marked as successfully completed.

    Args:
        status_map: A dictionary mapping filenames to status markers.
        marker: The marker that signifies successful completion.

    Returns:
        A list of stanza line filenames that are ready (canon-ready).
    """
    return [filename for filename, status in status_map.items() if status == marker]


def all_lines_ready(status_map: Dict[str, str], marker: str = "[✅ Success!]") -> bool:
    """
    Determines whether all stanza lines are marked as complete.

    Args:
        status_map: A dictionary mapping filenames to status markers.
        marker: The status marker that indicates completion.

    Returns:
        True if all lines are complete, False otherwise.
    """
    return all(status == marker for status in status_map.values())


def print_ready_status(status_map: Dict[str, str], marker: str = "[✅ Success!]") -> None:
    """
    Prints a summary of which stanza lines are ready and whether all are complete.

    Args:
        status_map: The dictionary of stanza lines and their statuses.
        marker: The marker used to denote success.
    """
    ready_lines = get_ready_lines(status_map, marker)
    print("✅ Ready Stanza Lines:")
    for line in ready_lines:
        print(f" • {line}")

    if all_lines_ready(status_map, marker):
        print("\n🎉 All lines are canon-ready! The stanza may be marked complete.")
    else:
        print("\n⏳ Some lines are still in progress or pending.")
