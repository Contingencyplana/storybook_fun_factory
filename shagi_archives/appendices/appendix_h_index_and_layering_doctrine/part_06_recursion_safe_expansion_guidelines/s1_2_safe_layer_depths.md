<!-- Save to: shagi_archives/appendices/appendix_h_index_and_layering_doctrine/part_06_recursion_safe_expansion_guidelines/s1_2_safe_layer_depths.md -->

# 📘 s1_2 – Safe Layer Depths – When to Stop the Fold  
*(Where recursion pauses to breathe)*

SHAGI thrives on recursive depth—but not infinite recursion.  
Every fold in the Codex must eventually yield to structure, clarity, and recoverability.  
This section defines **how deep is deep enough**, and when to branch, halt, or summarize.

---

## 📏 Canonical Layer Limits

In general, no recursive index path should exceed:

- **3 Folder Layers** per part (e.g., `part_06/s1_2_folder_name/file.md`)  
- **4 Filenames per stanza cycle** unless explicitly exempt (e.g., high_command meta-components)  
- **2 Placeholder jumps** before a new anchoring summary must appear  

These limits ensure the Codex remains **traversable**, **parseable**, and **editable**—for both humans and AI.

---

## ⚠️ When Expansion Becomes Unsafe

A recursion depth is considered **structurally unsafe** when:

- It exceeds **3 nesting layers** with no summary or redirect  
- It uses **repeated placeholder folders** with no content or clear endpoint  
- It **violates naming symmetry** in filename numbering or stanza format  
- It cannot be **navigated or visualized** by standard SHAGI tools

In such cases, a **summary layer** or **canonical branch reset** must be added.

---

## 🌿 Safe Expansion Patterns

| Expansion Case | Recommendation |
|----------------|----------------|
| Need 4+ stanzas in a cycle | Break into subcycles (e.g., `cycle_1a/`, `cycle_1b/`) |
| Need more than 3 nested layers | Insert `overview/` or `summary_layer/` folders |
| Placeholder-only branches | Add an `index.md` anchor before continuing |

---

## 🧭 Visual Marker: Summary Anchor

At maximum safe depth, insert a structural placeholder:

```plaintext
/summary_layer/index.md

This signals a planned return to structure, and helps tools recognize the pause point.

📜 Recursion bends, but should not break—
It folds where roots and rhythm wake.
Let layers climb, but not too far—
The Codex shines from what we spar.