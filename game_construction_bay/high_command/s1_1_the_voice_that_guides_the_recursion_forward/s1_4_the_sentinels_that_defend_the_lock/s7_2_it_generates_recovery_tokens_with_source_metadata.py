"""
Filename: s7_2_it_generates_recovery_tokens_with_source_metadata.py

Poetic-Functional Description:
This stanza line creates structured recovery tokens for each invalid stanza
entry detected earlier. These tokens contain the stanza's path, failure context,
and recovery source data, allowing future Cycles to retry or review with
full traceability.

Tokens are uniquely named by stanza and UTC timestamp, then saved to a
dedicated recovery_tokens directory for future invocation.

This line is purely preparatory. It creates no repairs—only structured intent.

Core Responsibilities:
- Accept invalid restoration results from previous validation logic
- Serialize recovery intent and context into token files
- Ensure token traceability via source and timestamp

Example Usage:
>>> generate_recovery_tokens(invalid_entries)
# Output: ["recovery_tokens/s7_2_badname_20250518T122411Z.token.json"]
"""

import os
import json
from datetime import datetime, timezone

TOKEN_DIR = "recovery_tokens"

def generate_recovery_tokens(invalid_results):
    os.makedirs(TOKEN_DIR, exist_ok=True)
    created = []

    for entry in invalid_results:
        if not entry.get("codex_valid") or not entry.get("filename_valid"):
            base_name = os.path.basename(entry.get("path", "unknown"))
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            token_name = f"s7_2_{base_name}_{timestamp}.token.json"
            token_path = os.path.join(TOKEN_DIR, token_name)

            token_data = {
                "source": entry.get("source"),
                "path": entry.get("path"),
                "filename": entry.get("filename"),
                "codex_valid": entry.get("codex_valid"),
                "filename_valid": entry.get("filename_valid"),
                "codex_reason": entry.get("codex_reason"),
                "created_at": datetime.now(timezone.utc).isoformat()
            }

            with open(token_path, "w", encoding="utf-8") as f:
                json.dump(token_data, f, indent=2)
            created.append(token_path)

    return created
