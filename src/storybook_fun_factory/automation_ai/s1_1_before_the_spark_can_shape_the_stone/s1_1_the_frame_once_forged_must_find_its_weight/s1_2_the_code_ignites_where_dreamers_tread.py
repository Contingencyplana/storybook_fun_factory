"""
Filename: s1_2_the_code_ignites_where_dreamers_tread.py
(The Code Ignites Where Dreamers Tread)

This file represents the ignition point of dynamic automation. It takes symbolic input
from dreamers—user instructions, AI prompts, or recursive templates—and begins to
transform them into structured, functional code components. It simulates the very first
conversion spark within the assistant's forge.
"""

class CodeIgniter:
    """
    Transforms symbolic user input (a dream fragment) into a preliminary code form.
    Simulates the first stage of automation: symbolic parsing and code shaping.
    """

    def __init__(self, dream_fragment: str):
        self.dream_fragment = dream_fragment
        self.ignited = False
        self.output = ""

    def ignite(self):
        """
        Ignites the transformation by wrapping the dream fragment in a mock code structure.
        """
        if not self.dream_fragment.strip():
            self.output = "🔥 Ignition failed: empty input."
            self.ignited = False
        else:
            self.output = f"# Auto-generated code:\ndef dream():\n    return \"{self.dream_fragment}\""
            self.ignited = True

    def get_output(self):
        """
        Returns the resulting ignited code or a failure message.
        """
        return self.output

    def is_ignited(self):
        """
        Returns True if the dream fragment has been successfully ignited.
        """
        return self.ignited
