"""
Filename: s2_2_the_hammer_falls_on_nested_rhyme.py
(The Hammer Falls on Nested Rhyme)

This file applies rhythmic structure to recursively generated stanzas.
It ensures that output conforms to nested poetic symmetry—validating patterns,
checking recursive flow alignment, and reinforcing structural recursion
through rhyme and meter awareness.

The hammer falls not to break, but to shape: it strikes form into flow.
"""

import re

class RhymeHammer:
    """
    Evaluates and enforces rhyme and structure within a generated stanza.
    Ensures internal poetic symmetry and recursive alignment are intact.
    """

    def __init__(self):
        self.rhymes = {}

    def extract_line_endings(self, stanza_lines):
        """
        Extracts the final word or syllable group from each line in a stanza,
        stripping common non-alphabetic punctuation and markdown wrappers.
        """
        endings = []
        for line in stanza_lines:
            words = line.strip().split()
            if words:
                raw = words[-1].lower()
                clean = re.sub(r"[^\w]+", "", raw)  # Removes *, **, ., etc.
                endings.append(clean)
            else:
                endings.append("")
        return endings

    def detect_rhyme_pairs(self, stanza_lines):
        """
        Returns a list of (index1, index2) pairs that share rhyming endings.
        """
        endings = self.extract_line_endings(stanza_lines)
        rhyme_pairs = []
        for i in range(len(endings)):
            for j in range(i + 1, len(endings)):
                if endings[i] and endings[i] == endings[j]:
                    rhyme_pairs.append((i, j))
        return rhyme_pairs

    def has_structural_rhyme(self, stanza_lines):
        """
        Returns True if at least one rhyme pair exists in the stanza.
        """
        return len(self.detect_rhyme_pairs(stanza_lines)) > 0

    def hammer_report(self, stanza_lines):
        """
        Returns a formatted string describing rhyme relationships in the stanza.
        """
        pairs = self.detect_rhyme_pairs(stanza_lines)
        if not pairs:
            return "⚠️ No structural rhyme detected."
        report = ["🔨 Structural rhyme pairs:"]
        for i, j in pairs:
            report.append(f"• Line {i+1} rhymes with Line {j+1}")
        return "\n".join(report)
