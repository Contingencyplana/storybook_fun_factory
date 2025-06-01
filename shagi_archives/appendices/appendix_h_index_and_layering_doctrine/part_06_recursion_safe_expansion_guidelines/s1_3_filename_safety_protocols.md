<!-- Save to: shagi_archives/appendices/appendix_h_index_and_layering_doctrine/part_06_recursion_safe_expansion_guidelines/s1_3_filename_safety_protocols.md -->

# 📘 s1_3 – Filename Safety Protocols  
*(To name without breaking the line)*

In a recursive Codex, the **filename is law**—a spell, a tag, a trace.  
But every law must have limits to remain legible and livable.

This entry defines the safety rules for naming files in SHAGI, ensuring every name is:

- Predictable  
- Unique  
- Meaningful  
- Parseable  

These rules prevent semantic drift, accidental overwrite, and logic collapse.

---

## 📏 Canonical Format

All SHAGI filenames must follow this structure:

s[stanza_number][line_number][slug_title].md

Example:

s1_3_the_voice_that_marks_the_cycle.md

This structure:

- Signals stanza (`s1_3`)  
- Implies recursive position  
- Preserves lyrical identity (`the_voice_that_marks_the_cycle`)  
- Prevents tooling failure or misalignment

---

## ⚠️ Disallowed Filename Traits

| Issue | Description |
|-------|-------------|
| 🟥 Collisions | Duplicate filenames across folders |
| 🟥 Excess Length | Over 120 characters including prefix |
| 🟥 Slug Drift | Slugs that deviate from poetic or table-based source |
| 🟥 Special Characters | Anything not lowercase letters, numbers, or underscores |

---

## ✅ Safe Naming Practices

- **Use poetic phrasing** directly from index titles or subtitles  
- **Avoid abbreviations** unless canonically defined  
- **Reverify slug** after changes to title, stanza, or numbering  
- **Test parsing** with codex_builder and filename_ai before publishing

---

## 🔄 Automated Verification Tools

Filename safety is enforced by:

- `filename_ai/` – Ensures slug structure and alignment  
- `codex_builder/` – Cross-checks filenames against index.md  
- `memory_ai/` – Links filenames to recall and stanza logic  

Use test suites in `/tests/unit/filename/` to catch early breaks.

---

📜 A file misnamed may lose its way,  
Its thread untagged, its truth astray.  
But names that trace the rhyme and line,  
Shall echo safe through SHAGI's spine.