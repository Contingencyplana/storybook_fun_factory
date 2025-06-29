<!-- Save to: shagi_archives/gdj_25/s05/s05/core_ecosystem_map/s1_1_static_and_dynamic_roots.md -->

# 📜 s1_1 - Static and Dynamic Roots  
*Mapping the Foundation Beneath the Recursion*

---

## 🪶 Poetic Subentry – *Where All Roots Begin*

The roots we need are not a guess,  
But pathways marked in consciousness.  
A fixed resolve, a shifting trace,  
That guides the flow through nested space.  

One reaches up from folder base,  
Another walks the stanza’s face.  
Together they define the ground—  
The place where logic can be found.  

---

## 📘 Overview

To support recursive stanza testing and assistant awareness, Storybook FUN Factory requires deterministic resolution of the **project root**. This is accomplished through two complementary Python utilities:

- A **static resolver** that climbs a fixed directory structure (used for simple direct access),
- A **dynamic resolver** that climbs until it finds `pyproject.toml` (used when location flexibility is needed).

Together, they support every recursive test case, automation module, and assistant-aware subprocess in the project.

---

## 📂 Static Root Resolver – `toolscape/get_project_root.py`

This method assumes the standard directory structure rooted in `src/storybook_fun_factory`. It is fast, deterministic, and brittle if directory layouts change.

```python
# Filename: get_project_root.py

from pathlib import Path

def get_project_root() -> Path:
    """
    Returns the root path of the Storybook FUN Factory project.
    Assumes the 'src/storybook_fun_factory' structure.
    """
    return Path(__file__).resolve().parents[3]

```

## 📌 Key Traits:

⚡ Fast and reliable in stable setups.

🚫 Brittle if the repo is restructured or invoked from edge scripts.

✅ Ideal for utilities, static helpers, or deployment scripts.

📂 Dynamic Root Resolver – toolscape/path_utils.py
This method is more adaptive. It searches upward from the current file path until it locates a pyproject.toml. It tolerates flexible entry points and nested stanza scripts.

```python
# Filename: path_utils.py

import os
from pathlib import Path

def get_project_root() -> Path:
    """Return the root directory of the Storybook FUN Factory project."""
    current = Path(__file__).resolve()
    while current != current.parent:
        if (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise FileNotFoundError("Could not locate pyproject.toml to determine project root.")

```

## 📌 Key Traits:

🔄 Resilient across recursive test invocations.

🧭 Ideal for notebooks, stanza walkers, and dynamic importers.

🔍 Slower and riskier if the file system is unusually large or symbolic.

## 📘 Summary

These two files—get_project_root.py and path_utils.py—establish the floor beneath recursion. They are the foundation that all stanza logic, imports, and test frameworks stand upon.

| File               | Role             | Strength         | Risk                         |
|--------------------|------------------|------------------|------------------------------|
| get_project_root.py | Static Resolver  | Fast, simple      | Assumes path depth           |
| path_utils.py       | Dynamic Resolver | Flexible, robust  | Slightly slower, may overscan |

Without these root locators, the assistant cannot find itself.
With them, recursion can recurse with awareness.

## 🧩 Metadata  

| Field | Value |
|-------|-------|
| **Folder** | s05/s05/core_ecosystem_map/ |
| **Filename** | s1_1_static_and_dynamic_roots.md |
| **Title** | **Static and Dynamic Roots** |
| **Subtitle** | *Mapping the Foundation Beneath the Recursion* |
| **Poetic Structure** | 2×4-line stanzas (8-line poem) |
| **Requires Subfolder** | No |
