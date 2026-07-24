# Student Identification Row Placement — Approved Clarification

**Decision:** Owner approved  
**Applies to:** SSS and HHH Student and Accessible worksheets  
**Status:** Required production rule

## Locked rule

The identification row is the first printable element inside the page margins on the first page of every Student and Accessible worksheet.

Default fields, in order:

1. Name
2. Date
3. Period

The row appears above the Mission Title Block, institutional insignia, case title, mission question, directions, and all other instructional content.

For a multi-page worksheet, the identification row appears only on page 1. Continuation pages use the compact continuation header and do not repeat Name, Date, or Period.

Teacher and Answer Key editions do not receive the student identification row.

## Accessibility and publishing behavior

- The accessible edition follows the same placement and first-page-only rule.
- Fillable fields require programmatic labels and keyboard access.
- Printed fields must remain writable and visible in grayscale.
- The row remains inside the selected page margins and printable safety area.
- Moving the row must not change task numbering, reading order after the row, or role separation.

## Required regression checks

After applying this rule to an existing packet, validate:

- Student and Accessible page counts;
- first-page reading and tab order;
- no repeated identification row on continuation pages;
- no identification row in Teacher or Answer Key roles;
- overflow in every role;
- grayscale and print-preview output;
- fillable persistence for Name, Date, and Period.
