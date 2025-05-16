"""
📄 test_s1_1_it_registers_the_known_helpers_and_tests.py

This test suite validates the canonical behavior of CanonRegistry
from s1_1_it_registers_the_known_helpers_and_tests.py.
It dynamically registers helpers and tests, ensuring correct
lookup, duplication prevention, and canonical output sorting.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../../../..")))
import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_3_the_registry_that_remembers_the_canon.s1_1_it_registers_the_known_helpers_and_tests import CanonRegistry

def test_register_and_check_helpers_and_tests():
    registry = CanonRegistry()

    # Dynamically register multiple helpers and tests
    helpers = ["helper_dispatch", "helper_canon_check", "helper_trace_logger"]
    tests = ["test_async_marker", "test_crosslayer_warning", "test_stanza_lock"]

    for h in helpers:
        registry.register_helper(h)
    for t in tests:
        registry.register_test(t)

    # Confirm all helpers and tests are correctly registered
    for h in helpers:
        assert registry.is_helper_registered(h)
    for t in tests:
        assert registry.is_test_registered(t)

    # Confirm sorting behavior
    assert registry.get_all_helpers() == sorted(helpers)
    assert registry.get_all_tests() == sorted(tests)

    # Register duplicates and confirm idempotence
    registry.register_helper("helper_dispatch")
    registry.register_test("test_async_marker")
    assert registry.get_all_helpers().count("helper_dispatch") == 1
    assert registry.get_all_tests().count("test_async_marker") == 1
