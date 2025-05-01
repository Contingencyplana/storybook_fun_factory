# s1_1_a_line_went_wrong_but_none_could_see.py

"""
Detects recursive deviations that were not immediately visible—
subtle faults in behavior that leave silent traces.
"""

from pathlib import Path
import logging
import datetime
import hashlib

# Configure logging
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
HIDDEN_TRACE_LOG = LOG_DIR / "hidden_trace_log.txt"
logging.basicConfig(filename=HIDDEN_TRACE_LOG, level=logging.INFO, format="%(message)s")

# Define a list of example trace anomalies (these would be provided by future subsystems)
potential_anomalies = [
    {"id": "dev_001", "timestamp": datetime.datetime.now(), "pattern": "loop-missync"},
    {"id": "dev_002", "timestamp": datetime.datetime.now(), "pattern": "echo-delay"},
    {"id": "dev_003", "timestamp": datetime.datetime.now(), "pattern": "symbol-breakage"},
]

def detect_subtle_deviation(anomaly: dict) -> str:
    """
    Generates a subtle trace signature for a hidden recursive deviation.
    """
    anomaly_signature = f"{anomaly['id']}::{anomaly['pattern']}::{anomaly['timestamp'].isoformat()}"
    hashed = hashlib.sha256(anomaly_signature.encode()).hexdigest()
    return hashed

def log_hidden_trace(anomaly: dict):
    """
    Logs a poetic echo of an undetected fault into the dream journal log.
    """
    signature = detect_subtle_deviation(anomaly)
    poetic_log = (
        f"[{anomaly['timestamp'].isoformat()}] "
        f"Hidden fault detected: '{anomaly['pattern']}' "
        f"→ trace signature: {signature[:16]}..."
    )
    logging.info(poetic_log)

def process_anomalies(anomalies: list[dict]):
    """
    Processes all received anomalies, logging each one’s hidden trace signature.
    """
    for anomaly in anomalies:
        log_hidden_trace(anomaly)

# Run if executed directly
if __name__ == "__main__":
    process_anomalies(potential_anomalies)
