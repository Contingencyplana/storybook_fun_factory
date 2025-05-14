"""
Filename: test_s2_1_the_ember_stirs_the_lines_align.py
(Tests for The Ember Stirs, the Lines Align)

This file tests the alignment logic that transforms poetic-functional multiline input
into structured line-aware templates. It validates trimming, line count, ordering,
and boundary-safe retrieval.
"""
import sys
import os
import importlib.util
import pytest

# Load dynamic_importer.py manually
helper_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py"))
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Dynamically import the stanza file
LineAligner = dynamic_importer.dynamic_import_module(
    os.path.abspath(os.path.join("src", "storybook_fun_factory", "automation_ai",
                                 "s1_1_before_the_spark_can_shape_the_stone",
                                 "s1_1_the_frame_once_forged_must_find_its_weight",
                                 "s2_1_the_ember_stirs_the_lines_align.py"))
).LineAligner

def test_alignment_removes_empty_lines_and_trims():
    block = """
        Line one
        Line two

          Line three    
    """
    aligner = LineAligner()
    result = aligner.align_lines(block)
    assert result == ["Line one", "Line two", "Line three"]

def test_get_valid_line():
    aligner = LineAligner()
    aligner.align_lines("Alpha\nBeta\nGamma")
    assert aligner.get_line(1) == "Beta"

def test_get_invalid_line_index():
    aligner = LineAligner()
    aligner.align_lines("Only one line")
    assert "⚠️" in aligner.get_line(5)

def test_total_lines_count():
    aligner = LineAligner()
    aligner.align_lines("A\nB\nC\nD")
    assert aligner.total_lines() == 4
