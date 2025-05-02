"""
Filename: s2_3_it_folds_the_thread_it_names_the_flame.py
(It Folds the Thread, It Names the Flame)

This file implements structural compounding logic. It receives poetic-functional inputs—
lines of recursive code or verse—and folds them into contextualized templates or sequences.
It then assigns names to these emergent constructs, preparing them for execution,
storage, or integration within broader automation cycles.

The folded thread remembers what it was—  
But becomes what it must be.
"""

import re
import hashlib

class ThreadFolder:
    """
    Compounds recursive poetic lines into cohesive unit structures,
    assigns symbolic or hashed identifiers, and prepares output for
    higher-order automation.
    """

    def __init__(self, namespace="flame"):
        self.namespace = namespace

    def fold_lines(self, lines):
        """
        Accepts a list of poetic-functional lines.
        Returns a single folded string with embedded structure.
        """
        return "\n".join(f"#> {line.strip()}" for line in lines if line.strip())

    def name_flame(self, folded_output):
        """
        Generates a symbolic name for the folded result based on content hash.
        """
        base = folded_output.encode("utf-8")
        digest = hashlib.sha1(base).hexdigest()[:8]
        return f"{self.namespace}_flame_{digest}"

    def fold_and_name(self, lines):
        """
        Combines folding and naming steps.
        Returns a dictionary with folded output and assigned name.
        """
        folded = self.fold_lines(lines)
        name = self.name_flame(folded)
        return {
            "folded_output": folded,
            "flame_name": name
        }
