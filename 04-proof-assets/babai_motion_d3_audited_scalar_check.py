#!/usr/bin/env python3
"""Exact scalar audit for the n/(12 d^3) candidate motion bound.

This verifies rational identities, one-variable inequalities, and the relaxed
integer endpoint factor used in the manuscript.  It does NOT verify the
imported graph-theoretic theorems or prove that all mathematical reductions are
correct; those require source-level/referee checking.
"""
from fractions import Fraction
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def exact_checks_to(limit: int = 10000) -> None:
    for d in range(3, limit + 1):
        D = Fraction(d)
        gamma = Fraction(1, 12 * d**3)
        eps = Fraction(2, 12 * d**3 - 1)
        alpha = (1 - gamma) / D

        require(eps * (1 - gamma) / 2 == gamma, f"closure d={d}")
        require(eps < Fraction(13, 2000), f"epsilon 0.0065 d={d}")
        require(eps < Fraction(1, d**2), f"epsilon d^-2 d={d}")
        require(eps < Fraction(1, 5 * d**3), f"epsilon (5d^3)^-1 d={d}")
        require(alpha**2 > 4 * gamma, f"Metsch trigger d={d}")
        require(alpha - 3 * gamma / (2 * alpha) > Fraction(1, d + 1),
                f"clique constant d={d}")
        require((d + 1)**2 * gamma < alpha, f"Bang-Koolen constant d={d}")
        require(alpha > gamma, f"lambda > mu constant d={d}")

        # Worst m is d for all monotone bounds below.
        m = d
        x = m * eps
        q = x / (1 - x)
        B = 1 + (m - 1) * eps
        A = (1 + (Fraction(5 * m, 3) - 1) * eps) / (1 - m * eps)
        delta = A - 1
        require(x <= Fraction(1, 45), f"x <= 1/45 d={d}")
        require(q < 1, f"q < 1 d={d}")
        require(gamma < q / m, f"h=t tail factor d={d}")
        require(A < Fraction(6, 5), f"A < 6/5 d={d}")
        require(B < 2 * (m - 1) * (1 - eps), f"base step B d={d}")
        require(A - B > Fraction(5 * m, 3) * eps, f"A-B d={d}")
        require(delta < Fraction(6, 11 * d**2), f"delta d={d}")

        # H_{d-2} <= d/2, exact.
        H = sum((Fraction(1, j) for j in range(1, d - 1)), Fraction(0))
        require(H <= Fraction(d, 2), f"harmonic d={d}")
        require(delta * H < Fraction(3, 11 * d), f"delta H d={d}")

        loss = Fraction(2 * (d + 1), 5 * d**3) + Fraction(6, 11 * d)
        require(loss < Fraction(1, d + 1), f"F loss d={d}")


def endpoint_integer_audit(m_limit: int = 2000) -> None:
    """Check the endpoint-factor inequalities under the manuscript's relaxed
    integer constraints. This is redundant with the analytic proof but catches
    sign/range errors.
    """
    for m in range(2, m_limit + 1):
        for t in range(2, m + 1):
            # Case c_t = t-1 is only admitted by the proof for 4 <= t <= m-1
            if 4 <= t <= m - 1:
                r = m - t + 1
                c = t - 1
                R = Fraction(c * r * (m - 1)**2,
                             m * (r + t - 2)**2)
                require(R >= Fraction(m + 1, m),
                        f"R equal-c case m={m},t={t}")

            # Case c_t >= t: it suffices to test c_t=t and endpoint r values,
            # except t=m where c_t=m is the designated endpoint.
            if t <= m - 1:
                for r in {1, m - t + 1}:
                    c = t
                    R = Fraction(c * r * (m - 1)**2,
                                 m * (r + t - 2)**2)
                    require(R >= Fraction(m + 1, m),
                            f"R c>=t case m={m},t={t},r={r}")
            else:  # t=m, nonendpoint requires c_t >= m+1
                r = 1
                c = m + 1
                R = Fraction(c * r * (m - 1)**2,
                             m * (r + t - 2)**2)
                require(R == Fraction(m + 1, m),
                        f"R t=m case m={m}")


def symbolic_factor_checks() -> None:
    d = sp.symbols('d', integer=True, positive=True)
    gamma = sp.Rational(1, 12) / d**3
    alpha = (1 - gamma) / d

    expressions = {
        "alpha^2-4gamma": sp.factor(alpha**2 - 4 * gamma),
        "clique margin": sp.factor(alpha - 3 * gamma / (2 * alpha) - 1 / (d + 1)),
        "Bang-Koolen margin": sp.factor(alpha - (d + 1)**2 * gamma),
        "F-loss margin": sp.factor(1 / (d + 1) - 2 * (d + 1) / (5 * d**3) - 6 / (11 * d)),
    }
    expected_numerators = {
        "alpha^2-4gamma": 144*d**6 - 48*d**5 - 24*d**3 + 1,
        "clique margin": 126*d**6 - 18*d**5 - 12*d**4 - 24*d**3 + d + 1,
        "Bang-Koolen margin": 11*d**3 - 2*d**2 - d - 1,
        "F-loss margin": 25*d**3 - 52*d**2 - 44*d - 22,
    }
    for name, expr in expressions.items():
        num, den = sp.fraction(sp.together(expr))
        require(sp.expand(num - expected_numerators[name]) == 0,
                f"unexpected numerator for {name}: {sp.factor(num)}")
        require(den.subs(d, 3) > 0, f"denominator sign for {name}")

    P = 25*d**3 - 52*d**2 - 44*d - 22
    forward = sp.expand(P.subs(d, d + 1) - P)
    require(forward == 75*d**2 - 29*d - 71, "forward difference")
    require(P.subs(d, 3) == 53, "P(3)")


def main() -> None:
    symbolic_factor_checks()
    exact_checks_to(10000)
    endpoint_integer_audit(2000)
    print("All exact scalar checks passed.")
    print("Uniform rational checks: 3 <= d <= 10000.")
    print("Relaxed endpoint-factor checks: 2 <= m <= 2000.")
    print("Scope warning: this script does not verify graph-theoretic reductions or imported theorems.")


if __name__ == "__main__":
    main()
