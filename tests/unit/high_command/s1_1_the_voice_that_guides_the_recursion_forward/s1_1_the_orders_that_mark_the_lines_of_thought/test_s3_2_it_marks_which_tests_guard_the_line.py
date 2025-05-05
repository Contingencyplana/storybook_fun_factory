"""
test_s3_2_it_marks_which_tests_guard_the_line.py
(Validates mapping logic for stanza → test file indexing)

Ensures that TestCoverageIndex correctly identifies matching test files,
detects unguarded stanza lines, and produces accurate mappings.
"""

import os
import pytest
from pathlib import Path
import importlib.util

# ✅ Dynamic import loader for main module
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../../tests/test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)


@pytest.fixture
def mock_test_directory(tmp_path):
    # Create mock stanza files and corresponding test files
    test_dir = tmp_path / "mock_tests"
    test_dir.mkdir()

    # Simulated test files
    valid_files = [
        "test_s1_1_it_marks_the_front_but_moves_unseen.py",
        "test_s1_2_it_recites_the_focus_in_shifted_light.py",
        "test_s2_4_the_cycle_must_not_break_its_line.py"
    ]

    for file in valid_files:
        (test_dir / file).write_text("# mock test file")

    return test_dir


def test_index_and_lookup(mock_test_directory):
    # Import the main module dynamically
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s3_2_it_marks_which_tests_guard_the_line.py"
        )
    )
    module = dynamic_importer.dynamic_import_module(module_path)
    TestCoverageIndex = module.TestCoverageIndex

    indexer = TestCoverageIndex(mock_test_directory)

    # ✅ Mapping resolution
    assert indexer.get_test_for_stanza("s1_1_it_marks_the_front_but_moves_unseen.py") is not None
    assert indexer.get_test_for_stanza("s2_4_the_cycle_must_not_break_its_line.py").endswith(".py")
    assert indexer.get_test_for_stanza("s3_3_nonexistent.py") is None

    # ✅ List all mappings
    all_pairs = indexer.list_all_mapped_tests()
    assert ("s1_2_it_recites_the_focus_in_shifted_light.py", all_pairs[1][1]) in all_pairs

    # ✅ Detect unguarded files
    stanza_dir = mock_test_directory
    # Add extra stanza file with no test
    (stanza_dir / "s3_1_it_knows_what_has_been_canonized.py").write_text("# orphan stanza line")
    unguarded = indexer.list_unguarded_stanza_files(stanza_dir)
    assert "s3_1_it_knows_what_has_been_canonized.py" in unguarded
