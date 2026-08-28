"""
constants.py — Planck units computed from CODATA fundamental constants.

Uses scipy.constants for CODATA values wherever possible.

All quantities are in SI units unless otherwise noted.
"""

import math
import scipy.constants as co


# ---------------------------------------------------------------------------
# Fundamental constants (CODATA 2018 via scipy.constants)
# ---------------------------------------------------------------------------

G = co.G          # Newtonian gravitational constant  [m³ kg⁻¹ s⁻²]
hbar = co.hbar    # Reduced Planck constant           [J s]
c = co.c          # Speed of light in vacuum          [m s⁻¹]
k_B = co.k        # Boltzmann constant                [J K⁻¹]


# ---------------------------------------------------------------------------
# Planck units
# ---------------------------------------------------------------------------

def planck_length() -> float:
    """
    Planck length: l_P = sqrt(hbar * G / c**3)

    Dimensions: [m]

    This is the unique combination of G, hbar, c with dimensions of length.
    Its appearance as a "minimum length" in theories of quantum gravity is
    model-dependent (E4); the definition itself is a derived consequence (E2).
    """
    return math.sqrt(hbar * G / c**3)


def planck_time() -> float:
    """
    Planck time: t_P = sqrt(hbar * G / c**5) = l_P / c

    Dimensions: [s]
    """
    return math.sqrt(hbar * G / c**5)


def planck_mass() -> float:
    """
    Planck mass: m_P = sqrt(hbar * c / G)

    Dimensions: [kg]
    """
    return math.sqrt(hbar * c / G)


def planck_energy() -> float:
    """
    Planck energy: E_P = m_P * c**2 = sqrt(hbar * c**5 / G)

    Dimensions: [J]
    """
    return math.sqrt(hbar * c**5 / G)


def planck_temperature() -> float:
    """
    Planck temperature: T_P = E_P / k_B

    Dimensions: [K]
    """
    return planck_energy() / k_B


# ---------------------------------------------------------------------------
# Convenience: Planck energy in electronvolts and GeV
# ---------------------------------------------------------------------------

def planck_energy_eV() -> float:
    """Planck energy in electronvolts [eV]."""
    return planck_energy() / co.eV


def planck_energy_GeV() -> float:
    """Planck energy in gigaelectronvolts [GeV]."""
    return planck_energy_eV() / 1e9


# ---------------------------------------------------------------------------
# Internal-consistency check
# ---------------------------------------------------------------------------

def check_internal_consistency() -> None:
    """
    Verify that derived relations hold to better than 1 part in 10^6.
    Raises AssertionError if any check fails.
    """
    l_P = planck_length()
    t_P = planck_time()
    m_P = planck_mass()
    E_P = planck_energy()

    # l_P / c should equal t_P
    ratio = (l_P / c) / t_P
    assert abs(ratio - 1.0) < 1e-10, f"l_P/c != t_P: ratio = {ratio}"

    # m_P * c**2 should equal E_P
    ratio2 = (m_P * c**2) / E_P
    assert abs(ratio2 - 1.0) < 1e-10, f"m_P*c^2 != E_P: ratio = {ratio2}"

    # E_P * t_P should equal hbar (Planck units relation)
    ratio3 = (E_P * t_P) / hbar
    assert abs(ratio3 - 1.0) < 1e-10, f"E_P*t_P != hbar: ratio = {ratio3}"


# ---------------------------------------------------------------------------
# Main: print a summary table
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        check_internal_consistency()
        consistency_status = "PASSED"
    except AssertionError as exc:
        consistency_status = f"FAILED: {exc}"

    print("Planck units (SI, CODATA 2018 via scipy.constants)")
    print("=" * 55)
    print(f"  Planck length     l_P  = {planck_length():.6e}  m")
    print(f"  Planck time       t_P  = {planck_time():.6e}  s")
    print(f"  Planck mass       m_P  = {planck_mass():.6e}  kg")
    print(f"  Planck energy     E_P  = {planck_energy():.6e}  J")
    print(f"  Planck energy     E_P  = {planck_energy_GeV():.6e}  GeV")
    print(f"  Planck temperature T_P = {planck_temperature():.6e}  K")
    print()
    print("Fundamental constants used:")
    print(f"  G   = {G:.6e}  m^3 kg^-1 s^-2")
    print(f"  hbar= {hbar:.6e}  J s")
    print(f"  c   = {c:.6e}  m s^-1")
    print(f"  k_B = {k_B:.6e}  J K^-1")
    print()
    print(f"Internal-consistency checks: {consistency_status}")
