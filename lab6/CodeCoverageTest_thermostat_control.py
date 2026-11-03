"""
CodeCoverageTest_thermostat_control.py
Test cases designed to achieve 100% code (line) coverage for thermostat_control.py.
Lab 6: Code and Branch Coverage Analysis
"""

import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert


# ============================================================================
# Test Cases for target_temperature (Lines 1 - 14)
# ============================================================================

def test_away_mode():
    """Test mode == 'away' returns 16 (lines 2-3)."""
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_early_morning():
    """Test mode == 'sleep' and hour < 6 returns 18 (lines 4-6)."""
    assert target_temperature("sleep", True, 4) == 18


def test_sleep_mode_daytime():
    """Test mode == 'sleep' and daytime hour returns 20 (lines 4, 7)."""
    assert target_temperature("sleep", True, 10) == 20


def test_unoccupied_mode():
    """Test unoccupied (occupied=False) returns 18 (lines 8-9)."""
    assert target_temperature("normal", False, 12) == 18


def test_occupied_morning_peak():
    """Test occupied morning peak (6 <= hour < 9) returns 22 (lines 10-11)."""
    assert target_temperature("normal", True, 7) == 22


def test_occupied_evening_peak():
    """Test occupied evening peak (17 <= hour < 22) returns 21 (lines 12-13)."""
    assert target_temperature("normal", True, 19) == 21


def test_occupied_standard_hours():
    """Test occupied default hours return 20 (line 14)."""
    assert target_temperature("normal", True, 12) == 20


# ============================================================================
# Test Cases for hvac_action (Lines 17 - 27)
# ============================================================================

def test_hvac_idle():
    """Test abs(diff) < 1 returns 'idle' (lines 19-20)."""
    assert hvac_action(20.0, 20.5, 10) == "idle"


def test_hvac_heat_boost():
    """Test diff > 0 and outside < 5 returns 'heat_boost' (lines 21-23)."""
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_hvac_heat_normal():
    """Test diff > 0 and outside >= 5 returns 'heat' (lines 21, 24)."""
    assert hvac_action(18, 22, 10) == "heat"


def test_hvac_cool_boost():
    """Test diff <= 0 and outside > 30 returns 'cool_boost' (lines 25-26)."""
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_hvac_cool_normal():
    """Test diff <= 0 and outside <= 30 returns 'cool' (line 27)."""
    assert hvac_action(25, 20, 25) == "cool"


# ============================================================================
# Test Cases for energy_alert (Lines 30 - 39)
# ============================================================================

def test_energy_alert_ok_empty():
    """Test empty readings returns 'ok' (line 36)."""
    assert energy_alert([], 10) == "ok"


def test_energy_alert_ok_readings():
    """Test readings below limit return 'ok' (lines 32-33, 36)."""
    assert energy_alert([5, 8], 10) == "ok"


def test_energy_alert_critical():
    """Test over * 2 > len(readings) returns 'critical' (lines 33-34, 37-38)."""
    assert energy_alert([15, 20], 10) == "critical"


def test_energy_alert_warning():
    """Test over > 0 but over * 2 <= len(readings) returns 'warning' (line 39)."""
    assert energy_alert([15, 5], 10) == "warning"
