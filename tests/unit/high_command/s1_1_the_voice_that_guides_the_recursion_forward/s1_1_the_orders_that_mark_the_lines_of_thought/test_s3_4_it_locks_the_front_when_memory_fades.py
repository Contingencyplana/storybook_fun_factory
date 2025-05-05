"""
test_s3_4_it_locks_the_front_when_memory_fades.py
(Tests FrontLockProtocol safeguard against memory file degradation)
"""

import os
import json
import importlib.util
import pytest


# ✅ Dynamic import setup
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)


@pytest.fixture
def valid_memory_files(tmp_path):
    gdj_index_path = tmp_path / "gdj_index.json"
    test_map_path = tmp_path / "test_map.json"
    gdj_index_path.write_text(json.dumps({"5.1": {"title": "Valid GDJ"}}))
    test_map_path.write_text(json.dumps({"filename_ai": ["test_1.py", "test_2.py"]}))
    return str(gdj_index_path), str(test_map_path)


@pytest.fixture
def corrupted_memory_file(tmp_path):
    gdj_index_path = tmp_path / "gdj_index.json"
    test_map_path = tmp_path / "test_map.json"
    gdj_index_path.write_text("{this is invalid JSON")
    test_map_path.write_text(json.dumps({"okay": "yes"}))
    return str(gdj_index_path), str(test_map_path)


@pytest.fixture
def missing_memory_file(tmp_path):
    # Only create one file, omit the other
    gdj_index_path = tmp_path / "gdj_index.json"
    gdj_index_path.write_text(json.dumps({"good": True}))
    test_map_path = tmp_path / "missing.json"  # will not be created
    return str(gdj_index_path), str(test_map_path)


def test_lock_with_valid_files(valid_memory_files):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s3_4_it_locks_the_front_when_memory_fades.py"
        )
    )
    module = dynamic_importer.dynamic_import_module(module_path)
    FrontLockProtocol = module.FrontLockProtocol

    lock = FrontLockProtocol(*valid_memory_files)
    assert lock.evaluate_lock() is False
    status = lock.get_status()
    assert status["locked"] is False
    assert status["gdj_index"] == "valid"
    assert status["test_map"] == "valid"


def test_lock_with_corrupted_file(corrupted_memory_file):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s3_4_it_locks_the_front_when_memory_fades.py"
        )
    )
    module = dynamic_importer.dynamic_import_module(module_path)
    FrontLockProtocol = module.FrontLockProtocol

    lock = FrontLockProtocol(*corrupted_memory_file)
    assert lock.evaluate_lock() is True
    status = lock.get_status()
    assert status["locked"] is True
    assert "gdj_index corrupted." in status["errors"]


def test_lock_with_missing_file(missing_memory_file):
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s3_4_it_locks_the_front_when_memory_fades.py"
        )
    )
    module = dynamic_importer.dynamic_import_module(module_path)
    FrontLockProtocol = module.FrontLockProtocol

    lock = FrontLockProtocol(*missing_memory_file)
    assert lock.evaluate_lock() is True
    status = lock.get_status()
    assert status["locked"] is True
    assert "test_map missing." in status["errors"]
