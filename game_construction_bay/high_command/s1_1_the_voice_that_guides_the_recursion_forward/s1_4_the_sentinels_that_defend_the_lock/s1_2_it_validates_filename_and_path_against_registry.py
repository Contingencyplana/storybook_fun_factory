"""
s1_2_it_validates_filename_and_path_against_registry.py

Validates whether a given file's name and full path match its canonical
entry in the registry of sealed stanza files.

This enforcement layer protects against unauthorized renames, relocations,
or filename mutations after canonization.

Dependencies:
- Registry file (JSON) assumed at `.canon_registry` in project root
- Each registry entry includes full absolute path and canonical filename

Example Registry Entry:
{
  "files": [
    {
      "canonical_name": "s1_2_the_codex_sorts_what_was_once_scattered.py",
      "canonical_path": "C:/Users/Admin/storybook_fun_factory/game_construction_bay/codex_builder/s1_1_structure/s1_2_the_codex_sorts_what_was_once_scattered.py"
    }
  ]
}

Example Usage:
>>> from s1_2_it_validates_filename_and_path_against_registry import validate_against_registry
>>> validate_against_registry("game_construction_bay/codex_builder/s1_1_structure/s1_2_the_codex_sorts_what_was_once_scattered.py")
True
"""

import json
from pathlib import Path

REGISTRY_FILENAME = ".canon_registry"

def load_registry() -> list:
    """Loads the registry JSON file."""
    registry_file = Path(REGISTRY_FILENAME)
    if not registry_file.exists():
        raise FileNotFoundError(f"Registry not found: {REGISTRY_FILENAME}")
    with registry_file.open("r", encoding="utf-8") as f:
        return json.load(f).get("files", [])

def validate_against_registry(file_path: str) -> bool:
    """
    Validates that the provided file matches a canonical entry in the registry.

    Args:
        file_path (str): Path to file to be validated.

    Returns:
        bool: True if file path and name match registry; False otherwise.
    """
    file = Path(file_path).resolve()
    registry_entries = load_registry()

    for entry in registry_entries:
        if (Path(entry["canonical_name"]).name == file.name and
            Path(entry["canonical_path"]).resolve() == file):
            return True
    return False
