"""
Filename: test_s9_2_it_confirms_the_names_and_saves_the_canon.py

Tests canonical validation of stanza names and JSON saving logic.
Follows the 📜 5.5 dynamic import methodology.
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
    "s9_2_it_confirms_the_names_and_saves_the_canon.py"

module = dynamic_importer.dynamic_import_module(str(target_path))
confirm_canonical_stanza_names = module.confirm_canonical_stanza_names
save_confirmed_canon = module.save_confirmed_canon

def test_confirm_canonical_stanza_names_and_save(tmp_path: Path):
    # Input: stanza memory map
    raw = {
        "line1.py": {"visualizer": {"meta": "v"}},
        "bad_line.py": {"filename_ai": {"meta": "f"}},
    }
    valid = {"line1.py"}

    # Call and check filtering
    filtered = confirm_canonical_stanza_names(raw, valid)
    assert "line1.py" in filtered
    assert "bad_line.py" not in filtered

    # Test save
    output_path = tmp_path / "confirmed" / "canon.json"
    save_confirmed_canon(filtered, output_path)
    assert output_path.exists()

    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert "line1.py" in data
        assert data["line1.py"]["visualizer"]["meta"] == "v"
