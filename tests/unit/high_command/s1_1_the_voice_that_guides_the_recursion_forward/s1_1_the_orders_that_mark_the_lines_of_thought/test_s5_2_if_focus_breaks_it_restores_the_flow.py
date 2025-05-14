# File: test_s5_2_if_focus_breaks_it_restores_the_flow.py

import os
import tempfile
import time
from pathlib import Path
from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import s5_2_if_focus_breaks_it_restores_the_flow as focus_restorer


def create_mock_file(path: Path, age_seconds: int):
    path.write_text("# mock file")
    mod_time = time.time() - age_seconds
    os.utime(path, (mod_time, mod_time))


def test_recommend_focus_file_identifies_largest_gap():
    with tempfile.TemporaryDirectory() as temp_dir:
        dir_path = Path(temp_dir)
        files = [
            ("s1_1_alpha.py", 4000),
            ("s1_2_beta.py", 1000),   # Freshest
            ("s1_3_gamma.py", 4000),  # Stale — should trigger as neglected
        ]
        for name, age in files:
            create_mock_file(dir_path / name, age)

        recommendation = focus_restorer.recommend_focus_file(temp_dir)
        assert recommendation is not None
        assert recommendation.endswith("s1_3_gamma.py")


def test_recommend_focus_file_returns_single_file_if_only_one_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        dir_path = Path(temp_dir)
        create_mock_file(dir_path / "s1_1_alpha.py", 4000)

        recommendation = focus_restorer.recommend_focus_file(temp_dir)
        assert recommendation is not None
        assert recommendation.endswith("s1_1_alpha.py")


def test_recommend_focus_file_ignores_tests():
    with tempfile.TemporaryDirectory() as temp_dir:
        dir_path = Path(temp_dir)
        files = [
            ("s1_1_alpha.py", 1000),                # Newest valid file
            ("test_s1_2_beta.py", 500),             # Should be ignored
            ("s1_3_gamma.py", 4000),                # Older
        ]
        for name, age in files:
            create_mock_file(dir_path / name, age)

        recommendation = focus_restorer.recommend_focus_file(temp_dir)
        assert recommendation is not None
        assert recommendation.endswith("s1_3_gamma.py")  # Correct expectation
