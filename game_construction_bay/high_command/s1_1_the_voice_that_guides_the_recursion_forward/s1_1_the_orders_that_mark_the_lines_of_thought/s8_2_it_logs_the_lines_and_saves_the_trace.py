"""
Filename: s8_2_it_logs_the_lines_and_saves_the_trace.py

Purpose:
Logs stanza line metadata produced by s8_1 to a persistent JSON trace file.
Used to inform later stanza coordination and GDJ validation in Cycle 4.

Poetic Role:
The Gate That Knows Each Line Beneath – Line 2
"""

import json
from pathlib import Path

TRACE_FILENAME = "layer5_trace.json"

def log_stanza_metadata_to_trace(stanza_metadata: dict, output_dir: Path) -> Path:
    """
    Saves stanza metadata to a trace file.

    Args:
        stanza_metadata (dict): Output from s8_1 stanza scan
        output_dir (Path): Path to folder where the trace should be saved

    Returns:
        Path: Path to the written trace file
    """
    trace_path = output_dir / TRACE_FILENAME
    with open(trace_path, "w", encoding="utf-8") as f:
        json.dump(stanza_metadata, f, indent=2)
    return trace_path

# Example usage
if __name__ == "__main__":
    sample = {
        "filename_ai": ["some/stanza1.py", "some/stanza2.py"],
        "memory_ai": ["mem/deep.py"]
    }
    output = Path.cwd()
    print(log_stanza_metadata_to_trace(sample, output))
