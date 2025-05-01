"""
Filename: test_s1_4_to_meet_the_code_yet_not_transcend.py

Tests the validate_final_filename function from filename_ai stanza
_s1_4_to_meet_the_code_yet_not_transcend.py
"""

import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from storybook_fun_factory.filename_ai._1_1_before_the_file_before_the_thread._1_1_each_line_must_hold_a_voice_a_shape import _1_4_to_meet_the_code_yet_not_transcend

def test_validate_final_filename():
    # Valid cases
    assert _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("a_valid_filename.py")
    assert _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("poetic_slug_case.py")
    assert _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("x1_y2_z3.py")

    # Invalid endings
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("missing_extension")
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("wrong.txt")

    # Invalid characters
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("camelCase.py")
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("has-dash.py")
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("has space.py")
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("semi;colon.py")

    # Structure violations
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("_starts_with_underscore.py")
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("ends_with_underscore_.py")
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("double__underscore.py")

    # Reserved words
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("def.py")
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename("class.py")

    # Excessive length
    long_name = "a_" * 51 + "x.py"  # 102 chars including .py
    assert not _1_4_to_meet_the_code_yet_not_transcend.validate_final_filename(long_name)
