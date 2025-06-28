<!-- Save to: shagi_archives/gdj_25/s05/s03/s1_1_1605_canonizing_the_dynamic_import_test_methodology.md -->

# 📜 s1_1 - 4:05 PM – Canonizing the Dynamic Import Test Methodology

*A Standard for Recursive Module Testing in Storybook FUN Factory*

---

## 🪶 Poetic Subentry: The Import Path of Truth  

A test must know what paths to trace,  
What roots to hold, what forms to face.  
Not fixed, but flexed through rhyme and flame—  
Its imports shift, yet name remains.  

---

## 📘 5.5.1 Introduction

As **Storybook FUN Factory** evolves into a recursive, stanza-structured ecosystem, its **test framework** must evolve with it.

Early test files relied on static import paths to access target modules, but this approach quickly revealed critical fragilities:

- Hardcoded paths broke under Poetry  
- Recursive folder structures confused Python import resolution  
- Test discovery became inconsistent and brittle  

This entry formalizes the **Dynamic Import Test Methodology**—a protocol now adopted across all recursive components to ensure:

- Modular isolation  
- Poetry compatibility  
- Recursive alignment  
- AI-ready structure

---

## ❌ 5.5.2 The Problem With Static Imports

Early stanza test files used patterns like:

```python
from storybook_fun_factory.filename_ai._1_1_path.to.module import my_function
```

But this fails under common conditions:

- Running tests from outside the project root  
- Using `Path.cwd()` in runtime logic  
- Deeply nested recursive stanzas  
- Uninstalled module references in Poetry environments  
- Folder restructuring mid-cycle  

This fragility led to:

- Inconsistent test discovery  
- Broken imports  
- High maintenance cost  

---

## 🔧 5.5.3 The Dynamic Import Solution

To solve this, a helper module was created: `dynamic_importer.py`.  
It uses `importlib` to load modules by absolute file path at runtime.

import os
import importlib.util

### Load helper

helper_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../test_helpers/dynamic_importer.py")
)
spec = importlib.util.spec_from_file_location("dynamic_importer", helper_path)
dynamic_importer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)

✅ Dynamically Load a Target Module

project_root = os.path.abspath(os.getcwd())
module = dynamic_importer.dynamic_import_module(
    os.path.join(
        project_root,
        "src",
        "storybook_fun_factory",
        "<component>",
        "<cycle_folder>",
        "<stanza_folder>",
        "<target_file>.py",
    )
)

## 🧠 5.5.4 Accessing Functions After Import

Once imported dynamically, functions can be accessed as usual:

target_func = module.detect_subtle_deviation
log_func = module.log_hidden_trace
This allows test files to remain portable and path-agnostic, regardless of folder depth or Poetry installation state.

## 🧼 5.5.5 Monkeypatching for Path Safety

Modules often use `Path.cwd()` to determine log or output paths.  
This is dangerous in test environments.

✅ Safe Override:

```python
monkeypatch.setattr("pathlib.Path.cwd", lambda: tmp_path)
```

This forces all I/O during tests to occur within isolated temp paths.

It is essential for tests involving:

- Logging trace files  
- Writing memory state  
- Simulating recursive poetic output  

---

## 🔁 5.5.6 Reuse Protocol and Templates

This methodology must be used for:

- All stanza tests in recursive modules  
- Any file not registered in `__init__.py`  
- Any test involving file I/O, recursion, or trace behavior  

✅ Canonical Checklist

| Step | Description |
|------|-------------|
| 1 | Use `dynamic_importer.py` to load module |
| 2 | Access desired functions via `module` object |
| 3 | Monkeypatch `Path.cwd()` if necessary |
| 4 | Avoid `from ... import ...` statements in stanza tests |

This ensures resilience, modularity, and recursive integrity.

## ✅ 5.5.7 Summary

The Dynamic Import Test Methodology is now canon.

It empowers all future GDJ stanza tests to:

Function at any depth

Adapt to recursion and restructuring

Stay Poetry-safe

Simulate system behavior without side effects

No stanza test shall bypass this rule unless a superior documented alternative is approved.

## 🧩 Metadata

| Field | Value |
|-------|-------|
| **Folder** | s05/s03/ |
| **Filename** | s1_1_1605_canonizing_the_dynamic_import_test_methodology.md |
| **Title** | **Canonizing the Dynamic Import Test Methodology** |
| **Subtitle** | *A Standard for Recursive Module Testing in Storybook FUN Factory* |
| **Poetic Structure** | 1×4-line stanza (4-line poem) |
| **Requires Subfolder** | No |
