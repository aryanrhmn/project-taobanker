"""Exact-arithmetic audit of the strengthened constant C0 = 5673/500 (claim: motion >= 500n/(5673 d^3)).

Verifies every constant-dependent inequality of the strengthened manuscript's
retuning layer, as reconstructed from the apply_strengthening.py patch script
and the r2 session's certificates. Graph-theoretic machinery was separately
verified line-by-line at 1/14 (see 06-fable-brief/FINDINGS.md F0); the
R-factor case analysis is constant-free and carries over verbatim.
"""
from fractions import Fraction as F

C0 = F(5673, 500)
PASS = []
def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    PASS.append(cond)
    print(f"[{status}] {name}" + (f"  {detail}" if detail else ""))

# ---------- 1. Kivva exact Johnson threshold: eps_K > 3/458 ----------
# p(x) = x^2 (x^2-1)^2 (x^2-3)(x^2-4) - 1 ; BN root theta_1 < -2 is its unique root below -2.
def p(x: F) -> F:
    x2 = x * x
    return x2 * (x2 - 1) ** 2 * (x2 - 3) * (x2 - 4) - 1

x0 = F(-913, 455)  # = -2 - 3/455
val = p(x0)
check("p(-913/455) < 0 (exact)", val < 0, f"p = {val.numerator}/{val.denominator}")
claimed = F(-12841664057813389062001, 380289177849714310556640625)
check("p(-913/455) equals manuscript's exact value", val == claimed)
# monotonicity: for x <= -2, all factors x^2, (x^2-1)^2, (x^2-3), (x^2-4) are >= 0 and increase as x decreases,
# so p is decreasing in x on (-infty,-2]; p(-2) = -1 < 0; p -> +inf. Unique root theta_1 < -2.
check("p(-2) = -1 < 0 (root bracketing base)", p(F(-2)) == -1)
# p(x0) < 0 and monotonicity => theta_1 < -913/455, i.e. s* = -2 - theta_1 > 3/455.
# eps_K = s/(1+s) is increasing in s, so eps_K > (3/455)/(1 + 3/455) = 3/458.
check("bracket algebra: (3/455)/(1+3/455) == 3/458", F(3,455)/(1+F(3,455)) == F(3,458))

# ---------- 2. eps(d=3) < 3/458 < eps_K ----------
def eps(d): return F(2, 1) / (C0 * d**3 - 1)
def gam(d): return F(1, 1) / (C0 * d**3)
e3 = eps(3)
check("eps(3) == 1000/152671", e3 == F(1000, 152671))
check("eps(3) < 3/458 (exact)", e3 < F(3, 458), f"margin = {(F(3,458)-e3)}")
check("margin equals manuscript's 13/69923318", F(3,458) - e3 == F(13, 69923318))
# eps decreasing in d => Johnson threshold check holds for all d >= 3
check("eps decreasing in d (spot d=4 < d=3)", eps(4) < e3)

# ---------- 3. C_lim < 919/81 < C0 ----------
# C_lim = (1 + 2/eps_K)/27 < (1 + 2/(3/458))/27 = (1 + 916/3)/27 = 919/81
check("(1 + 916/3)/27 == 919/81", (1 + F(916,3))/27 == F(919,81))
check("919/81 < 5673/500 (exact)", F(919,81) < C0, f"margin = {C0 - F(919,81)}")
check("margin equals manuscript's 13/40500", C0 - F(919,81) == F(13, 40500))

# ---------- 4. small-parameter certificates for all d in [3, 2000] ----------
ok = True
Hm = F(0)  # incremental H_{d-2}
worst = None
for d in range(3, 2001):
    if d == 3: Hm = F(1)
    else: Hm += F(1, d - 2)
    e, g = eps(d), gam(d)
    a = (1 - g) / F(d)
    conds = [
        e * (1 - g) / 2 == g,                      # closure identity (exact)
        g < F(1,2),
        e < F(2, 11 * d**3),
        d * e < F(1, 50),
        e < F(1, d * d),
        F(3,2) * d * d * e < 1,                    # z < 1 auxiliary
        a * a > 4 * g,                             # struct1
        a - 3 * g / (2 * a) > F(1, d + 1),         # struct2
        a > (d + 1)**2 * g,                        # struct3
        (1 - 3 * g) / 2 > F(1,3),                  # b1 > k/3 chain
        (3*d*d + 2*d + 2) * e < F(1, d + 1),       # F-loss (H_{d-2} <= d/2 route)
        2673*d**3 - 5000*d**2 - 4000*d - 2500 > 0, # equivalent polynomial certificate
        # mu=2 recurrence constants at worst case m = d:
        (1 + (F(5*d,3) - 1)*e) / (1 - d*e) < F(6,5),          # A < 6/5
        ((8*d - 3)*e) / (3*(1 - d*e)) < 3*d*e,                # delta < 3 m eps
        d * e / (1 - d * e) < 1,                              # q < 1
        # exact loss with true harmonic H_{d-2} (stronger than the d/2 route):
        2*(d+1)*e + 2*(((8*d-3)*e)/(3*(1-d*e)))*Hm < F(1, d+1),
        # mu=1 branch: k > 4 m d^2 needs C0 > 4; motion floor n/(4d^2) > gamma n:
        C0 * d > 4,
        F(1, 4*d*d) > g,
        # Doob exclusion and small checks:
        C0 * d**3 > 3*d,
        C0 * d**3 > 29,
        e < F(2, 7),
    ]
    if not all(conds):
        ok = False
        worst = (d, [i for i, c in enumerate(conds) if not c])
        break
check("all retuned scalar/branch certificates, 3 <= d <= 2000", ok, str(worst) if worst else "")

# ---------- 5. shifted-polynomial certificate (all d >= 3, analytic) ----------
# 2673 d^3 - 5000 d^2 - 4000 d - 2500 with d = x+3:
cs = [12671, 38171, 19057, 2673]  # constant..x^3, from expansion
chk = lambda x: 2673*(x+3)**3 - 5000*(x+3)**2 - 4000*(x+3) - 2500 == cs[0] + cs[1]*x + cs[2]*x**2 + cs[3]*x**3
check("F-loss shifted certificate coefficients (x=d-3) all positive", all(c > 0 for c in cs) and all(chk(x) for x in range(0, 50)))

# ---------- 6. high-precision cross-check of the true threshold ----------
from decimal import Decimal, getcontext
getcontext().prec = 60
def pd(x):
    x2 = x*x
    return x2*(x2-1)**2*(x2-3)*(x2-4) - 1
lo, hi = Decimal("-2.01"), Decimal("-2.006")
for _ in range(200):
    mid = (lo + hi) / 2
    if pd(mid) > 0: lo = mid
    else: hi = mid
theta1 = (lo + hi) / 2
epsK = (-2 - theta1) / (-1 - theta1)
Clim = (1 + 2 / epsK) / 27
print(f"  theta_1 ~ {theta1}")
print(f"  eps_K   ~ {epsK}")
print(f"  C_lim   ~ {Clim}")
check("theta_1 matches session value -2.00659361834...", abs(theta1 - Decimal("-2.0065936183460167")) < Decimal("1e-15"))
check("eps_K matches session value 0.00655042732821119...", abs(epsK - Decimal("0.006550427328211190")) < Decimal("1e-17"))
check("eps(3) < true eps_K (decimal, 60 digits)", Decimal(e3.numerator) / Decimal(e3.denominator) < epsK)
check("C_lim < C0 (decimal)", Clim < Decimal("11.346"))

print()
print(f"RESULT: {sum(PASS)}/{len(PASS)} checks passed" + ("" if all(PASS) else "  *** FAILURES PRESENT ***"))
