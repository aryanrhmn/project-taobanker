#!/usr/bin/env python3
"""Exact-arithmetic audit for the candidate 2/(5 d^3) motion bound.

This script checks all scalar inequalities in the structural reduction, the
exact finite recurrence/multiplicity calculation for 3 <= d <= 16, and the
analytic tail used for d >= 17.  It uses fractions.Fraction throughout.

It does *not* verify the imported graph-theoretic theorems or replace expert
review of their hypotheses.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


Q = Fraction


def harmonic(n: int) -> Fraction:
    return sum((Q(1, j) for j in range(1, n + 1)), Q(0))


def rising(r: int, h: int) -> int:
    out = 1
    for j in range(h):
        out *= r + j
    return out


def parameters(d: int, coefficient: Fraction = Q(2, 5)) -> tuple[Fraction, Fraction]:
    gamma = coefficient / d**3
    epsilon = 2 * gamma / (1 - gamma)
    return gamma, epsilon


@dataclass(frozen=True)
class FiniteCase:
    d: int
    m: int
    t: int
    r: int
    c_t: int
    kind: str


@dataclass(frozen=True)
class FiniteResult:
    case: FiniteCase
    M: Fraction
    K: Fraction
    U: Fraction
    max_Y: Fraction


def admissible_cases(d: int) -> Iterable[FiniteCase]:
    """Relaxed admissible cases outside the Hamming endpoint.

    Here r=m-tau_{t-1}.  Strict growth gives 1 <= r <= m-t+1.
    If c_t=t-1 then r=m-t+1 and 4 <= t <= m-1.
    Otherwise c_t>=t.  When t=m<d, c_t=m is impossible, so c_t>=m+1.
    When t=m=d, c_t is a multiple of m; outside the endpoint c_t>=2m.
    """
    for m in range(2, d + 1):
        for t in range(2, m + 1):
            for r in range(1, m - t + 2):
                if t == m:
                    c_t = 2 * m if d == t else m + 1
                else:
                    c_t = t
                yield FiniteCase(d, m, t, r, c_t, "c_t>=t")

                if 4 <= t <= m - 1 and r == m - t + 1:
                    yield FiniteCase(d, m, t, r, t - 1, "c_t=t-1")


def finite_result(case: FiniteCase, coefficient: Fraction = Q(2, 5)) -> FiniteResult:
    d, m, t, r, c_t = case.d, case.m, case.t, case.r, case.c_t
    gamma, eps = parameters(d, coefficient)
    B = 1 + (m - 1) * eps
    u_star = (1 - eps) * Q(m - 1, m)
    q = m * eps / (1 - m * eps)

    Y_values: list[Fraction] = []
    if t == 2:
        U = Q(1)
    else:
        # Exact bound for y_2=(u_1-u_2)/u_1.  The 1/k term is bounded by gamma.
        Y = B / (m - 1) + Q(m, m - 1) * gamma * (1 - u_star) / u_star
        assert 0 <= Y < 1, (case, "Y_2", Y)
        Y_values.append(Y)

        # For i=2,...,t-2, propagate the Riccati-type relative-drop bound.
        for i in range(2, t - 1):
            denominator = (r + t - 1 - i) * (1 - m * eps)
            Y = (B + m * eps * Y / (1 - Y)) / denominator
            assert 0 <= Y < 1, (case, f"Y_{i+1}", Y)
            Y_values.append(Y)

        U = Q(1)
        for Y in Y_values:
            U *= 1 - Y

    # Exact left sphere tail; rising(r,h)=r(r+1)...(r+h-1).
    left = sum((q**h / rising(r, h) for h in range(1, t + 1)), Q(0))

    # Sharper right tail at the two endpoints.
    if d == t:
        right = Q(0)
    elif d == t + 1:
        right = q / m
    else:
        right = q / (1 - q)

    K = 1 / (1 + left + right)
    M = K * U**2 * (1 - eps) ** 2 * Q(c_t * (m - 1) ** 2, r * m)
    return FiniteResult(case, M, K, U, max(Y_values, default=Q(0)))


def structural_checks() -> None:
    for d in range(3, 10_001):
        gamma, eps = parameters(d)
        alpha = (1 - gamma) / d

        assert gamma == Q(2, 5 * d**3)
        assert eps == Q(4, 5 * d**3 - 2)
        assert eps * (1 - gamma) / 2 == gamma
        assert gamma < Q(1, 9)
        assert eps < Q(2, 7)
        assert eps < Q(1, d**2)
        assert d * eps < Q(1, 2)

        # Metsch applicability and the full-clique lower bound.
        assert alpha**2 > 4 * gamma
        assert alpha - 3 * gamma / (2 * alpha) > Q(1, d + 1)

        # Bang-Koolen geometricity after the Delsarte clique bound m<d+1.
        assert (d + 1) ** 2 * gamma < alpha

        # Large-mu branch and the final comparisons in the mu=1 branch.
        assert Q(1, 4 * d**2) > gamma
        assert Q(3, 10 * d**2) > gamma

        # A convenient lower bound used to show b_1>k/3.
        assert Q(1, 2) - Q(3, 2) * gamma > Q(1, 3)


def finite_checks() -> list[FiniteResult]:
    minima: list[FiniteResult] = []
    for d in range(3, 17):
        results = [finite_result(case) for case in admissible_cases(d)]
        minimum = min(results, key=lambda result: result.M)
        assert minimum.M > 1, minimum
        minima.append(minimum)

    # The global finite minimum occurs at d=7, (m,t,r,c_t)=(6,6,1,7).
    global_min = min(minima, key=lambda result: result.M)
    assert global_min.case == FiniteCase(7, 6, 6, 1, 7, "c_t>=t")
    expected = Q(
        116108034801868413182297308409682258079489,
        115280354870777504601657083769030760079250,
    )
    assert global_min.M == expected
    return minima


def analytic_tail_checks() -> None:
    # H_{d-2} <= d/5 starts at d=17 and is preserved by induction because
    # 1/(d-1) <= 1/5 thereafter.
    assert harmonic(15) <= Q(17, 5)

    for d in range(17, 10_001):
        gamma, eps = parameters(d)
        m = d  # all loss expressions are increasing in m and t
        B = 1 + (m - 1) * eps
        A = (1 + (Q(5, 3) * m - 1) * eps) / (1 - m * eps)
        delta = A - 1
        u_star = (1 - eps) * Q(m - 1, m)

        assert A <= Q(6, 5)
        assert delta == Q(8 * m - 3, 3) * eps / (1 - m * eps)

        # Base step y_2 <= A/(m-1): a deliberately stronger sufficient bound.
        assert gamma * B / ((m - 1) * (1 - eps)) < eps
        assert A - B > Q(5, 3) * m * eps

        # The displayed analytic loss is below 1/(d+1).
        upper_loss = (
            Q(8 * (d + 1), 5 * d**3 - 2)
            + Q(8 * d * (8 * d - 3), 15 * (5 * d**3 - 4 * d - 2))
        )
        assert upper_loss < Q(1, d + 1)

        # Direct exact check of the less-coarsened loss as a backstop.
        exact_loss = 2 * (d + 1) * eps + 2 * delta * harmonic(d - 2)
        assert exact_loss < Q(1, d + 1)

    # Polynomial certificate for the analytic loss at every d>=17.
    def P(d: int) -> int:
        return (
            55 * d**6
            - 800 * d**5
            - 1380 * d**4
            - 292 * d**3
            + 1280 * d**2
            + 1032 * d
            + 300
        )

    def Qpoly(d: int) -> int:
        return 55 * d**3 - 800 * d**2 - 1380 * d - 292

    assert Qpoly(17) == 15_263 > 0
    assert 33 * 17**2 - 320 * 17 - 276 > 0  # Qpoly' / 5 at d=17
    assert P(17) > 0


def robustness_boundary() -> tuple[FiniteResult, FiniteResult]:
    # 5/12 survives this finite relaxation only narrowly; 1/2 fails it.
    five_twelfths: list[FiniteResult] = []
    one_half: list[FiniteResult] = []
    for d in range(3, 30):
        five_twelfths.extend(
            finite_result(case, Q(5, 12)) for case in admissible_cases(d)
        )
        one_half.extend(finite_result(case, Q(1, 2)) for case in admissible_cases(d))

    min_5_12 = min(five_twelfths, key=lambda result: result.M)
    min_1_2 = min(one_half, key=lambda result: result.M)
    assert min_5_12.M > 1
    assert min_1_2.M < 1
    return min_5_12, min_1_2


def main() -> None:
    structural_checks()
    minima = finite_checks()
    analytic_tail_checks()
    min_5_12, min_1_2 = robustness_boundary()

    print("All exact-arithmetic checks for the 2/(5 d^3) candidate passed.\n")
    print("Finite multiplicity minima (3 <= d <= 16):")
    for result in minima:
        c = result.case
        print(
            f"  d={c.d:2d}: M={float(result.M):.12f} "
            f"at (m,t,r,c_t)=({c.m},{c.t},{c.r},{c.c_t})"
        )

    global_min = min(minima, key=lambda result: result.M)
    print("\nGlobal finite minimum:")
    print(f"  M = {global_min.M}")
    print(f"    = {float(global_min.M):.12f}")
    print(f"  margin M-1 = {float(global_min.M - 1):.6%}")

    print("\nRobustness boundary of the same finite relaxation:")
    print(
        f"  coefficient 5/12: min M={float(min_5_12.M):.12f} "
        f"at d={min_5_12.case.d}"
    )
    print(
        f"  coefficient 1/2 : min M={float(min_1_2.M):.12f} "
        f"at d={min_1_2.case.d} (fails)"
    )
    print("\nAnalytic tail certificate checked for 17 <= d <= 10000.")
    print("Imported graph-theoretic hypotheses still require expert review.")


if __name__ == "__main__":
    main()
