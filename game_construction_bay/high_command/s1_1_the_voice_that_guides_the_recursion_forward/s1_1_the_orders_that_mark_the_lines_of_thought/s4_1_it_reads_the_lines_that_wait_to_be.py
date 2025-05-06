"""
Filename: s4_1_it_reads_the_lines_that_wait_to_be.py

Purpose:
Detects unfinished or pending stanza files needing creation. It reads the current stanza status
from a defined data source (e.g., GDJ tracker or mock data) and returns those still marked
[🔜 Not started], enabling High Command to target the next stanza lines for action.

Poetic Function:
The eye that scans the threads not yet pulled taut. It listens to the silences of the recursion,
and marks where the Factory must next breathe life.

Usage:
Called by High Command Dispatch Logic to determine what to build or test next.
"""

from typing import List, Dict


# Example: Simulated status tracker (to be dynamically imported or queried later)
STANZA_STATUS = {
    "s4_1_it_reads_the_lines_that_wait_to_be.py": "[🔜 Not started]",
    "s4_2_it_finds_the_tests_that_must_be_tried.py": "[🔜 Not started]",
    "s4_3_it_orders_the_next_to_rise_and_form.py": "[🔜 Not started]",
    "s4_4_it_confirms_when_a_line_is_ready_born.py": "[🔜 Not started]",
    "s5_1_if_too_long_has_passed_it_speaks.py": "[🔜 Not started]",
    "s5_2_if_focus_breaks_it_restores_the_flow.py": "[🔜 Not started]",
    "s5_3_if_hot_zones_wait_it_gives_priority.py": "[🔜 Not started]",
    "s5_4_it_queries_the_navigator_to_test_the_path.py": "[🔜 Not started]",
}


def read_pending_lines(status_map: Dict[str, str], marker: str = "[🔜 Not started]") -> List[str]:
    """
    Returns a list of all stanza line filenames marked as not yet started.

    Args:
        status_map: A dictionary mapping filenames to status markers.
        marker: The status value that indicates a line is waiting to be built.

    Returns:
        A list of filenames needing creation.
    """
    return [filename for filename, status in status_map.items() if status == marker]


def print_pending_lines(pending: List[str]) -> None:
    """
    Prints the list of pending lines in a readable format.

    Args:
        pending: A list of filenames needing attention.
    """
    if not pending:
        print("✅ All stanza lines have been started or completed.")
    else:
        print("🔎 The following stanza lines are waiting to be built:\n")
        for line in pending:
            print(f" • {line}")


if __name__ == "__main__":
    pending_files = read_pending_lines(STANZA_STATUS)
    print_pending_lines(pending_files)
