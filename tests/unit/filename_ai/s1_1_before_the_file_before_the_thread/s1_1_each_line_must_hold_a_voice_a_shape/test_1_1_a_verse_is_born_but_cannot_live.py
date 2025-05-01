"""
Filename: test_s1_1_a_verse_is_born_but_cannot_live.py

Tests the poetic_line_status function from filename_ai stanza
_s1_1_a_verse_is_born_but_cannot_live.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from storybook_fun_factory.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import _1_1_a_verse_is_born_but_cannot_live

def test_poetic_line_status():
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("The Light That Shaped the Sky") == "latent"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("a_whisper, shaped...") == "latent"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("  trailing_space  ") == "latent"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("the_light_that_shaped_the_sky") == "valid"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("whispered_rhythm_in_code") == "valid"
