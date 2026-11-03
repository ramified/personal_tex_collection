---
name: zhou-math-latex
description: Revise Xiaoxiang Zhou's mathematical LaTeX manuscripts using his notation, exposition, proof structure, preamble, and BibTeX conventions. Use when polishing or extending his mathematical writing, or when asked to apply his personal LaTeX style. These preferences are specific to his manuscripts, not a general replacement for another author's conventions.
---

# Xiaoxiang Zhou's mathematical LaTeX style

Read [the style requirements](references/style-requirements.md) before editing. They record the author's explicit preferences, including distinctions clarified through revision. Apply them to the requested scope; a new user instruction takes precedence.

## Editing workflow

1. Read the current source and any current selection. User edits on disk take precedence over previous assistant drafts. Inspect the actual preamble and bibliography setup before proposing changes.
2. Keep everything before `\begin{document}` intact by default, including unused macros, theorem environments, packages, metadata, comments, and layout. Add only a definition genuinely needed for the requested change; do not replace the preamble with a minimal one. If the request concerns only the body, compare the preamble before and after editing.
3. Preserve notation. Ask before a substantive notation change unless the user has already authorized that change. This requirement concerns changing the author's notation, not routine wording, numbering, or implementation choices.
4. Preserve the order of mathematical motivation. Explain the construction before adding conditions needed for a later application. Keep useful symbolic displays and organize long arguments into meaningful, automatically numbered steps or labeled subsections.
5. Use `\bibliographystyle{plain}` and `\bibliography{reference}` with an editable `reference.bib`. Keep citation keys and verified locators. Do not substitute an embedded bibliography or a different bibliography system.
6. Follow the requested version workflow. For a named new revision, copy the latest user-edited source and modify only the new revision. Otherwise edit the active file in place. Retain earlier versions for comparison.
7. When the built-in `compile_latex_document` tool is available, compile the saved target and fix errors in scope, including bibliography resolution. Keep the current editor open; do not create a separate PDF or change tabs unless requested. In another environment, use the project's existing build process.

## Review before delivery

Check the author's notation, the retained equivalence displays, automatic numbering and references, bibliography keys, and preservation of the preamble and earlier revisions. Check that proof divisions reflect distinct ideas and that technical details have been isolated without omitting necessary arguments. Report what changed and whether compilation succeeded; do not claim that a speculative replacement proof has been established.
