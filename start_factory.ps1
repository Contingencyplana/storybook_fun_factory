# Start the Storybook FUN Factory Project Environment

# Ensure we're using 64-bit PowerShell
if ($env:PROCESSOR_ARCHITECTURE -ne "AMD64") {
    Write-Host "⚠️ Switching to 64-bit PowerShell..."
    & "C:\Program Files\PowerShell\7\pwsh.exe"
    exit
}

# Navigate to project root
cd C:\Users\Admin\storybook_fun_factory

# Activate Poetry environment only if not already inside
if (-not $env:VIRTUAL_ENV) {
    poetry shell
}

# Set PYTHONPATH if not already set
if (-not $env:PYTHONPATH) {
    $env:PYTHONPATH = "."
}

# Confirmation
Write-Host "✅ FUN Factory environment initialized. PYTHONPATH set to: $env:PYTHONPATH"
