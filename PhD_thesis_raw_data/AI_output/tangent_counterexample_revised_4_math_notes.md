# Mathematical notes on revision 4

Updated on 4 November 2026 after the author's clarifications. The concise formulations in items 1 and 3 have now been incorporated. The author's corrections resolve items 2 and 4. The author has clarified the intended notation in item 5; the earlier recommendation to revert to the temporary symbol is withdrawn.

## 1. Countably many irreducible pieces: concise statement adopted

Location: [Theorem 2, proof of (1)](C:/Users/bbh8149/xiaoxiang_zhou/structured/github/personal_tex_collection/PhD_thesis_raw_data/AI_output/tangent_counterexample_revised_4.tex:300).

The manuscript now says:

> The nonsimple locus is a countable union of proper irreducible analytic subsets of $Z$, so a very general point gives a simple quotient.

This expresses the intended countability of the irreducible pieces. No explanation of the Hodge-locus or Baire argument has been added to the manuscript.

“Subsets of $Z$” avoids suggesting that these are irreducible components of $Z$, which has already been chosen irreducible. The nonsimple locus need not itself be closed, so describing the individual closed analytic pieces is also clearer than invoking its components without specifying a topology. The countable union language is consistent with the usual treatment of Hodge loci; see [Cattani–Deligne–Kaplan, *On the Locus of Hodge Classes*](https://arxiv.org/abs/alg-geom/9402009) for the general algebraic setting.

## 2. Translation case: corrected by the author

Location: [Theorem 2, proof of (2), translation case](C:/Users/bbh8149/xiaoxiang_zhou/structured/github/personal_tex_collection/PhD_thesis_raw_data/AI_output/tangent_counterexample_revised_4.tex:316).

The author has replaced “$\sigma$ is unramified” with “$\phi_C$ is unramified.” Interpreting $\phi_C$ as the Gauss map on the smooth curve $C$, with its conic image as target, this resolves the earlier objection.

Indeed, the nonidentity translations in the order-three action have no fixed points. The quotient map is unramified, and the quotient is identified with the conic by the Gauss map. The stated Riemann–Hurwitz contradiction follows. No further explanation has been inserted into the manuscript.

## 3. Rotation: a short definition and order argument added

Location: [Theorem 2, proof of (2)](C:/Users/bbh8149/xiaoxiang_zhou/structured/github/personal_tex_collection/PhD_thesis_raw_data/AI_output/tangent_counterexample_revised_4.tex:311).

The manuscript now observes that $\tau^3$ fixes the generating curve pointwise, so $\tau^3=\mathrm{id}$. It then defines a rotation in this argument as an automorphism whose linear part is multiplication by a primitive cube root of unity. This allows an affine automorphism with a translated center, rather than silently assuming that it fixes the chosen origin.

The definition supplies exactly the hypothesis used in [Lemma 3.15 of the companion manuscript](C:/Users/bbh8149/xiaoxiang_zhou/structured/github/personal_tex_collection/PhD_thesis_raw_data/reorganized_version/re_subvarieties_in_abelian_variety.tex:1098). Its proof need not be reproduced.

## 4. Elliptic-curve product: corrected by the author

Location: [the final item of the proof](C:/Users/bbh8149/xiaoxiang_zhou/structured/github/personal_tex_collection/PhD_thesis_raw_data/AI_output/tangent_counterexample_revised_4.tex:317).

The author has replaced $E_\rho^{\otimes3}$ with $E_\rho^{\oplus3}$. For the finite product of abelian varieties, this notation is acceptable; the tensor-product objection is resolved.

If this text is to stand alone, a brief definition of $E_\rho$ may still help: the intended elliptic curve is $\mathbb C/\mathbb Z[\zeta_3]$. This is a notation clarification, not another objection to the product.

## 5. 记号约定已澄清：识别后使用 $\phi_C$

作者已明确：$\phi$ 只是构造阶段对映射使用的临时记号。一旦识别出它就是切线 Gauss map $\phi_C$，后文就应使用具有几何意义的记号 $\phi_C$。

这是一项有意的记号转换，不需要为了保留临时记号而把后面的 $\phi_C$ 改回 $\phi$。此前提出的改名建议撤回，也不再将这一点列作数学问题。正文保留作者已经采用的 $\phi_C$。

## 6. Bibliography entry already added

The entry for “re_subvarieties_in_abelian_variety.pdf” is present in [the local bibliography](C:/Users/bbh8149/xiaoxiang_zhou/structured/github/personal_tex_collection/PhD_thesis_raw_data/AI_output/reference.bib), with the verified author and title: Xiaoxiang Zhou, *Subvarieties in complex abelian varieties*. The existing citation key is retained.

## Checks that do not call for expanding the proof

- The shortened line-bundle calculation in Lemma 2.1(1) gives $\mathcal O_C(2p)\cong\mathcal O_C(2p_0)$, so the conclusion that $p$ is Weierstrass follows. Its compact symbolic form can remain.
- The cited finiteness input is supported by [Treibich, Section 2, Proposition 2.5 and the cover correspondence](https://arxiv.org/html/2501.16483v1#S2). The deleted explanatory sentence need not be restored merely for length or style.
- The absolute-simplicity criterion used for the seed matches [Arias-de-Reyna et al., Proposition 3.4](https://arxiv.org/pdf/1507.05913). The point counts themselves were not recomputed during the language edit.
