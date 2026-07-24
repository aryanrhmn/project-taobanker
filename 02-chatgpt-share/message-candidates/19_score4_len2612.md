tweets = [
"""1/9 New preprint (unrefereed): if X is a primitive distance-regular graph on n vertices, diameter dâ¥3, then X is Johnson/Hamming or

motion(X) â¥ n/(12dÂ³).

This improves the published dâ»â¶ dependence to dâ»Â³. Proof, source, audits: [LINK]""",
"""2/9 Plain English: a graph symmetry relabels the vertices without changing which pairs are connected. âMotionâ is the fewest vertices moved by any nontrivial symmetry.

Our result says that, outside two structured families, every symmetry must move a large part of the graph.""",
"""3/9 Distance-regular graphs are networks whose local distance statistics look identical from every vertex. They sit at a crossroads of algebraic combinatorics, coding theory, spectral graph theory and permutation groupsâand can have enormous symmetry.""",
"""4/9 Babai conjectured a diameter-independent linear bound: apart from Johnson and Hamming graphs, every nontrivial symmetry should move â¥cn vertices.

We do not prove that conjecture. We replace the best published polynomial dependence n/dâ¶ by the explicit n/(12dÂ³).""",
"""5/9 The proofâs spine is:

tiny support of an automorphism
â small Î¼ and large Î»
â large canonical clique geometry
â smallest eigenvalue parameter mâ¤d
â Johnson/Hamming structure, or a quantitative contradiction.

Three powers of d disappear along this chain.""",
"""6/9 Two potentially reusable ingredients:

â¢ an exact formula for vertices distinguishing an adjacent pair;
â¢ a direct geodesic PoincarÃ© inequality
  kâÎ¸â â¥ nÂ²k/Î£â,áµ§ dist(x,y)Â² â¥ k/dÂ²

for symmetric relations in homogeneous coherent configurations.""",
"""7/9 Since dâ¤5 logân for distance-regular graphs of valency >2, the theorem gives

motion(X) â¥ n/[1500(logân)Â³].

The same permutation-group machinery improves the associated thickness exponent from logâ·n to logâ´n; under the same transitivity assumptions, base size from logâ¹n to logâ¶n.""",
"""8/9 Verification status: the proof was developed and audited with AI assistance; every imported theorem is identified, the new algebra has exact and symbolic checks, and a separate hostile review found no error.

That is evidenceânot peer review. The delicate point is the Î¼=2 multiplicity argument.""",
"""9/9 Iâm posting the manuscript, LaTeX and audit code together and inviting an adversarial reading.

Best response: identify the earliest invalid implication or confirm the source interfaces, especially Proposition 7.1.

Please quote the exact line you think succeeds or fails. [LINK]"""
]
[(i+1, len(t)) for i,t in enumerate(tweets)]
