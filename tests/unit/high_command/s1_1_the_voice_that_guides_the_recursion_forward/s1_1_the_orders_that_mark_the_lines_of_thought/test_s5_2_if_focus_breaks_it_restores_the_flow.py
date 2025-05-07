# File: test_s5_2_if_focus_breaks_it_restores_the_flow.py

"""
test_s5_2_if_focus_breaks_it_restores_the_flow.py

Tests for the recursive focus restoration logic in:
s5_2_if_focus_breaks_it_restores_the_flow.py
"""

import os
import tempfile
import time
from pathlib import Path
from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import s5_2_if_focus_breaks_it_restores_the_flow as focus_restorer

def create_mock_file(path: Path, age_seconds: int):
    path.touch()
    os.utime(path, (time.time() - age_seconds, time.time() - age_seconds))

def test_find_last_modified_file_returns_latest():
    with tempfile.TemporaryDirectory() as temp_dir:
        dir_path = Path(temp_dir)
        file1 = dir_path / "s1_1_alpha.py"
        file2 = dir_path / "s1_2_beta.py"
        create_mock_file(file1, 4000)  # older
        create_mock_file(file2, 100)   # newer

        result = focus_restorer.find_last_modified_file(temp_dir)
        assert result is not None
        assert result.endswith("s1_2_beta.py")

def test_recommend_focus_file_returns_gapped_neighbor():
    with tempfile.TemporaryDirectory() as temp_dir:
        dir_path = Path(temp_dir)
        files = [
            ("s1_1_alpha.py", 4000),
            ("s1_2_beta.py", 3000),
            ("s1_3_gamma.py", 8000),  # very stale
        ]
        for name, age in files:
            create_mock_file(dir_path / name, age)

        recommendation = focus_restorer.recommend_focus_file(temp_dir)
        assert recommendation is not None
        assert recommendation.endswith("s1_3_gamma.py")

def test_recommend_focus_file_returns_last_if_no_gap():
    with tempfile.TemporaryDirectory() as temp_dir:
        dir_path = Path(temp_dir)
        files = [
            ("s1_1_alpha.py", 4000),
            ("s1_2_beta.py", 3500),
            ("s1_3_gamma.py", 3000),
        ]
        for name, age in files:
            create_mock_file(dir_path / name, age)

        recommendation = focus_restorer.recommend_focus_file(temp_dir)
        assert recommendation is not None
        assert recommendation.endswith("s1_3_gamma.py")

def test_find_last_modified_file_none_if_empty():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = focus_restorer.find_last_modified_file(temp_dir)
        assert result is None
