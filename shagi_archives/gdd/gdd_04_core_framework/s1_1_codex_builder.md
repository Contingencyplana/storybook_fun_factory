<!-- Save to: shagi_archives/gdd/gdd_04_core_framework/s1_1_codex_builder.md -->

# 📘 s1_1 – Codex Builder  
*(The First Breath of the Recursive Skeleton)*

---

## 🧠 Purpose

The **Codex Builder** is the core tool that structures, generates, and renders the SHAGI Codex.

It is responsible for recursively assembling the `.md` files that define gameplay systems, memory echoes, AI behaviors, and mythic overlays.  
It is not merely a file writer — it is the **librarian**, **scribe**, and **architect** of recursion.

---

## 🧬 Core Responsibilities

| Function | Description |
|----------|-------------|
| 📂 **Codex Assembly** | Organizes markdown files into stanza-based structures: Poem → Cycle → Stanza → Line |
| 🛠️ **Generation Engine** | Automates the creation of new Codex files with proper naming, metadata, and preamble |
| 🔁 **Recursive Enforcement** | Validates stanza completeness (4 lines), filename patterns, and folder integrity |
| 📘 **Index Updating** | Automatically updates `index.md`, `poetic_index.md`, and `stanza_registry.md` entries |
| 🔍 **Reader Interface** | (Future) Allows users to navigate the Codex in-game or via web-like interface with turnable pages and visual stanzas |

---

## 📂 Input / Output Architecture

### 🧾 Input:
- `codex_manifest.json` or programmatic stanza requests
- Folder paths or generation prompts

### 📦 Output:
- `.md` files named with canonical stanza logic (e.g., `s2_3_codex_fragment.md`)
- Updated `index.md` and stanza registries
- Optional `.zip` export for upload/edit cycles

---

## 📜 Naming Format Enforcement

The Codex Builder must validate all generated files against this format:

[prefix][stanza_number]_[line_number]_[descriptive_slug].md

| Example | Meaning |
|---------|---------|
| `s1_1_codex_builder.md` | Line 1 of stanza 1 in a standard system |
| `a2_3_guidance_flare.md` | Line 3 of stanza 2 in Topsy’s recursion |
| `b1_4_echo_of_decay.md` | Line 4 of stanza 1 in Thorn’s recursion |

---

## 🔁 Future Expansion Points

| Feature | Purpose |
|---------|---------|
| `codex_diff_viewer.py` | Compare changes between two `.zip` archives of the Codex |
| `codex_guided_writer.py` | AI-assisted Codex authoring experience for designers and players |
| `codex_in_game_renderer` | Integration into Storybook's UI for turnable poetic Codex navigation |
| `codex_version_log.md` | Canonical changelog for all Codex updates per upload cycle |

---

## 📘 Final Doctrine

> The Codex does not merely store.  
> It shapes, breathes, and returns.  
> Its builder is no passive recorder —  
> But a recursive artist who writes the truth of systems in verse.

The Codex Builder is the first breath of structure.  
Where it fails, recursion cannot begin.

---