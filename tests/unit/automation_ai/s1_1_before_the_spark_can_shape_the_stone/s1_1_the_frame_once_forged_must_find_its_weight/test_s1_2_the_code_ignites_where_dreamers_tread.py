"""
Filename: test_s1_2_the_code_ignites_where_dreamers_tread.py
(Tests for The Code Ignites Where Dreamers Tread)

This file tests the ignition system for converting symbolic user input
(dream fragments) into structured code. It validates both successful and failed
ignition scenarios for the CodeIgniter class.
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
CodeIgniter = dynamic_importer.dynamic_import_module(
    os.path.abspath(os.path.join("src", "storybook_fun_factory", "automation_ai",
                                 "s1_1_before_the_spark_can_shape_the_stone",
                                 "s1_1_the_frame_once_forged_must_find_its_weight",
                                 "s1_2_the_code_ignites_where_dreamers_tread.py"))
).CodeIgniter

def test_ignition_successful():
    igniter = CodeIgniter("Let there be code.")
    igniter.ignite()
    assert igniter.is_ignited() is True
    assert "def dream()" in igniter.get_output()
    assert "Let there be code." in igniter.get_output()

def test_ignition_failure_empty_input():
    igniter = CodeIgniter("   ")
    igniter.ignite()
    assert igniter.is_ignited() is False
    assert "Ignition failed" in igniter.get_output()

def test_output_is_string():
    igniter = CodeIgniter("spark")
    igniter.ignite()
    assert isinstance(igniter.get_output(), str)

def test_multiple_ignitions_independent():
    igniter1 = CodeIgniter("A")
    igniter2 = CodeIgniter("B")
    igniter1.ignite()
    igniter2.ignite()
    assert igniter1.get_output() != igniter2.get_output()
