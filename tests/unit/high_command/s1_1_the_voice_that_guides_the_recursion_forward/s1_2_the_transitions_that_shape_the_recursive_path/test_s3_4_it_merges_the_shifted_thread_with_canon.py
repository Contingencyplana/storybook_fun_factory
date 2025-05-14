"""
Test for s3_4_it_merges_the_shifted_thread_with_canon.py
Uses 📜 5.5-compliant dynamic import methodology.
"""

import os
import json
import importlib.util
from pathlib import Path
import pytest


def dynamic_import_module(module_path: str, module_name: str = "dynamic_module"):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def canon_and_thread(tmp_path):
    canon_path = tmp_path / "canon.json"
    thread_path = tmp_path / "thread.json"

    canon_data = ["A", "B", "C"]
    thread_data = ["B", "C", "X"]

    canon_path.write_text(json.dumps(canon_data), encoding="utf-8")
    thread_path.write_text(json.dumps(thread_data), encoding="utf-8")

    return canon_path, thread_path


def test_merge_shifted_thread_with_canon(canon_and_thread):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_2_the_transitions_that_shape_the_recursive_path/s3_4_it_merges_the_shifted_thread_with_canon.py"
        )
    )
    module = dynamic_import_module(module_path)
    canon_path, thread_path = canon_and_thread

    result = module.merge_shifted_thread_with_canon(canon_path, thread_path)
    assert result == ["A", "B", "C", "X"]
