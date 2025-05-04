import os
import sys
from pathlib import Path

print("🧠 Current Working Directory:", os.getcwd())
print("📁 __file__:", __file__)
print("🧭 sys.path:")
for p in sys.path:
    print("  •", p)

src_path = os.path.join(os.getcwd(), "src")
print("\n🔍 Expected module path:", os.path.join(src_path, "storybook_fun_factory", "toolscape", "path_utils.py"))

# Try the import manually
try:
    from storybook_fun_factory.toolscape.path_utils import get_project_root
    print("\n✅ SUCCESS: Imported get_project_root!")
except ModuleNotFoundError as e:
    print("\n❌ ERROR: Could not import get_project_root")
    print("   Exception:", e)
