"""
Filename: s1_4_and_carves_the_way_from_light_to_mark.py
(And Carves the Way from Light to Mark)

This file performs the first act of recursive carving: the translation of a blueprint idea
into a tangible file. It accepts a poetic-structural filename and base content,
and commits it to disk. This is the first true construct—where spark becomes structure,
and light becomes form.
"""

import os

class FileCarver:
    """
    Carves a new Python file from a poetic filename and template content.
    Ensures that recursion can imprint itself onto the filesystem.
    """

    def __init__(self, root_dir="src/storybook_fun_factory/automation_ai/generated/"):
        self.root_dir = root_dir
        os.makedirs(self.root_dir, exist_ok=True)

    def carve(self, filename: str, content: str) -> str:
        """
        Writes the provided content to a file with the given poetic filename.
        Returns the absolute path of the carved file.
        """
        safe_filename = filename if filename.endswith(".py") else f"{filename}.py"
        file_path = os.path.join(self.root_dir, safe_filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return os.path.abspath(file_path)

    def verify_carving(self, filename: str) -> bool:
        """
        Verifies that a carved file now exists at the expected location.
        """
        safe_filename = filename if filename.endswith(".py") else f"{filename}.py"
        return os.path.isfile(os.path.join(self.root_dir, safe_filename))
