"""
🧪 test_s1_2_it_checks_if_an_echo_matches_a_prior_trace.py
----------------------------------------------------------
Tests for matching logic between echo signals and prior trace signatures.
"""

import pytest
import tempfile
import json
from src.storybook_fun_factory.quarantine_ai.s1_2_it_knows_the_pattern_will_return_again.recursive_signal_detection import s1_2_it_checks_if_an_echo_matches_a_prior_trace as mod

@pytest.fixture
def prior_trace_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as f:
        sigs = [mod.generate_signature({'signal': 'alpha'}), mod.generate_signature({'signal': 'beta'})]
        json.dump(sigs, f)
        return f.name

def test_match_found(prior_trace_file):
    echo = {'signal': 'beta'}
    assert mod.echo_matches_prior_trace(echo, prior_trace_file) is True

def test_match_not_found(prior_trace_file):
    echo = {'signal': 'gamma'}
    assert mod.echo_matches_prior_trace(echo, prior_trace_file) is False

def test_add_trace_if_new_adds(prior_trace_file):
    new_echo = {'signal': 'delta'}
    added = mod.add_trace_if_new(new_echo, prior_trace_file)
    assert added is True
    assert mod.echo_matches_prior_trace(new_echo, prior_trace_file) is True

def test_add_trace_if_new_ignores_duplicate(prior_trace_file):
    existing_echo = {'signal': 'alpha'}
    added = mod.add_trace_if_new(existing_echo, prior_trace_file)
    assert added is False
