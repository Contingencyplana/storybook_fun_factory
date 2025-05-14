"""
Filename: test_s9_3_it_prepares_the_paths_for_crossing_safe.py

Tests readiness detection for stanza crossings.
Follows 📜 5.5 dynamic import strategy.
"""

import os
import json
from pathlib import Path
import pytest
import importlib.util

# ✅ Load dynamic importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Load target module
project_root = Path(__file__).resolve().parents[5]
target_path = project_root / "game_construction_bay" / "high_command" / \
    "s1_1_the_voice_that_guides_the_recursion_forward" / \
    "s1_1_the_orders_that_mark_the_lines_of_thought" / \
    "s9_3_it_prepares_the_paths_for_crossing_safe.py"

module = dynamic_importer.dynamic_import_module(str(target_path))
mark_ready_stanza_paths = module.mark_ready_stanza_paths
save_ready_paths = module.save_ready_paths

def test_mark_ready_stanza_paths_and_save(tmp_path: Path):
    confirmed = {
        "line1.py": {
            "visualizer": {},
            "filename_ai": {}
        },
        "line2.py": {
            "memory_ai": {}
        },
        "line3.py": {
            "codex_builder": {},
            "visualizer": {},
            "dream_journal": {}
        }
    }

    ready = mark_ready_stanza_paths(confirmed)
    assert "line1.py" in ready
    assert "line2.py" not in ready
    assert "line3.py" in ready
    assert ready["line3.py"]["status"] == "ready"

    # Save to disk
    out_path = tmp_path / "ready" / "crossings.json"
    save_ready_paths(ready, out_path)
    assert out_path.exists()

    with open(out_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert "line1.py" in data
        assert "line2.py" not in data
