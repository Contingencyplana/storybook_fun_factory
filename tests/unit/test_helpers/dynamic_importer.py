# dynamic_importer.py

import importlib.util
import os

def dynamic_import_module(relative_module_path):
    """
    Dynamically imports a Python module from a relative file path.
    
    Args:
        relative_module_path (str): Path to the module file, relative to the test file.
        
    Returns:
        module: The imported Python module object.
    """
    module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", relative_module_path))
    spec = importlib.util.spec_from_file_location("dynamic_module", module_path)
    dynamic_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dynamic_module)
    return dynamic_module
