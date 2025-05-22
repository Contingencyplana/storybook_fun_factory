"""
Filename: s3_4_not_when_first_seen_but_when_reseen.py

Purpose:
This module filters anomaly signals based on whether they have been seen before.
Only signals that reoccur and match previous memory are passed through for action.

Philosophy:
The first appearance is just a whisper. The second, a declaration. We act not on first sight,
but on the echo that confirms presence.

Example Usage:
    filter = EchoBasedFilter()
    assert filter.should_act("alpha") is False
    assert filter.should_act("alpha") is True
"""

class EchoBasedFilter:
    def __init__(self):
        self.memory = set()

    def should_act(self, signal_id: str) -> bool:
        if signal_id in self.memory:
            return True
        self.memory.add(signal_id)
        return False
