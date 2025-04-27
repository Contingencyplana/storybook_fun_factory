import os

# Define the root directory where we want to rename poetic folders/files
ROOT_DIR = "src/storybook_fun_factory"

# Define a mapping from digits to words (optional)
NUMBER_MAP = {
    "1_1": "one",
    "1_2": "two",
    "1_3": "three",
    "1_4": "four",
    "2_1": "five",
    "2_2": "six",
    "2_3": "seven",
    "2_4": "eight",
    "3_1": "nine",
    "3_2": "ten",
    "3_3": "eleven",
    "3_4": "twelve"
}

def rename_path(path):
    base = os.path.basename(path)

    # Skip system files like __init__.py or __pycache__ folders
    if base.startswith("__"):
        return None

    # Only target paths that start with a single underscore
    if base.startswith("_") and not base.startswith("__"):
        # Remove leading underscore
        new_base = base[1:]

        # Optional: replace number prefixes if they match NUMBER_MAP
        for prefix, word in NUMBER_MAP.items():
            if new_base.startswith(prefix):
                new_base = new_base.replace(prefix, word, 1)
                break

        new_path = os.path.join(os.path.dirname(path), new_base)
        print(f"Renaming: {path} -> {new_path}")
        os.rename(path, new_path)
        return new_path

    return None

def walk_and_rename(root_dir):
    # Rename directories first (deepest first)
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            rename_path(full_path)

    # Rename files second
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            rename_path(full_path)

if __name__ == "__main__":
    walk_and_rename(ROOT_DIR)
    print("\n✅ Rename operation complete.")
