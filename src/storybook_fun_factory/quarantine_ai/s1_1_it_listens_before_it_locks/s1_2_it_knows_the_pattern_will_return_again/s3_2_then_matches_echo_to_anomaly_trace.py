"""
Filename: s3_2_then_matches_echo_to_anomaly_trace.py

Purpose:
This module implements echo-to-anomaly trace matching for deferred signals.
When a signal reappears, this system checks whether its content and signature
match a previously recorded low-confidence anomaly. If so, the system affirms the match.

Philosophy:
It is not enough for the signal to return — it must resemble what was once recorded
in its anomaly form. The echo must trace its origin.

Example Usage:
    matcher = EchoMatcher()
    matcher.remember_anomaly("id_abc", {"key": "value"})
    result = matcher.match_echo("id_abc", {"key": "value"})
    assert result is True
"""

class EchoMatcher:
    def __init__(self):
        self.anomaly_memory = {}

    def remember_anomaly(self, signal_id: str, signal_payload: dict):
        self.anomaly_memory[signal_id] = signal_payload

    def match_echo(self, signal_id: str, echo_payload: dict) -> bool:
        stored = self.anomaly_memory.get(signal_id)
        return stored == echo_payload if stored else False
