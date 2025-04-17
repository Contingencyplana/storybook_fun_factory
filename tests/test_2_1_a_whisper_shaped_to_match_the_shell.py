"""
tests/test_2_1_a_whisper_shaped_to_match_the_shell.py

Tests the format_poetic_slug function from filename_ai stanza
_2_1_a_whisper_shaped_to_match_the_shell.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from game_construction_bay.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import _2_1_a_whisper_shaped_to_match_the_shell


def test_format_poetic_slug():
    assert _2_1_a_whisper_shaped_to_match_the_shell.format_poetic_slug("the shell holds space and tone") == "the_shell_holds_space_and_tone"
    assert _2_1_a_whisper_shaped_to_match_the_shell.format_poetic_slug("  a     line     with   gaps  ") == "a_line_with_gaps"
    assert _2_1_a_whisper_shaped_to_match_the_shell.format_poetic_slug("emphasized__pause__line") == "emphasized__pause__line"
    assert _2_1_a_whisper_shaped_to_match_the_shell.format_poetic_slug("_leading and trailing_") == "leading_and_trailing"
    assert _2_1_a_whisper_shaped_to_match_the_shell.format_poetic_slug("") == "unnamed_slug"
