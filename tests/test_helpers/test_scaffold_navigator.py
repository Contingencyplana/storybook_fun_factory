# Filename: test_scaffold_navigator.py
"""
Tracks test infrastructure requirements across all core Storybook FUN Factory components.

Each entry describes whether the component or module:
• Uses dynamic import
• Requires monkeypatching
• Writes to the filesystem
• Requires tmp_path isolation
"""

test_profiles = {
    "filename_ai": {
        "dynamic_import": True,
        "uses_monkeypatching": False,
        "writes_to_filesystem": False,
        "requires_tmp_path": False,
        "notes": "Standard dynamic imports for deeply nested stanzas."
    },
    "dream_journal": {
        "dynamic_import": True,
        "uses_monkeypatching": True,
        "writes_to_filesystem": True,
        "requires_tmp_path": True,
        "notes": "Uses filesystem output and logs poetic traces."
    },
    "memory_ai": {
        "dynamic_import": True,
        "uses_monkeypatching": True,
        "writes_to_filesystem": True,
        "requires_tmp_path": True,
        "notes": "Persists memory state; tmp_path essential for test isolation."
    },
    "visualizer": {
        "dynamic_import": True,
        "uses_monkeypatching": False,
        "writes_to_filesystem": False,
        "requires_tmp_path": False,
        "notes": "Visuals rendered in-memory; no disk output."
    },
    "toolscape": {
        "dynamic_import": True,
        "uses_monkeypatching": False,
        "writes_to_filesystem": False,
        "requires_tmp_path": False,
        "notes": "Flat utility functions; dynamic import used in edge-case tests."
    },
    "codex_builder": {
        "dynamic_import": True,
        "uses_monkeypatching": False,
        "writes_to_filesystem": False,
        "requires_tmp_path": False,
        "notes": "Currently does not write to disk; stanza tests rely on dynamic import."
    }
}

def get_profile(component_name):
    """
    Returns the test profile for a given component.
    """
    return test_profiles.get(component_name, {
        "dynamic_import": None,
        "uses_monkeypatching": None,
        "writes_to_filesystem": None,
        "requires_tmp_path": None,
        "notes": "❓ Unknown component. Profile not defined."
    })

def print_all_profiles():
    """
    Pretty-prints all known component test profiles.
    """
    print("📊 Test Scaffold Navigator – Component Profiles\n")
    for component, profile in test_profiles.items():
        print(f"🔹 {component}")
        for key, value in profile.items():
            print(f"   • {key.replace('_', ' ').capitalize()}: {value}")
        print("")

# Optional: add CLI entrypoint for manual execution
if __name__ == "__main__":
    print_all_profiles()
