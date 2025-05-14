"""
Filename: test_s1_3_it_maps_the_hand_that_shapes_the_spark.py
(Tests for It Maps the Hand That Shapes the Spark)

This file tests the mapping system that records symbolic user inputs and their corresponding
generated outputs. It ensures that mappings are accurately stored, retrieved, and verified.
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
SparkMapper = dynamic_importer.dynamic_import_module(
    os.path.abspath(os.path.join("src", "storybook_fun_factory", "automation_ai",
                                 "s1_1_before_the_spark_can_shape_the_stone",
                                 "s1_1_the_frame_once_forged_must_find_its_weight",
                                 "s1_3_it_maps_the_hand_that_shapes_the_spark.py"))
).SparkMapper

def test_mapping_creation_and_retrieval():
    mapper = SparkMapper()
    mapper.map_spark("dream-input", "def code(): pass")
    result = mapper.get_mapping("dream-input")
    assert result == "def code(): pass"

def test_has_mapping_true():
    mapper = SparkMapper()
    mapper.map_spark("spark", "print('mapped')")
    assert mapper.has_mapping("spark") is True

def test_has_mapping_false():
    mapper = SparkMapper()
    assert mapper.has_mapping("unknown") is False

def test_get_mapping_missing_key():
    mapper = SparkMapper()
    result = mapper.get_mapping("missing")
    assert "No mapping found" in result

def test_all_mappings_is_copy():
    mapper = SparkMapper()
    mapper.map_spark("alpha", "return 'A'")
    all_map = mapper.all_mappings()
    all_map["alpha"] = "tampered"
    assert mapper.get_mapping("alpha") == "return 'A'"
