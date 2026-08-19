# Student-Facing Metadata and Visual Hierarchy v1.0.1

**Status:** Approved shared clarification  
**Scope:** Student and Accessible editions primarily; the corresponding reused figure, caption and status treatments in Teacher and Answer Key where applicable  
**Authority:** Human design judgment remains final  
**Clarifies:** `VISUAL_STYLE_GUIDE_v1.0.md` sections 45–47 (figure captions and metadata bands, source-status vocabulary, evidence status) and `SSS_TO_HHH_PRODUCTION_LESSONS_v1.0.md` section 9  
**Effective with:** HHH Campaign 2, Core Case 07 — The Audit

## Purpose

Source status stays explicit. The explanatory metadata around it does not.

Curriculum production had begun printing authoring and provenance *explanations* inside
student-facing metadata bands, and stacking a frame around every component that could
technically be boxed. The result reads as an audit artifact rather than as student
instructional material, and it buries the one distinction that actually matters.

This clarification keeps the required distinction among fictional case evidence, real
documented reference material, and curriculum-created diagrams. It removes the prose
that surrounds that distinction without serving a learner.

**This clarifies rather than removes the Visual Style Guide's requirement for explicit
source status.** Every rule in sections 45, 46 and 47 remains in force: a figure that
requires a status term still carries one, the controlled source-status vocabulary is
unchanged, and evidence status must still be stated rather than implied. What changes is
how much prose may accompany that statement on a learner-facing page.

## 1. Student-facing metadata minimization

1. **Preserve necessary source and evidence provenance.** Nothing here authorizes
   dropping a status distinction a learner needs in order to reason correctly.

2. **Visible provenance metadata uses the shortest controlled label that establishes the
   needed distinction.** The preferred form is:

   ```text
   SOURCE STATUS · <CLASSIFICATION>
   ```

   where `<CLASSIFICATION>` is a term from the approved source-status vocabulary or the
   case's declared evidence-layer labels.

3. **Authoring, production, audit and implementation explanations do not belong inside a
   student-facing metadata band.** A band states what a thing is. It does not explain how
   it came to exist.

4. Statements about how a figure was constructed, which internal source it was drawn
   from, or why curriculum authors created it **do not belong in a prominent subtitle**
   merely because that information is useful to production staff. Their home is the task
   registry, the package README, or production records.

5. If a learner genuinely needs an evidence-boundary clarification in order to reason
   correctly, **put it in a short ordinary-language caption or note**, in one place.

6. **Do not print "this is not evidence" warnings defensively.** Use one only where a
   reasonable learner could otherwise mistake an organizer, model, or curriculum-created
   schematic for case evidence. A diagram that plainly organizes the learner's own work
   does not need the warning; an organizer that sits beside real evidence cards and looks
   like one of them does.

7. **Consolidate repeated provenance and status labelling at the highest sensible visual
   level.** Where one figure-level or source-group status band clearly governs its
   contents, the same classification is not repeated on every nested component.

8. **Machine-readable source and evidence-layer markup is preserved even when the visible
   wording is shortened.** Visible student text and internal semantic metadata do not need
   to be identical, and validation should bind to the markup rather than to
   paragraph-length prose.

## 2. Panels and framing

1. A border or panel must improve grouping, hierarchy, or interpretation. If it does
   none of the three, it is decoration with weight.

2. **Do not retain frame-within-frame structures** merely because each component can
   technically be boxed. The common offender is an outer figure frame wrapping an inner
   container frame wrapping already-bordered components.

3. An ordinary figure normally uses:
   - one clean figure boundary, when a boundary is needed;
   - one useful caption, when a caption is needed;
   - one concise provenance/status line, when status is required.

4. Use an open figure, or unboxed explanatory content, where another frame adds visual
   weight without improving comprehension.

5. **Do not remove a frame that genuinely separates evidence records or response areas.**
   Evidence-record separation, response-field borders, tables that need visible structure,
   and task-level hierarchy all stay.

The goal is not fewer borders at all costs. It is clearer hierarchy.

## 3. Label and response-control alignment

A short label and its response field form **one visual unit**.

- Keep the label immediately beside its field, vertically centred, with one controlled gap.
- Do not distribute a label and its field across a wide container simply because
  horizontal space is available.
- Group each label/field pair semantically — a flex or grid pair that sizes to its
  content — rather than patching the gap with one-off margins.
- Where several such pairs sit side by side, use the same gap for each so the groups read
  as parallel.

## 4. Application and validation

When applying this clarification to an existing package, inventory every visible
provenance or status string in the learner editions and classify each as **keep**,
**shorten to the status label**, **move the necessary limit to a caption**, or **remove as
redundant production metadata**. Implement the minimal cleanup that follows; do not delete
sentences without asking whether a learner needs them.

Case-level validation should assert that:

- the case's evidence and source classes remain correctly distinguished;
- learner-visible provenance labels use the controlled concise form;
- a required evidence-boundary clarification remains wherever it is genuinely needed;
- no assessed source attribution changed;
- machine-readable evidence-layer semantics remain intact.

Validation must not be written so that it can only be satisfied by paragraph-length
metadata prose.

## 5. Scope boundary

This clarification changes visible metadata density, figure framing, and label/field
grouping. It does not change instructional content, task identifiers, evidence
architecture, source certification, assessment boundaries, accessibility obligations, or
any other approved visual standard. It supersedes no existing amendment.
