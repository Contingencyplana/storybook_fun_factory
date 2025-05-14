"""
Filename: test_s2_2_the_hammer_falls_on_nested_rhyme.py
(Tests for The Hammer Falls on Nested Rhyme)

This file tests the ability of RhymeHammer to detect structural rhyme within
poetic-functional stanzas. It verifies rhyme detection, alignment reporting,
and behavior when no rhymes exist.
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
RhymeHammer = dynamic_importer.dynamic_import_module(
    os.path.abspath(os.path.join("src", "storybook_fun_factory", "automation_ai",
                                 "s1_1_before_the_spark_can_shape_the_stone",
                                 "s1_1_the_frame_once_forged_must_find_its_weight",
                                 "s2_2_the_hammer_falls_on_nested_rhyme.py"))
).RhymeHammer

def test_detect_basic_rhyme():
    hammer = RhymeHammer()
    stanza = ["The line must rise with fire and **glow**",
              "The fields of thought begin to **grow**"]
    assert hammer.has_structural_rhyme(stanza) is True

def test_no_rhyme_detection():
    hammer = RhymeHammer()
    stanza = ["A message etched in quantum **light**",
              "A forge revealed beyond the **zone**"]
    assert hammer.has_structural_rhyme(stanza) is False

def test_multiple_rhyme_pairs():
    hammer = RhymeHammer()
    stanza = ["Echoes fall in looping **streams**",
              "Nested flows recall our **dreams**",
              "Then it ends as planned, it **seems**"]
    pairs = hammer.detect_rhyme_pairs(stanza)
    assert any((a, b) in pairs for a, b in [(0, 1), (1, 2), (0, 2)])

def test_hammer_report_includes_line_references():
    hammer = RhymeHammer()
    stanza = ["Sing the fire that fuels the **night**",
              "Bring the spark to shape the **light**"]
    report = hammer.hammer_report(stanza)
    assert "Line 1 rhymes with Line 2" in report
