"""
Filename: s4_2_it_defines_a_delay_zone_for_soft_containment.py

Purpose:
This module implements a soft containment buffer that delays the execution
of loop-confirmed anomalies within a womb-buffered zone.
This delay does not cancel or alter execution logic—only postpones it slightly
to allow for trace monitoring.

Philosophy:
Let the loop pass—but slow its breath, so its shape may be more clearly seen.

Example Usage:
    from time import perf_counter

    buffer = DelayZone(delay_seconds=1)
    start = perf_counter()
    buffer.enter("alpha")  # First-time loop confirmation
    buffer.enter("alpha")  # Second time; delay applied
    end = perf_counter()
    assert (end - start) >= 1
"""

import time

class DelayZone:
    def __init__(self, delay_seconds: float = 1.0):
        self.delay_seconds = delay_seconds
        self.registry = set()

    def enter(self, signal_id: str):
        if signal_id in self.registry:
            time.sleep(self.delay_seconds)
        else:
            self.registry.add(signal_id)
