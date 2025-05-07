"""
Filename: s4_2_it_finds_the_tests_that_must_be_tried.py

Purpose:
Locates test files still missing or marked [⏳ In progress]. This line reads a stanza status tracker
and filters for test-related files that have not been completed, helping High Command prioritize
test generation or finalization during dispatch.

Poetic Function:
The seeker of unfinished trials. It watches for tests left mid-run, mid-born, or never written—
and urges them forward into completeness.

Usage:
Invoked by Dispatch Logic to determine which tests should be issued next.
"""

from typing import List, Dict


def find_pending_tests(status_map: Dict[str, str], marker: str = "[⏳ In progress]") -> List[str]:
    """
    Returns a list of all test file names marked as pending or incomplete.

    Args:
        status_map: A dictionary mapping filenames to status markers.
        marker: The status value indicating a test file is not complete.

    Returns:
        A list of filenames (likely tests) needing attention.
    """
    return [filename for filename, status in status_map.items() if "test_" in filename and status == marker]


def print_pending_tests(pending: List[str]) -> None:
    """
    Nicely prints a list of test files that need to be completed.

    Args:
        pending: A list of test file names that are incomplete.
    """
    if not pending:
        print("✅ All test files are complete or have already passed.")
    else:
        print("🧪 The following test files are pending or in progress:\n")
        for test_file in pending:
            print(f" • {test_file}")


if __name__ == "__main__":
    # Mock data for demonstration or debugging
    STANZA_TEST_STATUS = {
        "tes_s4_1_it_reads_the_lines_that_wait_to_be.py": "[✅ Success!]",
        "test_s4_2_it_finds_the_tests_that_must_be_tried.py": "[⏳ In progress]",
        "test_s4_3_it_orders_the_next_to_rise_and_form.py": "[🔜 Not started]",
        test_s4_4_it_confirms_when_a_line_is_ready_born.py": "[⏳ In progress]",
        "test_s5_1_if_too_long_has_passed_it_speaks.py": "[✅ Success!]",
        "test_s5_2_if_focus_breaks_it_restores_the_flow.py": "[🔜 Not started]",
    }

   pending_tests = find_pending_tests(STANZA_TEST_STATUS)
    print_pending_tests(pending_tests)
