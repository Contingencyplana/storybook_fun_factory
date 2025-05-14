"""
Test File: test_s1_2_it_recites_the_focus_in_shifted_light.py

📜 Tests the diagnostic reflection logic in:
s1_2_it_recites_the_focus_in_shifted_light.py

Ensures the active recursive focus is summarized clearly and accurately.
"""
import json
import shutil
import tempfile
from pathlib import Path

import pytest

# ✅ Import the module under test
from storybook_fun_factory.game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_1_the_orders_that_mark_the_lines_of_thought import (
    s1_2_it_recites_the_focus_in_shifted_light as reciter
)

@pytest.fixture
def temp_active_front(monkeypatch):
    """
    Fixture to isolate the ACTIVE_FRONT_PATH to a temp directory.
    """
    temp_dir = Path(tempfile.mkdtemp())
    fake_path = temp_dir / "active_front.json"
    monkeypatch.setattr(reciter, "ACTIVE_FRONT_PATH", fake_path)
    yield fake_path
    shutil.rmtree(temp_dir)

def test_recite_focus_when_missing(temp_active_front, capsys):
    """
    Validates fallback output when no active front is set.
    """
    result = reciter.recite_active_focus(verbose=True)
    captured = capsys.readouterr().out

    assert result.startswith("🔕")
    assert "No active recursive front" in captured
