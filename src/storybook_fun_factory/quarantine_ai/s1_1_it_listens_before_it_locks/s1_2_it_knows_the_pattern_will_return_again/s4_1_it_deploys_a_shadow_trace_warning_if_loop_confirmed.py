"""
Filename: s4_1_it_deploys_a_shadow_trace_warning_if_loop_confirmed.py

Purpose:
This module issues a soft shadow trace warning when an anomaly is confirmed as a loop.
It logs the signal for future containment planning but does not halt or block execution.

Philosophy:
Where there is confirmation, there need not yet be containment—only acknowledgment.

Example Usage:
    tracer = ShadowTraceWarningSystem()
    tracer.warn_if_loop_confirmed("loop_alpha", confirmed=True)
    assert tracer.was_warned("loop_alpha") is True
"""

class ShadowTraceWarningSystem:
    def __init__(self):
        self.shadow_warnings = set()

    def warn_if_loop_confirmed(self, signal_id: str, confirmed: bool):
        if confirmed:
            self.shadow_warnings.add(signal_id)

    def was_warned(self, signal_id: str) -> bool:
        return signal_id in self.shadow_warnings
