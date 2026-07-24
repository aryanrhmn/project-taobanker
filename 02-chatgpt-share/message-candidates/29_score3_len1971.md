bash -lc python - <<'PY'
from pathlib import Path
p=Path('/mnt/data/babai_motion_d3_audited.tex')
s=p.read_text()
s=s.replace('''If $m=2$, then $k>4$ and \\cite[Proposition 2.15]{PS} gives
$\\mot(X)\\ge n/16>n/(12d^3)$.''','''If $m<3$, then $m=2$: indeed $m$ is a positive integer, and $m=1$ would put every vertex in exactly one clique of the Delsarte geometry, forcing the connected graph $X$ itself to be complete.  Thus $k>4$ and \\cite[Proposition 2.15]{PS} gives
$\\mot(X)\\ge n/16>n/(12d^3)$.''')
s=s.replace('''Hence every local graph is a disjoint union of $m$ cliques.  The geometric identities are''','''Hence every local graph is a disjoint union of $m$ cliques.  We shall use Terwilliger's intersection-number inequality below.  Its induced-quadrangle hypothesis is automatic here: if $x,y$ are at distance two and $u,v$ are their two common neighbors, then $u$ and $v$ cannot be adjacent, since in the local graph at $u$ the nonadjacent vertices $x,y$ would otherwise have the common neighbor $v$ despite lying in different clique components.  Thus $x,u,y,v$ is an induced quadrangle.  The geometric identities are''')
s=s.replace('''It remains to consider $c_t=t=m=d$.  Lemma 4.2 and the defining equality $\\tau_d=m$ give
\\[
 1=\\tau_1<\\tau_2<\\cdots<\\tau_d=d,
\\]''','''It remains to consider $c_t=t=m=d$.  Lemma 4.2 gives strict growth through $\\tau_{d-1}$; moreover $\\tau_{d-1}\\le m-1<\\tau_d=m$ by the definition of the geometric parameters.  Hence
\\[
 1=\\tau_1<\\tau_2<\\cdots<\\tau_d=d,
\\]''')
s=s.replace('''''','')
# Make dependency ledger note self-contained quadrangle check.
s=s.replace('''the Terwilliger intersection-number inequality (Theorem 2.6);''','''the Terwilliger intersection-number inequality (Theorem 2.6), whose induced-quadrangle hypothesis is verified directly in the $\\mu=2$ section;''')
p.write_text(s)
PY

grep -n -A8 -B3 'If \$m<3\|induced-quadrangle\|It remains to consider' /mnt/data/babai_motion_d3_audited.tex