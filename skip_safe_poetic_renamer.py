import os

# Define the folders to scan
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

# Helper function to generate a new name
def generate_new_name(name):
    if name.startswith("_"):
        return "s" + name[1:]
    elif name[0].isdigit():
        return "s" + name
    else:
        return name  # Should not happen

# Main function to walk and rename with skip-safety
def walk_and_poetic_rename():
    for root_folder in TARGET_ROOTS:
        if not os.path.exists(root_folder):
            print(f"⚠️ Warning: {root_folder} does not exist, skipping.")
            continue

        # Rename folders first (deepest first)
        for dirpath, dirnames, filenames in os.walk(root_folder, topdown=False):
            for dirname in dirnames:
                full_old_path = os.path.join(dirpath, dirname)
                if should_rename(dirname):
                    new_dirname = generate_new_name(dirname)
                    new_path = os.path.join(dirpath, new_dirname)
                    if not os.path.exists(new_path):
                        print(f"Renaming folder: {full_old_path} -> {new_path}")
                        os.rename(full_old_path, new_path)
                    else:
                        print(f"⚠️ Skipping folder (already exists): {full_old_path}")

        # Rename files second
        for dirpath, dirnames, filenames in os.walk(root_folder, topdown=True):
            for filename in filenames:
                full_old_path = os.path.join(dirpath, filename)
                if should_rename(filename):
                    new_filename = generate_new_name(filename)
                    new_path = os.path.join(dirpath, new_filename)
                    if not os.path.exists(new_path):
                        print(f"Renaming file: {full_old_path} -> {new_path}")
                        os.rename(full_old_path, new_path)
                    else:
                        print(f"⚠️ Skipping file (already exists): {full_old_path}")

if __name__ == "__main__":
    walk_and_poetic_rename()
    print("\n✅ Skip-safe poetic renaming operation complete.")
