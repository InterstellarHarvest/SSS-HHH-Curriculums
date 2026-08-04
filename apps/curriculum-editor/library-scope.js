/**
 * Curriculum → campaign → case scoping rules for the central editor library.
 *
 * The canonical registry is the sole source of the relationships between a curriculum,
 * its campaigns, and the cases registered under each campaign. These helpers are pure so
 * the scoping contract can be asserted directly against a registry document.
 */

/**
 * Flatten a registry document into the editor-compatible case selections, in display order.
 * Only cases that declare an editorPackage are compatible.
 */
export function libraryCasesFromRegistry(registry) {
  if (registry?.schemaVersion !== 2) throw new Error(`Unsupported registry schema: ${registry?.schemaVersion}`);
  const cases = [];
  for (const curriculum of registry.curricula ?? []) {
    for (const campaign of curriculum.campaigns ?? []) {
      for (const caseEntry of campaign.cases ?? []) {
        if (caseEntry.editorPackage) cases.push({ curriculum, campaign, caseEntry });
      }
    }
  }
  for (const { caseEntry } of cases) {
    if (!Number.isInteger(caseEntry.displayOrder) || !caseEntry.displayLabel) {
      throw new Error(`Case registry display metadata is missing: ${caseEntry.id}`);
    }
  }
  if (new Set(cases.map(item => item.caseEntry.displayOrder)).size !== cases.length) {
    throw new Error("Case registry display order values must be unique.");
  }
  cases.sort((a, b) => a.caseEntry.displayOrder - b.caseEntry.displayOrder);
  return cases;
}

/** The curricula that have at least one registered, editor-compatible case. */
export function curriculaWithCases(cases) {
  return [...new Map(cases.map(item => [item.curriculum.id, item.curriculum])).values()];
}

/** The campaigns of one curriculum that have at least one registered case. */
export function campaignsForCurriculum(cases, curriculumId) {
  return [...new Map(
    cases.filter(item => item.curriculum.id === curriculumId).map(item => [item.campaign.id, item.campaign])
  ).values()];
}

/** Exactly the cases registered under one curriculum and one campaign, in display order. */
export function casesForCampaign(cases, curriculumId, campaignId) {
  return cases.filter(item => item.curriculum.id === curriculumId && item.campaign.id === campaignId);
}

/** The selection that owns a case id, or undefined when the case is not registered. */
export function scopeForCase(cases, caseId) {
  return cases.find(item => item.caseEntry.id === caseId);
}

/**
 * The case to load when a campaign becomes the selected scope: the remembered case when it is
 * still registered under that campaign, otherwise the first registered case of that campaign.
 */
export function preferredCaseForCampaign(cases, curriculumId, campaignId, rememberedCaseId) {
  const scoped = casesForCampaign(cases, curriculumId, campaignId);
  return scoped.find(item => item.caseEntry.id === rememberedCaseId) || scoped[0];
}

/** Stable key identifying one curriculum + campaign scope. */
export function scopeKey(curriculumId, campaignId) {
  return `${curriculumId}:${campaignId}`;
}
