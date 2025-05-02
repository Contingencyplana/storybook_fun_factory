import importlib.util
import os
import sys

def dynamic_import_module(relative_module_path: str):
    """
    Dynamically imports a Python module from a relative file path.
    
    Args:
        relative_module_path (str): Path to the module file, relative to the test file.
        
    Returns:
        module: The imported Python module object.
    """
    # Ensure Poetry-style 'src/' is in sys.path
    project_root = os.path.abspath(os.getcwd())
    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    # Resolve the full absolute path to the target module
    module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", relative_module_path))
    spec = importlib.util.spec_from_file_location("dynamic_module", module_path)
    dynamic_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dynamic_module)
    return dynamic_module
