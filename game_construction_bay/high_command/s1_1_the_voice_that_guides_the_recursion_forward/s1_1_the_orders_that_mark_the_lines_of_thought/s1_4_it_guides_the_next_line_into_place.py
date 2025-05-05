"""
Filename: s1_4_it_guides_the_next_line_into_place.py

📜 See GDJ 5.8: May 6 – The Genesis Command
(Final line of Stanza 1 in the Layer 5 Genesis Cycle of high_command)

Purpose:
Infers the next stanza line the assistant or user is likely to move to—
based on the last known active front and recent trace history.

This enables recursive continuity, assists in restructure pacing,
and enables High Command to recommend the next action contextually.
"""

from pathlib import Path
import json
from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s1_1_it_marks_the_front_but_moves_unseen as marker,
    s1_3_it_traces_the_path_in_stanza_form as tracer
)

def suggest_next_target():
    """
    Suggests the next stanza line to move to,
    based on trace history and active front data.

    Returns:
        dict: Proposed next target or empty dict if unknown.
    """
    front = marker.get_active_front()
    traces = tracer.get_recent_traces(limit=3)

    if not front:
        return {"reason": "No active front currently marked."}

    if not traces:
        return {
            "reason": "No prior stanza path trace found. Defaulting to next file in current stanza.",
            "suggested": _suggest_next_by_filename(front["line"])
        }

    last_file = front["line"]
    next_guess = _suggest_next_by_filename(last_file)

    return {
        "reason": "Inferred from active front filename.",
        "suggested": next_guess
    }

def _suggest_next_by_filename(current_filename: str):
    """
    Very naive filename-based suggestion.
    Assumes standard format like: _2_3_filename.py → _2_4_...

    Args:
        current_filename (str): The currently active file.

    Returns:
        str: The guessed next file name.
    """
    parts = current_filename.split("_")
    if len(parts) < 3:
        return "unknown_filename_format.py"

    try:
        stanza_num = int(parts[1])
        next_stanza_num = stanza_num + 1
        new_parts = parts[:1] + [str(next_stanza_num)] + parts[2:]
        return "_".join(new_parts)
    except ValueError:
        return "unparseable_filename_increment.py"

# Optional CLI usage
if __name__ == "__main__":
    suggestion = suggest_next_target()
    print("📈 Next Target Suggestion")
    print(json.dumps(suggestion, indent=2))
