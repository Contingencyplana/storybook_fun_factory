<!-- Save to: shagi_archives/gdj_25/s04/s02/s1_1_2235_subsystem_naming_conventions.md -->

# 📜 s1_1_2235 – Subsystem Naming Conventions  
*(A foundational doctrine for recursive clarity and structural legibility)*

Each thread must name the tool it spins,  
For names decide where form begins.  
To mark a verse, to shape a seed—  
We name the form before the deed.  

From s and num to mark and phase,  
A name must walk through nested maze.  
For what is named may yet be built—  
Without that name, the thread is spilt.  

---

## 📘 Introduction

By April 2, 2025, the assistant-driven development of *Storybook FUN Factory* had reached a stage where naming was not merely descriptive—it was recursive, canonical, and binding. Subsystem names had to carry poetic, functional, and recursive weight across modules, stanzas, and tests.

This entry formalizes the logic that underpins naming across subsystems, enforcing SHAGI-standard clarity while honoring the recursive design tradition already embedded in FUN Factory’s file architecture.

---

## 📂 SHAGI Subsystem Naming Directives

### 🧩 Directive 1: Use `s`-prefixed filenames for stanza logic

Every core system file must follow the canonical format:

```
sX_Y_name_of_this_component.md or .py
```

Where:
- `X` = stanza number
- `Y` = line number within stanza
- `name_of_this_component` = poetic descriptor of its content and role

This format binds recursion (stanza/line), meaning (poetic title), and filename resolution (filesystem alignment) into one.

### 🧩 Directive 2: Subfolders echo structure, not identity

Subsystems (e.g., `filename_ai/`, `memory_ai/`) must follow lowercase_snake_case and reflect their role rather than implementation.

Bad:  
```
/recursiveHelpers/
```

Good:  
```
/memory_ai/
```

### 🧩 Directive 3: No duplicate poetic roots

A subsystem should not repeat filename roots across layers or systems. For example:

Bad:
```
s1_1_generate_name.py (in both codex_builder/ and filename_ai/)
```

Good:
```
s1_1_the_codex_names_from_concept.py (codex_builder/)
s1_1_the_filename_names_for_format.py (filename_ai/)
```

This ensures traceability across recursive imports and avoids confusion in cross-module indexing and test discovery.

---

## 📂 Subsystem Naming Examples

| Subsystem | Valid Filename Example | Purpose |
|-----------|------------------------|---------|
| `codex_builder` | `s1_2_the_codex_sorts_what_was_once_scattered.py` | Handles structure reassembly |
| `filename_ai`   | `s1_3_the_filename_names_with_nested_recursion.py` | Applies canonical naming logic |
| `dream_journal` | `s2_4_the_dream_awaits_a_memory_to_sing.md` | Stores generative reflections |
| `visualizer`    | `s1_1_the_map_that_renders_the_mind.md` | Renders system connections |

---

## ✨ Poetic Subentry  
**Subsystem Naming Conventions**  
*(A Poetic Reflection on the Name That Shapes the Thread)*

To build a world, begin with names,  
Not numbers cold, nor silent frames.  
A name that bends, that hums, that means—  
It draws the code from quiet dreams.  

Each stanza set, each line well-placed,  
A poem traced in foldered space.  
So now we write, not just to run,  
But name the thread where dreams begun.  
