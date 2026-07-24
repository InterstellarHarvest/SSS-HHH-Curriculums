# Task Reference Parity — v1.0.1 Clarification

**Applies to:** SSS and HHH Student worksheets, Accessible editions, Answer Keys, annotated packets, and Teacher documents  
**Status:** Approved production clarification

## Locked rule

The standard Student worksheet is the source of truth for numbered task identifiers and visible task titles.

- Every keyed Answer Key section preserves the Student task's original number and exact visible title.
- Non-keyable tasks may be omitted silently. Later Answer Key sections keep their original Student numbers and are not renumbered.
- Teacher-facing references to a specific worksheet task include the same number and title.
- General teacher sections remain unnumbered when they are not cross-references to one Student task.
- Accessible editions preserve the same numbered task identifiers and titles as the standard Student edition.
- Technical labels may distinguish model guidance, rejected alternatives, scoring guidance, or other teacher functions without replacing the shared numbered title.

## Case 01 application

The Case 01 Answer Key begins with `3 · Investigate four evidence sources`. Tasks 1 and 2 are omitted because they do not require keyed responses. No explanatory note is added. Tasks 3–9 retain the exact Student numbering and titles.

## Teacher reference emphasis

When Teacher material directly refers to a numbered Student task, the complete matching task number and title appear in **bold**. Only the reference is bolded; surrounding prose stays regular weight, and italics or color alone are not used.

- HTML: `<strong class="task-reference">6 · Diagnose and reject an alternative</strong>`
- Shared CSS: `.task-reference { font-weight: 700; }`

General Teacher concepts and Teacher-only sections that do not point to a specific Student task remain unnumbered and unbolded. See `TEACHER_TASK_REFERENCE_EMPHASIS_v1.0.1.md`.
