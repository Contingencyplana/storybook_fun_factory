import os

# Define the root directory where we want to fix the poetic stanza naming
ROOT_DIR = "src/storybook_fun_factory"

def poetic_rename_path(path):
    base = os.path.basename(path)

    # Skip system files like __init__.py, __pycache__, etc.
    if base.startswith("__"):
        return None

    # Only target names that start with a single underscore followed by numbers
    if base.startswith("_") and base[1:2].isdigit():
        # Remove leading underscore
        new_base = base[1:]

        # Add "s" prefix to the beginning
        new_base = "s" + new_base

        new_path = os.path.join(os.path.dirname(path), new_base)
        print(f"Renaming: {path} -> {new_path}")
        os.rename(path, new_path)
        return new_path

    return None

def walk_and_poetic_rename(root_dir):
    # Rename directories first (deepest first)
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            poetic_rename_path(full_path)

    # Rename files second
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            poetic_rename_path(full_path)

if __name__ == "__main__":
    walk_and_poetic_rename(ROOT_DIR)
    print("\n✅ Poetic renaming operation complete.")