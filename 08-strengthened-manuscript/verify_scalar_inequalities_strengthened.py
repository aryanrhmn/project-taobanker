#!/usr/bin/env python3
"""Exact-arithmetic checks for the strengthened 500/5673 manuscript.

The script uses SymPy rationals only for every proof-critical comparison.  For
inequalities in d >= 3, it substitutes d = x + 3 and checks that the numerator
has nonnegative rational coefficients and positive constant term.  It also
certifies the rational lower bracket 3/458 for Kivva's exact Johnson threshold.
"""

from __future__ import annotations

import sympy as sp


d, x, m, t, a, b, e, y, z = sp.symbols(
    "d x m t a b e y z", real=True
)
C0 = sp.Rational(5673, 500)


def assert_zero(expr: sp.Expr, name: str) -> None:
    value = sp.factor(sp.together(expr))
    assert value == 0, f"{name}: expected 0, got {value}"
    print(f"PASS identity: {name}")


def positive_poly_for_d_ge_3(poly: sp.Expr, name: str) -> None:
    shifted = sp.Poly(sp.expand(poly.subs(d, x + 3)), x, domain=sp.QQ)
    coeffs = shifted.all_coeffs()
    assert all(c >= 0 for c in coeffs), (
        f"{name}: d=x+3 polynomial has a negative coefficient: {shifted.as_expr()}"
    )
    assert shifted.eval(0) > 0, f"{name}: constant term is not positive"
    print(f"PASS d>=3 polynomial: {name} -> {shifted.as_expr()}")


def positive_rational_for_d_ge_3(expr: sp.Expr, name: str) -> None:
    num, den = sp.fraction(sp.factor(sp.together(expr)))
    positive_poly_for_d_ge_3(sp.expand(num), name)
    assert den.subs(d, 3) > 0, f"{name}: denominator not positive at d=3: {den}"
    print(f"      denominator: {sp.factor(den)}")


def main() -> None:
    gamma = 1 / (C0 * d**3)
    eps = 2 / (C0 * d**3 - 1)
    alpha = (1 - gamma) / d

    assert C0 == sp.Rational(5673, 500)
    assert C0 > sp.Rational(919, 81)
    print(f"PASS chosen coefficient: C0={C0}, margin over 919/81={sp.factor(C0-sp.Rational(919,81))}")

    # Parameter identities and elementary bounds.
    assert_zero(eps * (1 - gamma) / 2 - gamma, "closure identity (3)")
    positive_rational_for_d_ge_3(sp.Rational(1, 2) - gamma, "gamma < 1/2")
    positive_rational_for_d_ge_3(sp.Rational(2, 11) / d**3 - eps, "epsilon < 2/(11 d^3)")
    positive_rational_for_d_ge_3(sp.Rational(1, 50) - d * eps, "d epsilon < 1/50")
    positive_rational_for_d_ge_3(sp.Rational(1, 2) - eps, "epsilon < 1/2")
    positive_rational_for_d_ge_3(eps - 2 * gamma, "2 gamma < epsilon")
    assert sp.factor((d * eps).subs(d, 3) - sp.Rational(3000, 152671)) == 0
    print("PASS displayed d=3 value: d epsilon = 3000/152671")

    # The cycle dispatch: for d>=3, gamma <= 500/(5673*27) < 1/3,
    # while a cycle with diameter >=3 has n>=6 and n-2 >= 2n/3.
    assert sp.Rational(500, 5673 * 27) < sp.Rational(1, 3)
    print("PASS cycle-case numerical domination")

    # Structural inequalities (17).
    positive_rational_for_d_ge_3(alpha**2 - 4 * gamma, "(17a) alpha^2 > 4 gamma")
    positive_rational_for_d_ge_3(
        alpha - 3 * gamma / (2 * alpha) - 1 / (d + 1),
        "(17b) alpha - 3 gamma/(2 alpha) > 1/(d+1)",
    )
    positive_rational_for_d_ge_3(alpha - (d + 1) ** 2 * gamma, "(17c) (d+1)^2 gamma < alpha")
    positive_rational_for_d_ge_3((1 - 3 * gamma) / 2 - sp.Rational(1, 3), "b1 scalar lower bound")
    positive_rational_for_d_ge_3(1 / (4 * d**2) - gamma, "relation-bound branches exceed gamma")

    # Exact Kivva threshold bracket.  Put h(Y)=Y(Y-1)^2(Y-3)(Y-4)-1.
    # Kivva's theta_1 is the smallest root of p(theta)=h(theta^2).
    h = y * (y - 1) ** 2 * (y - 3) * (y - 4) - 1
    hprime_shift = sp.Poly(sp.expand(sp.diff(h, y).subs(y, z + 4)), z, domain=sp.QQ)
    assert all(c >= 0 for c in hprime_shift.all_coeffs())
    assert hprime_shift.eval(0) > 0
    print(f"PASS monotonicity for y>=4: h'(z+4)={hprime_shift.as_expr()}")

    theta0 = -sp.Rational(913, 455)  # -2 - 3/455
    p0 = sp.factor(theta0**2 * (theta0**2 - 1) ** 2 * (theta0**2 - 3) * (theta0**2 - 4) - 1)
    expected_p0 = -sp.Rational(
        12841664057813389062001,
        380289177849714310556640625,
    )
    assert p0 == expected_p0 and p0 < 0
    print(f"PASS Kivva root bracket polynomial value: p(-913/455)={p0}")

    eps_at_3 = sp.factor(eps.subs(d, 3))
    assert eps_at_3 == sp.Rational(1000, 152671)
    threshold_margin = sp.Rational(3, 458) - eps_at_3
    assert threshold_margin == sp.Rational(13, 69923318) > 0
    print(f"PASS epsilon(d=3) < 3/458: margin={threshold_margin}")

    # Kivva strict-growth interface and z<1.
    positive_rational_for_d_ge_3(1 / d**2 - eps, "epsilon < 1/d^2")
    positive_rational_for_d_ge_3(1 - sp.Rational(3, 2) * d**2 * eps, "(3/2)d^2 epsilon < 1")

    # High-theta and mu=1 scalar interfaces.
    positive_rational_for_d_ge_3(C0 * d**3 / 6 - d, "C0 d^3/6 > d")
    positive_rational_for_d_ge_3(C0 * d**3 - 4 * d**3, "C0 d^3 > 4 d^3")
    positive_rational_for_d_ge_3(C0 * d**3 - 3 * d, "C0 d^3 > 3d")
    assert C0 * 3**3 > 29
    print("PASS valency thresholds for Johnson, mu=1, and Doob exclusion")

    # Small-parameter estimates.  Put X=m epsilon, with 0 <= X < 1/50.
    X = sp.symbols("X", real=True)
    A_upper = (1 + sp.Rational(5, 3) * X) / (1 - X)
    derivative = sp.factor(sp.diff(A_upper, X))
    assert derivative.subs(X, sp.Rational(1, 100)) > 0
    assert sp.factor(sp.Rational(6, 5) - A_upper.subs(X, sp.Rational(1, 50))) > 0
    print(f"PASS A<6/5: derivative={derivative}, endpoint={A_upper.subs(X, sp.Rational(1,50))}")

    delta_coefficient = 8 / (3 * (1 - X))
    assert sp.diff(delta_coefficient, X).subs(X, sp.Rational(1, 100)) > 0
    assert sp.factor(3 - delta_coefficient.subs(X, sp.Rational(1, 50))) > 0
    print(f"PASS delta<3 d epsilon: endpoint coefficient={delta_coefficient.subs(X, sp.Rational(1,50))}")

    positive_rational_for_d_ge_3(sp.Rational(1, 3) - eps, "epsilon < 1/3")

    B = 1 + (m - 1) * e
    A = (1 + (sp.Rational(5, 3) * m - 1) * e) / (1 - m * e)
    assert_zero(A - B - m * e * (B + sp.Rational(2, 3)) / (1 - m * e), "A-B identity")

    q_at_endpoint = sp.Rational(1, 50) / (1 - sp.Rational(1, 50))
    assert q_at_endpoint < 1
    print(f"PASS q<1 at worst endpoint: q={q_at_endpoint}")

    # Scalar parts of the R case split.
    assert_zero(a * b - 2 * (a + b - 2) - (a - 2) * (b - 2), "ab >= 2(a+b-2) decomposition")
    assert (2 * (m - 2) - (m + 1)).subs(m, 5) == 0
    print("PASS 2(m-2) >= m+1 for m>=5")

    g = t / (t - 1) ** 2
    assert_zero(sp.diff(g, t) + (t + 1) / (t - 1) ** 3, "monotonicity derivative")
    assert_zero((m - 1) ** 3 - (m + 1) * (m - 2) ** 2 - (3 * m - 5), "r=1 endpoint identity")
    assert (3 * m - 5).subs(m, 3) > 0
    print("PASS r=1 endpoint inequality for m>=3")

    assert sp.factor(2 * (m - 1) - (m + 1)) == m - 3
    print("PASS opposite endpoint inequality for m>=3")

    # Harmonic-loss estimate and strengthened polynomial certificate.
    loss_poly = 2673 * d**3 - 5000 * d**2 - 4000 * d - 2500
    positive_poly_for_d_ge_3(loss_poly, "(3d^2+2d+2)epsilon < 1/(d+1)")
    expected_shift = 2673 * x**3 + 19057 * x**2 + 38171 * x + 12671
    assert sp.expand(loss_poly.subs(d, x + 3)) == expected_shift
    print("PASS displayed strengthened x=d-3 polynomial certificate")

    # Exact regression sweep.
    for D in range(3, 501):
        G = sp.Rational(500, 5673 * D**3)
        E = sp.Rational(1000, 5673 * D**3 - 500)
        assert G < sp.Rational(1, 2)
        assert E < sp.Rational(2, 11 * D**3)
        assert D * E < sp.Rational(1, 50)
        assert E < sp.Rational(1, D**2)
        assert sp.Rational(3, 2) * D**2 * E < 1
        assert (3 * D**2 + 2 * D + 2) * E < sp.Rational(1, D + 1)
    print("PASS exact regression sweep for 3 <= d <= 500")

    print("\nAll strengthened exact-arithmetic checks passed.")


if __name__ == "__main__":
    main()
