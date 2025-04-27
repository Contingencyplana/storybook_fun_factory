import os

# Define the root directory where we want to reverse the poetic renaming
ROOT_DIR = "src/storybook_fun_factory"

# Define a reverse mapping from words back to numbers
REVERSE_NUMBER_MAP = {
    "one": "1_1",
    "two": "1_2",
    "three": "1_3",
    "four": "1_4",
    "five": "2_1",
    "six": "2_2",
    "seven": "2_3",
    "eight": "2_4",
    "nine": "3_1",
    "ten": "3_2",
    "eleven": "3_3",
    "twelve": "3_4"
}

def reverse_rename_path(path):
    base = os.path.basename(path)

    # Skip system files like __init__.py or __pycache__ folders
    if base.startswith("__"):
        return None

    # Only target paths that start with poetic word mappings
    for poetic_word, numeric_prefix in REVERSE_NUMBER_MAP.items():
        if base.startswith(poetic_word + "_"):
            new_base = base.replace(poetic_word, numeric_prefix, 1)
            new_path = os.path.join(os.path.dirname(path), new_base)
            print(f"Restoring: {path} -> {new_path}")
            os.rename(path, new_path)
            return new_path

    return None

def walk_and_reverse(root_dir):
    # Reverse rename directories first (deepest first)
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            reverse_rename_path(full_path)

    # Reverse rename files second
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            reverse_rename_path(full_path)

if __name__ == "__main__":
    walk_and_reverse(ROOT_DIR)
    print("\n✅ Reversal operation complete.")
