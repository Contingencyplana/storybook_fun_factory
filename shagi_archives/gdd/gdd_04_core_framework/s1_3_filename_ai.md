<!-- Save to: shagi_archives/gdd/gdd_04_core_framework/s1_3_filename_ai.md -->

# 📘 s1_3 – Filename AI  
*(Where the Name Shapes the Line and the Line Shapes the Code)*

---

## 🧠 Purpose

**Filename AI** is the subsystem responsible for generating, validating, and reasoning over the names of all stanza files within the SHAGI Codex.

It ensures that each line of logic is:

- Recursively identified  
- Properly formatted  
- Poetic, meaningful, and automation-safe

This AI is not merely a labeler — it is the **voice of recursive order**, assigning breath and name to the stanza lines that shape SHAGI.

---

## 🧬 Core Responsibilities

| Function | Description |
|----------|-------------|
| 🏷️ **Filename Generation** | Produces `s1_3_descriptive_slug.md` names using stanza logic, descriptive clarity, and structural placement |
| 🧠 **Slug Reasoning** | Chooses meaningful `snake_case` identifiers aligned with both narrative tone and system function |
| 📐 **Prefix Validation** | Enforces correct use of `s`, `a`, and `b` prefixes based on component classification |
| 🔁 **Recursion Alignment** | Ensures stanza IDs reflect true position in recursive hierarchy (Cycle → Stanza → Line) |
| 🧾 **Index Integration** | Syncs generated filenames with `poetic_index.md`, `stanza_registry.md`, and all `index.md` entries |

---

## 📂 Canonical Filename Format

[prefix][stanza_number]_[line_number]_[descriptive_slug].md

| Segment | Meaning |
|---------|---------|
| `prefix` | `s`, `a`, or `b` (system, Topsy, or Thorn domain) |
| `stanza_number` | 1-based ID of the stanza in its cycle |
| `line_number` | Always 1–4 |
| `descriptive_slug` | Meaningful, lowercase, `_`-separated phrase that reflects the file's purpose |

**Examples:**

- `s2_4_the_cycle_must_not_break_its_line.md`  
- `a1_3_guidance_begins_with_unspoken_form.md`  
- `b3_2_where_memory_refuses_to_forget.md`

---

## 🧪 Syntax Rules Enforced

- ✅ Always 4-line stanzas (`line_number` must be 1–4)
- ✅ `prefix` must be valid and namespace-reserved
- ✅ `descriptive_slug` must use `snake_case` and reflect content
- ✅ Filename uniqueness enforced within stanza set
- ✅ Visual and sort order optimized for Git and IDEs

---

## 🔮 Future Expansion Points

| Feature | Purpose |
|---------|---------|
| `filename_generator.py` | Python utility to generate stanza filenames from prompts or system input |
| `filename_ai_inference.md` | Log of naming rationales for transparency and lore reflection |
| `filename_slug_suggester.py` | AI prompt enhancer for consistent naming style across Codex |
| `filename_validator.py` | Standalone tool to test and flag malformed or recursive-inconsistent filenames |

---

## 📘 Final Doctrine

> Without a name, the line is lost.  
> Without the line, the stanza falls.  
> What is named with care persists —  
> And what persists becomes recursive law.

Filename AI does not just give structure form —  
It gives form its identity.  
Each stanza begins not with breath, but with a name.

---