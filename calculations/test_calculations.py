"""
test_calculations.py — Automated tests for constants.py and scaling_relations.py.

Run with:  python -m pytest calculations/test_calculations.py -v
       or: python calculations/test_calculations.py
"""

import math
import sys
import os

# Allow running directly from project root or from calculations/ directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import scipy.constants as co
from calculations.constants import (
    planck_length,
    planck_time,
    planck_mass,
    planck_energy,
    planck_temperature,
    planck_energy_GeV,
    check_internal_consistency,
)
from calculations.scaling_relations import (
    metric_energy_ratio,
    metric_length_ratio,
    metric_momentum_ratio,
    metric_snr,
    orders_of_magnitude_gap,
    lhc_energy_metric,
    ligo_length_metric,
)


# ---------------------------------------------------------------------------
# Tolerance for approximate value checks
# ---------------------------------------------------------------------------
# We allow 0.5% relative tolerance to accommodate minor differences between
# scipy.constants versions and published rounded values.
REL_TOL = 0.005


# ---------------------------------------------------------------------------
# Tests: Planck constants — approximate values
# ---------------------------------------------------------------------------

def test_planck_length_approximate():
    """l_P ≈ 1.616e-35 m (published rounded value)."""
    l_P = planck_length()
    expected = 1.616e-35  # m
    assert abs(l_P - expected) / expected < REL_TOL, (
        f"Planck length {l_P:.4e} m differs from expected {expected:.4e} m "
        f"by more than {REL_TOL*100:.1f}%"
    )


def test_planck_time_approximate():
    """t_P ≈ 5.391e-44 s (published rounded value)."""
    t_P = planck_time()
    expected = 5.391e-44  # s
    assert abs(t_P - expected) / expected < REL_TOL, (
        f"Planck time {t_P:.4e} s differs from expected {expected:.4e} s"
    )


def test_planck_mass_approximate():
    """m_P ≈ 2.176e-8 kg (published rounded value)."""
    m_P = planck_mass()
    expected = 2.176e-8  # kg
    assert abs(m_P - expected) / expected < REL_TOL, (
        f"Planck mass {m_P:.4e} kg differs from expected {expected:.4e} kg"
    )


def test_planck_energy_approximate():
    """E_P ≈ 1.956e9 J (published rounded value)."""
    E_P = planck_energy()
    expected = 1.956e9  # J
    assert abs(E_P - expected) / expected < REL_TOL, (
        f"Planck energy {E_P:.4e} J differs from expected {expected:.4e} J"
    )


def test_planck_energy_gev_approximate():
    """E_P ≈ 1.22e19 GeV."""
    E_P_GeV = planck_energy_GeV()
    expected = 1.22e19  # GeV
    assert abs(E_P_GeV - expected) / expected < REL_TOL, (
        f"Planck energy {E_P_GeV:.4e} GeV differs from expected {expected:.4e} GeV"
    )


# ---------------------------------------------------------------------------
# Tests: internal consistency
# ---------------------------------------------------------------------------

def test_internal_consistency():
    """Derived relations: l_P/c == t_P, m_P*c^2 == E_P, E_P*t_P == hbar."""
    check_internal_consistency()  # raises AssertionError if any check fails


def test_l_p_over_c_equals_t_p():
    """l_P / c == t_P to better than 1 part in 1e10."""
    assert abs(planck_length() / co.c - planck_time()) / planck_time() < 1e-10


def test_m_p_c_squared_equals_e_p():
    """m_P * c^2 == E_P to better than 1 part in 1e10."""
    assert abs(planck_mass() * co.c**2 - planck_energy()) / planck_energy() < 1e-10


def test_e_p_t_p_equals_hbar():
    """E_P * t_P == hbar to better than 1 part in 1e10."""
    val = planck_energy() * planck_time()
    assert abs(val - co.hbar) / co.hbar < 1e-10


# ---------------------------------------------------------------------------
# Tests: scaling-relation functions
# ---------------------------------------------------------------------------

def test_metric_energy_ratio_positive():
    """Energy ratio is positive for any positive energy."""
    assert metric_energy_ratio(1.0) > 0


def test_metric_energy_ratio_lhc_less_than_one():
    """LHC energy is far below the Planck energy."""
    assert lhc_energy_metric() < 1.0


def test_metric_energy_ratio_lhc_order_of_magnitude():
    """LHC ε_E ≈ 10^-15 (within 2 orders)."""
    eps = lhc_energy_metric()
    assert 1e-17 < eps < 1e-13, f"LHC ε_E = {eps:.3e} out of expected range"


def test_metric_length_ratio_ligo():
    """LIGO ε_L = l_P / 4km ≈ 4e-39 (within 2 orders)."""
    eps = ligo_length_metric()
    assert 1e-41 < eps < 1e-37, f"LIGO ε_L = {eps:.3e} out of expected range"


def test_metric_momentum_ratio_positive():
    """Momentum ratio is positive for positive momentum."""
    assert metric_momentum_ratio(1.0) > 0


def test_metric_snr_ratio():
    """SNR metric returns signal / uncertainty."""
    assert abs(metric_snr(1e-40, 1e-20) - 1e-20) / 1e-20 < 1e-10


def test_metric_snr_raises_on_zero_uncertainty():
    """SNR metric raises ValueError for zero uncertainty."""
    import pytest
    with pytest.raises(ValueError):
        metric_snr(1.0, 0.0)


def test_orders_of_magnitude_gap():
    """Gap for 1e-15 is 15."""
    assert abs(orders_of_magnitude_gap(1e-15) - 15.0) < 1e-10


def test_orders_of_magnitude_gap_raises_on_nonpositive():
    """Gap function raises ValueError for non-positive input."""
    import pytest
    with pytest.raises(ValueError):
        orders_of_magnitude_gap(0.0)


# ---------------------------------------------------------------------------
# Simple test runner (no pytest required)
# ---------------------------------------------------------------------------

def _run_all_tests():
    tests = [
        test_planck_length_approximate,
        test_planck_time_approximate,
        test_planck_mass_approximate,
        test_planck_energy_approximate,
        test_planck_energy_gev_approximate,
        test_internal_consistency,
        test_l_p_over_c_equals_t_p,
        test_m_p_c_squared_equals_e_p,
        test_e_p_t_p_equals_hbar,
        test_metric_energy_ratio_positive,
        test_metric_energy_ratio_lhc_less_than_one,
        test_metric_energy_ratio_lhc_order_of_magnitude,
        test_metric_length_ratio_ligo,
        test_metric_momentum_ratio_positive,
        test_metric_snr_ratio,
        test_metric_snr_raises_on_zero_uncertainty,
        test_orders_of_magnitude_gap,
        test_orders_of_magnitude_gap_raises_on_nonpositive,
    ]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except ImportError as e:
            # Tests that use pytest.raises cannot run without pytest
            print(f"  SKIP  {t.__name__} (requires pytest: {e})")
        except Exception as e:
            print(f"  FAIL  {t.__name__}: {e}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    print("Running QuantumGravity calculation tests")
    print("=" * 45)
    _run_all_tests()
