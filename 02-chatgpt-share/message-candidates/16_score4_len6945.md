bash -lc cat > /mnt/data/babai_motion_d3_sharpened_audit.py <<'PY'
#!/usr/bin/env python3
"""Supplementary audit for the candidate n/(8 d^3) motion bound.

The proof in the accompanying note is analytic.  This script independently checks
all finite/scalar inequalities used there, using exact rational arithmetic wherever
practical and high-precision Decimal arithmetic for the long harmonic sweep.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from math import cos, pi

getcontext().prec = 80


def harmonic_fraction(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def check_structural_constants(limit: int = 10000) -> None:
    for d in range(3, limit + 1):
        gamma = Fraction(1, 8 * d**3)
        alpha = (1 - gamma) / d
        epsilon = Fraction(13, 50 * d**3)

        assert alpha * alpha > 4 * gamma
        assert alpha - Fraction(3, 2) * gamma / alpha > Fraction(1, d + 1)
        assert (d + 1) ** 2 * gamma < alpha
        assert epsilon * (1 - gamma) / 2 > gamma
        assert epsilon > gamma
        assert epsilon < Fraction(2, 7)
        assert epsilon < Fraction(1, d * d)
        if d >= 4:
            # Kivva's published constant is > 0.0065.
            assert epsilon < Fraction(65, 10000)


def check_recurrence_endpoint() -> None:
    q = Fraction(9, 4)
    xmax = Fraction(4, 121)
    A = (1 + q * xmax) / (1 - xmax)
    assert A == Fraction(10, 9)
    assert 1 - A / 2 == 1 / q

    # Base step: u_0 <= Q u_1 in the worst case m=2.
    epsmax = xmax / 2
    assert q * (1 - epsmax) / 2 > 1


def check_hamming_constants(limit: int = 10000) -> None:
    # Exact endpoint checks that are separated in the proof.
    expected = {
        3: Fraction(1284860332337, 313236902250000),
        4: Fraction(1838147774924563, 162363867136000000),
    }
    for d in (3, 4):
        eps = Fraction(13, 50 * d**3)
        x = d * eps
        delta = Fraction(13, 4) * x / (1 - x)
        F = (1 - 2 * x) * (1 - delta * harmonic_fraction(d - 2)) ** 2 * (1 - eps) ** 2
        diff = F - Fraction(d, d + 1)
        assert diff == expected[d]
        assert diff > 0

    # High-precision sweep for the exact F_d inequality.
    H = Decimal(0)
    min_margin = None
    min_d = None
    for d in range(3, limit + 1):
        if d >= 3:
            # H_{d-2}; update by adding 1/(d-2) after d increases.
            if d == 3:
                H = Decimal(1)
            elif d > 3:
                H += Decimal(1) / Decimal(d - 2)

        dd = Decimal(d)
        eps = Decimal(13) / (Decimal(50) * dd**3)
        x = Decimal(13) / (Decimal(50) * dd**2)
        delta = Decimal(169) / (Decimal(200) * dd**2 - Decimal(52))
        F = (1 - 2 * x) * (1 - delta * H) ** 2 * (1 - eps) ** 2
        margin = F - dd / (dd + 1)
        assert margin > 0
        if min_margin is None or margin < min_margin:
            min_margin = margin
            min_d = d

        assert x <= Decimal(4) / Decimal(121)
        assert delta * H < 1

    # Analytic inequalities used for all d >= 5.
    for d in range(5, limit + 1):
        assert Fraction(13, 25 * d**2) + Fraction(13, 25 * d**3) < Fraction(1, 8 * d)
        assert Fraction(169, 245 * d) < Fraction(7, 10 * d)
        assert Fraction(33, 40 * d) < Fraction(1, d + 1)

    print(f"  smallest high-precision Hamming margin: d={min_d}, margin={min_margin}")


def check_R_factor(max_m: int = 300) -> None:
    one = Fraction(1)
    for m in range(2, max_m + 1):
        target = one + Fraction(1, m)
        for t in range(2, m + 1):
            # Case c_t >= t.  The smallest allowed c_t is t; the sole exception
            # is (t,r,c_t)=(m,1,m).
            for r in range(1, m - t + 2):
                R = Fraction(t * r * (m - 1) ** 2, m * (r + t - 2) ** 2)
                if t == m and r == 1:
                    assert R == 1
                else:
                    assert R >= target, (m, t, r, R, target)

            # Case c_t=t-1 can occur only for 4 <= t <= m-1, and then
            # r=m-t+1.
            if 4 <= t <= m - 1:
                r = m - t + 1
                R = Fraction((t - 1) * r, m)
                assert R >= target, (m, t, r, R, target)


def dual_fraction(d: int, m: int, u: Fraction) -> Fraction:
    eta = Fraction(1, 8 * d * d)
    return u * (eta * m * u - (m - 2)) / ((m - 1) * (u + 1) ** 2)


def check_mu_one(max_d: int = 500) -> None:
    for d in range(3, max_d + 1):
        gamma = Fraction(1, 8 * d**3)
        for m in range(3, d + 1):
            u0 = Fraction(8 * d**3, m)
            assert dual_fraction(d, m, u0) > gamma, (d, m)

        assert Fraction(2, 8 * d**3 + 3 * d) > gamma
        assert Fraction(1, 16) > gamma


def check_local_cycle_modes(max_cycle: int = 1000) -> None:
    # Supplemental numerical check of the Fourier-mode lemma used at d=3.
    threshold = 2 * cos(8 * pi / 9) - 1
    assert threshold < -2.5
    worst = -10.0
    for ell in range(2, max_cycle + 1):
        candidates = []
        for r in range(1, ell):
            theta = 2 * pi * r / ell
            if 2 * pi / 3 - 1e-15 <= theta <= 4 * pi / 3 + 1e-15:
                vals = [2 * cos((theta + 2 * pi * j) / 3) - 1 for j in range(3)]
                candidates.append(min(vals))
        assert candidates
        witness = min(candidates)
        assert witness <= threshold + 1e-12
        worst = max(worst, witness)


def check_global_reduction(limit: int = 10000) -> None:
    def g(r: int) -> Fraction:
        if r <= 2:
            return Fraction(1, 8)
        return Fraction(1, 8 * r**3)

    def gp(r: int) -> Fraction:
        assert r >= 4
        return g(r // 2) / 2

    for d in range(3, limit + 1):
        target = g(d)
        assert Fraction(1, 14) > target
        assert g(d // 2) >= target
        if d >= 4:
            assert gp(d) >= target
        if d // 2 >= 4:
            assert gp(d // 2) >= target


def main() -> None:
    print("Auditing candidate n/(8 d^3) motion theorem...")
    check_structural_constants()
    print("  structural, Metsch, geometricity, and low-spectrum constants passed")
    check_recurrence_endpoint()
    print("  sharpened standard-sequence recurrence endpoint passed")
    check_hamming_constants()
    print("  exact Hamming-stability constants passed")
    check_R_factor()
    print("  full abstract R-factor domain passed for 2 <= m <= 300")
    check_mu_one()
    print("  exact mu=1 dual-transfer inequalities passed for 3 <= d <= 500")
    check_local_cycle_modes()
    print("  d=3 local Fourier-mode check passed for cycle lengths <= 1000")
    check_global_reduction()
    print("  imprimitive reduction constants passed for 3 <= d <= 10000")
    print("All supplementary audit checks passed.")


if __name__ == "__main__":
    main()
PY
chmod +x /mnt/data/babai_motion_d3_sharpened_audit.py
python /mnt/data/babai_motion_d3_sharpened_audit.py