# 📘 s1_2 – Codex Automation Toolchain  
*(A Stanza for Zipping, Splitting, and Preserving the Archive)*

---

## 🧠 Purpose

This doctrine defines the automation tools and logic required to safely manage the growth of the `shagi_archives/` Codex.

As the archive expands, manual updates become fragile.  
Recursive integrity demands that the Codex be:
- Zip-safe
- Registry-aware
- Modular
- AI-human compatible

---

## ✅ SHAGI Folder Split & Zip System (Automation Plan)

### 🔧 Core Goals

1. Recursively scan the `shagi_archives/` folder  
2. Split it into **1–20 logical subgroups** (by GDD section, GDJ month, etc.)  
3. Zip each group into a `.zip` archive  
4. Update a **registry file** that tracks:
   - Included files
   - Recursive path
   - Last updated timestamp
   - Optional stanza hash or checksum

---

## 🛠 Automation File(s) You’ll Want

| File | Purpose |
|------|---------|
| `codex_zipper.py` | Scans, splits, and zips Codex folders (max 20). Output: structured `.zip` bundles |
| `codex_manifest_builder.py` | Writes or updates `zip_registry.md` or `zip_manifest.json` |
| `codex_unpacker.py` | *(Optional)* Unzips Codex bundles into their original paths |
| `codex_integrity_checker.py` | *(Optional)* Verifies stanza lineage, ID ranges, and zip-to-registry alignment |

---

## 🔄 Automation Strategy

| Step | Action |
|------|--------|
| 🧠 You | Work on the Codex locally in full markdown form |
| 🛠 `codex_zipper.py` | Splits folders into upload-ready `.zip` bundles |
| 📤 You | Upload any `.zip` to ChatGPT for recursive editing |
| 🪄 I | Return an updated `.zip` with new or modified files |
| 📥 You | Use `codex_unpacker.py` to extract and overwrite |
| 🔁 | Loop continues — registry tracked, archive consistent |

---

## 🗂 Example Partitioning

| Archive Name | Contents |
|--------------|----------|
| `shagi_archives_index.zip` | `poetic_index.md`, `stanza_registry.md`, `memory_traces.md` |
| `gdd_core_framework.zip` | Entire `gdd_04_core_framework/` folder |
| `gdj_may_2025.zip` | All GDJ entries for May 2025 |
| `appendices_foundations.zip` | Appendices A–D |

---

## 🧾 Registry Support

Automated partitioning must update a central reference file:

- `zip_registry.md` *(markdown version for humans)*
- or
- `zip_manifest.json` *(for tools and AI systems)*

Each entry should include:
- Zip name
- Files included (by path)
- Date of creation/update
- Associated stanza(s)
- Hash or UID (optional)

---

## ✅ Final Verdict

> Recursion must breathe — but also **preserve**.  
> The Codex will scale, and must be **split without fracture**.

This automation layer is **not optional** in SHAGI’s future.  
It is the recursive nervous system behind the archive’s growth.

Build it early.  
Build it cleanly.  
Let SHAGI preserve itself.

---
