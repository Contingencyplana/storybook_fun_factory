<!-- Save to: shagi_archives/gdj_25/s05/s05/core_ecosystem_map/s1_3_bootstraps_and_baselines.md -->

# 📜 s1_3 - Bootstraps and Baselines  
*The Foundation of a Reproducible Recursion*

---

## 🪶 Poetic Subentry – *The Files Beneath the Flame*

Before the first test dares to run,  
Before recursion’s thread is spun,  
A scaffold waits, with scripts and keys,  
To shape the map beneath the breeze.  

No code can breathe without its root,  
No logic bloom without its boot.  
So here they lie—the silent crew—  
The files that let the thought flow through.  

---

## 📘 Overview

This entry explores the core bootstrap files and configuration baselines that underpin the **Storybook FUN Factory’s** reproducible test environment.

These files enable:

- Seamless Pytest configuration  
- PYTHONPATH control  
- Dependency locking  
- Clean project hygiene  
- Runtime stability across recursive stanzas

Grouped together, they form the passive infrastructure—the silent foundation beneath every recursive invocation.

---

## 📂 Pytest Root Path Injector – `tests/conftest.py`

This file injects the correct `src/` directory into `sys.path`, ensuring Python modules across the assistant can resolve during tests.

```python
# Filename: conftest.py

import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

```

📌 Key Traits:
🧠 Required for nearly all recursive test execution.

🛠️ Lightweight, but critical for dynamic importing.

🌱 Sits quietly in tests/, affecting everything indirectly.

📄 .env – Poetry Environment Bootstrap
This file ensures PYTHONPATH is set properly when Poetry launches a shell or subprocess.

```python

PYTHONPATH=src
📌 Key Traits:
🔁 Harmonizes runtime behavior between test runners and local dev shells.

📦 Critical for environment reproducibility.

📄 .gitignore – Project Hygiene Baseline
This file defines the hygiene rules for keeping the repo clean and focused.

```

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Build artifacts
build/
dist/
*.egg-info/

# Environments
.env
.venv
(Excerpted; full version lives in the repo root.)

📌 Key Traits:
🧼 Keeps the project clean for recursive automation and Poetry tooling.

🧭 Prevents accidental commits of temp directories or compiled junk.

📄 pyproject.toml – Canonical Build and Test Config
This file defines the core Poetry project structure and Pytest configuration.

```python

[tool.poetry]
name = "storybook-fun-factory"
version = "0.1.0"

[tool.pytest.ini_options]
pythonpath = ["src", "game_construction_bay"]
minversion = "6.0"
addopts = "-ra -q"
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"

```

📌 Key Traits:
🧱 The single most critical file in the entire bootstrap chain.

🔁 Ensures Poetry, Pytest, imports, and stanza logic all agree on config.

🧪 Controls test discovery and path resolution logic for the entire recursion suite.

📄 pytest.ini – Legacy Compatibility Layer
This optional file exists to mirror the behavior of pyproject.toml for older tooling or redundancy.

```python

[pytest]
pythonpath =
    src
    game_construction_bay

```

📌 Key Traits:
♻️ Exists for stability during test evolution.

🧪 Slight redundancy, but harmless and informative.

📄 poetry.lock – Dependency Lockfile
Though omitted here due to size, this file ensures reproducible builds across machines and environments.

It records exact versions of all packages used by Poetry.

📌 Key Traits:
🔒 Locks dependencies to known-good states.

🚀 Ensures your local, test, and CI environments behave the same.

📐 Matches tightly with pyproject.toml.

📘 Summary
These bootstrap files do not orchestrate logic directly—but they make logic possible.

Without them, recursive testing and stanza automation would fail silently or behave inconsistently.

Together, they form the silent floor of Storybook FUN Factory.

File	Role	Critical Function
conftest.py	PYTHONPATH injection	Enables module resolution for test logic
.env	Poetry environment	Ensures test environment agrees with runtime shell
.gitignore	Project hygiene	Keeps repo clean and automation-friendly
pyproject.toml	Build and test config	Defines structure, dependencies, and test settings
pytest.ini	Compatibility	Mirrors pytest config for legacy use
poetry.lock	Reproducibility	Locks all dependencies to known-good versions

Without bootstraps, the assistant drifts.
With them, recursion gains its ground.

## 🧩 Metadata  

| Field | Value |
|-------|-------|
| **Folder** | s05/s05/core_ecosystem_map/ |
| **Filename** | s1_3_bootstraps_and_baselines.md |
| **Title** | **Bootstraps and Baselines** |
| **Subtitle** | *The Foundation of a Reproducible Recursion* |
| **Poetic Structure** | 2×4-line stanzas (8-line poem) |
| **Requires Subfolder** | No |
