# Xiaoxiang Zhou's mathematical writing and LaTeX requirements

These are personal preferences collected from the author's revision requests. They are intended to preserve his writing style, not to impose a universal standard for mathematics. New explicit instructions and the current user-edited source take precedence. Apply changes within the requested scope.

## 1. Preserve the author's source and preamble

- Read the latest source before editing; do not rebuild a manuscript from an earlier assistant response. Preserve the author's intervening edits.
- Do not simplify, replace, or prune anything before `\begin{document}` merely to make the document shorter or more self-contained.
- Retain theorem declarations, especially environments such as `remark`, even if the current draft does not use them. The author needs them for later additions.
- Retain existing packages, macros, operator definitions, theorem styles and counters, comments, layout, title, affiliation, email, and date commands. Do not restore stale metadata from an older revision.
- Minimal additions are appropriate when needed for the requested feature. A genuine compilation defect can be repaired narrowly; a stylistic preference does not justify rewriting the preamble.
- Do not compress typography, reduce font size, or change margins to conceal an expanded proof.

## 2. Preserve notation and minimize the reader's memory burden

- Respect the author's transition from provisional notation to the established geometric notation. In the tangent-counterexample manuscript, $\phi$ is only the temporary name of the constructed map. Once it is identified with the tangent Gauss map $\phi_C$, use $\phi_C$ thereafter. Do not recommend reverting to $\phi$, or treat this deliberate identification as a mathematical defect merely because the Gauss map is being used on the smooth model.
- Do not rename established mathematical objects without asking first, unless the current request already authorizes that particular change.
- Prefer direct use of existing symbols to either verbal expansion or a new abbreviation. Write `\deg f` rather than introducing `e=\deg f` when the degree needs no separate name. Preserve concise expressions such as `\ord(\sigma)`, `\sigma=\id`, and the author's existing image notation.
- Correct the English connecting formulas without turning a short symbolic argument into a paragraph of paraphrase. New symbols should earn their place through a real need, not merely reduce the assistant's typing.
- In the tangent-counterexample manuscript, the curve is `C`, with `C_t` for its deformations. Do not introduce `X` to replace it.
- Use `|\mathcal{L}|` for the map associated with the complete linear system, rather than introducing `\psi_{\mathcal{L}}`.
- Use short sheaf-cohomology notation such as `\Hnm^0(\mathcal{L})` and `\Hnm^0(\omega_C)`. Do not routinely expand it to `\Hnm^0(C,\mathcal{L})`. Retain `h^0(\mathcal{L})` for dimensions.
- For Betti cohomology, include the space and separate coefficients with a semicolon: `\Hnm^1(C;\mathbb{Q})`, `\Hnm^1(C_t;\mathbb{C})`. Preserve the author's `\Hnm` macro.
- Identify `\Sym^2\Hnm^0(\mathcal{L})` with the relevant subspace under multiplication in one short explanation when needed. Do not introduce a new function such as `W(C,\mathcal{L})` solely to name that image.
- The author **does want** `W_t` and `V_t`. The rejection of `W(C,\mathcal{L})` does not authorize removing `W_t`.
- Avoid introducing names for familiar objects when their existing expression is clearer. In this manuscript, use `\mathcal{O}_C(2p)` for a Weierstrass point `p`, rather than introducing `H_t` for a hyperelliptic pencil. Explain degree-two maps without requiring the reader to learn the term “pencil.”
- Follow the current source's spelling and terminology choices rather than imposing an assistant house style.

## 3. Mathematical typography

Use the author's forms:

```latex
\leqslant  \geqslant
\left\{t\in B\;\middle|\;h^0(\mathcal{L}_t)\geqslant2\right\}
\Hnm^0(\mathcal{L})
\Hnm^1(C;\mathbb{Q})
\longrightarrow  \longmapsto  \Longleftrightarrow
```

- Use `\left` and `\right` when delimiters need enlargement. Preserve or use `\rule{0mm}{...mm}` inside delimiters if a height adjustment is genuinely needed. Do not mechanically enlarge every ordinary parenthesis.
- Prefer long arrows whenever there is a choice. For labeled arrows, retain readable spacing and the existing map notation.
- Set-builder notation uses `\left\{ ... \;\middle|\; ... \right\}` with a visible condition separator.
- Prefer `$$...$$` to `\[...\]` for ordinary unnumbered displays in the author's manuscripts. Keep structured environments such as `equation` or `align` when their numbering or alignment is needed. If the actual document has a concrete compatibility or layout problem with `$$...$$`, explain that specific reason before proposing a different convention; do not replace the preference merely to enforce a general LaTeX convention.

## 4. Let the reader see the reason for each construction

- Present the mathematical construction and its immediate properties before imposing extra conditions needed for a later application.
- In the tangent-counterexample argument, introduce the linear system
  `(\mathcal{L}^{\otimes2},\Sym^2\Hnm^0(\mathcal{L}))`, its factorization through `|\mathcal{L}|`, and its failure of generic injectivity **before** the canonical-bundle and Hodge conditions. The failure of generic injectivity does not depend on those two additional conditions.
- State that the construction seeks a suitable pair `(C,\mathcal{L})`; avoid wording that suggests every initially described map is to be realized as a tangent Gauss map.
- Motivate the seed: relaxing nonhyperellipticity makes an example available; deformation preserves the desired conditions while leaving the hyperelliptic locus. Do not begin with an unexplained “Start with…” construction.
- Prefer the Hodge-theoretic formulation where the argument is linear algebra. Holomorphic differentials are the **(1,0)-part**, not the (0,1)-part.
- Defer the geometric abelian quotient to the point where the actual image curve is constructed. A necessary geometric explanation can be isolated in a lemma.

## 5. Keep the two deformations visibly parallel

The key idea is that two initially compatible subspaces are deformed by different mechanisms:

```latex
\begin{aligned}
V_0&\longmapsto V_t\subset\Hnm^1(C_t;\mathbb{Q})
&&\text{by Gauss--Manin parallel transport},\\
W_0&\longmapsto W_t:=\Sym^2\Hnm^0(\mathcal{L}_t)
&&\text{by deforming the line bundle}.
\end{aligned}
```

Retain the displayed chain of equivalent compatibility conditions. Do not replace it with a long verbal paraphrase:

```latex
\begin{aligned}
&\begin{cases}
V_t\text{ remains a Hodge substructure},\\
V_{t,\mathbb{C}}\cap\Hnm^0(\omega_{C_t})=W_t
\end{cases}\\
\Longleftrightarrow\;&V_{t,\mathbb{C}}=W_t\oplus\overline{W}_t\\
\Longleftrightarrow\;&W_t\subseteq V_{t,\mathbb{C}}\\
\Longleftrightarrow\;&
\rk\left[W_t\longrightarrow
\Hnm^1(C_t;\mathbb{C})/V_{t,\mathbb{C}}\right]=0.
\end{aligned}
```

Give only the short justification needed for the equivalences. Preserve the required rationality and dimension hypotheses. Do not restore the incorrect definition obtained by intersecting rational cohomology with holomorphic forms.

## 6. Use automatic structure and separable proofs

- Whenever listing numbered parts or steps, use `enumerate` and `\item`. Do not type labels such as `\noindent(1)` and `\noindent(2)` by hand.
- Use `\label` and `\ref` for references to numbered parts, theorems, equations, and subsections. A reference generated by `\ref` is appropriate; a hard-coded part number is not.
- Divide a long proof into meaningful steps, or into labeled subsections where that improves navigation. Unnumbered descriptive headings are appropriate for internal stages. Do not split a short argument into artificial fragments or treat every division as requiring another numbered list.
- If a theorem or lemma has distinct essential claims, enumerate the claims and make the proof parts correspond directly: proof part (1) proves statement part (1), and proof part (2) proves statement part (2). Use automatic labels and references; do not let the proof's visible numbering suggest a different correspondence.
- In Theorem 2 of this manuscript, keep one proof with two enumerated parts: simplicity first, exclusion of scalar symmetries second. Within each part, use unnumbered descriptive headings for its stages, as in the author's revision. Do not turn the proof into two independent lists of two steps (a confusing “2+2” structure).
- Separate proof blocks or subsections can help in other arguments, but are not a default requirement. Preserve the author's chosen structure when it already lets readers locate each claim's proof independently.
- Isolate technical arguments as lemmas or remarks so that readers can follow the main dimension count without reading every calculation. Preserve the author's choice to put the tangential-cover finiteness discussion in a remark.
- The deformation roadmap should remain visible: choose the deformation space, impose the conditions, estimate dimensions, remove the unwanted locus, and construct the image curve.

## 7. Be concise without cutting proof ideas

- Prefer shorter notation, direct sentences, and clear motivation. Do not expand a compact proof into a long treatise merely to add formal detail or emphasize the strongest conclusion early.
- Complete the weaker construction before discussing simplicity. Keep simplicity and its auxiliary verification at the end.
- Separate routine technical verification from the main idea, but retain steps necessary for correctness, including dimension bounds and the normalization argument.
- Do not claim that a proposed moduli or monodromy argument proves the existence of a simple seed until its missing input has actually been established. The preference for a conceptual proof is not permission to remove a verified argument and leave an unacknowledged gap.
- Explain a mathematical concern candidly, and do not silently change the theorem being proved. When mathematical revision is authorized, correct the argument explicitly; when the request is language-only, preserve the source's mathematical content and record the concern separately as described below.

## 8. Keep references editable with BibTeX

Use the following at the end of the document:

```latex
\bibliographystyle{plain}
\bibliography{reference}
```

- Keep entries in the corresponding `reference.bib`; create a local file if the document has none. Add entries without overwriting existing ones or changing existing citation keys unnecessarily.
- Do not substitute `thebibliography`, hand-written `\bibitem` entries, or a different bibliography engine for this workflow.
- When migrating an embedded bibliography, retain all cited sources, keys, links, and verified information. Do not invent missing bibliographic fields.
- Preserve the author's citation-locator conventions, including forms such as `Proposition~2.5, 3.`. Different punctuation is not by itself a mathematical error.
- Protect proper names and required capitalization in BibTeX titles as necessary for the `plain` style.

## 9. Version history and the editor

- When asked for `tangent_counterexample_revised_4`, start from the latest user-edited revision, preserve earlier versions, and put the new changes in that named file.
- For follow-up edits without a new-version request, follow the active document instructions and edit that source in place.
- Keep the existing editor open. Do not open another tab or generate a separate PDF unless requested.
- Use the built-in `compile_latex_document` tool when available and confirm successful compilation of the actual requested target, including its bibliography. Otherwise follow the project's established build process.
- Check that changes preserve the preamble, notation, automatic numbering, proof logic, and earlier versions. A successful compile alone does not establish mathematical correctness.

## 10. Language-only editing and separate mathematical notes

- A request to correct only the language is a strict scope limit. Fix grammar, articles, idiom, spelling, punctuation, and sentence flow while keeping the author's argument, order, claims, notation, and divisions. Do not restore longer arguments from an earlier assistant version.
- Use the user's current manuscript to learn what makes the proof readable to him: concise symbolic implications, direct expressions such as `\deg f`, short purposeful steps, and references to existing results instead of repeatedly reproducing their proofs. Preserve these choices unless they create a mathematical issue; then flag the issue separately.
- Do not add hypotheses, fill proof gaps, replace formulas, change maps or domains, introduce definitions, or strengthen claims under the label of language correction. For example, replacing “the automorphism is unramified” with “its action is free” changes the mathematical assertion and belongs in the notes.
- Put mathematical concerns in a separate Markdown document with a precise location and enough explanation to assess each point. Distinguish an actual error, a missing justification, ambiguous notation, and an unresolved reference. Suggested repairs may appear there, clearly marked as unapplied.
- Do not treat a valid compressed argument as a gap merely because it omits routine intermediate calculations. If a familiar one-line justification or an existing citation suffices, say so rather than demanding a long expansion.
- When the author explicitly wants a standard fact stated without its proof, retain a concise, accurate statement and keep any supporting explanation in the separate notes. For example, stating that the nonsimple locus is a countable union of proper irreducible analytic subsets does not require inserting the rational-projector or Baire argument into the manuscript. Distinguish a harmless convention about a map on a normalization from an actual proof gap.
- Preserve citation keys and check whether they resolve. Report a missing or unverifiable reference separately; do not invent bibliographic data or silently replace the cited result.
- For this scope, compare mathematical expressions and structural commands before and after editing, allowing only the user's explicitly requested formatting changes. Report any unresolved mathematical or citation issue separately from compilation success.
