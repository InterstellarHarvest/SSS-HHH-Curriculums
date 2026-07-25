# Content Ordering and Accessible Flow — v1.0.2 Clarification

**Applies to:** SSS and HHH Student worksheets, Accessible editions, Answer Keys, editable HTML masters, controlled Markdown sources, templates, and validation harnesses  
**Status:** Approved production clarification  
**Effective with:** SSS Campaign 1, Case 02 — Lunar Greenhouse

## 1. Vocabulary ordering

Student-facing vocabulary tables and lists use **alphabetical order by displayed term**. The Accessible edition preserves the same alphabetical term order.

A non-alphabetical vocabulary order is allowed only when the terms themselves form an essential scientific or historical sequence. That exception must be documented in Teacher or production notes; game-discovery order alone is not a valid reason.

## 2. Word banks for sequence tasks

A word bank used to populate ordered stages, boxes, timelines, chains, or other sequential structures must not appear in answer order.

- Shuffle the entries into a **fixed non-sequential order** for the published version.
- Student and Accessible editions use the same shuffled order.
- The Answer Key repeats the same bank terms exactly but may separately display the completed correct sequence.
- Do not dynamically reshuffle on page load; stable print, accessibility, persistence, and validation behavior take priority.
- All existing exact-match rules still apply: one entry per blank or target, no decoys, no extras, no omissions, and intact phrase answers.

## 3. Directions must describe unfinished student actions

Do not instruct students to create a visual feature that the document already supplies.

Examples:

- If arrows already connect sequence boxes, do not say “connect the boxes with arrows.”
- If stages are already numbered, do not ask students to number them.
- If a diagram already labels a structure, do not ask students to add that same label.

Keep the supplied visual affordance and remove the redundant action from the directions. Directions state only what the student must still do.

## 4. Student-facing grading commentary

Student and Accessible materials do not state that a prompt is “not graded for correctness,” “ungraded,” “for participation only,” or otherwise explain internal grading policy.

When an activity is diagnostic, formative, non-keyable, or excluded from correctness scoring, record that in Teacher materials, rubrics, task registries, or production metadata. The teacher controls how the lesson is graded.

## 5. Accessible continuous-flow pagination

The Accessible edition is a parallel, lower-density edition, but it is not a one-task-per-page format.

- Preserve canonical task order and exact task titles.
- Place consecutive tasks one after another and allow multiple compact tasks to share a page when they fit at the approved accessible type size with adequate response space.
- Use available printable vertical space before creating another page.
- Do not apply forced page breaks or `break-inside: avoid` to an entire numbered task by default.
- Keep bounded components together when splitting would harm comprehension, such as a process model and its labels, a word bank and its targets, or a short prompt and its response box.
- Continue a task onto the next page only when it genuinely cannot fit intact without cramped response space or reduced readability. Label a continuation clearly when needed.
- Large unexplained blank regions caused by automatic task isolation are a pagination defect.
- Accessible editions may use more pages than Standard editions, but added pages must be justified by readability, alternate response modes, or genuinely larger working areas—not unused space.

## 6. Validation requirement

Case-level and shared validation should assert, where applicable:

1. vocabulary is alphabetical in Student and Accessible roles;
2. sequence word-bank order differs from the completed sequence;
3. Student and Accessible word-bank order matches;
4. no redundant direction requests an already supplied visual action;
5. student-facing grading-policy commentary is absent;
6. Accessible tasks are packed continuously without overflow or unnecessary blank pages.

## 7. Case 02 application

Case 02 established the first validated application:

- alphabetical pollination vocabulary;
- a fixed shuffled six-term sequence bank;
- existing arrows retained while the redundant arrow-drawing direction was removed;
- grading-policy commentary confined to Teacher materials;
- Accessible pagination reduced from seven pages to five by pairing Tasks 3–4, 6–7, and 8–9 while keeping Task 5 intact.
