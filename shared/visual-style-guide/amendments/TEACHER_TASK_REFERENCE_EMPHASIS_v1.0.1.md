# Teacher Task-Reference Emphasis

**Amendment:** v1.0.1  
**Applies to:** SSS and HHH teacher-facing curriculum documents  
**Status:** Locked clarification  
**Related rule:** `TASK_REFERENCE_PARITY_v1.0.1.md`

## Decision

When Teacher material directly refers to a numbered Student task, the complete matching Student task number and title must appear in **bold**.

Only the task reference is bolded. Surrounding instructional prose remains regular weight.

Example:

> Students complete **6 · Diagnose and reject an alternative** after the game unlocks, then complete **7 · Claim-Evidence-Reasoning** using evidence from several sources.

## Required behavior

- Reproduce the Student task number and title exactly.
- Bold the complete reference, including the number.
- Use bold rather than italics.
- Keep surrounding prose at ordinary weight.
- Retain the same reference in grayscale and photocopied output.
- Use the canonical task registry where one exists.
- Do not invent shortened aliases when the reference is intended to help a teacher locate a Student task.

## Scope boundary

The rule applies only when Teacher content points to a specific Student worksheet task.

The following remain unnumbered and unbolded unless they directly cite a Student task:

- preparation;
- standards;
- objectives;
- general pacing labels;
- misconceptions;
- source notes;
- technical fallback;
- teacher-only procedures;
- general instructional concepts.

## HTML implementation

Preferred markup:

```html
<strong class="task-reference">6 · Diagnose and reject an alternative</strong>
```

Recommended shared style:

```css
.task-reference {
  font-weight: 700;
}
```

Do not use color alone to mark a task reference.

## Relationship to task parity

This amendment does not change task numbering or titles. It adds a visual navigation requirement to the existing parity rule:

- Student task identifiers remain canonical.
- Answer Key and Accessible references preserve those identifiers.
- Teacher references use exact identifiers where appropriate.
- Direct Teacher references are bold for rapid scanning.
