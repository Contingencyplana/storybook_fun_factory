"""
tests/test_1_1_a_verse_is_born_but_cannot_live.py

Tests the poetic_line_status function from filename_ai stanza
_1_1_a_verse_is_born_but_cannot_live.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from game_construction_bay.filename_ai.the_voice_that_names_the_form.the_styles_that_bind_the_line import _1_1_a_verse_is_born_but_cannot_live


def test_poetic_line_status():
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("The Light That Shaped the Sky") == "latent"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("a_whisper, shaped...") == "latent"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("  trailing_space  ") == "latent"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("the_light_that_shaped_the_sky") == "valid"
    assert _1_1_a_verse_is_born_but_cannot_live.poetic_line_status("whispered_rhythm_in_code") == "valid"
