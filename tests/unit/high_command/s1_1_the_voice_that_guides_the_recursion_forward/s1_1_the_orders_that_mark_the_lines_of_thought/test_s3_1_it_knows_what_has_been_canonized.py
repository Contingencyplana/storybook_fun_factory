"""
test_s3_1_it_knows_what_has_been_canonized.py
(Tests CanonMemory logic for GDJ-to-Stanza linkage tracking)

This test uses the Dynamic Import Methodology (📜 5.5) to validate 
that High Command can correctly identify canonized GDJ entries, 
locate stanza mappings, and detect unlinked records.
"""

import os
import importlib.util
import json
import pytest
from pathlib import Path


# ✅ Load dynamic_importer.py
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)


@pytest.fixture
def sample_gdj_index(tmp_path):
    # Create a mock GDJ index JSON file in the expected structure
    gdj_data = {
        "5.1": {
            "title": "May 1 – Memory Bleed Protocol",
            "stanza_path": "memory_ai/s1_1_echoes_that_recall_the_trace"
        },
        "5.2": {
            "title": "May 1 – First Stanza",
            "stanza_path": "filename_ai/s1_1_the_voice_that_names_the_form"
        },
        "5.3": {
            "title": "May 2 – Untied Threads"
            # No stanza_path yet
        }
    }
    index_path = tmp_path / "gdj_index.json"
    with index_path.open("w", encoding="utf-8") as f:
        json.dump(gdj_data, f)
    return index_path


def test_canon_memory_queries(sample_gdj_index):
    # Dynamically import the module
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../src/storybook_fun_factory/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_3_the_registry_that_remembers_the_canon/s3_1_it_knows_what_has_been_canonized.py"
        )
    )
    module = dynamic_importer.dynamic_import_module(module_path)
    CanonMemory = module.CanonMemory

    memory = CanonMemory(gdj_index_path=sample_gdj_index)

    # ✅ Check GDJ-to-stanza mapping
    assert memory.get_stanza_by_gdj("5.1") == "memory_ai/s1_1_echoes_that_recall_the_trace"
    assert memory.get_stanza_by_gdj("5.3") is None

    # ✅ Check stanza-to-GDJ mapping
    assert memory.get_gdj_by_stanza("filename_ai/s1_1_the_voice_that_names_the_form")["title"] == "May 1 – First Stanza"

    # ✅ Check canonized detection
    assert memory.is_canonized("memory_ai/s1_1_echoes_that_recall_the_trace") is True
    assert memory.is_canonized("dream_journal/s1_2_path_that_dreams_inward") is False

    # ✅ Check unlinked GDJs
    unlinked = memory.list_unlinked_gdjs()
    assert "5.3" in unlinked
    assert "5.1" not in unlinked

    # ✅ Check pair listing
    pairs = memory.list_all_canonized_pairs()
    assert ("5.1", "memory_ai/s1_1_echoes_that_recall_the_trace") in pairs
