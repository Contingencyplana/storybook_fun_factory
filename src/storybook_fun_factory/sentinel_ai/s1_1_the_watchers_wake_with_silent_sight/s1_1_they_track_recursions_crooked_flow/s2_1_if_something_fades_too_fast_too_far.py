"""
_2_1_if_something_fades_too_fast_too_far.py

Detects when recursive cycles dissipate prematurely, signaling that vital narrative
or logical flows are vanishing faster than sustainable stability allows.
"""

def detect_fading_recursion(recursive_cycles):
    """
    Observes the provided recursive cycles and identifies any that are fading
    (i.e., losing structure, coherence, or energy) too quickly compared to expected parameters.

    Args:
        recursive_cycles (list of dict): A list where each element represents a recursion cycle
            with associated metadata such as 'strength', 'coherence', and 'age'.

    Returns:
        list of dict: A list of recursion cycles that are flagged as fading too fast.
    """
    fading_cycles = []

    for cycle in recursive_cycles:
        strength = cycle.get('strength', 1.0)
        coherence = cycle.get('coherence', 1.0)
        age = cycle.get('age', 0)

        # Define threshold heuristics for premature fading
        if strength < 0.3 and coherence < 0.5 and age < 5:
            fading_cycles.append(cycle)

    return fading_cycles


# Example structure for future testing (not executable without test harness)
if __name__ == "__main__":
    sample_cycles = [
        {'id': 'loop_001', 'strength': 0.2, 'coherence': 0.4, 'age': 3},
        {'id': 'loop_002', 'strength': 0.8, 'coherence': 0.9, 'age': 7},
        {'id': 'loop_003', 'strength': 0.1, 'coherence': 0.3, 'age': 2},
    ]

    faded = detect_fading_recursion(sample_cycles)
    for cycle in faded:
        print(f"⚠️ Fading detected: {cycle['id']}")
