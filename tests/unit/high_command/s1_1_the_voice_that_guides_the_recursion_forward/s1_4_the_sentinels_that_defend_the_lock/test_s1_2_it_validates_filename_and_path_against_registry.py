"""
test_s1_2_it_validates_filename_and_path_against_registry.py

Tests filename and path validation against the canon registry.

Compliant with 📜 5.5 – Dynamic Import Methodology
"""

import pytest
import tempfile
import json
from pathlib import Path
from importlib import import_module

MODULE_PATH = "game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock.s1_2_it_validates_filename_and_path_against_registry"

@pytest.fixture
def fake_registry_and_file(tmp_path):
    # Create a fake file to validate
    file_path = tmp_path / "s1_2_the_codex_sorts_what_was_once_scattered.py"
    file_path.write_text("# pretend stanza\n", encoding="utf-8")

    # Create fake registry in project root
    registry_data = {
        "files": [
            {
                "canonical_name": file_path.name,
                "canonical_path": str(file_path.resolve())
            }
        ]
    }

    registry_file = Path(".canon_registry")
    with registry_file.open("w", encoding="utf-8") as f:
        json.dump(registry_data, f, indent=2)

    yield file_path

    registry_file.unlink(missing_ok=True)

def test_validates_filename_and_path_against_registry(fake_registry_and_file):
    module = import_module(MODULE_PATH)
    validate = getattr(module, "validate_against_registry")

    assert validate(str(fake_registry_and_file)) is True

def test_rejects_modified_name(fake_registry_and_file):
    module = import_module(MODULE_PATH)
    validate = getattr(module, "validate_against_registry")

    renamed = fake_registry_and_file.with_name("tampered_name.py")
    fake_registry_and_file.rename(renamed)

    assert validate(str(renamed)) is False
