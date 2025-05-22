"""
🧪 test_s1_2_it_checks_if_an_echo_matches_a_prior_trace.py
----------------------------------------------------------
Tests for echo signal recognition using dynamic import (📜 5.5-compliant).
"""

import os
import json
import pytest
import tempfile
import importlib.util

# ✅ Load dynamic_importer helper
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Dynamically import the target stanza file
project_root = os.path.abspath(os.getcwd())
module_path = os.path.join(
    project_root,
    "src",
    "storybook_fun_factory",
    "quarantine_ai",
    "s1_1_it_listens_before_it_locks",
    "s1_2_it_knows_the_pattern_will_return_again",
    "s1_2_it_checks_if_an_echo_matches_a_prior_trace.py"
)
module = dynamic_importer.dynamic_import_module(module_path)

@pytest.fixture
def prior_trace_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as f:
        sigs = [module.generate_signature({'signal': 'alpha'}),
                module.generate_signature({'signal': 'beta'})]
        json.dump(sigs, f)
        return f.name

def test_match_found(prior_trace_file):
    echo = {'signal': 'beta'}
    assert module.echo_matches_prior_trace(echo, prior_trace_file) is True

def test_match_not_found(prior_trace_file):
    echo = {'signal': 'gamma'}
    assert module.echo_matches_prior_trace(echo, prior_trace_file) is False

def test_add_trace_if_new_adds(prior_trace_file):
    new_echo = {'signal': 'delta'}
    added = module.add_trace_if_new(new_echo, prior_trace_file)
    assert added is True
    assert module.echo_matches_prior_trace(new_echo, prior_trace_file) is True

def test_add_trace_if_new_ignores_duplicate(prior_trace_file):
    existing_echo = {'signal': 'alpha'}
    added = module.add_trace_if_new(existing_echo, prior_trace_file)
    assert added is False
