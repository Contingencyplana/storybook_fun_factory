import sys
import os

# Calculate the absolute path to the src/ folder
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT_DIR, "src")

# Insert src/ at the beginning of sys.path
sys.path.insert(0, SRC_DIR)
