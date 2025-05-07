# File: test_s5_1_if_too_long_has_passed_it_speaks.py

import os
import tempfile
import time
import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import s5_1_if_too_long_has_passed_it_speaks as idle_checker

def test_file_has_been_idle_too_long_false_for_recent_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp_path = temp.name
    try:
        assert not idle_checker.file_has_been_idle_too_long(temp_path, max_idle_seconds=60)
    finally:
        os.remove(temp_path)

def test_file_has_been_idle_too_long_true_for_old_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:
        temp_path = temp.name
    try:
        # Simulate idle time by backdating modification time
        old_time = time.time() - 7200  # 2 hours ago
        os.utime(temp_path, (old_time, old_time))
        assert idle_checker.file_has_been_idle_too_long(temp_path, max_idle_seconds=3600)
    finally:
        os.remove(temp_path)

def test_list_stale_files_detects_old_file(tmp_path):
    test_file = tmp_path / "old_script.py"
    test_file.write_text("# dummy script\n")
    old_time = time.time() - 7200
    os.utime(test_file, (old_time, old_time))

    stale_files = idle_checker.list_stale_files(str(tmp_path), max_idle_seconds=3600)
    assert str(test_file) in stale_files

def test_list_stale_files_ignores_recent_and_test_files(tmp_path):
    fresh_file = tmp_path / "fresh_script.py"
    fresh_file.write_text("# recent script\n")

    test_file = tmp_path / "test_example.py"
    test_file.write_text("# should be ignored\n")

    stale_files = idle_checker.list_stale_files(str(tmp_path), max_idle_seconds=3600)
    assert str(fresh_file) not in stale_files
    assert str(test_file) not in stale_files
