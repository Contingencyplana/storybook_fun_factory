# Start the Storybook FUN Factory Project Environment
cd C:\Users\Admin\storybook_fun_factory

# Activate Poetry environment only if not already inside
if (-not $env:VIRTUAL_ENV) {
    poetry shell
}

# Set PYTHONPATH if not already set
if (-not $env:PYTHONPATH) {
    $env:PYTHONPATH = "."
}

# Debug command
Write-Host "✅ FUN Factory environment initialized. PYTHONPATH set to: $env:PYTHONPATH"
