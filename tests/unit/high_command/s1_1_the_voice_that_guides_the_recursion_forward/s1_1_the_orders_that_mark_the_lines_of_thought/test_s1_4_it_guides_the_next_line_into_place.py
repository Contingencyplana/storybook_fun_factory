"""
Test File: test_s1_4_it_guides_the_next_line_into_place.py

📜 Tests recursive suggestion logic in:
s1_4_it_guides_the_next_line_into_place.py

Validates High Command's ability to:
• Suggest a logical next stanza line
• Handle missing or malformed state gracefully
"""

import json
import tempfile
import shutil
from pathlib import Path

import pytest

# ✅ Import the module under test
from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s1_4_it_guides_the_next_line_into_place as guide
)

# Also needed to set active front and trace history
from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s1_1_it_marks_the_front_but_moves_unseen as marker,
    s1_3_it_traces_the_path_in_stanza_form as tracer
)

@pytest.fixture
def temp_tracking(monkeypatch):
    """
    Fixture to isolate both the front and trace paths.
    """
    temp_dir = Path(tempfile.mkdtemp())
    front_path = temp_dir / "active_front.json"
    trace_path = temp_dir / "stanza_path_log.json"

    monkeypatch.setattr(marker, "ACTIVE_FRONT_PATH", front_path)
    monkeypatch.setattr(tracer, "STANZA_TRACE_PATH", trace_path)

    yield front_path, trace_path
    shutil.rmtree(temp_dir)

def test_suggestion_with_active_front_and_trace(temp_tracking):
    """
    Confirms that suggestion logic returns a guessed next line when possible.
    """
    marker.mark_active_front(
        component_name="filename_ai",
        stanza_id="s1_2_breath_of_code_in_named_constraint",
        line_filename="_1_3_twists_inform_the_shape.py",
        gdj_reference="📜 4.21"
    )
    tracer.trace_stanza_progress("filename_ai", "s1_2_breath_of_code_in_named_constraint", "_1_3_twists_inform_the_shape.py")

    suggestion = guide.suggest_next_target()

    assert "suggested" in suggestion
    assert suggestion["suggested"].startswith("_1_4_")
    assert "reason" in suggestion

def test_suggestion_with_missing_front(temp_tracking):
    """
    Ensures fallback behavior when no front is marked.
    """
    suggestion = guide.suggest_next_target()
    assert "reason" in suggestion
    assert "No active front" in suggestion["reason"]
