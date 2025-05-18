"""
Filename: test_s6_3_it_validates_alignment_with_codex_and_filename_ai.py

Tests stanza proposal validation via codex_builder and filename_ai simulations.
Verifies:
- Codex validation for required structure
- Filename validation for stanza naming convention
- Combination outcomes for mixed validity scenarios
"""

import pytest

from high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import (
    s6_3_it_validates_alignment_with_codex_and_filename_ai as validator
)

@pytest.fixture
def sample_reconstructions():
    return [
        {
            "restored_content": "def safe_function():\n    pass\n",
            "path": "game_construction_bay/component/s6_3_it_validates_alignment_with_codex_and_filename_ai",
            "source": "memory_ai"
        },
        {
            "restored_content": "def f():\n    eval('bad()')",
            "path": "game_construction_bay/component/s6_3_it_validates_alignment_with_codex_and_filename_ai",
            "source": "archivist_ai"
        },
        {
            "restored_content": "def broken():\n    pass",
            "path": "game_construction_bay/component/badname",
            "source": "memory_ai"
        }
    ]

def test_codex_and_filename_validation(sample_reconstructions):
    results = validator.validate_reconstructions(sample_reconstructions)

    assert len(results) == 3

    # First: valid everything
    assert results[0]["codex_valid"] is True
    assert results[0]["filename_valid"] is True

    # Second: invalid due to forbidden syntax
    assert results[1]["codex_valid"] is False
    assert "forbidden" in results[1]["codex_reason"]

    # Third: valid code but invalid filename
    assert results[2]["codex_valid"] is True
    assert results[2]["filename_valid"] is False
