"""Independent re-implementation of the unit-coefficient manuscript's mu=2 certificate
(Lemma 7.2 + d>=53 tail), built solely from the displayed formulas (32)-(50).
Exact rational arithmetic throughout."""
from fractions import Fraction as F
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def params(d):
    g = F(1, d**3)
    e = F(2, d**3 - 1)
    return g, e

def coarse_M(d, m, t, r, case):
    """Coarse envelope value M from (32)-(36). case in {'t2','eq','gen'}.
    Returns (M, min_one_minus_Y) or (None, reason) if an envelope breaks."""
    g, e = params(d)
    B = 1 + (m - 1) * e
    ustar = (1 - e) * F(m - 1, m)
    q = m * e / (1 - m * e)
    if t == 2:
        L2 = F(2 * m, m - 1) * g * (1 + g)
        if (d, m) == (3, 3):
            Q2 = e / (1 - 3 * e)
        else:
            Q2 = sum(q**j for j in range(1, d - 2 + 1))
        M = F(2 * m, m - 1) * ustar**2 / (1 + L2 + Q2)
        return M, None
    # t >= 3
    if case == 'eq':
        chi = m * (t - 1) * g
        c0 = t - 1
    else:
        chi = m * e
        if t < m:
            c0 = t
        elif t == m < d:
            c0 = m + 2
        else:  # t == m == d, nonendpoint
            c0 = 2 * m
    # Y-envelopes (33)-(34)
    Y = {1: B / F(m)}
    Y[2] = (B + m * g * Y[1] / (1 - Y[1])) / (m - 1)
    minfac = 1 - Y[2]
    for i in range(2, t - 1):          # defines Y[i+1], i = 2..t-2
        h = 2 * m * g if i == 2 else chi
        den = (r + t - 1 - i) * (1 - chi / (i + 1))
        if Y[i] >= 1 or den <= 0:
            return None, f"envelope breaks at Y[{i}]"
        Y[i + 1] = (B + h * Y[i] / (1 - Y[i])) / den
        if 1 - Y[i + 1] < minfac:
            minfac = 1 - Y[i + 1]
    U = ustar
    for i in range(2, t):
        if Y[i] >= 1:
            return None, f"Y[{i}] >= 1"
        U *= (1 - Y[i])
    # left-tail ells (35)
    ell = {1: g, 2: F(2 * m, m - 1) * g}
    for i in range(3, t):
        ell[i] = chi / ((r + t - i) * (1 - chi / i))
    ell[t] = chi / (r * (1 - chi))
    Lsum = F(0)
    for j in range(1, t + 1):
        prod = F(1)
        for i in range(j, t + 1):
            prod *= ell[i]
        Lsum += prod
    Qsum = sum(q**j for j in range(1, d - t + 1))
    M = F(m * c0) * U**2 / (r * (1 + Lsum + Qsum))
    return M, minfac

def scan_coarse(dmax=52):
    exceptions = []
    global_minfac = None
    for d in range(3, dmax + 1):
        for m in range(3, d + 1):
            for t in range(2, m + 1):
                if t == 2:
                    M, _ = coarse_M(d, m, t, 1, 't2')
                    if M <= 1:
                        exceptions.append(('t2', d, m, t, None))
                    continue
                # equality case: c_t = t-1, needs 4 <= t <= m-1, r = m-t+1
                if 4 <= t <= m - 1:
                    r = m - t + 1
                    M, mf = coarse_M(d, m, t, r, 'eq')
                    if M is None or M <= 1:
                        exceptions.append(('eq', d, m, t, r))
                    if mf is not None:
                        global_minfac = mf if global_minfac is None else min(global_minfac, mf)
                # generic case: all admissible r (t=m forces r=1)
                rmax = 1 if t == m else m - t + 1
                for r in range(1, rmax + 1):
                    M, mf = coarse_M(d, m, t, r, 'gen')
                    if M is None or M <= 1:
                        exceptions.append(('gen', d, m, t, r))
                    if mf is not None:
                        global_minfac = mf if global_minfac is None else min(global_minfac, mf)
    return exceptions, global_minfac

# ---------------- refined certificates ----------------
def refined_pieces(d, m, t, r, c, beta, tail):
    """Compute (M_{t-1}, M_t, M_{t-2}) at integer beta with tail in {'beta','inf'}."""
    g, e = params(d)
    B = 1 + (m - 1) * e
    ustar = (1 - e) * F(m - 1, m)
    b = F(beta)
    Y = {1: B / F(m)}
    Y[2] = (B + Y[1] / (b * (1 - Y[1]))) / (m - 1)
    for i in range(2, t - 1):
        cs = 2 if i == 2 else c
        den = (r + t - 1 - i) * (1 + 1 / b - F(c, i + 1) / b)
        if Y[i] >= 1 or den <= 0:
            return None
        Y[i + 1] = (B + (F(cs) / b) * Y[i] / (1 - Y[i])) / den
    U = {1: ustar}
    for j in range(2, t):
        if Y[j] >= 1:
            return None
        U[j] = U[j - 1] * (1 - Y[j])
    # hat-ells (39)
    ell = {1: 1 / (m * b), 2: F(2) / ((m - 1) * b)}
    for i in range(3, t):
        ell[i] = F(c) / ((r + t - i) * (b + 1 - F(c, i)))
    ell[t] = F(c) / (r * (b + 1 - c))
    Lsum = F(0)
    for j in range(1, t + 1):
        prod = F(1)
        for i in range(j, t + 1):
            prod *= ell[i]
        Lsum += prod
    qb = e * m * b / (b + 1 - e * m * b)
    qi = m * e / (1 - m * e)
    qq = qi if tail == 'inf' else qb
    Qsum = sum(qq**j for j in range(1, d - t + 1))
    D = 1 + Lsum + Qsum
    Mt1 = F(m * c, r) * U[t - 1]**2 / D
    # M_t: Y_t from recurrence with b_{t-1} >= r(beta+1-c)
    den_t = r * (1 + 1 / b - F(c) / b)
    Yt = (B + (F(c) / b) * Y[t - 1] / (1 - Y[t - 1])) / den_t if t - 1 in Y and Y[t - 1] < 1 else None
    Mt = None
    if Yt is not None and Yt < 1:
        Ut = U[t - 1] * (1 - Yt)
        Mt = m * b * Ut**2 / D
    # M_{t-2}
    Mt2 = None
    if t - 2 >= 1 and (t - 2) in U:
        Mt2 = F(m * c * (t - 1), r * (m - t + 2)) / b * U[t - 2]**2 / D
    return Mt1, Mt, Mt2

def beta0_of(d, m, c):
    g, e = params(d)
    b0 = d**3 // m + 1
    while not (m * b0 > d**3 and F(c) < e * m * b0):
        b0 += 1
    return b0

ROWS = [
    ('t2',        (3, 3, 2, 2, 2),   10, 't',      None),
    ('ep3',       (3, 3, 3, 1, 6),   27, 'bridge', 41),
    ('ep4',       (4, 4, 4, 1, 8),   64, 'one',    None),
    ('int54',     (5, 4, 4, 1, 6),   94, 'one',    None),
    ('eq554',     (5, 5, 4, 2, 3),   38, 't',      None),
    ('eq654',     (6, 5, 4, 2, 3),   65, 'one',    None),
    ('int655',    (6, 5, 5, 1, 7),  151, 'one',    None),
    ('gen665',    (6, 6, 5, 1, 5),   90, 'one',    None),
    ('eq665',     (6, 6, 5, 2, 4),   72, 'one',    None),
    ('int766',    (7, 6, 6, 1, 8),  229, 'one',    None),
    ('gen776',    (7, 7, 6, 1, 6),  147, 'bridge', 180),
    ('gen887',    (8, 8, 7, 1, 7),  224, 'bridge', 306),
    ('gen998',    (9, 9, 8, 1, 8),  324, 'bridge', 456),
    ('gen10109',  (10, 10, 9, 1, 9), 450, 'bridge', 619),
    ('gen111110', (11, 11, 10, 1, 10), 605, 'bridge', 787),
    ('gen121211', (12, 12, 11, 1, 11), 792, 'bridge', 958),
    ('gen131312', (13, 13, 12, 1, 12), 1014, 'bridge', 1130),
    ('gen141413', (14, 14, 13, 1, 13), 1274, 'bridge', 1303),
    ('gen151514', (15, 15, 14, 1, 14), 1575, 'one',   None),
]

def t2_certificate(d, m, c, beta0):
    """t=2 refined: k k1 u1^2/n with exact beta; plus M_2 (the t-sphere term k k_2 u_2^2/n)."""
    g, e = params(d)
    B = 1 + (m - 1) * e
    ustar = (1 - e) * F(m - 1, m)
    qi = m * e / (1 - m * e)
    results = []
    b = F(beta0)
    # n/k2 <= 1 + L2b + Q: L2b = (1+k)/k2*... exact: (k0+k1)/k2 = (1+m*b)/(m*b*(m-1)*b/2)
    k2ratio = (1 + m * b) * 2 / (m * b * (m - 1) * b)
    Q = sum(qi**j for j in range(1, d - 2 + 1))
    D = 1 + k2ratio + Q
    M1 = F(2 * m, m - 1) * ustar**2 / D
    # t-term: u2 via recurrence, b1=(m-1)beta, c1=1
    y1 = 1 - ustar
    y2 = (B + (1 / b) * y1 / (1 - y1)) / (m - 1)
    M2 = None
    if y2 < 1:
        u2 = ustar * (1 - y2)
        # k k2 u2^2/n >= (k2/n)*k*u2^2 >= (m*(m-1)*b/2)*u2^2 / D  [k2 = k(m-1)b/2 / k... k*k2/n >= k2*k/(k2*D) = k/D? no:]
        # k k2 u2^2 / n = k u2^2 * (k2/n) >= k u2^2 / D_n where n/k2 <= D  => = (m*b)*u2^2/D
        M2 = m * b * u2**2 / D
    return M1, M2

print("=" * 70)
print("PART 1: coarse scan 3 <= d <= 52")
exc, minfac = scan_coarse(52)
print(f"exceptional tuples found: {len(exc)}")
for row in exc:
    print("  ", row)
print(f"min (1 - Y_i) over scan: {float(minfac):.6f}  (claim: > 0.388)")

print()
print("=" * 70)
print("PART 2: refined certificates for the 19 rows")
worst = None
for name, (d, m, t, r, c), b0_claim, kind, cutoff in ROWS:
    b0 = beta0_of(d, m, c)
    ok_b0 = (b0 == b0_claim)
    if name == 't2':
        M1, M2 = t2_certificate(d, m, c, b0)
        val = M1 + (M2 or 0)
        status = val > 1
        print(f"{name:10s} beta0={b0} (claim {b0_claim} {'OK' if ok_b0 else 'MISMATCH'}) cert=t  value={float(val):.9f} {'PASS' if status else 'FAIL'}")
        if worst is None or val < worst[0]: worst = (val, name)
        continue
    if kind == 'one':
        pieces = refined_pieces(d, m, t, r, c, b0, 'inf')
        val = pieces[0]
        status = val > 1
        print(f"{name:10s} beta0={b0} (claim {b0_claim} {'OK' if ok_b0 else 'MISMATCH'}) cert=one value={float(val):.9f} {'PASS' if status else 'FAIL'}")
        if worst is None or val < worst[0]: worst = (val, name)
    elif kind == 't':
        pieces = refined_pieces(d, m, t, r, c, b0, 'inf')
        val = pieces[0] + (pieces[1] or 0)
        status = val > 1
        print(f"{name:10s} beta0={b0} (claim {b0_claim} {'OK' if ok_b0 else 'MISMATCH'}) cert=t   value={float(val):.9f} {'PASS' if status else 'FAIL'}")
        if worst is None or val < worst[0]: worst = (val, name)
    else:  # bridge
        allok = True
        bridge_min = None
        for b in range(b0, cutoff):
            pieces = refined_pieces(d, m, t, r, c, b, 'beta')
            v = pieces[0] + (pieces[2] or 0)
            if bridge_min is None or v < bridge_min: bridge_min = v
            if v <= 1:
                allok = False
        cut = refined_pieces(d, m, t, r, c, cutoff, 'inf')[0]
        status = allok and cut > 1
        print(f"{name:10s} beta0={b0} (claim {b0_claim} {'OK' if ok_b0 else 'MISMATCH'}) cert=bridge[{b0},{cutoff}) min={float(bridge_min):.9f} cutoff={float(cut):.16f} {'PASS' if status else 'FAIL'}")
        if worst is None or cut < worst[0]: worst = (cut, name + "-cutoff")
        if bridge_min is not None and bridge_min < worst[0]: worst = (bridge_min, name + "-bridge")
print(f"WORST refined value: {float(worst[0]):.16f} at {worst[1]}  (claim: 1.0000005977102229... at gen121211 cutoff)")

print()
print("=" * 70)
print("PART 3: larger-c_t coverage for the 19 tuples (coarse with next admissible c)")
def next_c(d, m, t, r, c, kind):
    if t == 2: return None            # c fixed = 2
    if kind.startswith('eq'): return None  # larger c -> generic case, scanned already
    if t == m == d: return 3 * m      # c_d = m*psi, next is 3m
    return c + 1
allcov = True
for name, (d, m, t, r, c), *_ in ROWS:
    nc = next_c(d, m, t, r, c, name)
    if nc is None:
        continue
    # coarse with c0 replaced by nc (chi = m*eps generic envelope)
    g, e = params(d)
    M, _ = coarse_M(d, m, t, r, 'gen')
    Mnext = M / F(t if t < m else (m + 2 if (t == m < d) else 2 * m)) * nc if M is not None else None
    ok = Mnext is not None and Mnext > 1
    if not ok: allcov = False
    print(f"{name:10s} next c={nc}: coarse value={float(Mnext):.6f} {'PASS' if ok else 'FAIL'}")
print("larger-c coverage:", "ALL PASS" if allcov else "FAILURES")

print()
print("=" * 70)
print("PART 4: d >= 53 analytic tail")
def Delta(d):
    g, e = params(d)
    H = sum(F(1, i) for i in range(1, d - 1))
    return 2 * d * e + 2 * e + F(2 * (8 * d - 3), 3) * e / (1 - d * e) * H
ok_all = True
for d in range(53, 64):
    ok = Delta(d) < F(1, d + 1)
    if not ok: ok_all = False
print("Delta_d < 1/(d+1) for 53<=d<=63:", "PASS" if ok_all else "FAIL")
m53 = F(1, 54) - Delta(53)
print(f"margin at d=53: {m53}")
print(f"  claim: 2465298954227032982505949/141425508012555648280913514000 -> {'MATCH' if m53 == F(2465298954227032982505949, 141425508012555648280913514000) else 'DIFFERENT'}")
H62 = sum(F(1, i) for i in range(1, 63))
mH = F(24, 5) - H62
print(f"H_62 < 24/5: {'PASS' if H62 < F(24,5) else 'FAIL'}, margin {mH}")
print(f"  claim: 17262497921202896432747309/197044480683803711251893600 -> {'MATCH' if mH == F(17262497921202896432747309, 197044480683803711251893600) else 'DIFFERENT'}")
print("9d^2-118d-91 at d=64:", 9*64**2 - 118*64 - 91, "> 0:", 9*64**2 - 118*64 - 91 > 0)
# final chain margin: 64/65 - (65/1024 + 65/65536 + 1625/1999)
chain = F(64, 65) - (F(65, 1024) + F(65, 65536) + F(1625, 1999))
print(f"final chain margin 64/65 - sum = {chain}")
print(f"  claim: 913198321/8515420160 -> {'MATCH' if chain == F(913198321, 8515420160) else 'DIFFERENT'}")
# supporting: eps < 65/(32 d^3) and d*eps < 1/2000 for d >= 64
d = 64
g, e = params(d)
print("eps < 65/(32 d^3) at d=64:", e < F(65, 32 * d**3), "| d*eps < 1/2000 at d=64:", d * e < F(1, 2000))
print("m*eps < 1/50 at d=53:", 53 * params(53)[1] < F(1, 50))
