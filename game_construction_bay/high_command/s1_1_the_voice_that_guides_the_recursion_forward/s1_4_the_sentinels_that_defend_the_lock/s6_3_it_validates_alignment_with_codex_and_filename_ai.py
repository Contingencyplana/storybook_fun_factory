"""
Filename: s6_3_it_validates_alignment_with_codex_and_filename_ai.py

Poetic-Functional Description:
This stanza line receives simulated stanza reconstructions and validates them against
two enforcement systems: codex_builder and filename_ai.

codex_builder confirms the stanza’s internal structure matches expected poetic and
recursive law. filename_ai ensures the folder and file names align with naming standards.

The validation does not write to the canon or approve repair — it marks whether
the proposed stanza is valid and includes reasoning for rejection when applicable.

Core Responsibilities:
- Accept proposed stanza reconstructions
- Validate stanza format via codex_builder interface
- Validate filename format via filename_ai logic
- Return enriched stanza proposals with pass/fail results

Example Usage:
>>> validate_results = validate_reconstructions([proposal])
>>> validate_results[0]["codex_valid"]  # True or False
"""

import re

def validate_codex_alignment(restored_content):
    """
    Placeholder for real codex_builder stanza structure validation.
    This mock checks for the presence of at least one function def and no forbidden syntax.
    """
    if "def " not in restored_content:
        return False, "No function definition found"
    if "eval(" in restored_content or "exec(" in restored_content:
        return False, "Use of forbidden syntax"
    return True, None

def validate_filename_alignment(original_path):
    """
    Placeholder for filename_ai enforcement. Validates stanza name conventions.
    E.g., must start with 's' + stanza number and have at least 7 words in snake_case.
    """
    name = original_path.split("/")[-1]
    return bool(re.fullmatch(r"s\d+_[a-z0-9_]{20,}", name)), name

def validate_reconstructions(reconstructions):
    validated = []

    for proposal in reconstructions:
        stanza_code = proposal.get("restored_content", "")
        orig_path = proposal.get("path", "")

        codex_ok, codex_reason = validate_codex_alignment(stanza_code)
        filename_ok, raw_name = validate_filename_alignment(orig_path)

        validated.append({
            **proposal,
            "codex_valid": codex_ok,
            "codex_reason": codex_reason,
            "filename_valid": filename_ok,
            "filename": raw_name,
        })

    return validated
