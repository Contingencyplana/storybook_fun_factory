import os

# Define the specific root folders to scan (relative to where the script is run)
TARGET_ROOTS = [
    "game_construction_bay",
    "src",
    "tests",
    "tests_archive"
]

# Safety rules
SKIP_PREFIXES = ("__", ".")  # Skip system files and hidden folders

# Helper function to determine if a name should be renamed
def should_rename(name):
    if name.startswith(SKIP_PREFIXES):
        return False
    if name.startswith("_"):
        return True
    if name and name[0].isdigit():
        return True
    return False

# Helper function to perform the renaming
def generate_new_name(name):
    if name.startswith("_"):
        return "s" + name[1:]
    elif name[0].isdigit():
        return "s" + name
    else:
        return name  # Should not happen due to should_rename

# Main function to walk and rename
def walk_and_poetic_rename():
    for root_folder in TARGET_ROOTS:
        if not os.path.exists(root_folder):
            print(f"⚠️ Warning: {root_folder} does not exist, skipping.")
            continue

        # First, rename folders (deepest first)
        for dirpath, dirnames, filenames in os.walk(root_folder, topdown=False):
            for dirname in dirnames:
                old_path = os.path.join(dirpath, dirname)
                if should_rename(dirname):
                    new_dirname = generate_new_name(dirname)
                    new_path = os.path.join(dirpath, new_dirname)
                    print(f"Renaming folder: {old_path} -> {new_path}")
                    os.rename(old_path, new_path)

        # Then, rename files (shallowest first)
        for dirpath, dirnames, filenames in os.walk(root_folder, topdown=True):
            for filename in filenames:
                old_path = os.path.join(dirpath, filename)
                if should_rename(filename):
                    new_filename = generate_new_name(filename)
                    new_path = os.path.join(dirpath, new_filename)
                    print(f"Renaming file: {old_path} -> {new_path}")
                    os.rename(old_path, new_path)

if __name__ == "__main__":
    walk_and_poetic_rename()
    print("\n✅ Poetic renaming operation complete across targeted folders.")
