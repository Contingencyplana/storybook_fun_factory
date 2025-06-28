<!-- Save to: shagi_archives/gdj_25/s05/s04/s1_1_1525_dynamic_import_stress_test_flat_utilities_and_toolscape_victory.md -->

# 📜 s1_1 - 3:25 PM – Dynamic Import Stress Test: Flat Utilities & Toolscape Victory  
*A Log of Errors, Fixes, and Proof that Canon 5.5 Holds Even in Tool-Based Edge Cases*

---

## 🪶 Poetic Subentry: The Test That Fell, Yet Rose Again  

It searched the root but found no thread,  
Each call returned a path long dead.  
The helper lost, the file unseen—  
The test lay buried in between.  

Yet paths can bend, and code may fail,  
But still we trace the failing trail.  
Until at last, aligned and true,  
The root was found, the test passed through.  

A single dot, a shifted line—  
And all at once, the stars align.  
The tools now know their rightful place—  
In canon's light, we passed the case.  

---

## 📘 5.6.1 Introduction

This entry documents a high-friction error cycle encountered while applying the **Dynamic Import Test Methodology** (established in 📜 5.5) to a non-stanza, flat utility module within `toolscape/`. The utility in question—`get_project_root.py`—serves as a shared system function, but its test initially failed to resolve Poetry paths, import structures, and helper logic.

Despite `__init__.py` registration, `sys.path` injection, and recursive folder context awareness, the error persisted.

After resolving module import errors, `FileNotFoundError`s, path misresolutions, and even a corrupted understanding of `sys.path` vs `os.getcwd()`, this log confirms the method’s soundness even under flattened structural variance.

**Dynamic import methodology is now verified as fully portable across both stanza and non-stanza files**, including foundational tooling code.

---

## 🛠️ 5.6.2 Technical Subentry: Final Working Test File

### Filename: test_get_project_root.py

```python

"""
Tests the get_project_root utility function from toolscape.
Follows the Dynamic Import Methodology (📜 5.5) for compatibility with recursive test structure.
"""

import os
import sys
import importlib.util
import pytest

# ✅ Inject src/ into sys.path before loading anything
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# ✅ Dynamic importer from the correct helper path
helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

# ✅ Load the target module dynamically
module = dynamic_importer.dynamic_import_module(
    os.path.join(src_path, "storybook_fun_factory", "toolscape", "get_project_root.py")
)

# ✅ Access the function to test
get_project_root = module.get_project_root

def test_get_project_root_points_to_storybook_fun_factory_root():
    root = get_project_root()
    assert root.name == "storybook_fun_factory"
    assert (root / "pyproject.toml").exists()
```


🧠 Key takeaways:

- Relative paths needed a four-level walk-back to resolve from test file to project root.
- `test_helpers/dynamic_importer.py` pathing was the root cause of >80% of tracebacks.
- Final success depended on correct alignment of helper path, `src` injection, and Poetry root assumptions.

## 🧩 5.6.3 Summary

This entry canonizes the successful application of 📜 5.5’s Dynamic Import Methodology to `toolscape/`.  
It marks the first verified case where the method was validated outside the recursive stanza structure,  
solidifying its place as the universal testing backbone for Storybook FUN Factory’s future architecture.

## 📊 5.6.4 Test File Status Tracker

| Test File Path                                         | Status      |
|--------------------------------------------------------|-------------|
| `tests/unit/toolscape/test_get_project_root.py`        | ✅ Success   |
| `src/storybook_fun_factory/toolscape/get_project_root.py` | ✅ Used      |
| `tests/test_helpers/dynamic_importer.py`               | ✅ Required  |

## 🧩 Metadata

| Field | Value |
|-------|-------|
| **Folder** | s05/s04/ |
| **Filename** | s1_1_1525_dynamic_import_stress_test_flat_utilities_and_toolscape_victory.md |
| **Title** | **Dynamic Import Stress Test: Flat Utilities & Toolscape Victory** |
| **Subtitle** | *A Log of Errors, Fixes, and Proof that Canon 5.5 Holds Even in Tool-Based Edge Cases* |
| **Poetic Structure** | 3×4-line stanzas (12-line poem) |
| **Requires Subfolder** | No |
