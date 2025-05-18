"""
s5_2_it_tags_lines_for_assistant_or_player_intervention.py

Tags anomalies that require human (assistant or player) review due to uncertainty, narrative impact,
or structural ambiguity. This allows recursive automation to defer critical judgment.
"""

from typing import List, Dict

ESCALATION_TAGS = {"human_review", "ambiguous", "story_conflict", "runtime_dispute"}

def tag_for_manual_intervention(anomalies: List[Dict]) -> List[Dict]:
    """
    Tags anomalies requiring manual (assistant/player) attention.

    Args:
        anomalies (List[Dict]): A list of anomaly records with optional 'tags' field (List[str]).

    Returns:
        List[Dict]: Anomalies that include any escalation tag.

    Example:
        >>> tag_for_manual_intervention([
        ...     {"id": "a1", "tags": ["overflow"]},
        ...     {"id": "a2", "tags": ["human_review", "ghost_trace"]}
        ... ])
        [{'id': 'a2', 'tags': ['human_review', 'ghost_trace']}]
    """
    return [a for a in anomalies if set(a.get("tags", [])) & ESCALATION_TAGS]
