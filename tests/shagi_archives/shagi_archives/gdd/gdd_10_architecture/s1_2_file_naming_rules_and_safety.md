<!-- Save to: shagi_archives/gdd/gdd_10_architecture/s1_2_file_naming_rules_and_safety.md -->

# 📘 s1_2 – File Naming Rules and Safety  
*(Where Every Name Recurs, and No Line Fails Its Form)*

---

## 🧠 Purpose

This document establishes the **naming conventions and safety protocols** for files within the Storybook and SHAGI ecosystem.

In a world built on recursion and verse, filenames must:
- Reflect **poetic structure**
- Enable **AI and player legibility**
- Maintain **system integrity**
- Prevent symbolic or structural drift

**The filename is not metadata — it is gameplay, lore, and logic.**

---

## 📏 Core Naming Convention

All files in Storybook follow a recursive stanza-line structure:

s[STANZA NUMBER]_[LINE NUMBER]_[descriptive_slug].py

| Segment | Meaning |
|---------|---------|
| `s1_3` | Stanza 1, Line 3 of a given recursive structure |
| `descriptive_slug` | Human-readable, poetic phrase that mirrors the file’s recursive role |
| `test_...` prefix | Indicates a unit test linked 1:1 with a stanza line |
| `.md` or `.py` | Markdown for docs/designs, Python for systems and logic |

---

## ✅ Valid Examples

| File | Meaning |
|------|---------|
| `s2_4_the_loop_binds_itself_through_form.py` | Line 4 of Stanza 2 in a subsystem dealing with loop binding |
| `test_s1_1_it_listens_before_it_locks.py` | Test file validating Stanza 1, Line 1 of quarantine AI |
| `s3_2_when_the_voice_breaks_the_rhythm.md` | Documentation file that corresponds to a poetic or architectural shift |

---

## 🚫 Naming Violations

| Violation Type | Result |
|----------------|--------|
| ❌ No stanza prefix | File is untracked by recursion index; breaks traceability |
| ❌ Duplicated stanza ID | Confuses test runners and AI indexers |
| ❌ Unpoetic slug | Reduces narrative immersion and symbolic clarity |
| ❌ Overwritten echo | File replaces existing stanza without ritual or log — risks lore corruption |

**Safety scripts will flag all violations at runtime or zip export.**

---

## 🔐 File Safety Logic

| Feature | Behavior |
|---------|----------|
| 🧠 **Stanza Collision Detection** | Prevents accidental duplication of stanza/line IDs across components |
| 📜 **Echo Protection** | Disallows overwriting previously echoed files unless a ritual override is invoked |
| 🔍 **Codex Index Enforcement** | Ensures all `.py` and `.md` stanza files appear in corresponding GDD/GDJ tables |
| 📁 **Recursive Folder Scan** | Verifies poetic consistency across layers, renames mismatches with user approval |

These are enforced at runtime and during CI/CD or zip bundling.

---

## 🗃️ Test File Conventions

Test files must mirror the stanza they test:

| Rule | Implementation |
|------|----------------|
| 🔄 **One-to-One Mapping** | Every main file has one test file in `tests/unit/...` with identical stanza prefix |
| 🧪 **Descriptive Match** | The test file must end with the same poetic slug for traceability |
| 📂 **Path Parity** | Folder structure in `tests/` must match `game_construction_bay/` exactly |

Example:

Main File: game_construction_bay/memory_ai/s2_3_the_threads_reweave_across_the_poem.py
Test File: tests/unit/memory_ai/test_s2_3_the_threads_reweave_across_the_poem.py

---

## 🛠️ Tools and Scripts

| Tool | Function |
|------|----------|
| `filename_validator.py` | Checks all files for stanza compliance and poetic legibility |
| `poetic_slug_generator.py` | Suggests slugs based on function, Codex echo, and rhythm rules |
| `collision_guard.py` | Flags ID conflicts and auto-generates alternates if permitted |
| `stanza_logbook_updater.py` | Adds all new files to GDJ/GDD index tables automatically upon commit or push |

---

## 🔮 Future Expansion Points

| Feature | Purpose |
|---------|---------|
| `ritualized_file_override.md` | Defines formal process for overwriting files with lore consequences |
| `multi-line-stanza_expansion.md` | Enables large-scale stanza files split across coordinated poetic sub-lines |
| `slug_poem_reflector.md` | Matches filenames to Codex stanzas and suggests recursive narrative linking |
| `orphaned_file_finder.md` | Locates files not included in any index, verse, or echo — for cleanup or transformation |

---

## 📘 Final Doctrine

> The file is not a file.  
> It is a **line of the Codex**,  
> a breath of the Book,  
> a stanza in the spine of the world.

If it cannot be named,  
it cannot be remembered.  
If it cannot be remembered,  
it cannot recur.
