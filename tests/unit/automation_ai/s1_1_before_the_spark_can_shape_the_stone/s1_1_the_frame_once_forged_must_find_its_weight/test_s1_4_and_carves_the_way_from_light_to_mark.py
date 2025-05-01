"""
Filename: test_s1_4_and_carves_the_way_from_light_to_mark.py
(Tests for And Carves the Way from Light to Mark)

This file tests the carving process—transforming blueprint content and poetic filenames
into real, tangible .py files within the recursive system. It validates successful creation,
content accuracy, and file verification logic.
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

# Use it to load the stanza file
FileCarver = dynamic_importer.dynamic_import_module(
    os.path.abspath(os.path.join("src", "storybook_fun_factory", "automation_ai",
                                 "s1_1_before_the_spark_can_shape_the_stone",
                                 "s1_1_the_frame_once_forged_must_find_its_weight",
                                 "s1_4_and_carves_the_way_from_light_to_mark.py"))
).FileCarver

def test_file_carving_and_verification(tmp_path):
    carver = FileCarver(root_dir=tmp_path)
    filename = "s1_5_the_light_that_forges_the_loop"
    content = "# This is a carved test file.\nprint('Hello, recursion!')"

    path = carver.carve(filename, content)
    assert os.path.isfile(path)
    assert carver.verify_carving(filename)

    with open(path, "r", encoding="utf-8") as f:
        read_content = f.read()
    assert content in read_content

def test_file_extension_auto_addition(tmp_path):
    carver = FileCarver(root_dir=tmp_path)
    filename = "s1_6_the_echo_that_names_the_return"
    content = "# Auto-extension test"
    path = carver.carve(filename, content)
    assert path.endswith(".py")
    assert os.path.exists(path)

def test_file_overwrite_behavior(tmp_path):
    carver = FileCarver(root_dir=tmp_path)
    filename = "overwrite_test"
    initial_content = "# First version"
    updated_content = "# Second version"
    
    path = carver.carve(filename, initial_content)
    carver.carve(filename, updated_content)

    with open(path, "r", encoding="utf-8") as f:
        final_content = f.read()
    assert final_content == updated_content
