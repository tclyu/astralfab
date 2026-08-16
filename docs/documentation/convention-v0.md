# Documentation convention v0 — provisional

**Authority:** the bootstrap window (see `bootstrap/operations.md`).
**Expiry:** superseded by the documentation standard v1, designed from research
written under this convention. Files written under v0 are then re-graded, never
erased. Envelope: the `Documentation` issue.

This convention is deliberately minimal. It exists so the estate's first
research is writable at all; it decides nothing v1 will not revisit with
evidence.

## What every research file must state

1. **Subject** — one sentence: what question this file answers.
2. **Sources** — where each input came from, specific enough to re-find it.
   A source that cannot be re-found is a claim, not a source.
3. **Claims separated from facts** — a fact is verified against the estate or a
   source; a claim is believed or inferred. Mark every statement as one or the
   other; never interleave them in one sentence.
4. **Confidence** — for the file as a whole and for any load-bearing claim:
   high, medium, or low, with one line of why.
5. **Date** — when the research was current. Undated research is expired
   research.

## Form

- One file, one subject. Markdown. Lives under `docs/`, lands by pull request citing its envelope issue.
- Prose is never hard-wrapped: one logical line per paragraph and per list item. Newlines are structural only — headings, list boundaries, table rows, code fences. Display width is the reader's setting, not the author's; a manual line break inside a paragraph is a display decision baked into content, and it turns every later edit into a whole-paragraph rewrap.
- Provisional files state their provisional status and this convention's name in a header line, so re-grading under v1 is a search, not an excavation.
