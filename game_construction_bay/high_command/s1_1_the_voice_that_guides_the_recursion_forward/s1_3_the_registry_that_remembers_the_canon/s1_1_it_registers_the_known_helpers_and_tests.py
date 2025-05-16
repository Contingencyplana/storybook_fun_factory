"""
📄 s1_1_it_registers_the_known_helpers_and_tests.py

This module initializes and maintains a registry of known helper modules and test cases.
It ensures the assistant is aware of which supporting components are canonized and active
across recursive recursion zones.

Functional Roles:
- Registers all helper and test files currently in use.
- Stores them in a dictionary structure.
- Provides lookup and existence-checking methods.
- Can be imported by any stanza line that depends on helper awareness.

Example Usage:
>>> from s1_1_it_registers_the_known_helpers_and_tests import CanonRegistry
>>> registry = CanonRegistry()
>>> registry.register_helper("test_dispatch_marker")
>>> registry.is_helper_registered("test_dispatch_marker")
True
"""

class CanonRegistry:
    def __init__(self):
        self.helpers = set()
        self.tests = set()

    def register_helper(self, helper_name: str) -> None:
        """Register a helper file name."""
        self.helpers.add(helper_name)

    def register_test(self, test_name: str) -> None:
        """Register a test file name."""
        self.tests.add(test_name)

    def is_helper_registered(self, helper_name: str) -> bool:
        """Check if a helper is already registered."""
        return helper_name in self.helpers

    def is_test_registered(self, test_name: str) -> bool:
        """Check if a test is already registered."""
        return test_name in self.tests

    def get_all_helpers(self) -> list[str]:
        """Return a list of all registered helpers."""
        return sorted(self.helpers)

    def get_all_tests(self) -> list[str]:
        """Return a list of all registered tests."""
        return sorted(self.tests)
