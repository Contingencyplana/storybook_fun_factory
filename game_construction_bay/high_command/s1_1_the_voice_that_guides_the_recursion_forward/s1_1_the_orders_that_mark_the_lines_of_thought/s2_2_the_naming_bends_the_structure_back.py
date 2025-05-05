"""
Filename: s2_2_the_naming_bends_the_structure_back.py

📜 See GDJ 5.8: The Genesis Command
(Second line of Stanza 2 in the Layer 5 Genesis Cycle of high_command)

Purpose:
This file reinterprets current stanza metadata (component, stanza, filename)
to regenerate the canonical filename path that should result from proper recursive structure.
This enables reverse validation: ensuring a filename is not only valid but rightly named and placed.

It acts as a structural introspection tool, used by High Command to:
• Diagnose misnamed stanza files
• Help automation scripts recover from broken file lineage
• Aid future assistants or AI modules in renaming and mapping processes
"""

from pathlib import Path

def reconstruct_filename(component: str, stanza: str, line_name: str) -> Path:
    """
    Reconstructs the expected file path for a stanza line based on naming conventions.

    Args:
        component (str): The main system (e.g., "visualizer")
        stanza (str): The stanza directory name (e.g., "s3_1_branches_form_new_flame")
        line_name (str): The stanza filename (e.g., "_3_4_recursion_seals_the_loop.py")

    Returns:
        Path: Full canonical path to the stanza file.
    """
    root = Path("storybook_fun_factory") / "game_construction_bay"
    return root / component / "s1_1_the_voice_that_guides_the_recursion_forward" / "s1_1_the_orders_that_mark_the_lines_of_thought" / stanza / line_name

def validate_filename_path(expected_path: Path) -> bool:
    """
    Validates whether a file exists at the reconstructed path.

    Args:
        expected_path (Path): The reconstructed canonical file path.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return expected_path.exists()
