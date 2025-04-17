"""
tests/test_2_3_four_lines_compose_the_form_in_flame.py

Tests the enforce_stanza_consistency function from filename_ai stanza
_2_3_four_lines_compose_the_form_in_flame.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from game_construction_bay.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import _2_3_four_lines_compose_the_form_in_flame


def test_enforce_stanza_consistency():
    fn = _2_3_four_lines_compose_the_form_in_flame.enforce_stanza_consistency

    input_filenames = [
        "  WHISPER__to__FLAME.py",
        "echo-chamber.py",
        "flame.song().py",
        "__Structure__Is___KEY__.PY",
        "invalid name with spaces",
        "already_good_filename.py"
    ]

    expected = [
        "whisper_to_flame.py",
        "echochamber.py",
        "flamesong.py",
        "structure_is_key.py",
        "invalidnamewithspaces.py",
        "already_good_filename.py"
    ]

    assert fn(input_filenames) == expected
