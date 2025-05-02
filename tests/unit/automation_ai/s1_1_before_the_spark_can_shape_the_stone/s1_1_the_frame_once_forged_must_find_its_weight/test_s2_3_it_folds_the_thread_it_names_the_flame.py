"""
Filename: test_s2_3_it_folds_the_thread_it_names_the_flame.py
(Tests for It Folds the Thread, It Names the Flame)

This file tests the ability of ThreadFolder to compound lines,
generate folded structures, and assign hashed flame names.
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

# Import the stanza file
ThreadFolder = dynamic_importer.dynamic_import_module(
    os.path.abspath(os.path.join("src", "storybook_fun_factory", "automation_ai",
                                 "s1_1_before_the_spark_can_shape_the_stone",
                                 "s1_1_the_frame_once_forged_must_find_its_weight",
                                 "s2_3_it_folds_the_thread_it_names_the_flame.py"))
).ThreadFolder

def test_fold_lines_output_format():
    folder = ThreadFolder()
    lines = ["The code ignites", "Where dreamers tread"]
    folded = folder.fold_lines(lines)
    assert "#> The code ignites" in folded
    assert "#> Where dreamers tread" in folded

def test_name_flame_consistency():
    folder = ThreadFolder(namespace="test")
    lines = ["One", "Two", "Three"]
    folded = folder.fold_lines(lines)
    name1 = folder.name_flame(folded)
    name2 = folder.name_flame(folded)
    assert name1 == name2
    assert name1.startswith("test_flame_")

def test_fold_and_name_output_structure():
    folder = ThreadFolder(namespace="alpha")
    lines = ["Fold me", "Name me"]
    result = folder.fold_and_name(lines)
    assert "folded_output" in result
    assert "flame_name" in result
    assert result["flame_name"].startswith("alpha_flame_")
