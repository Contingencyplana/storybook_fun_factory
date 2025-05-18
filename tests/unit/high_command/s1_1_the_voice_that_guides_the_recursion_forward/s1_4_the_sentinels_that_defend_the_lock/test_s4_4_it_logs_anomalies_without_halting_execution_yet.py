"""
test_s4_4_it_logs_anomalies_without_halting_execution_yet.py

Tests logging of anomalies without halting program execution.
"""

import os
import tempfile
import logging
from game_construction_bay.high_command.s1_1_the_voice_that_guides_the_recursion_forward.s1_4_the_sentinels_that_defend_the_lock import s4_4_it_logs_anomalies_without_halting_execution_yet as logger_module

def test_logs_to_file_and_confirms_content():
    anomalies = [
        {"id": "x1", "type": "orphan"},
        {"id": "x2", "type": "unacknowledged"}
    ]

    with tempfile.NamedTemporaryFile(delete=False, mode='r+', encoding='utf-8') as temp_log:
        temp_path = temp_log.name
        logger_module.log_anomalies(anomalies, output_path=temp_path)
        temp_log.close()

        # Manually close logger handlers before removing
        for handler in logger_module.logger.handlers:
            handler.close()
        logger_module.logger.handlers.clear()

        with open(temp_path, "r", encoding="utf-8") as f:
            content = f.read()
            assert "x1" in content
            assert "orphan" in content
            assert "x2" in content
            assert "unacknowledged" in content

    os.remove(temp_path)

def test_logs_to_console_without_crash(capsys):
    anomalies = [{"id": "z9", "type": "ghost_trace"}]
    logger_module.log_anomalies(anomalies)

    captured = capsys.readouterr()
    assert "z9" in captured.err
    assert "ghost_trace" in captured.err
