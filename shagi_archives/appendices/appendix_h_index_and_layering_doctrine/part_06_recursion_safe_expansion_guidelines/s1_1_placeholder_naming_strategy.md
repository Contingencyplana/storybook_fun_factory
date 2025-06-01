<!-- Save to: shagi_archives/appendices/appendix_h_index_and_layering_doctrine/part_06_recursion_safe_expansion_guidelines/s1_1_placeholder_naming_strategy.md -->

# 📘 s1_1 – Placeholder Naming Strategy  
*(How to mark what has not yet bloomed)*

In the SHAGI Codex, placeholders serve as signposts—pre-authorized gaps in the recursive structure, reserved for future stanzas, layers, or logic yet to be composed.  
Their names must be predictable, parseable, and aligned with poetic and structural convention.

---

## 🔖 Purpose of Placeholder Naming

Placeholders allow:

- **Planned expansion** without disrupting recursive order  
- **Automated tools** to skip or populate them in future passes  
- **Clear editorial signals** that a part is intentionally unwritten—not missing  

---

## 📛 Naming Convention

Use the format:

```plaintext
s1_4_placeholder.md
s2_3_placeholder.md
The slug placeholder must be lowercase and must occupy the expected position of a future stanza file.

If the placeholder is reserved for a specific topic, it may take the format:

s2_4_placeholder_indexing_strategy.md
…but must still include the placeholder keyword for automation tools to detect it as safely skippable.

⚙️ System Recognition Rules
All SHAGI tools treat a file or folder as a placeholder if:

The filename includes _placeholder

The title contains “Placeholder”

The file is structurally valid but content-sparse

These files are excluded from:

Canonical stanza analysis

Visual recursion maps

Memory archival propagation

## 📘 Examples

Filename	Valid?	Notes
s1_3_placeholder.md	✅	Standard generic placeholder
s2_2_placeholder_mythic_depths.md	✅	Reserved for a known topic
s3_4_mythic_depths_placeholder.md	❌	Misordered keyword; will not be detected
s1_5_tbd.md	❌	Lacks the _placeholder keyword

📜 Not yet the code, not yet the name,
But space preserved to spark the flame.
A sign that says “the tale’s not done”—
The scroll held back, the verse begun.