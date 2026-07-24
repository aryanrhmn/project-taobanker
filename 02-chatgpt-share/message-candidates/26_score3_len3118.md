bash -lc cat > /mnt/data/babai_motion_twitter_thread.txt <<'EOF'
1/10 Proof-audit thread. New machine-generated candidate:

For primitive distance-regular X of diameter d>=3,
X is Johnson/Hamming, or

mot(X) >= 2n/(5d^3).

Published benchmark: Cn/d^6. This is NOT a theorem yet. Please try to break it.

2/10 Small support forces geometry. For adjacent vertices,

D(1)=2+(2/k) sum_{i>=2} k_i c_i > (mu/k)n.

A support-sensitive geodesic boundary argument then gives, for support density rho,

mu<rho k,  lambda>(1-rho)k/d.

3/10 Put rho<2/(5d^3). Keeping the full Metsch clique expressionânot the usual lambda/2 shortcutâthen combining Delsarte's clique bound with Bang-Koolen yields Delsarte geometry and smallest eigenvalue -m with m<=d.

4/10 The mu>=3 branch collapses sharply.

psi_1=1 contradicts Kivva's theta+1 <= 5b_1/7. Otherwise

2<=psi_1<=tau_2<...<tau_d=m<=d,

so m=d and psi_1=tau_2=2; a Lv-Koolen endpoint theorem gives Johnson.

5/10 The new breakthrough is the mu=2 branch. For the standard sequence, track relative drops

y_i=(u_{i-1}-u_i)/u_{i-1}

and retain the exact Riccati recurrence, instead of replacing every step by one uniform additive error.

6/10 Also retain exact sphere tails:

k_{t-h}/k_t <= q^h/[r(r+1)...(r+h-1)].

At the endpoint d=t+1, the right tail is q/m, not q. These two changes turn the previous harmonic/coarse loss into a multiplicative certificate.

7/10 The certificate is

k_{t-1}u_{t-1}^2 >= (n/k) M.

Exact rational audit over every relaxed case for 3<=d<=16 gives min M=1.007179713... at

d=7, (m,t,r,c_t)=(6,6,1,7).

For d>=17, one explicit degree-6 polynomial is positive.

8/10 Robustness check: the same finite relaxation barely supports coefficient 5/12 (minimum margin 0.083%), while coefficient 1/2 fails (M=0.96497...). I headline 2/5 because its worst audited margin is 0.718%, not because it is numerically maximal.

9/10 The mu=1 branch is cleaner. A geodesic Poincare inequality gives

k-theta_1 >= n^2 k / sum_{x,y} dist(x,y)^2 >= k/d^2.

Dualization + Babai's spectral motion estimate then gives mot(X)>3n/(10d^2).

10/10 Status: unrefereed machine proof. Most attackable point: the mu=2 recurrence/multiplicity interface. Recent-preprint dependency: psi_1=tau_2=2 => Johnson.

There is also a source-conservative fallback mot(X)>=n/(15d^3). PDF, TeX, exact audit attached.
EOF
python - <<'PY'
from pathlib import Path
text=Path('/mnt/data/babai_motion_twitter_thread.txt').read_text()
chunks=[]
cur=[]
for line in text.splitlines():
    if line and line.split('/')[0].isdigit() and '/10 ' in line and cur:
        chunks.append('\n'.join(cur).strip()); cur=[]
    cur.append(line)
if cur: chunks.append('\n'.join(cur).strip())
for i,c in enumerate(chunks,1): print(i,len(c))
assert len(chunks)==10 and all(len(c)<=280 for c in chunks)
PY
printf '\n---SANITY---\n'
pdftotext /mnt/data/babai_motion_d3_final_candidate.pdf - | sed -n '1,35p'
printf '\n---OUTPUTS---\n'
ls -lh /mnt/data/babai_motion_d3_final_candidate.pdf /mnt/data/babai_motion_d3_final_candidate.tex /mnt/data/babai_motion_d3_final_audit.py /mnt/data/babai_motion_twitter_thread.txt
