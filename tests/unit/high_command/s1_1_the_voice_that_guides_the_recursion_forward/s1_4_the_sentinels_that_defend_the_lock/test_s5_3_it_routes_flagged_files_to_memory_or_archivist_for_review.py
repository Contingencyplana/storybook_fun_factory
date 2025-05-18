"""
test_s5_3_it_routes_flagged_files_to_memory_or_archivist_for_review.py

Tests routing logic for flagged anomalies.
"""

import pytest
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import s5_3_it_routes_flagged_files_to_memory_or_archivist_for_review as router

def test_routes_to_memory_ai():
    anomalies = [{"id": "m1"}, {"id": "m2"}]
    result = router.route_anomalies(anomalies, destination="memory_ai")
    assert "memory_ai" in result
    assert result["memory_ai"] == anomalies

def test_routes_to_archivist_ai():
    anomalies = [{"id": "a1"}]
    result = router.route_anomalies(anomalies, destination="archivist_ai")
    assert "archivist_ai" in result
    assert result["archivist_ai"] == anomalies

def test_invalid_destination_raises_error():
    with pytest.raises(ValueError):
        router.route_anomalies([{"id": "z1"}], destination="black_hole")
