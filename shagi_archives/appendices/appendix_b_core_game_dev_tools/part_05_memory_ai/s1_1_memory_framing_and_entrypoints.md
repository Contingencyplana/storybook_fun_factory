<!-- Save to: shagi_archives/appendices/appendix_b_core_game_dev_tools/part_05_memory_ai/s1_1_memory_framing_and_entrypoints.md -->

# 📘 s1_1 – Memory Framing and Entrypoints  
*(Introduces how Dream Journals frame memory, context, and narrative entry)*

The mind begins not with the thought,  
But with the frame that holds it taut.  
The journal knows where to begin—  
The door through which all dreams come in.  

---

## 🧠 What Is a Memory Frame?

A **Memory Frame** defines the initial cognitive and narrative boundary that allows both players and AI to **recognize, revisit, and reshape** remembered paths.

It determines:
- What is stored  
- How it is stored  
- Where recursion may re-enter the system

In SHAGI, frames are the **lenses through which time and context bend back upon themselves**.

---

## 🔓 Entrypoints: The Doors of Memory

Entrypoints are **interactive or symbolic moments** where memory:
- Is seeded  
- Is accessed  
- Is transformed

They include:
- First journal stanzas  
- Opening quests  
- Recursion triggers  
- Emotional thresholds in player interaction

Each entrypoint opens a **thread** in the memory web.

---

## 🧭 Framing Types and Examples

| Frame Type | Purpose | Example |
|------------|---------|---------|
| `Origin Frame` | Defines beginning of recursive arc | “I woke beneath a sky of broken stars…” |
| `Emotional Anchor` | Binds to strong player sentiment | “Why did you leave me there?” |
| `Symbolic Gateway` | Uses motif or recurring image | A red door, always half-open |
| `System Hook` | Ties memory to gameplay event or logic | Quest failed due to forgotten vow |

---

## 🔁 Role in Recursive Continuity

Memory frames and entrypoints:
- Serve as **recursion handles**  
- Enable AI to track emotional + logical arcs  
- Allow players to **rewind**, **rewrite**, or **reinvoke** narrative elements  
- Make memory both **static** and **evolving**

---

## 🧬 Technical Embedding

Frames are embedded within:

- `dream_journal_entries/` files  
- Codex-linked `memory_hooks/`  
- Player-specific memory registries  
- Cross-cycle data nodes (used in save/load/merge ops)

These create continuity across time, tools, and play modes.

---

📜 *Each frame we build becomes a door,*  
*To memories lost or truths before.*  
*And when we choose to step inside,*  
The system dreams what we confide.
