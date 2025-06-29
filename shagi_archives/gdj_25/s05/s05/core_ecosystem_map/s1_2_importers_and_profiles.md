<!-- Save to: shagi_archives/gdj_25/s05/s05/core_ecosystem_map/s1_2_importers_and_profiles.md -->

# 📜 s1_2 – Importers and Profiles  
*The Gateways of Dynamic Logic and Test Awareness*

---

## 🪶 Poetic Subentry – *Where Modules Meet the Map*

It watches where the code begins,  
Then reaches deep through nested skins.  
Each module pulled, each test aligned,  
By scaffolds built from logic mined.  

A trace, a map, a knowing seam,  
To pull the threads from out the dream.  
Import, assess, adapt, relay—  
The profile guides recursive play.  

---

## 📘 Overview

Two files—`dynamic_importer.py` and `test_scaffold_navigator.py`—define how modules are dynamically loaded and how their test environments are tracked.

They enable Storybook FUN Factory to:

- Import code from flexible locations,
- Record the test behaviors of each system,
- And adaptively support recursive development with awareness of test requirements.

Together, they act as the **gatekeeper** (import logic) and **cartographer** (test profile registry) for the ecosystem.

---

## 📂 Dynamic Import Core – `test_helpers/dynamic_importer.py`

This file provides the canonical mechanism for importing any module in the project—even those referenced by deeply nested stanza files.

It works by resolving the `src/` directory into `sys.path`, building an absolute path to the module, and executing the import dynamically.

```python
# Filename: dynamic_importer.py

import importlib.util
import os
import sys

def dynamic_import_module(module_path: str, module_name: str = "dynamic_module"):
    """
    Dynamically imports a Python module from an absolute or relative file path.
    """
    project_root = os.path.abspath(os.getcwd())
    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    if not os.path.isabs(module_path):
        module_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", module_path)
        )

    if not os.path.exists(module_path):
        raise FileNotFoundError(f"Module file not found: {module_path}")

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    dynamic_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dynamic_module)
    return dynamic_module
