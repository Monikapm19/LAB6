"""
test_thermostat_control.py
Comprehensive test suite for thermostat_control.py.
Lab 6: Code and Branch Coverage Analysis
"""

import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert


# Example starter test cases:
def test_away_mode():
    assert target_temperature("away", True, 12) == 16


def test_no_readings():
    assert energy_alert([], 10) == "ok"


# Additional test cases to achieve 100% code coverage:
def test_sleep_mode_early_morning():
    assert target_temperature("sleep", True, 4) == 18


def test_sleep_mode_daytime():
    assert target_temperature("sleep", True, 10) == 20


def test_unoccupied_mode():
    assert target_temperature("normal", False, 12) == 18


def test_occupied_morning_peak():
    assert target_temperature("normal", True, 7) == 22


def test_occupied_evening_peak():
    assert target_temperature("normal", True, 19) == 21


def test_occupied_standard_hours():
    assert target_temperature("normal", True, 12) == 20


def test_hvac_idle():
    assert hvac_action(20.0, 20.5, 10) == "idle"


def test_hvac_heat_boost():
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_hvac_heat_normal():
    assert hvac_action(18, 22, 10) == "heat"


def test_hvac_cool_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_hvac_cool_normal():
    assert hvac_action(25, 20, 25) == "cool"


def test_energy_alert_ok_readings():
    assert energy_alert([5, 8], 10) == "ok"


def test_energy_alert_critical():
    assert energy_alert([15, 20], 10) == "critical"


def test_energy_alert_warning():
    assert energy_alert([15, 5], 10) == "warning"
