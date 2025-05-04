# Filename: dynamic_importer.py

import importlib.util
import os
import sys

def dynamic_import_module(module_path: str):
    """
    Dynamically imports a Python module from an absolute or relative file path.

    Args:
        module_path (str): Absolute or relative path to the module .py file.

    Returns:
        module: The imported Python module object.
    """
    # ✅ Ensure 'src/' is in sys.path BEFORE importing the target module
    project_root = os.path.abspath(os.getcwd())
    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    # Resolve full absolute path to the module
    if not os.path.isabs(module_path):
        module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", module_path))

    # Load the module
    spec = importlib.util.spec_from_file_location("dynamic_module", module_path)
    dynamic_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dynamic_module)
    return dynamic_module
