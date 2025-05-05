"""
Filename: s1_3_it_traces_the_path_in_stanza_form.py

📜 See GDJ 5.8: May 6 – The Genesis Command
(Third line of Stanza 1 in the Layer 5 Genesis Cycle of high_command)

Purpose:
Records a trail of stanza lines recently marked as active,
building a poetic and structural memory of recursive traversal.

This helps track project momentum, replay work sequences,
and prepare assistant-guided diagnostics or dashboard summaries.
"""

from pathlib import Path
import json
from datetime import datetime

# 🔖 Location for active path log
STANZA_TRACE_PATH = Path(__file__).parent / "stanza_path_log.json"

def trace_stanza_progress(component: str, stanza: str, line: str, timestamp: str = None):
    """
    Logs a stanza line traversal with timestamp and component.

    Args:
        component (str): The name of the recursive component.
        stanza (str): The stanza folder or logical group.
        line (str): The active filename being recorded.
        timestamp (str, optional): Override timestamp. If None, auto-generated.
    """
    if not timestamp:
        timestamp = datetime.utcnow().isoformat()

    entry = {
        "timestamp": timestamp
    }
