"""
Filename: s2_1_the_ember_stirs_the_lines_align.py
(The Ember Stirs, the Lines Align)

This file begins the alignment process of poetic-functional input lines into structured,
ordered templates. It reads symbolic input (such as poetic verse, stanza titles, or
abstract descriptions) and converts them into line-aware blueprint scaffolds, ready
for recursive generation.

This is the ember before full ignition: the logic that places the lines where
they must go, forming the skeletal blueprint from which recursion will carve deeper.
"""

class LineAligner:
    """
    Aligns poetic-functional input into structured, line-aware blueprint format.
    """

    def __init__(self):
        self.aligned_lines = []

    def align_lines(self, input_block: str) -> list:
        """
        Processes a multiline input block into aligned, ordered blueprint lines.
        Trims and structures each line, discarding empties and maintaining poetic flow.
        """
        self.aligned_lines = [
            line.strip() for line in input_block.strip().splitlines() if line.strip()
        ]
        return self.aligned_lines

    def get_line(self, index: int) -> str:
        """
        Retrieves a specific aligned line by index. Returns an error message if out of range.
        """
        if 0 <= index < len(self.aligned_lines):
            return self.aligned_lines[index]
        return "⚠️ Invalid line index."

    def total_lines(self) -> int:
        """
        Returns the total number of aligned lines.
        """
        return len(self.aligned_lines)
