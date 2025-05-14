"""
test_s3_3_it_watches_the_helpers_we_depend_on.py
(Tests HelperWatchdog logic for monitoring critical helper files)

This test confirms that the HelperWatchdog system in High Command
can accurately detect, list, and validate key test helper files.
"""

import os
import pytest
import shutil
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec

# ✅ Load module dynamically
HELPER_PATH = Path(__file__).resolve().parent / "../../../../../tests/test_helpers/dynamic_importer.py"
spec = spec_from_file_location("dynamic_importer", HELPER_PATH)
dynamic_importer = module_from_spec(spec)
spec.loader.exec_module(dynamic_importer)


def test_helper_file_monitoring(tmp_path):
    # Setup: create temporary helper directory
    helper_dir = tmp_path / "test_helpers"
    helper_dir.mkdir()

    # Create a valid Python helper file
    valid_helper = helper_dir / "valid_helper.py"
    valid_helper.write_text("def test_func(): return True", encoding="utf-8")

    # Create a broken helper file
    broken_helper = helper_dir / "broken_helper.py"
    broken_helper.write_text("def oops: return 1", encoding="utf-8")

    # Import the target module dynamically
    module_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../../../game_construction_bay/high_command/s1_1_the_voice_that_guides_the_recursion_forward/s1_1_the_orders_that_mark_the_lines_of_thought/s3_3_it_watches_the_helpers_we_depend_on.py"
        )
    )
    module = dynamic_importer.dynamic_import_module(module_path)
    HelperWatchdog = module.HelperWatchdog

    watchdog = HelperWatchdog(helper_root=helper_dir)

    # ✅ Detect files
    helpers = watchdog.list_helpers()
    assert valid_helper in helpers
    assert broken_helper in helpers

    # ✅ File exists checks
    assert watchdog.file_exists("valid_helper.py") is True
    assert watchdog.file_exists("missing.py") is False

    # ✅ Import readiness checks
    assert watchdog.check_import_ready("valid_helper.py") is True
    assert watchdog.check_import_ready("broken_helper.py") is False
