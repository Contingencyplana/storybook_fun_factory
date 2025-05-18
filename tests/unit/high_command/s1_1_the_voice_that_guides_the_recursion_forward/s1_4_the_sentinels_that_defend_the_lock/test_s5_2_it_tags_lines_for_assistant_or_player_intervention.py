"""
test_s5_2_it_tags_lines_for_assistant_or_player_intervention.py

Tests tagging logic for anomalies that require human or assistant escalation.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import s5_2_it_tags_lines_for_assistant_or_player_intervention as tagger

def test_tags_human_review_anomaly():
    anomalies = [
        {"id": "x1", "tags": ["runtime_dispute"]},
        {"id": "x2", "tags": ["ambiguous"]},
        {"id": "x3", "tags": ["ghost_trace"]}
    ]
    result = tagger.tag_for_manual_intervention(anomalies)
    assert len(result) == 2
    assert result[0]["id"] == "x1"
    assert result[1]["id"] == "x2"

def test_no_escalation_needed():
    anomalies = [
        {"id": "ok1", "tags": ["overflow"]},
        {"id": "ok2", "tags": ["orphan"]}
    ]
    result = tagger.tag_for_manual_intervention(anomalies)
    assert result == []

def test_partial_overlap_tags():
    anomalies = [
        {"id": "c1", "tags": ["ambiguous", "structural_mismatch"]},
        {"id": "c2", "tags": ["story_conflict"]},
        {"id": "c3", "tags": []}
    ]
    result = tagger.tag_for_manual_intervention(anomalies)
    assert len(result) == 2
    assert any(a["id"] == "c1" for a in result)
    assert any(a["id"] == "c2" for a in result)
