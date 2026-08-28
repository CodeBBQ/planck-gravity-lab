"""
scaling_relations.py — Scaling laws and proximity metrics for Planck-scale experiments.

See definitions/common_metrics.md for the conceptual framework.

All quantities in SI unless noted.
"""

import math
import scipy.constants as co

try:
    from calculations.constants import (
        planck_length,
        planck_time,
        planck_mass,
        planck_energy,
    )
except ImportError:
    # Allow running as `python calculations/scaling_relations.py` from project root
    # when the package is not installed.
    from constants import (  # type: ignore[import]
        planck_length,
        planck_time,
        planck_mass,
        planck_energy,
    )


# ---------------------------------------------------------------------------
# Metric 1: Energy ratio  ε_E = E / E_P
# ---------------------------------------------------------------------------

def metric_energy_ratio(E_joules: float) -> float:
    """
    ε_E = E / E_P

    E_joules: characteristic energy of the experiment [J]

    Returns the dimensionless ratio. Values much less than 1 mean the
    experiment operates far below the Planck energy.
    """
    return E_joules / planck_energy()


# ---------------------------------------------------------------------------
# Metric 2: Length ratio  ε_L = l_P / L
# ---------------------------------------------------------------------------

def metric_length_ratio(L_meters: float) -> float:
    """
    ε_L = l_P / L

    L_meters: characteristic length scale of the experiment [m]

    Returns the dimensionless ratio. A small ε_L does NOT by itself imply
    Planck sensitivity — a physical effect proportional to (l_P/L)^n must
    appear in the governing equation.
    """
    return planck_length() / L_meters


# ---------------------------------------------------------------------------
# Metric 3: Momentum ratio  ε_q = q * l_P / hbar
# ---------------------------------------------------------------------------

def metric_momentum_ratio(q_SI: float) -> float:
    """
    ε_q = q * l_P / hbar = q / (hbar / l_P) = q / (m_P * c)

    q_SI: momentum transfer [kg m s⁻¹]

    Relevant for scattering experiments.
    """
    return q_SI * planck_length() / co.hbar


# ---------------------------------------------------------------------------
# Metric 4: Signal-to-noise ratio for a Planck-scale effect  ε_SNR
# ---------------------------------------------------------------------------

def metric_snr(predicted_signal: float, experimental_uncertainty: float) -> float:
    """
    ε_SNR = predicted_Planck_signal / experimental_uncertainty

    Both arguments must be in the same units.

    Returns the dimensionless ratio. Values << 1 mean the experiment cannot
    detect the predicted effect.

    IMPORTANT: predicted_signal is always model-dependent (E3 or E4 at best).
    Label the result accordingly.
    """
    if experimental_uncertainty <= 0:
        raise ValueError("experimental_uncertainty must be positive")
    return predicted_signal / experimental_uncertainty


# ---------------------------------------------------------------------------
# Orders-of-magnitude gap
# ---------------------------------------------------------------------------

def orders_of_magnitude_gap(metric_value: float) -> float:
    """
    gap = -log10(metric_value)

    Returns the number of orders of magnitude by which the experiment falls
    short of Planck sensitivity on the given metric.

    A gap of N means the experiment is 10^N times less sensitive than needed.
    """
    if metric_value <= 0:
        raise ValueError("metric_value must be positive")
    return -math.log10(metric_value)


# ---------------------------------------------------------------------------
# Reference calculations: current-technology benchmarks
# ---------------------------------------------------------------------------

def lhc_energy_metric() -> float:
    """
    ε_E for the LHC at its highest demonstrated collision energy.

    LHC Run 2 top collision energy: 13 TeV = 13e12 eV.
    This is an approximate benchmark; for precision work use a cited E1 source.
    """
    E_lhc_joules = 13e12 * co.eV  # 13 TeV in joules
    return metric_energy_ratio(E_lhc_joules)


def ligo_length_metric() -> float:
    """
    ε_L for LIGO arm length (4 km).

    This is a dimensional benchmark only. A small ε_L for LIGO does not imply
    LIGO is sensitive to Planck-scale physics — see definitions/what_counts_as_probe.md.
    """
    L_ligo = 4e3  # metres
    return metric_length_ratio(L_ligo)


# ---------------------------------------------------------------------------
# Main: print benchmark summary
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Proximity metrics for reference experiments")
    print("=" * 55)

    eps_E_lhc = lhc_energy_metric()
    print(f"\nLHC (13 TeV collision energy)")
    print(f"  ε_E = E/E_P = {eps_E_lhc:.3e}")
    print(f"  gap = {orders_of_magnitude_gap(eps_E_lhc):.1f} orders of magnitude")

    eps_L_ligo = ligo_length_metric()
    print(f"\nLIGO (4 km arm length, dimensional benchmark only)")
    print(f"  ε_L = l_P/L = {eps_L_ligo:.3e}")
    print(f"  gap = {orders_of_magnitude_gap(eps_L_ligo):.1f} orders of magnitude")

    print()
    print("NOTE: ε_L for LIGO is a dimensional benchmark, not a Planck sensitivity")
    print("claim. See definitions/what_counts_as_probe.md.")
    print()
    print("TODO: Add approach-specific signal estimates as approach templates are filled.")
