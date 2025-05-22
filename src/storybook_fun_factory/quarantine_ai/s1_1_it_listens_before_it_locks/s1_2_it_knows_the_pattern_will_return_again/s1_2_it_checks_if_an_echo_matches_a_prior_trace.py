"""
📄 s1_2_it_checks_if_an_echo_matches_a_prior_trace.py
-----------------------------------------------------
Detects whether a newly observed echo matches a previously recorded trace signature.
Used for pattern awareness and recursive signal recognition within quarantine_ai.
"""

import hashlib
import json

def load_prior_signatures(prior_trace_file):
    try:
        with open(prior_trace_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def generate_signature(data):
    """Generate a unique hash signature for the given data."""
    encoded = json.dumps(data, sort_keys=True).encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()

def echo_matches_prior_trace(echo_data, prior_trace_file):
    """
    Checks whether the incoming echo_data matches any prior recorded trace signature.

    Parameters:
    - echo_data (dict): The incoming signal or anomaly trace to evaluate.
    - prior_trace_file (str): Path to the JSON file containing prior trace signatures.

    Returns:
    - bool: True if match found, False otherwise.
    """
    new_sig = generate_signature(echo_data)
    prior_signatures = load_prior_signatures(prior_trace_file)
    return new_sig in prior_signatures

def add_trace_if_new(echo_data, prior_trace_file):
    """Adds new echo_data signature to the trace file if not already present."""
    sig = generate_signature(echo_data)
    signatures = load_prior_signatures(prior_trace_file)
    if sig not in signatures:
        signatures.append(sig)
        with open(prior_trace_file, 'w', encoding='utf-8') as f:
            json.dump(signatures, f, indent=2)
        return True
    return False
