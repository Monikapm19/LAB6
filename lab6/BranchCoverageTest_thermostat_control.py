"""
BranchCoverageTest_thermostat_control.py
Comprehensive test cases designed to achieve 100% branch coverage for thermostat_control.py.
Lab 6: Code and Branch Coverage Analysis
"""

import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert


# ============================================================================
# Branch Coverage Tests for target_temperature
# ============================================================================

def test_away_mode_branch():
    """Branch: mode == 'away' is True."""
    assert target_temperature("away", True, 12) == 16


def test_sleep_mode_early_hours():
    """Branch: mode == 'sleep', hour < 6 is True (hour = 3)."""
    assert target_temperature("sleep", True, 3) == 18


def test_sleep_mode_boundary_hour_5():
    """Branch: mode == 'sleep', boundary hour < 6 is True (hour = 5)."""
    assert target_temperature("sleep", True, 5) == 18


def test_sleep_mode_boundary_hour_22():
    """Branch: mode == 'sleep', hour < 6 is False, hour >= 22 is True (hour = 22)."""
    assert target_temperature("sleep", True, 22) == 18


def test_sleep_mode_late_night():
    """Branch: mode == 'sleep', hour >= 22 is True (hour = 23)."""
    assert target_temperature("sleep", True, 23) == 18


def test_sleep_mode_daytime_boundary_6():
    """Branch: mode == 'sleep', hour < 6 is False, hour >= 22 is False (hour = 6)."""
    assert target_temperature("sleep", True, 6) == 20


def test_sleep_mode_daytime_boundary_21():
    """Branch: mode == 'sleep', hour < 6 is False, hour >= 22 is False (hour = 21)."""
    assert target_temperature("sleep", True, 21) == 20


def test_sleep_mode_midday():
    """Branch: mode == 'sleep', daytime hour = 12 returns 20."""
    assert target_temperature("sleep", False, 12) == 20


def test_unoccupied_branch():
    """Branch: not occupied is True."""
    assert target_temperature("normal", False, 8) == 18


def test_occupied_morning_peak_start():
    """Branch: 6 <= hour < 9 is True at lower boundary (hour = 6)."""
    assert target_temperature("normal", True, 6) == 22


def test_occupied_morning_peak_end():
    """Branch: 6 <= hour < 9 is True at upper boundary (hour = 8)."""
    assert target_temperature("normal", True, 8) == 22


def test_occupied_evening_peak_start():
    """Branch: 17 <= hour < 22 is True at lower boundary (hour = 17)."""
    assert target_temperature("normal", True, 17) == 21


def test_occupied_evening_peak_end():
    """Branch: 17 <= hour < 22 is True at upper boundary (hour = 21)."""
    assert target_temperature("normal", True, 21) == 21


def test_occupied_default_midday():
    """Branch: occupied, 9 <= hour < 17 falls through to default 20 (hour = 12)."""
    assert target_temperature("normal", True, 12) == 20


def test_occupied_default_early_morning():
    """Branch: occupied, hour < 6 falls through to default 20 (hour = 4)."""
    assert target_temperature("normal", True, 4) == 20


def test_occupied_default_late_night():
    """Branch: occupied, hour >= 22 falls through to default 20 (hour = 23)."""
    assert target_temperature("normal", True, 23) == 20


# ============================================================================
# Branch Coverage Tests for hvac_action
# ============================================================================

def test_hvac_idle_exact_zero():
    """Branch: abs(diff) < 1 is True with diff == 0."""
    assert hvac_action(20.0, 20.0, 15) == "idle"


def test_hvac_idle_positive_diff():
    """Branch: abs(diff) < 1 is True with diff == 0.5."""
    assert hvac_action(20.0, 20.5, 10) == "idle"


def test_hvac_idle_negative_diff():
    """Branch: abs(diff) < 1 is True with diff == -0.5."""
    assert hvac_action(20.5, 20.0, 10) == "idle"


def test_hvac_idle_boundary_positive():
    """Branch: abs(diff) < 1 is True at boundary diff == 0.99."""
    assert hvac_action(20.0, 20.99, 10) == "idle"


def test_hvac_idle_boundary_negative():
    """Branch: abs(diff) < 1 is True at boundary diff == -0.99."""
    assert hvac_action(20.99, 20.0, 10) == "idle"


def test_hvac_heat_boost_cold():
    """Branch: diff > 0 is True, outside < 5 is True (outside = 2)."""
    assert hvac_action(18, 22, 2) == "heat_boost"


def test_hvac_heat_boost_subzero():
    """Branch: diff > 0 is True, outside < 5 is True (outside = -5)."""
    assert hvac_action(18, 22, -5) == "heat_boost"


def test_hvac_heat_boost_boundary():
    """Branch: diff > 0 is True, outside < 5 is True at boundary (outside = 4)."""
    assert hvac_action(18, 22, 4) == "heat_boost"


def test_hvac_heat_normal_boundary_5():
    """Branch: diff > 0 is True, outside < 5 is False at boundary (outside = 5)."""
    assert hvac_action(18, 22, 5) == "heat"


def test_hvac_heat_normal_moderate():
    """Branch: diff > 0 is True, outside < 5 is False (outside = 15)."""
    assert hvac_action(18, 22, 15) == "heat"


def test_hvac_heat_diff_exact_one():
    """Branch: diff == 1.0 (abs(diff) < 1 is False, diff > 0 is True)."""
    assert hvac_action(20.0, 21.0, 10) == "heat"


def test_hvac_cool_boost_hot():
    """Branch: diff > 0 is False, outside > 30 is True (outside = 35)."""
    assert hvac_action(25, 20, 35) == "cool_boost"


def test_hvac_cool_boost_boundary():
    """Branch: diff > 0 is False, outside > 30 is True at boundary (outside = 31)."""
    assert hvac_action(25, 20, 31) == "cool_boost"


def test_hvac_cool_normal_boundary_30():
    """Branch: diff > 0 is False, outside > 30 is False at boundary (outside = 30)."""
    assert hvac_action(25, 20, 30) == "cool"


def test_hvac_cool_normal_moderate():
    """Branch: diff > 0 is False, outside > 30 is False (outside = 24)."""
    assert hvac_action(25, 20, 24) == "cool"


def test_hvac_cool_diff_exact_negative_one():
    """Branch: diff == -1.0 (abs(diff) < 1 is False, diff > 0 is False)."""
    assert hvac_action(21.0, 20.0, 25) == "cool"


# ============================================================================
# Branch Coverage Tests for energy_alert
# ============================================================================

def test_energy_alert_empty_readings():
    """Branch: readings is empty list -> loop body skipped, over == 0 is True."""
    assert energy_alert([], 10) == "ok"


def test_energy_alert_all_below_limit():
    """Branch: reading > limit is False for all items, over == 0 is True."""
    assert energy_alert([3, 7, 9], 10) == "ok"


def test_energy_alert_exact_limit_boundary():
    """Branch: reading == limit -> reading > limit is False, over == 0 is True."""
    assert energy_alert([10, 10], 10) == "ok"


def test_energy_alert_critical_all_exceeded():
    """Branch: all readings > limit, over * 2 > len(readings) is True."""
    assert energy_alert([15, 20], 10) == "critical"


def test_energy_alert_critical_majority_exceeded():
    """Branch: 2 of 3 readings > limit (over*2 = 4 > 3) is True."""
    assert energy_alert([15, 20, 5], 10) == "critical"


def test_energy_alert_warning_exact_half_boundary():
    """Branch: exactly half exceed limit (over*2 == len), over*2 > len is False."""
    assert energy_alert([15, 5], 10) == "warning"


def test_energy_alert_warning_exact_half_four_items():
    """Branch: 2 of 4 readings exceed limit (over*2 = 4 == 4), over*2 > len is False."""
    assert energy_alert([15, 16, 5, 5], 10) == "warning"


def test_energy_alert_warning_minority_exceeded():
    """Branch: 1 of 3 readings exceeds limit (over*2 = 2 < 3), over*2 > len is False."""
    assert energy_alert([15, 5, 5], 10) == "warning"
