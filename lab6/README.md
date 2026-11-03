# L6_L7_29 — Smart Thermostat Controller

## Lab 6: Code and Branch Coverage Analysis

### About
A Python module for smart thermostat control that selects target temperatures based on mode and time of day, determines HVAC heating or cooling actions, and monitors energy consumption readings to raise alerts.

---

### Deliverables Summary

| File | Description | Coverage Type | Coverage Achieved |
|---|---|---|---|
| `thermostat_control.py` | Source module under test | - | - |
| `test_thermostat_control.py` | Full test suite combining all test scenarios | Both | 100% Line / 100% Branch |
| `CodeCoverageTest_thermostat_control.py` | Targeted test cases for line/statement coverage | Line Coverage | **100%** |
| `BranchCoverageTest_thermostat_control.py` | Targeted test cases covering all decision branches & boundaries | Branch Coverage | **100%** |
| `code_coverage_screenshot.png` | Terminal output screenshot for code coverage | Line Coverage | 100% |
| `branch_coverage_screenshot.png` | Terminal output screenshot for branch coverage | Branch Coverage | 100% |

---

### 1. Code Coverage (Line Coverage)

Line coverage measures whether every statement in the source code executes at least once during testing.

#### Commands to Run Code Coverage:
```powershell
coverage run -m pytest CodeCoverageTest_thermostat_control.py
coverage report -m
```

#### Results:
- **Statements**: 35
- **Missed**: 0
- **Line Coverage**: **100%**


---

### 2. Branch Coverage

Branch coverage tests every possible direction (True and False branches) of all control flow structures (`if`, `else`, logical operators `and`/`or`, and loop entry/bypass).

#### Commands to Run Branch Coverage:
```powershell
coverage run --branch -m pytest BranchCoverageTest_thermostat_control.py
coverage report -m
```

#### Results:
- **Statements**: 35
- **Branches**: 28
- **Partial Branches (BrPart)**: 0
- **Branch Coverage**: **100%**



---

### Verification and Test Execution
All test cases can be run together using `pytest`:
```powershell
pytest -v
```
All tests pass cleanly without errors or warnings.
