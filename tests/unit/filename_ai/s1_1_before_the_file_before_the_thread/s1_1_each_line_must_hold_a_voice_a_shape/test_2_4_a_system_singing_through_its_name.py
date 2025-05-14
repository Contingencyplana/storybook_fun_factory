"""
Filename: test_2_4_a_system_singing_through_its_name.py
(Tests for recursive filename signature annotation in filename_ai)

This suite validates name normalization and signature attachment
from s2_4_a_system_singing_through_its_name.py using dynamic import.
"""

import os
import importlib.util
from pathlib import Path
import pytest

# Load dynamic_importer
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# Dynamically import the stanza module under test
project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "filename_ai",
        "s1_1_before_the_file_before_the_thread",
        "s1_1_each_line_must_hold_a_voice_a_shape",
        "s2_4_a_system_singing_through_its_name.py",
    )
)

# Access the function
annotate_filename_with_signature = module.annotate_filename_with_signature


def test_annotate_filename_with_signature():
    fn = annotate_filename_with_signature

    assert fn("whisper_to_flame.py") == "whisper_to_flame_sig.py"
    assert fn(" already_formatted_SIG.py ") == "already_formatted_sig.py"
    assert fn("multi___underscore--mess.py") == "multi_underscore_mess_sig.py"
    assert fn("__ends_in_sig_SIG.py") == "ends_in_sig_sig.py"
    assert fn("line.with.periods.py") == "line_with_periods_sig.py"
    assert fn("song that shall not end") == "song_that_shall_not_end_sig.py"
    assert fn("sig.sig.sig") == "sig_sig_sig.py"
    assert fn("  trail__lead...echo  ") == "trail_lead_echo_sig.py"
