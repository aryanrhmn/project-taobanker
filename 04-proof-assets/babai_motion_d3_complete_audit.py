#!/usr/bin/env python3
"""Exact scalar audit for the proof draft

    motion(X) >= n/(14 d^3)

outside the Johnson and Hamming families for primitive distance-regular graphs.

This script verifies every purely scalar inequality and every finite integer
inequality used in the new parts of the proof.  It does NOT verify the imported
graph-theoretic theorems of Pyber--Skresanov, Kivva, Bang--Koolen,
Terwilliger, Biggs, Metsch, or Egawa.

All rational checks use fractions.Fraction.  Polynomial certificates use SymPy.
"""

from __future__ import annotations

from fractions import Fraction
from math import prod
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def shifted_coefficients(poly: sp.Expr, var: sp.Symbol, shift: int) -> list[int]:
    x = sp.symbols("x", nonnegative=True)
    p = sp.Poly(sp.expand(poly.subs(var, x + shift)), x)
    return [int(c) for c in reversed(p.all_coeffs())]


def check_polynomial_certificates() -> None:
    d = sp.symbols("d", real=True)

    p_alpha2 = 196*d**6 - 56*d**5 - 28*d**3 + 1
    p_metsch = 175*d**6 - 21*d**5 - 14*d**4 - 28*d**3 + d + 1
    p_bk = 13*d**3 - 2*d**2 - d - 1
    p_loss = 2*d**3 + 8*d**2 + 16*d - 5

    for name, poly in {
        "alpha^2 > 4 gamma": p_alpha2,
        "full Metsch clique > k/(d+1)": p_metsch,
        "Bang--Koolen closure": p_bk,
        "Hamming loss < 1/(d+1)": p_loss,
    }.items():
        coeffs = shifted_coefficients(poly, d, 3)
        require(all(c >= 0 for c in coeffs), f"negative shifted coefficient: {name}: {coeffs}")
        require(coeffs[0] > 0, f"zero constant term after shift: {name}")


def check_scalar_range(limit: int = 100_000) -> None:
    for d in range(3, limit + 1):
        gamma = Fraction(1, 14*d**3)
        eps = Fraction(2, 14*d**3 - 1)
        alpha = Fraction(1, d) * (1 - gamma)

        require(eps * (1 - gamma) / 2 == gamma, f"closure failed at d={d}")
        require(gamma < Fraction(1, 2), f"gamma >= 1/2 at d={d}")
        require(eps > gamma, f"epsilon <= gamma at d={d}")
        require(eps < Fraction(1, 7), f"epsilon >= 1/7 at d={d}")
        require(eps < Fraction(65, 10_000), f"epsilon >= 0.0065 at d={d}")
        require(eps < Fraction(1, d*d), f"epsilon >= 1/d^2 at d={d}")
        require(2*d*eps < Fraction(1, 30), f"m epsilon upper bound failed at d={d}")

        require(alpha*alpha > 4*gamma, f"alpha^2 <= 4 gamma at d={d}")
        require(alpha - 3*gamma/(2*alpha) > Fraction(1, d+1),
                f"Metsch scalar failed at d={d}")
        require(alpha > (d+1)**2 * gamma, f"Bang--Koolen scalar failed at d={d}")

        # Worst-case m=d for the recurrence constants.
        m = d
        x = m*eps
        C = 1 + (Fraction(5*m, 3) - 1)*eps
        A = C/(1-x)
        delta = A - 1
        require(x < Fraction(1, 60), f"m epsilon >=1/60 at d={d}")
        require(A < Fraction(6, 5), f"A >=6/5 at d={d}")
        require(delta < 3*m*eps, f"delta >=3m epsilon at d={d}")

        loss = 2*(m+1)*eps + 2*delta*sum(Fraction(1, j) for j in range(1, max(1, d-1)))
        # The proof uses the coarser H_{d-2} <= d-2.  This exact check is stronger.
        require(loss < Fraction(1, d+1), f"exact Hamming loss failed at d={d}: {loss}")

        coarse_loss = eps*(6*d*d - 10*d + 2)
        require(coarse_loss < Fraction(1, d+1), f"coarse Hamming loss failed at d={d}")

        # Published spectral gap on the dual in the mu=1 branch.
        eta = Fraction(1, 8*d*d)
        dual_fraction = eta - Fraction(1, 14*d*d)
        require(dual_fraction == Fraction(3, 56*d*d), f"dual fraction arithmetic at d={d}")
        require(dual_fraction/2 > gamma, f"mu=1 transfer too weak at d={d}")


def check_R_factor(max_m: int = 2_000) -> None:
    """Exhaust the integer cases in the strengthened Kivva multiplicity factor.

    r = m - tau_{t-1}, 1 <= r <= m-t+1.
    R = c_t r (m-1)^2 / [m(r+t-2)^2].
    Outside c_t=t=m=d, the proof claims R >= 1+1/m.
    """
    worst: tuple[Fraction, tuple[int, int, int, int, str]] | None = None

    for m in range(2, max_m + 1):
        target = Fraction(m+1, m)

        # Case c_t=t-1: the source argument forces 4 <= t <= m-1 and r=m-t+1.
        for t in range(4, m):
            r = m - t + 1
            c = t - 1
            R = Fraction(c*r*(m-1)**2, m*(r+t-2)**2)
            require(R >= target, f"R failure, c=t-1: m={m}, t={t}, R={R}, target={target}")
            if worst is None or R/target < worst[0]:
                worst = (R/target, (m, t, r, c, "c=t-1"))

        # Case c_t >= t and t <= m-1.  The minimum in c is c=t.
        for t in range(2, m):
            for r in range(1, m-t+2):
                c = t
                R = Fraction(c*r*(m-1)**2, m*(r+t-2)**2)
                require(R >= target, f"R failure, c>=t: m={m}, t={t}, r={r}, R={R}")
                if worst is None or R/target < worst[0]:
                    worst = (R/target, (m, t, r, c, "c>=t"))

        # t=m, r=1: outside the endpoint c=m, one has c>=m+1.
        t = m
        r = 1
        c = m + 1
        R = Fraction(c*r*(m-1)**2, m*(r+t-2)**2)
        require(R == target, f"endpoint-adjacent R arithmetic failed at m={m}")
        if worst is None or R/target < worst[0]:
            worst = (R/target, (m, t, r, c, "t=m,c>=m+1"))

    require(worst is not None, "no R cases checked")
    ratio, data = worst
    print(f"R-factor minimum ratio R/(1+1/m) = {ratio} at {data}")


def check_endpoint_and_auxiliary(max_m: int = 10_000) -> None:
    # Endpoint inequalities used to prove R >= 1+1/m.
    for m in range(3, max_m + 1):
        for t in range(2, m):
            require(t*(m-1)**2 >= (m+1)*(t-1)**2,
                    f"r=1 endpoint inequality failed: m={m}, t={t}")
            require(t*(m-t+1) >= m+1,
                    f"r=m-t+1 endpoint inequality failed: m={m}, t={t}")

    for m in range(5, max_m + 1):
        for t in range(4, m):
            require((t-1)*(m-t+1) >= m+1,
                    f"c=t-1 case inequality failed: m={m}, t={t}")


def main() -> None:
    check_polynomial_certificates()
    check_scalar_range()
    check_R_factor()
    check_endpoint_and_auxiliary()
    print("All exact scalar and integer audit checks passed.")
    print("Checked all d with 3 <= d <= 100000 using exact rational arithmetic.")
    print("Checked all strengthened multiplicity R-cases with 2 <= m <= 2000.")
    print("Checked endpoint inequalities with 3 <= m <= 10000.")
    print("IMPORTANT: imported graph-theoretic theorems are not machine-verified by this script.")


if __name__ == "__main__":
    main()
