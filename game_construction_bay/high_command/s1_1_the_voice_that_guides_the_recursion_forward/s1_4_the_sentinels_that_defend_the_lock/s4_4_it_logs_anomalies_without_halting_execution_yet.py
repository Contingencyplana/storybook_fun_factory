"""
s4_4_it_logs_anomalies_without_halting_execution_yet.py

Logs detected anomalies to a designated output stream or file without halting execution.
This sentinel module records irregularities for downstream handling.
"""

import logging
from typing import List, Dict, Optional

logger = logging.getLogger("anomaly_logger")
logger.setLevel(logging.INFO)

def configure_logger(output_path: Optional[str] = None):
    """
    Configures the anomaly logger to write to a file or console.

    Args:
        output_path (Optional[str]): If provided, logs will be written to this file.
    """
    if logger.handlers:
        logger.handlers.clear()
    handler = logging.FileHandler(output_path) if output_path else logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - ANOMALY - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log_anomalies(anomalies: List[Dict], output_path: Optional[str] = None):
    """
    Logs a list of anomaly records to the configured log stream.

    Args:
        anomalies (List[Dict]): A list of anomaly entries to log.
        output_path (Optional[str]): If provided, logs are written to this file.
    """
    configure_logger(output_path)
    for anomaly in anomalies:
        logger.info(f"Detected anomaly: {anomaly}")
