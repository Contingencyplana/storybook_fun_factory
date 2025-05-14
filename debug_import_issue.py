# Filename: debug_import_issue.py

import os
import sys
from pathlib import Path

project_root = os.path.abspath(os.getcwd())
src_path = os.path.join(project_root, "src")

# ✅ Inject src/ into sys.path manually
if src_path not in sys.path:
    sys.path.insert(0, src_path)

print("🧠 Current Working Directory:", os.getcwd())
print("📁 __file__:", __file__)
print("🧭 sys.path:")
for p in sys.path:
    print("  •", p)

print("\n🔍 Expected module path:", os.path.join(src_path, "storybook_fun_factory", "toolscape", "path_utils.py"))

try:
    from storybook_fun_factory.toolscape.get_project_root import get_project_root
    print("\n✅ SUCCESS: Imported get_project_root!")
except ModuleNotFoundError as e:
    print("\n❌ ERROR: Could not import get_project_root")
    print("   Exception:", e)
