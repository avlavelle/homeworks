#!/usr/bin/env python3

#Anna Victoria Lavelle
#AVL578
#February 14, 2023

from analyze_water2 import calculate_turbidity, is_safe, calculate_time
import pytest
import math

tester = {"turbidity_data": [{"calibration_constant": 1, "detector_current": 2},
                            {"calibration_constant":3, "detector_current": 4},
                            {"calibration_constant": 5, "detector_current": 6},
                            {"calibration_constant": 7, "detector_current": 8},
                            {"calibration_constant": 9, "detector_current": 10},
                            {"calibration_constant": 11, "detector_current": 12}]}
def test_calculate_turbidity():
    assert calculate_turbidity(tester) == 64


def test_is_safe():
    assert is_safe(calculate_turbidity(tester)) == "Warning: Turbidity is above the threshold for safe use"

def test_calculate_time():
    assert calculate_time(tester) == -(math.log(64, 0.98))
