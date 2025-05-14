# File: test_s5_3_if_hot_zones_wait_it_gives_priority.py

import os
import tempfile
from pathlib import Path
from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import s5_3_if_hot_zones_wait_it_gives_priority as prioritizer


def create_mock_file(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# mock file")


def test_identifies_hot_zone_paths_correctly():
    assert prioritizer.is_hot_zone_path("src/recursion_renders/visual.py")
    assert prioritizer.is_hot_zone_path("core/active_zone/module.py")
    assert not prioritizer.is_hot_zone_path("src/ordinary_module.py")
    assert not prioritizer.is_hot_zone_path("notes/misc.txt")


def test_lists_hot_zone_files_only():
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        hot = root / "recursion_renders" / "hot_1.py"
        cold = root / "ordinary" / "cold_1.py"
        test_file = root / "test_suites" / "test_hot.py"

        create_mock_file(hot)
        create_mock_file(cold)
        create_mock_file(test_file)

        hot_files = set(map(Path, prioritizer.list_hot_zone_files(temp_dir)))
        assert hot in hot_files
        assert cold not in hot_files
        assert test_file not in hot_files


def test_includes_tests_when_flag_set():
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        test_file = root / "test_suites" / "test_urgent.py"
        create_mock_file(test_file)

        result = set(map(Path, prioritizer.list_hot_zone_files(temp_dir, include_tests=True)))
        assert test_file in result
