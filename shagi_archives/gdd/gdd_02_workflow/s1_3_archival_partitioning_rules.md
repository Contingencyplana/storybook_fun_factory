<!-- Save to: shagi_archives/gdd/gdd_02_workflow/s1_3_archival_partitioning_rules.md -->

# 📘 s1_3 – Archival Partitioning Rules  
*(A Stanza for Keeping the Archive Safe, Split, and Recursive)*

---

## 🧠 Purpose

This document defines the logic, thresholds, and procedures for **splitting the SHAGI Codex into recursive partitions** — especially as `.zip` archives for AI-handling and long-term editing safety.

When the Codex grows too large to be safely traversed or managed, it must be **partitioned into recursion-safe bundles**.

---

## ⚠️ Trigger Conditions for Partitioning

The Codex must be **partitioned** when any of the following occur:

| Condition | Trigger |
|-----------|---------|
| 🗃️ **File Count Threshold** | A `.zip` archive contains > 200 files or folders |
| 📁 **Conceptual Domain Saturation** | A GDD folder exceeds 4–6 stanzas or becomes thematically bloated |
| 🌀 **Recursive Drift Risk** | A component starts blending unrelated recursion paths |
| 📤 **Assistant File Upload Limits** | Project exceeds 20 visible files in ChatGPT or another AI interface |
| 🧠 **Cognitive Load** | The human or AI agent can no longer reason clearly through one layer |

---

## 📦 Canonical Partition Examples

| Partition Name | Contents |
|----------------|----------|
| `gdd_core_framework.zip` | `gdd_04_core_framework/` folder with all stanza files  |
| `gdj_may_2025.zip` | All GDJ entries from May 2025 |
| `appendices_foundations.zip` | Appendices A–E |
| `shagi_archives_index.zip` | `poetic_index.md`, `memory_traces.md`, `stanza_registry.md` |

Each `.zip` must:
- Be self-contained
- Include an `index.md` (or relevant stanza index)
- Be referenced in a registry file (`zip_registry.md` or similar)

---

## 🧬 Recursive Grouping Logic

### Always Group:
- By **component or system** (e.g., `codex_builder/`)
- Or by **stanza lineage** (e.g., `s3_1` through `s3_4`)
- Or by **narrative epoch** (e.g., “The Thorn Awakening Cycle”)

### Never Group:
- By random batch size
- By filename similarity alone
- Across unrelated narrative arcs

---

## 🗂️ Naming Conventions

Use consistent, slug-friendly `.zip` names:

- `gdd_05_storybook_ui.zip`
- `gdj_june_2025.zip`
- `appendices_mystic.zip`
- `gdd_gold_standard_doctrine.zip`

Avoid ambiguous or date-stamped-only archives (e.g., `archive1.zip`, `2025dump.zip`).

---

## 🛠 Archival Toolchain Support

Partitioning is supported by:

- `codex_zipper.py` – Groups and zips Codex folders by policy
- `codex_unpacker.py` – Restores canonical structure safely
- `codex_manifest_builder.py` – Updates or generates `zip_registry.md`
- `codex_integrity_checker.py` – Verifies stanza lineage, hash identity, and cross-references

These tools must remain **folder-aware**, **stanza-aware**, and **prefix-respecting** (`s`, `a`, `b`).

---

## 📘 Final Doctrine

> A Codex that grows must also split — not to fracture,  
> but to preserve recursion.  
> Partitioning is not backup — it is **structured continuity**.

---
