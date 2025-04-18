"""
tests/test_2_4_a_system_singing_through_its_name.py

Tests the annotate_filename_with_signature function from filename_ai stanza
_2_4_a_system_singing_through_its_name.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from game_construction_bay.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import (
    _2_4_a_system_singing_through_its_name
)


def test_annotate_filename_with_signature():
    fn = _2_4_a_system_singing_through_its_name.annotate_filename_with_signature

    assert fn("whisper_to_flame.py") == "whisper_to_flame_sig.py"
    assert fn(" already_formatted_SIG.py ") == "already_formatted_sig.py"
    assert fn("multi___underscore--mess.py") == "multi_underscore_mess_sig.py"
    assert fn("__ends_in_sig_SIG.py") == "ends_in_sig_sig.py"
    assert fn("line.with.periods.py") == "line_with_periods_sig.py"
    assert fn("song that shall not end") == "song_that_shall_not_end_sig.py"
    assert fn("sig.sig.sig") == "sig_sig_sig.py"  # ✅ Matches actual logic
    assert fn("  trail__lead...echo  ") == "trail_lead_echo_sig.py"
