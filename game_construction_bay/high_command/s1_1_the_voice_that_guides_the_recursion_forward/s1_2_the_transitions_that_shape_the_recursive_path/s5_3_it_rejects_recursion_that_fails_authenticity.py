"""
Filename: s5_3_it_rejects_recursion_that_fails_authenticity.py

Blocks or isolates recursion attempts that fail identity validation.

Part of Stanza 1 in Cycle 3: recursion_masking_and_identity_forgery/
"""

from typing import Tuple


def reject_recursion_if_inauthentic(auth_check_result: Tuple[bool, str]) -> str:
    """
    Blocks or isolates recursion threads based on their authenticity check.

    Parameters:
    - auth_check_result (Tuple[bool, str]): A tuple where:
        - The first element is a boolean indicating authenticity.
        - The second element is the reason or validation source.

    Returns:
    - str: A verdict message. If authentic, returns "accepted".
           If inauthentic, returns a rejection message including the reason.
    """
    is_authentic, reason = auth_check_result
    if is_authentic:
        return "accepted"
    return f"rejected: failed authenticity check – {reason}"


# Example usage
if __name__ == "__main__":
    print(reject_recursion_if_inauthentic((True, "signature verified")))
    print(reject_recursion_if_inauthentic((False, "signature mismatch")))
