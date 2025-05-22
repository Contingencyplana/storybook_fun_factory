"""
Filename: s4_3_it_enables_a_reversible_pre_lock_on_suspect_patterns.py

Purpose:
This module allows loop-confirmed anomalies to be temporarily pre-locked.
These pre-locks are reversible, allowing execution to proceed if the anomaly
does not persist or escalate beyond the configured observation window.

Philosophy:
The lock should be ready, but not closed. It must wait with purpose, not fear.

Example Usage:
    lock = ReversiblePreLock()
    assert lock.is_locked("omega") is False
    lock.pre_lock("omega")
    assert lock.is_locked("omega") is True
    lock.revoke("omega")
    assert lock.is_locked("omega") is False
"""

class ReversiblePreLock:
    def __init__(self):
        self.locked_signals = set()

    def pre_lock(self, signal_id: str):
        self.locked_signals.add(signal_id)

    def is_locked(self, signal_id: str) -> bool:
        return signal_id in self.locked_signals

    def revoke(self, signal_id: str):
        self.locked_signals.discard(signal_id)
