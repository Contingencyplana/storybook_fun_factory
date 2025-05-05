"""
Filename: s1_2_it_recites_the_focus_in_shifted_light.py

📜 See GDJ 5.8: May 6 – The Genesis Command
(Second line of Stanza 1 in the Layer 5 Genesis Cycle of high_command)

Purpose:
Provides a structured diagnostic of the current recursive focus,
using the active front data and summarizing the player's or assistant’s
point of engagement during major operations.

It is not concerned with dispatch or orchestration—only reflection.
"""

from pathlib import Path
import json

# 🔖 Shared memory location from previous stanza line
ACTIVE_FRONT_PATH = Path(__file__).parent / "active_front.json"

def recite_active_focus(verbose: bool = True) -> str:
    """
    Summarizes the current active recursive focus.
    Returns a human-readable string suitable for logging or CLI.

    Args:
        verbose (bool): Whether to print the output immediately.

    Returns:
        str: Summary report of the active recursive front.
    """
    if not ACTIVE_FRONT_PATH.exists():
        summary = "🔕 No active recursive front has been marked yet."
        if verbose:
            print(summary)
        return summary

    with ACTIVE_FRONT_PATH.open("r", encoding="utf-8") as f:
        front = json.load(f)

    summary = (
        f"🧠 RECURSIVE FOCUS SUMMARY\n"
        f"──────────────────────────────\n"
        f"🧩 Component: {front.get('component', '[Unknown]')}\n"
        f"📂 Stanza:    {front.get('stanza', '[Unknown]')}\n"
        f"📄 File:      {front.get('line', '[Unknown]')}\n"
    )

    if front.get("gdj"):
        summary += f"📜 GDJ Ref:   {front['gdj']}\n"

    if verbose:
        print(summary)

    return summary

# Optional CLI usage
if __name__ == "__main__":
    recite_active_focus(verbose=True)
