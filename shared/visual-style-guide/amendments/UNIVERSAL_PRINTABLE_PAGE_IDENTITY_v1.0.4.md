# Universal Printable Page Identity — v1.0.4 Clarification

**Applies to:** SSS and HHH Student, Accessible, Teacher, Answer Key, and other ordinary printable curriculum roles  
**Status:** Approved production clarification  
**Supersedes:** The first-page, continuation-header, visible-status, and footer details in `MISSION_TITLE_AND_CONTINUATION_HEADER_PARITY_v1.0.3.md`

## 1. Universal first-page banner

Every ordinary printable role uses the same first-page anatomy:

1. a narrow institutional accent rail at the far left;
2. the case or packet title and a compact subtitle on the left;
3. the institutional insignia, full institution name, and document role on the right;
4. one thin rule beneath the banner;
5. no colored rule along the top.

The case title is the primary heading. The subtitle contains only campaign number, case number, and location. A science focus, lesson topic, student identity, or game-level descriptor belongs in the instructional body rather than the universal banner.

### Compact geometry

The universal first-page banner uses compact production geometry rather than a cover-style vertical footprint:

- the primary title is 26 pt;
- the location subtitle is 9 pt;
- the identification row sits close to the banner;
- the banner's bottom rule sits close to the first instructional block;
- the accent rail is only as tall as the title, subtitle, and institutional lockup require;
- excess blank space must not be added above or below the banner merely to create atmosphere.

The institutional name is a fixed three-line lockup—`Solar`, `Agricultural`, `Agency`—left-aligned beside the insignia. The same lockup is used in first-page and continuation headers, with visible padding between the insignia and text.

Examples:

- `Campaign 1 · Case 01 · Low Earth Orbit`
- `Campaign 1 · Case 02 · Shackleton Crater, Lunar South Pole`

## 2. Universal continuation header

Continuation pages use one generic header within each document role. Authors do not invent page-specific continuation titles merely to describe whatever tasks happen to land on the page.

Left side:

- case title;
- document role followed by `Continued`.

Right side:

- institutional insignia;
- full institution name.

Examples:

- `Lunar Greenhouse` / `Student Mission · Continued`
- `Lunar Greenhouse` / `Teacher Guide · Continued`
- `Lunar Greenhouse` / `Answer Key · Continued`
- `Lunar Greenhouse` / `Accessible Mission · Continued`

## 3. Minimal printable footer

The visible footer contains only the role and position within that role:

- `Student Mission 1 of 2`
- `Teacher Guide 1 of 7`
- `Answer Key 1 of 3`
- `Accessible Mission 1 of 5`

Grayscale is a production mode, not a document role; a grayscale Student output still says `Student Mission`.

Document codes, master versions, curriculum versions, game baselines, publication dates, validation states, approval states, checksums, and repository paths do not appear in the printable footer.

## 4. Production metadata separation

Production metadata remains available through HTML `<meta>` elements, manifests, validation reports, repository history, and non-printing editor controls where operationally necessary. Ordinary printable pages must not visibly display `VALIDATION BUILD`, `APPROVED`, release-candidate labels, version boxes, or similar production-state marks.

## 5. Versioning

Applying this shared visual correction to an existing v1.0 master creates a v1.1 master. The v1.0 master remains unchanged as a historical source. Validators and current-master pointers move to v1.1 only after the new file exists and passes review.

## 6. Published-output policy

PDFs and other fixed outputs do not need to be committed during ordinary master iteration. Temporary test PDFs, screenshots, and contact sheets may be generated outside the release package. The `published/` folder is reserved for approved fixed outputs after automated review and owner physical print testing.

## 7. Repository overlay packaging

A corrective repository overlay contains only files actually added or modified by that correction. Unchanged assets, diagrams, sources, and generated outputs are not repeated merely because they live in the same case directory. A delta overlay must state which prior overlay or repository state it expects.
