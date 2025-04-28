"""
test_1_1_a_breath_of_steel_a_whispers_thread.py
(Tests for the Foundational Breath of Automation)

This file tests the initial whisper-thread of automation.
It verifies the breathing, whispering, and monitoring capabilities
of the WhispersThread class.
"""
import sys
sys.path.append('src')
import pytest
from storybook_fun_factory.automation_ai.s1_1_before_the_spark_can_shape_the_stone.s1_1_the_frame_once_forged_must_find_its_weight.s1_1_a_breath_of_steel_a_whispers_thread import WhispersThread

def test_initial_state():
    thread = WhispersThread()
    status = thread.monitor_status()
    assert status["active"] is False
    assert status["signal_strength"] == 0

def test_breathe_awakens_thread():
    thread = WhispersThread()
    thread.breathe()
    status = thread.monitor_status()
    assert status["active"] is True
    assert status["signal_strength"] == 1

def test_whisper_before_breath():
    thread = WhispersThread()
    response = thread.whisper("test action")
    assert response == "No breath to whisper yet."

def test_whisper_after_breath():
    thread = WhispersThread()
    thread.breathe()
    response = thread.whisper("test action")
    assert response == "Action whispered: test action"

def test_multiple_breaths_increase_signal():
    thread = WhispersThread()
    thread.breathe()
    thread.breathe()
    thread.breathe()
    status = thread.monitor_status()
    assert status["signal_strength"] == 3
    assert status["active"] is True
