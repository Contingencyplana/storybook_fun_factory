"""
Filename: s4_2_it_finds_the_tests_that_must_be_tried.py

Purpose:
Locates test files still marked [⏳ In progress], helping High Command identify what still
needs testing. Focuses on filenames that begin with "test_" and match the marker status.

Poetic Function:
The keen-eyed sentinel. It hunts for work not yet complete—finding tests that flicker
midway through the recursion.

Usage:
Used in Dispatch Logic to trigger pending tests across recursive stanza lines.
"""

from typing import List, Dict


# Example: Simulated status tracker (to be dynamically imported or queried later)
STANZA_STATUS = {
    "test_s4_1_it_reads_the_lines_that_wait_to_be.py": "[✅ Success!]",
    "test_s4_2_it_finds_the_tests_that_must_be_tried.py": "[✅ Success!]",
    "test_s4_3_it_orders_the_next_to_rise_and_form.py": "[✅ Success!]",
    "test_s4_4_it_confirms_when_a_line_is_ready_born.py": "[⏳ In progress]",
    "s4_4_it_confirms_when_a_line_is_ready_born.py": "[✅ Success!]",
    "s5_1_if_too_long_has_passed_it_speaks.py": "[🔜 Not started]",
}


def find_pending_tests(status_map: Dict[str, str], marker: str = "[⏳ In progress]") -> List[str]:
    """
    Returns a list of test filenames still marked as in progress.

    Args:
        status_map: A dictionary mapping filenames to status markers.
        marker: The status indicating a test is pending.

    Returns:
        A list of test files that need to be run or completed.
    """
    return [filename for filename, status in status_map.items()
            if filename.startswith("test_") and status == marker]


def print_pending_tests(pending: List[str]) -> None:
    """
    Prints the list of pending test files in a readable format.

    Args:
        pending: A list of test filenames needing attention.
    """
    if not pending:
        print("✅ All tests have either passed or are not marked as in progress.")
    else:
        print("🔍 The following test files are still in progress:\n")
        for line in pending:
            print(f" • {line}")


if __name__ == "__main__":
    pending_tests = find_pending_tests(STANZA_STATUS)
    print_pending_tests(pending_tests)
