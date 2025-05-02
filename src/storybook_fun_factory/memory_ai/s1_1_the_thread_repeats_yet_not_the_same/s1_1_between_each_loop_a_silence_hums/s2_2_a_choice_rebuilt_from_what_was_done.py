"""
Filename: s2_2_a_choice_rebuilt_from_what_was_done.py

Reconstructs prior choices based on stored memory traces, enabling contextual
adaptation and recursive learning. This Line attempts to reverse-engineer
decision-making logic from historical actions and match it against known templates.
"""

from pathlib import Path
from typing import List, Dict, Optional
import json
import datetime

# Shared trace path from _1_1 and _2_1
TRACE_DIR = Path.cwd() / "memory_ai" / "memory_chain" / "trace_logs"
TRACE_FILE = TRACE_DIR / "recursion_signatures.json"

# Ensure directory exists
TRACE_DIR.mkdir(parents=True, exist_ok=True)

def load_past_choices() -> List[Dict]:
    """Loads previously stored memory events."""
    if TRACE_FILE.exists():
        try:
            with open(TRACE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def reconstruct_choices_by_action_chain(
    required_actions: List[str],
    tolerance: int = 0
) -> List[List[Dict]]:
    """
    Attempts to find sequences of past actions that match a known chain,
    within an optional tolerance (skipped or intervening actions).
    """
    traces = load_past_choices()
    reconstructions = []
    buffer = []
    idx = 0

    for trace in traces:
        action = trace.get("action")
        if not action:
            continue

        if action == required_actions[idx]:
            buffer.append(trace)
            idx += 1
            if idx == len(required_actions):
                reconstructions.append(buffer.copy())
                buffer.clear()
                idx = 0
        elif tolerance > 0:
            tolerance -= 1
            continue
        else:
            buffer.clear()
            idx = 0

    return reconstructions

# Example usage
if __name__ == "__main__":
    expected = ["observe", "reflect", "choose"]
    recon = reconstruct_choices_by_action_chain(expected)

    if not recon:
        print("🔍 No matching choice chains reconstructed.")
    else:
        print(f"🧠 {len(recon)} matching choice chain(s) found:")
        for i, chain in enumerate(recon, 1):
            print(f"  {i}. {[step.get('action') for step in chain]}")
