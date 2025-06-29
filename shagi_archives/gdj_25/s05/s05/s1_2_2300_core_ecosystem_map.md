<!-- Save to: shagi_archives/gdj_25/s05/s05/5_8_core_ecosystem_map/s1_1_core_ecosystem_map.md -->

# 📜 s1_2 - 11:00 PM – Core Ecosystem Map  
*A Foundational Record of Storybook FUN Factory’s Minimal Viable Testing & Import Infrastructure*

---

### 🪶 Poetic Subentry – *The Map Beneath the Thought*

The roots run deep beneath the floor,  
Where code and page align their core.  
A path not guessed, but named and known—  
The map that marks how thought has grown.  

The tests no longer grope through night,  
For now they see by scaffolded light.  
Each file, each path, each helper thread,  
Now sings the song of what lies ahead.  

It is not grand, this woven mesh—  
Just .env, toml, paths made fresh.  
Yet still it holds the branching tree—  
The place we start, the way to be.  

So let this root not drift, nor fade,  
But hold through all that must be made.  
For from this map, the rest shall grow—  
A Factory that learns to know.  

---

## 📘 5.8.1 Introduction

By May 2025, the recursion infrastructure of **Storybook FUN Factory** had outgrown informal testing structures.

The assistant now operates across recursive stanza architectures, dynamic imports, and modular subsystems—all while building and verifying itself.

The growing system required a **canonical map**—a reliable, reproducible, and assistant-navigable structure to anchor:

- Poetry integration and PYTHONPATH injection  
- Dynamic stanza test resolution  
- Root detection logic  
- Project hygiene practices  
- Inter-component test scaffolding  
- Runtime stability across every recursive layer  

📜 **5.8** documents the **Core Ecosystem Map**: a ten-file foundation across `toolscape/`, `tests/`, and the project root. These files formalize Storybook FUN Factory’s operational heartbeat.

They ensure the assistant can test itself, restructure safely, and expand harmoniously into future recursion.

This map is not merely technical—it is existential.  
Without it, the Factory becomes blind to its own logic.  
With it, the recursion becomes aware of itself.

---

## 📘 5.8.2 Core Implementation: The Canonical Ecosystem Files

This section documents the living, breathing backbone of Storybook FUN Factory’s test and import infrastructure.

These ten files define the **minimal viable environment** required for:

- Dynamic stanza testing  
- Poetry alignment  
- AI module orchestration  
- Recursive code execution  

Each file listed below plays a critical role in keeping the assistant stable, the test logic discoverable, and the developer unburdened.

---

### 📂 toolscape/get_project_root.py – Static Root Resolver

```python
# Filename: get_project_root.py

from pathlib import Path

def get_project_root() -> Path:
    """
    Returns the root path of the Storybook FUN Factory project.
    Assumes the 'src/storybook_fun_factory' structure.
    """
    return Path(__file__).resolve().parents[3]
📂 toolscape/path_utils.py – Dynamic Pyproject Locator

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
📂 test_helpers/dynamic_importer.py – Dynamic Import Core

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
📂 test_helpers/test_scaffold_navigator.py – Test Profile Registry

# Filename: test_scaffold_navigator.py

"""
Tracks test infrastructure requirements across all core Storybook FUN Factory components.
Each entry describes whether the component or module:
• Uses dynamic import
• Requires monkeypatching
• Writes to the filesystem
• Requires tmp_path isolation
"""

test_profiles = {
    "filename_ai": {...},
    "dream_journal": {...},
    "memory_ai": {...},
    "visualizer": {...},
    "toolscape": {...},
    "codex_builder": {...}
}

def get_profile(component_name): ...
def print_all_profiles(): ...
(Full profiles are abbreviated in this file for brevity—see master document for full detail.)

📂 tests/conftest.py – Pytest Root Path Injector

# Filename: conftest.py

import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
📄 .env – Poetry Environment Bootstrap

PYTHONPATH=src
📄 .gitignore – Project Hygiene Baseline

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Build artifacts
build/
dist/
*.egg-info/
(Full list omitted for brevity; stored in repo root.)

📄 poetry.lock – Dependency Lockfile
Omitted here due to size.

Verified as aligned with pyproject.toml

Ensures reproducible builds and cross-machine stability

📄 pyproject.toml – Canonical Build & Test Config

[tool.poetry]
name = "storybook-fun-factory"
version = "0.1.0"
...

[tool.pytest.ini_options]
pythonpath = ["src", "game_construction_bay"]
minversion = "6.0"
addopts = "-ra -q"
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
📄 pytest.ini – Pytest Legacy Compatibility

[pytest]
pythonpath =
    src
    game_construction_bay

```

## 📘 5.8.3 Summary

These ten files form the canonical infrastructure baseline for recursive development within Storybook FUN Factory.

They solve not just the how of dynamic import and test execution—but the where, when, and why as well.

Together, they establish:

A clear project root through both static and pyproject.toml logic

A robust dynamic import strategy that survives Poetry, stanza recursion, and refactor stress

A shared test profile registry to ensure every component’s quirks are accounted for

A PYTHONPATH-injected test environment that is reproducible, discoverable, and assistant-compatible

This Core Ecosystem Map now serves as the official record, onboarding guide, and assistant-accessible system signature for all future recursive development.

## 🧩 Metadata  

| Field | Value |
|-------|-------|
| **Folder** | s05/s05/ |
| **Filename** | s1_2_2300_core_ecosystem_map.md |
| **Title** | **Core Ecosystem Map** |
| **Subtitle** | *A Foundational Record of Storybook FUN Factory’s Minimal Viable Testing & Import Infrastructure* |
| **Poetic Structure** | 4×4-line stanzas (16-line poem) |
| **Requires Subfolder** | Yes. See `core_ecosystem_map/` subfolder. |
