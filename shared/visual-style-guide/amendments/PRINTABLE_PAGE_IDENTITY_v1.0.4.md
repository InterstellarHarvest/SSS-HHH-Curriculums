# Printable Page Identity — v1.0.4 Clarification

**Applies to:** SSS and HHH Student, Accessible, Teacher, Answer Key, and ordinary printable curriculum roles  
**Status:** Approved production clarification  
**Consolidates and supersedes:** `MISSION_TITLE_AND_CONTINUATION_HEADER_PARITY_v1.0.3.md` and `UNIVERSAL_PRINTABLE_PAGE_IDENTITY_v1.0.4.md`

## 1. First-page identity

Every ordinary printable role uses one shared first-page structure:

1. a narrow institutional accent rail at far left;
2. case or packet title and compact campaign/case/location subtitle at left;
3. institutional insignia, the fixed three-line institution lockup, and document role at right;
4. one thin rule beneath the header;
5. no top color rule and no boxed production-status panel.

The compact geometry is part of the approved design: 26 pt title, 9 pt subtitle, close identification-to-header spacing, close header-to-content spacing, a 0.58-inch first-page insignia, and no atmospheric blank band above or below the header.

For SSS the institution lockup is left-aligned beside the insignia as three lines: `Solar`, `Agricultural`, `Agency`. HHH uses the corresponding TAA identity variables.

## 2. Continuation identity

Continuation pages use a compact shared composition:

- case title and `<Document Role> · Continued` at left;
- compact institutional insignia and full institution lockup at right;
- one thin bottom rule;
- no page-specific replacement banner and no visible production-state mark.

## 3. Footer

The printable footer contains only the document role and role-specific position, for example:

- `Student Mission 1 of 2`
- `Teacher Guide 1 of 7`
- `Answer Key 1 of 3`
- `Accessible Mission 1 of 5`

Grayscale is a production mode, not a separate role. A grayscale Student export retains the Student Mission footer.

## 4. Production metadata separation

Document codes, curriculum/master versions, game baselines, publication dates, approval or validation states, checksums, and repository paths remain in HTML metadata, manifests, reports, and repository history. They do not appear in ordinary printable headers or footers.

## 5. Versioning and current-master rules

- An approved v1.0 master remains byte-identical when a separate v1.1 design successor is created.
- A case may apply this identity correction to its existing validation master without creating a contradictory duplicate master layer when its content version remains unchanged.
- Only one file may claim to be the current production master for a case.
- Validators, manifests, reports, outputs, and checksums must agree with the selected track.

## 6. Interaction with Balanced Page Fill and Vertical Rhythm v1.0.2

The header, insignia, role lockup, and footer are fixed identity components and must not be enlarged to consume surplus space. Page-fill refinement begins with task separation and proportionate work-area sizing while preserving intentional bottom reserve.

## 7. Validation

Validation must confirm first-page structure, continuation structure, institution/role lockup, role-specific footer numbering, absence of visible production-state text, zero overflow, correct role page counts, JavaScript behavior, PDF preflight, rendered visual review, current checksums, and absence of machine-local paths.
