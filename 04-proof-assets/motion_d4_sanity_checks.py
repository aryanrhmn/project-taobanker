"""Finite/symbolic sanity checks for the inequalities in research_note_motion_d4.tex.

This is not a formal verification of the graph-theoretic inputs.  It checks the
new one-variable inequalities and the integer endpoint estimates used in the
refined multiplicity argument.
"""
from fractions import Fraction


def check_coefficient_grid() -> None:
    # Check at rational grid points x in [0,1/16] and integer s >= 2.
    for den in range(16, 513):
        for num in range(0, den // 16 + 1):
            x = Fraction(num, den)
            if x > Fraction(1, 16):
                continue
            for s in range(2, 250):
                left = 1 - (1 + 4*x) / (s * (1-x))
                assert left >= Fraction(1, 3)
                right = (1-6*x) * (1-Fraction(1, s))
                assert left >= right


def check_arithmetic_gap(max_m: int = 10000) -> None:
    for m in range(2, max_m + 1):
        target = Fraction(m+1, m)
        for t in range(2, m+1):
            max_a = m-t+1
            for a in range(1, max_a+1):
                # It suffices to take the least allowed c_t.  The exceptional
                # c_t=t-1 case has the additional constraints below.
                for c in (t-1, t):
                    if c == t-1:
                        if not (4 <= t <= m-1 and a == m-t+1):
                            continue
                    F = Fraction(c*a*(m-1)**2, m*(a+t-2)**2)
                    if c == t and t == m and a == 1:
                        # Exact exceptional parameter set F=1.
                        assert F == 1
                    else:
                        assert F >= target, (m, t, a, c, F, target)


def check_e_gap(max_m: int = 1000) -> None:
    # Worst-case Bernoulli lower bound used in the note.
    for m in range(2, max_m+1):
        assert 1 - Fraction(1, 4*m) > Fraction(m, m+1)


def check_retuned_constants(max_d: int = 10000) -> None:
    A = 256
    for d in range(3, max_d+1):
        # Metsch and Bang--Koolen comparisons after mu <= k/(A d^3).
        assert Fraction(1, 4*d*d) >= Fraction(4, A*d**3)
        assert Fraction(25, A*d) < Fraction(1, 2*d)
        # k >= A d^3 is more than enough for m<5d and the later k-bounds.
        k0 = A*d**3
        assert k0 > 20*d
        assert k0 > (5*d)**3
        assert k0 > 32*(5*d)*d*d


if __name__ == "__main__":
    check_coefficient_grid()
    check_arithmetic_gap()
    check_e_gap()
    check_retuned_constants()
    print("All sanity checks passed.")
