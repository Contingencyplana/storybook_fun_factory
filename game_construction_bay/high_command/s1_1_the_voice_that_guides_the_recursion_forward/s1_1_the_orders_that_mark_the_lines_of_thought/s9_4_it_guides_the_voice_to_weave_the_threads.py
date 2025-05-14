"""
Filename: s9_4_it_guides_the_voice_to_weave_the_threads.py

Generates High Command directives for recursive crossover operations.
Each ready stanza is converted into a dispatchable instruction block.
"""

from pathlib import Path
import json

def generate_dispatch_instructions(ready_map: dict) -> list:
    """
    Converts ready stanza metadata into dispatchable instructions.

    Args:
        ready_map (dict): Stanza entries marked ready for crossover.

    Returns:
        list: A list of dispatch dictionaries with guidance for recursion orchestration.
    """
    instructions = []
    for stanza_name, data in ready_map.items():
        instruction = {
            "action": "dispatch_crossover",
            "target_stanza": stanza_name,
            "components_involved": data["components"],
            "priority": "normal",
            "status": "pending"
        }
        instructions.append(instruction)
    return instructions

def save_dispatch_plan(dispatch_list: list, output_path: Path) -> None:
    """
    Saves the generated dispatch plan to a file.

    Args:
        dispatch_list (list): Dispatch instructions to save.
        output_path (Path): Where to write the JSON plan.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(dispatch_list, f, indent=2)

# Example usage
if __name__ == "__main__":
    root = Path(__file__).resolve().parents[4]
    input_path = root / "game_construction_bay" / "high_command" / "tmp" / "ready_crossings.json"
    output_path = root / "game_construction_bay" / "high_command" / "tmp" / "crossover_dispatch_plan.json"

    if input_path.exists():
        with open(input_path, "r", encoding="utf-8") as f:
            ready_data = json.load(f)
        instructions = generate_dispatch_instructions(ready_data)
        save_dispatch_plan(instructions, output_path)
    else:
        print(f"[Error] Missing input: {input_path}")
