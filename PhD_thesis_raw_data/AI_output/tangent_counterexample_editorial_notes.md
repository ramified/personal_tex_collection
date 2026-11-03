# Editorial notes

Update: `tangent_counterexample_revised.tex` and its PDF now incorporate the mathematical revisions and complete the argument, while preserving the original strategy. The earlier English-only version is retained. The notes below describe the earlier draft; the citation-style and notation comments have been updated to reflect your clarification.

The accompanying revision is an English-language edit, as requested. It preserves the order of the argument, the mathematical claims, the formulas, and the citation locator, including the issues listed below. These notes are separate from the article; none of the suggested mathematical corrections has been applied.

The prose now uses shorter sentences, more direct transitions, and standard expressions such as "Let ... denote," "parallel transport under the Gauss--Manin connection," and "admits a tangential cover." The phrase "cotangent-space condition" is introduced once to avoid repeating "the cotangent subspace of a subabelian variety." This is only a shorthand for your existing requirement, not a new definition of its mathematical content. The placeholder title has also been replaced.

## Mathematical concerns to revisit

### 1. The definition of the rational subspace

In Section 2, item (2), the intersection

\[
H^1(C_0;\mathbb Q)\cap H^0(\omega_C(-2p_0))
\]

is zero under the usual Hodge-theoretic identification: a rational cohomology class is real, whereas a nonzero class of type \((1,0)\) cannot be real. It therefore cannot be the intended rational six-dimensional subspace.

Once a seed quotient \(q_0:J(C_0)\twoheadrightarrow A_0\) has been chosen, the intended definition appears to be

\[
V_0=q_0^*H^1(A_0;\mathbb Q),\qquad
V_{0,\mathbb C}=W_0\oplus\overline{W_0}.
\]

This is the construction used in Lemma 2 of the supplied blueprint (page 3).

### 2. The extra symmetric square in the seed discussion

In Section 1, the expression

\[
\operatorname{Sym}^2 H^0(\omega_C(-2p_0))\subset H^0(\omega_C)
\]

does not have the stated natural inclusion. Multiplying two sections of \(\omega_C(-2p_0)\) gives a section of \(\omega_C^{\otimes 2}(-4p_0)\), not of \(\omega_C\). The intended subspace seems to be \(H^0(\omega_C(-2p_0))\) itself, consistent with your next displayed identity.

### 3. Dimension bounds versus equalities

The vanishing of a map from a rank-three bundle to a rank-two bundle gives six local equations. Without an independence argument, this gives codimension **at most** six, not necessarily exactly six. Thus the useful conclusion is

\[
\dim Z\geq 9-1-6=2.
\]

Likewise, the finiteness argument is intended to give \(\dim(Z\cap\mathcal H_4)\leq 1\), not necessarily equality. The last paragraph instead compares dimensions three and two. The comparison consistent with the preceding argument and the blueprint is **at least two versus at most one**. All original numerical claims have been retained in the polished article.

### 4. Abelian subvariety versus abelian quotient

A subspace of \(H^0(C,\omega_C)\) naturally arises by pulling back invariant differentials from an **abelian quotient**:

\[
q:J(C)\twoheadrightarrow A,\qquad
W=q^*H^0(A,\Omega_A^1).
\]

An inclusion of an abelian subvariety instead induces restriction of differentials in the opposite direction. A polarization or a complementary factor can relate the two descriptions, but the identification should be specified. In a future mathematical revision, "comes from an abelian quotient" would be a concise, precise replacement. The current edit retains your subvariety formulation.

### 5. Where the bundles and the Hodge equivalences are defined

The discussion should explicitly restrict to the theta-null locus near the seed, where \(h^0(\mathcal L_t)=2\). Constant rank is needed for \(W_t\) to form a holomorphic rank-three subbundle and for the six-equation count. The displayed Hodge equivalences also use that \(V_t\) is rational of rank six and that \(W_t\) has dimension three. The blueprint supplies the constant-rank justification using upper semicontinuity and parity (page 3).

### 6. The hyperelliptic line-bundle assertion

Degree three and two sections alone do not force \(\mathcal L\cong\mathcal O_C(3p)\) for a Weierstrass point. On a genus-four hyperelliptic curve, let \(H\) be its degree-two pencil. For any point \(p\), the bundle \(H(p)\) has degree three and two sections; \(p\) need not be a Weierstrass point.

The additional theta-characteristic hypothesis is essential here. The surrounding spin-deformation setting supplies it, but the sentence should explicitly use it when explaining why \(p\) is Weierstrass. Also distinguish a varying marked point \(p_t\) from the original point \(p_0\).

### 7. The finiteness lemma and its application

The cited result concerns **hyperelliptic tangential covers** with marked data, counted up to the appropriate isomorphism. Proposition 2.5(3) gives finiteness for a fixed Severi set; Remark 1(3)--(4) following Proposition 2.3 supplies the cover correspondence. For fixed cover degree \(n\), the relation \(2n+1=\sum_i\mu_i^2+4d\) leaves finitely many types. Here the paper's \(d\) is not the cover degree. See [Treibich, arXiv:2501.16483v1](https://arxiv.org/html/2501.16483v1#S2).

Your citation locator "Proposition 2.5, 3." is a reasonable way to follow the paper's unparenthesized item numbering; adding parentheses is not a mathematical correction. The revised article uses your preferred style. The blueprint's attribution of the correspondence to "Propositions 2.3(3)--(4)" does need care: in the version linked above these are parts of the following remark.

To deduce a local dimension bound, explain why the covers arising from the fixed rational cohomology data have a fixed degree locally. The blueprint addresses this using a rational projector and the fixed integral homology map (pages 3--4). Finiteness separately for each degree does not by itself supply that step.

### 8. Notation and conventions

The definition of \(\phi_C\) is already present in the companion manuscript. It has been added to the new revision so that this file can be read independently. In the earlier draft's Lemma 2.1, the hypothesis names \(C\), but the formula uses \(C_t\); the first definition of \(V_0\) similarly mixes \(C_0\) and \(\omega_C\). These inconsistencies are corrected in the new revision.

Specify whether \(\operatorname{Aut}(A)\) means group automorphisms or all automorphisms. For a general affine automorphism, its differential at the origin maps to the tangent space at its image; the scalar condition uses translation to identify that space with \(T_0A\). The blueprint explicitly treats affine automorphisms.

### 9. What remains beyond the deformation argument

The draft ends after finding a nonhyperelliptic deformation. To prove the opening theorem as a standalone result, it still needs the existence of a seed with a simple complementary threefold, a justification for choosing a deformation with simple quotient, and the passage from the abstract curve to its image in that quotient. In particular, establish the normalization statement before transferring the degree of the Gauss map to the image curve, and exclude the scalar-differential automorphisms.

These are addressed in the supplied blueprint by Lemma 1, the end of Lemma 2, and Lemmas 3--4, respectively. They have not been inserted because that would go beyond an English-only edit. The blueprint proves an immersive normalization map; it does not assert that the image curve is smooth or embedded.

## Files and compilation

The original source is unchanged. All outputs are in `AI_output`.

The new mathematical revision has a compact preamble and an embedded bibliography; it does not require a separate `.bib` file or `quiver.sty`. Build it with two XeLaTeX runs:

```powershell
xelatex -interaction=nonstopmode -halt-on-error tangent_counterexample_revised.tex
xelatex -interaction=nonstopmode -halt-on-error tangent_counterexample_revised.tex
```

The main text follows the original sequence: the squared trigonal pencil, the hyperelliptic seed, and the deformation dimension count. It then proves the normalization and symmetry statements. The seed construction and simplicity certificate from Lemma 1 of `AI_counterexamples/blueprint_verified.pdf` are reproduced in an appendix, with primary references. The accompanying `verify_tangent_seed.py` checks the arithmetic independently with the Python standard library; it does not replace the cited geometric results about Lamé covers.

The earlier English-only source, compiled PDF, bibliography, and local `quiver.sty` dependency remain available. That version retains the original preamble and document layout.

To rebuild the English-only version from that folder:

```powershell
xelatex -interaction=nonstopmode -halt-on-error tangent_counterexample_polished.tex
bibtex tangent_counterexample_polished
xelatex -interaction=nonstopmode -halt-on-error tangent_counterexample_polished.tex
xelatex -interaction=nonstopmode -halt-on-error tangent_counterexample_polished.tex
```
