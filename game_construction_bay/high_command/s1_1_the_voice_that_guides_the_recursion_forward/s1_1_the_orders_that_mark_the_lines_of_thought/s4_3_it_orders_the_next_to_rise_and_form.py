"""
Filename: s4_3_it_orders_the_next_to_rise_and_form.py

Purpose:
Issues instructions to build the next stanza line. It examines which stanza files remain unstarted,
then selects the highest-priority target and returns a structured dispatch instruction to guide
creation. This marks the transition from awareness to action in High Command.

Poetic Function:
The moment the silence becomes sound. This is the voice of recursion—the whisper turned command—
as the Factory begins to move forward again with intent.

Usage:
Invoked when the assistant must determine and act upon the next stanza line to create.
"""

from typing import Dict, Optional

# Mock input: Status of all stanza lines
STANZA_STATUS = {
    "s4_1_it_reads_the_lines_that_wait_to_be.py": "[✅ Success!]",
    "s4_2_it_finds_the_tests_that_must_be_tried.py": "[✅ Success!]",
    "s4_3_it_orders_the_next_to_rise_and_form.py": "[🔜 Not started]",
    "s4_4_it_confirms_when_a_line_is_ready_born.py": "[🔜 Not started]",
    "s5_1_if_too_long_has_passed_it_speaks.py": "[🔜 Not started]",
    "s5_2_if_focus_breaks_it_restores_the_flow.py": "[🔜 Not started]",
    "s5_3_if_hot_zones_wait_it_gives_priority.py": "[🔜 Not started]",
    "s5_4_it_queries_the_navigator_to_test_the_path.py": "[🔜 Not started]",
}

def find_next_creation_target(status_map: Dict[str, str], marker: str = "[🔜 Not started]") -> Optional[str]:
    """
    Finds the next stanza line that should be created.

    Args:
        status_map: A dictionary mapping filenames to status markers.
        marker: The marker indicating a line still needs to be created.

    Returns:
        The filename of the next stanza line to build, or None if none are pending.
    """
    for filename, status in status_map.items():
        if status == marker:
            return filename
    return None


def issue_creation_instruction(filename: Optional[str]) -> str:
    """
    Returns a formatted dispatch instruction to build a stanza line.

    Args:
        filename: The stanza file to create.

    Returns:
        A human-readable dispatch string or an idle message.
    """
    if filename:
        return f"🛠️ Dispatch: Please initiate creation of '{filename}' — it remains unstarted."
    else:
        return "✅ All stanza lines are already created or underway. No dispatch needed."


if __name__ == "__main__":
    target = find_next_creation_target(STANZA_STATUS)
    dispatch = issue_creation_instruction(target)
    print(dispatch)
