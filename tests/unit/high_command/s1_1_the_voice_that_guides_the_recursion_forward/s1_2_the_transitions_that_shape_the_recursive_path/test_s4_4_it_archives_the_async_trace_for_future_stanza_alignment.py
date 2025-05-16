"""
Test: test_s4_4_it_archives_the_async_trace_for_future_stanza_alignment.py

Validates the behavior of archive_async_trace_for_future_stanza_alignment using 📜 5.5 dynamic import methodology.
"""

import os
import json
import importlib.util
from pathlib import Path

import pytest

# Load dynamic_importer helper
HELPER_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Load the module under test
MODULE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s4_4_it_archives_the_async_trace_for_future_stanza_alignment.py"
    )
)
module = dynamic_importer.dynamic_import_module(MODULE_PATH)
archive_async_trace_for_future_stanza_alignment = module.archive_async_trace_for_future_stanza_alignment

def test_async_trace_archives_successfully(tmp_path):
    trace_data = {
        "destination": "filename_ai",
        "metadata": {"transition_id": "T789"},
        "dispatched_at": "2025-05-16T04:00:00Z"
    }

    archive_path = archive_async_trace_for_future_stanza_alignment(trace_data, archive_dir=tmp_path)
    assert archive_path.exists()

    with archive_path.open("r", encoding="utf-8") as f:
        archive = json.load(f)

    assert isinstance(archive, list)
    assert archive[0]["trace"]["metadata"]["transition_id"] == "T789"
    assert "archived_at" in archive[0]

def test_archiving_appends_to_existing_file(tmp_path):
    trace_1 = {
        "destination": "visualizer",
        "metadata": {"transition_id": "T001"},
        "dispatched_at": "2025-05-16T04:00:00Z"
    }
    trace_2 = {
        "destination": "memory_ai",
        "metadata": {"transition_id": "T002"},
        "dispatched_at": "2025-05-16T04:05:00Z"
    }

    archive_async_trace_for_future_stanza_alignment(trace_1, archive_dir=tmp_path)
    archive_async_trace_for_future_stanza_alignment(trace_2, archive_dir=tmp_path)

    archive_path = tmp_path / "archived_async_transitions.json"
    with archive_path.open("r", encoding="utf-8") as f:
        archive = json.load(f)

    assert len(archive) == 2
    assert archive[1]["trace"]["destination"] == "memory_ai"
