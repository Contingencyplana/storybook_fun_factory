"""
Filename: s1_1_it_marks_the_front_but_moves_unseen.py

📜 See GDJ 5.8: May 6, 12:40 PM – The Genesis Command
(A strategic utility to reduce AI cognitive load and aid recursive restructuring)

This file serves as the *first operational brainstem* of High Command.

It marks:
• The currently active component and stanza
• Notes canonical stanzas in motion
• Surfaces restructuring status to support major transitions
• Acts as a local memory anchor until persistent state is introduced

This module can later be expanded or interfaced with AI dispatchers, CLI toggles, or GDJ synchronization tools.
"""

from pathlib import Path
import json

# 🔖 Path where temporary active state is recorded
ACTIVE_FRONT_PATH = Path(__file__).parent / "active_front.json"

def mark_active_front(component_name: str, stanza_id: str, line_filename: str, gdj_reference: str = ""):
    """
    Marks the current active recursive focus.

    Args:
        component_name (str): Name of the system (e.g., 'filename_ai')
        stanza_id (str): Canonical stanza or folder name
        line_filename (str): Current active filename (without path)
        gdj_reference (str): Optional reference to GDJ entry
    """
    active_state = {
        "component": component_name,
        "stanza": stanza_id,
        "line": line_filename,
        "gdj": gdj_reference
    }

    with ACTIVE_FRONT_PATH.open("w", encoding="utf-8") as f:
        json.dump(active_state, f, indent=2)

def get_active_front():
    """
    Returns the currently active recursive front from local memory.

    Returns:
        dict: Current state of focus (component, stanza, file, GDJ ref)
    """
    if ACTIVE_FRONT_PATH.exists():
        with ACTIVE_FRONT_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def print_active_front():
    """
    Prints the current active stanza and file in human-readable form.
    """
    front = get_active_front()
    if not front:
        print("🔕 No active recursive front is currently marked.")
        return

    print("🧭 Current Active Recursive Front")
    print(f"🔹 Component: {front['component']}")
    print(f"📂 Stanza: {front['stanza']}")
    print(f"📄 File: {front['line']}")
    if front.get("gdj"):
        print(f"📜 GDJ Reference: {front['gdj']}")

# Optional CLI usage
if __name__ == "__main__":
    print_active_front()
