import { createVerticalResizeController } from "./vertical-resize.js";

const REGISTRY_PATH = "/shared/implementation/case-registry.v2.json";
const PROTECTED_COMPONENT_STYLES_PATH = "shared/implementation/editor-shell/v1.0/protected-printable-components.css";
const SELECTED_CASE_KEY = "curriculum-editor:selected-case:v1";
const SUPPORTED_PACKAGE_SCHEMA = 2;
const NAVIGATION_ROLES = ["student", "teacher", "answer", "accessible"];
const ROLE_LABELS = {
  student: "Student",
  teacher: "Teacher",
  answer: "Answer Key",
  accessible: "Accessible",
  all: "All Pages"
};
const PRINT_DOCUMENT_CSS = `
html,body{min-height:0!important;margin:0!important;padding:0!important;background:#fff!important}
body.print-document{display:block!important;min-height:0!important;background:#fff!important}
body.print-document .print-assets{position:absolute!important;width:0!important;height:0!important;overflow:hidden!important}
body.print-document #workspace{display:block!important;min-height:0!important;margin:0!important;padding:0!important;background:transparent!important}
body.print-document .page{display:block!important;margin:0 auto!important;box-shadow:none!important;break-after:page!important;page-break-after:always!important}
body.print-document .page:last-child{break-after:auto!important;page-break-after:auto!important}
body.print-document .overflow-warning{display:none!important}
@media print{
  html,body,body.print-document,body.print-document #workspace{min-height:0!important;margin:0!important;padding:0!important;background:#fff!important}
  body.print-document .page{box-shadow:none!important}
}`;
const EDITOR_WORKSHEET_LAYOUT_CSS = `
@media screen {
  .worksheet-document {
    width: 100%;
    min-width: 0;
    max-width: 100%;
  }
  .worksheet-document .workspace {
    width: 100%;
    min-width: 0;
    max-width: 100%;
    overflow-x: auto;
    overflow-y: visible;
    align-items: safe center;
    padding-inline: 18px;
  }
  .worksheet-document .page {
    flex-shrink: 0;
    width: var(--page-w);
    min-width: var(--page-w);
    max-width: var(--page-w);
    height: var(--page-h);
    min-height: var(--page-h);
    max-height: var(--page-h);
  }
  .worksheet-document [data-layout-resizable] { position: relative; }
  .worksheet-document .layout-resize-handle {
    position: absolute;
    z-index: 12;
    right: 5px;
    bottom: 3px;
    display: none;
    min-width: 72px;
    min-height: 24px;
    padding: 3px 6px;
    color: #fff;
    background: #245f5d;
    border: 2px solid #fff;
    border-radius: 4px;
    box-shadow: 0 0 0 1px #245f5d;
    cursor: ns-resize;
    font: 700 9px/1 "JetBrains Mono", monospace;
  }
  .worksheet-document.edit-mode[data-role="accessible"] .layout-resize-handle { display: block; }
  .worksheet-document.edit-mode[data-role="accessible"] [data-layout-resizable] { outline: 2px dashed #397b78; outline-offset: 2px; }
  .worksheet-document [data-layout-validation="approaching"] { outline-color: #ba7410!important; }
  .worksheet-document [data-layout-validation="invalid"] { outline-color: #b12f2f!important; background-color: #fff5f5!important; }
}`;

const elements = {
  toolbarHost: document.querySelector("#editorToolbarHost"),
  icons: document.querySelector("#packageIcons"),
  worksheetHost: document.querySelector("#worksheetHost"),
  workspace: null,
  curriculum: document.querySelector("#curriculumSelect"),
  campaign: document.querySelector("#campaignSelect"),
  caseSelect: document.querySelector("#caseSelect"),
  caseStatusLabel: document.querySelector(".case-status > span"),
  caseStatus: document.querySelector("#caseStatus"),
  roleLibrary: document.querySelector("#roleLibrary"),
  title: document.querySelector("#workspaceTitle"),
  breadcrumb: document.querySelector("#caseBreadcrumb"),
  mode: document.querySelector("#modeIndicator"),
  loadStatus: document.querySelector("#loadStatus"),
  saveMirror: document.querySelector("#saveStatusMirror"),
  overflowMirror: document.querySelector("#overflowStatusMirror"),
  error: document.querySelector("#editorError"),
  pdfNotice: document.querySelector("#pdfNotice"),
  layoutPanel: document.querySelector("#layoutChangesPanel")
};

let registry;
let compatibleCases = [];
let currentSelection;
let casePackage;
let taskRegistry;
let state;
let defaultState;
let stateKey;
let contentKey;
let sourceBaseline = new Map();
let contentState = {};
let packageStyleText = [];
let assetSourceText = new Map();
let worksheetDocument;
let worksheetShadow;
let portableRuntimeSource = "";
let portableToolbarTemplate;
let toolbarResizeObserver;
let exportSequence = 0;
let globalEventsBound = false;
let libraryBound = false;
let layoutManifest;
let layoutController;
let caseLoading = false;

const $ = selector => document.querySelector(selector);
const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));

function repoUrl(path) {
  if (!path || path.startsWith("/") || path.includes("..")) {
    throw new Error(`Unsafe repository path: ${path || "(empty)"}`);
  }
  return `/${path}`;
}

async function fetchText(path) {
  const response = await fetch(repoUrl(path), { cache: "no-store" });
  if (!response.ok) throw new Error(`Missing package file (${response.status}): ${path}`);
  return response.text();
}

async function fetchJson(path) {
  const response = await fetch(path.startsWith("/") ? path : repoUrl(path), { cache: "no-store" });
  if (!response.ok) throw new Error(`Unable to load JSON (${response.status}): ${path}`);
  try {
    return await response.json();
  } catch {
    throw new Error(`Invalid JSON: ${path}`);
  }
}

function safeStorageGet(key) {
  try { return localStorage.getItem(key); } catch { return null; }
}

function safeStorageSet(key, value) {
  try { localStorage.setItem(key, value); return true; } catch { return false; }
}

function safeStorageRemove(key) {
  try { localStorage.removeItem(key); } catch { /* storage is recovery-only */ }
}

function safeJson(value, fallback) {
  if (!value) return fallback;
  try { return JSON.parse(value); } catch { return fallback; }
}

function requireFields(object, fields, label) {
  if (!object || typeof object !== "object") throw new Error(`${label} must be an object.`);
  for (const field of fields) {
    if (!(field in object)) throw new Error(`${label} is missing required field: ${field}`);
  }
}

function validatePackage(pkg) {
  requireFields(pkg, [
    "schemaVersion", "id", "curriculum", "campaign", "title", "version", "status", "approval",
    "documentKey", "supportedRoles", "defaultRole", "shell", "taskRegistry", "content", "layoutOverrides",
    "presentation", "assets", "rolePageStructure", "outputs", "defaultToolbarState", "accessibility",
    "sourceHashes"
  ], "Case package");
  if (pkg.schemaVersion !== SUPPORTED_PACKAGE_SCHEMA) {
    throw new Error(`Unsupported case-package schema version: ${pkg.schemaVersion}`);
  }
  const requiredRoles = ["student", "teacher", "answer", "accessible"];
  if (JSON.stringify(pkg.supportedRoles) !== JSON.stringify(requiredRoles)) {
    throw new Error("Case package roles must be exactly student, teacher, answer, and accessible.");
  }
  for (const role of requiredRoles) {
    if (!pkg.supportedRoles.includes(role) || !pkg.rolePageStructure[role] || !pkg.outputs[role]) {
      throw new Error(`Case package is missing role definition: ${role}`);
    }
    const structure = pkg.rolePageStructure[role];
    if (!Number.isInteger(structure.pageCount) || structure.pageCount < 1 || !structure.documentRole) {
      throw new Error(`Invalid page structure for role: ${role}`);
    }
  }
  if (JSON.stringify(Object.keys(pkg.rolePageStructure)) !== JSON.stringify(requiredRoles)) {
    throw new Error("Role page structure contains an unsupported role.");
  }
  if (JSON.stringify(Object.keys(pkg.outputs)) !== JSON.stringify(["complete", ...requiredRoles])) {
    throw new Error("Output templates must contain complete plus the four instructional roles.");
  }
  if (!pkg.supportedRoles.includes(pkg.defaultRole)) throw new Error("Default role is not supported.");
  if (pkg.shell.version !== "1.0") throw new Error(`Unsupported editor shell: ${pkg.shell.version}`);
  if (!Array.isArray(pkg.shell.styles) || !pkg.shell.styles.length) throw new Error("Shared shell styles are missing.");
  if (/master\//i.test(pkg.content.source)) throw new Error("A case package may not use an approved master as content.");
  requireFields(pkg.presentation, ["source", "isolation"], "Presentation package");
  requireFields(pkg.layoutOverrides, ["source", "schemaVersion"], "Layout override contract");
  requireFields(pkg.sourceHashes, ["content", "presentation", "taskRegistry", "layoutOverrides"], "Source hashes");
  if (pkg.layoutOverrides.schemaVersion !== 1) throw new Error(`Unsupported layout override schema: ${pkg.layoutOverrides.schemaVersion}`);
  if (pkg.presentation.isolation !== "shadow-dom") throw new Error(`Unsupported worksheet isolation: ${pkg.presentation.isolation}`);
  if (pkg.phraseBank) {
    requireFields(pkg.phraseBank, ["contract", "taskId", "sourceRole", "sourceStages", "displayOrderSourceStages", "label", "instruction", "itemCount", "roles"], "Phrase-bank contract");
    if (pkg.phraseBank.contract !== "sequence-v1.0") throw new Error(`Unsupported phrase-bank contract: ${pkg.phraseBank.contract}`);
    if (pkg.phraseBank.sourceStages.length !== pkg.phraseBank.itemCount || pkg.phraseBank.displayOrderSourceStages.length !== pkg.phraseBank.itemCount) {
      throw new Error("Phrase-bank stage counts do not match itemCount.");
    }
    if (new Set(pkg.phraseBank.sourceStages).size !== pkg.phraseBank.itemCount || new Set(pkg.phraseBank.displayOrderSourceStages).size !== pkg.phraseBank.itemCount) {
      throw new Error("Phrase-bank stages must be unique.");
    }
    if (JSON.stringify([...pkg.phraseBank.sourceStages].sort()) !== JSON.stringify([...pkg.phraseBank.displayOrderSourceStages].sort())) {
      throw new Error("Phrase-bank display order must contain exactly the configured source stages.");
    }
    if (JSON.stringify(pkg.phraseBank.sourceStages) === JSON.stringify(pkg.phraseBank.displayOrderSourceStages)) {
      throw new Error("Phrase-bank display order must differ from the answer sequence.");
    }
  }
  requireFields(pkg.approval, ["owner", "status", "printStatus"], "Approval summary");
  const lifecycle = ["DRAFT", "VALIDATION_BUILD", "OWNER_GATE_OPEN", "APPROVED_STABLE"];
  if (!lifecycle.includes(pkg.status)) throw new Error(`Unsupported package lifecycle status: ${pkg.status}`);
  if (pkg.status === "APPROVED_STABLE") {
    requireFields(pkg.approval, ["date", "owner", "status", "printStatus"], "Approved package summary");
    if (pkg.approval.status !== "APPROVED" || pkg.approval.printStatus !== "PASS" || !pkg.releaseHistory) {
      throw new Error("Approved package summary or release history is incomplete.");
    }
  } else if (pkg.releaseHistory) {
    throw new Error("Unreleased packages may not declare release history.");
  }
  if (pkg.status === "DRAFT" && (pkg.approval.status !== "OWNER_REVIEW_NOT_STARTED" || pkg.approval.printStatus !== "NOT_RUN")) {
    throw new Error("Draft package must remain OWNER_REVIEW_NOT_STARTED with print status NOT_RUN.");
  }
}

async function sha256Text(value) {
  const bytes = new TextEncoder().encode(value);
  const hash = await crypto.subtle.digest("SHA-256", bytes);
  return Array.from(new Uint8Array(hash), byte => byte.toString(16).padStart(2, "0")).join("");
}

async function requireTextHash(value, expected, label) {
  const actual = await sha256Text(value);
  if (actual !== expected) throw new Error(`${label} hash mismatch: expected ${expected}, received ${actual}`);
}

function parseTaskRegistry(source, globalName) {
  const prefix = new RegExp(`^\\s*window\\.${globalName.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\s*=\\s*`);
  const jsonText = source.replace(prefix, "").replace(/;\s*$/, "");
  let parsed;
  try { parsed = JSON.parse(jsonText); } catch { throw new Error("Task registry is not a JSON-compatible assignment."); }
  requireFields(parsed, ["schemaVersion", "case", "tasks", "roles"], "Task registry");
  if (parsed.schemaVersion !== casePackage.taskRegistry.schemaVersion || parsed.case !== casePackage.id) {
    throw new Error("Task registry does not match the case package.");
  }
  return parsed;
}

function createTaskHeading(task) {
  const heading = document.createElement("h2");
  heading.className = "section-heading task-heading";
  heading.dataset.taskId = String(task.number);
  heading.dataset.taskTitle = task.title;
  const icon = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  icon.setAttribute("class", "ph-icon");
  icon.setAttribute("aria-hidden", "true");
  const use = document.createElementNS("http://www.w3.org/2000/svg", "use");
  use.setAttribute("href", `#${task.icon}`);
  icon.append(use);
  const copy = document.createElement("span");
  copy.className = "task-heading-copy";
  const label = document.createElement("span");
  label.className = "technical-label";
  label.textContent = task.semanticLabel;
  const title = document.createElement("span");
  title.className = "section-title";
  title.textContent = `${task.number} · ${task.title}`;
  copy.append(label, title);
  heading.append(icon, copy);
  return heading;
}

function prepareContent(contentText) {
  const template = document.createElement("template");
  template.innerHTML = contentText.trim();
  if (template.content.querySelector("script, style, link")) {
    throw new Error("Instructional content packages may not contain runtime or style elements.");
  }
  const tasks = new Map(taskRegistry.tasks.map(task => [String(task.number), task]));
  for (const placeholder of $$("[data-shell-task-heading]", template.content)) {
    const task = tasks.get(placeholder.dataset.shellTaskHeading);
    if (!task) throw new Error(`Invalid task reference: ${placeholder.dataset.shellTaskHeading}`);
    placeholder.replaceWith(createTaskHeading(task));
  }
  if (template.content.querySelector("[data-shell-task-heading]")) throw new Error("Unexpanded task reference remains.");
  for (const asset of casePackage.assets) {
    if (asset.selector && !template.content.querySelector(asset.selector)) {
      throw new Error(`Embedded asset selector was not found: ${asset.selector}`);
    }
  }
  const packageMain = template.content.querySelector("main");
  if (!packageMain) throw new Error("Instructional content is missing its main worksheet landmark.");
  elements.workspace.innerHTML = packageMain.innerHTML;
  const persistNodes = $$("[data-persist-id]", elements.workspace);
  const ids = persistNodes.map(node => node.dataset.persistId);
  if (new Set(ids).size !== ids.length) throw new Error("Instructional content contains duplicate persistence IDs.");
  sourceBaseline = new Map(persistNodes.map(node => [node.dataset.persistId, baselineValue(node)]));
}

function baselineValue(node) {
  if (node.matches("input, textarea, select")) return { value: node.value, response: node.hasAttribute("data-response") };
  return { html: layoutController?.cleanInnerHTML(node) ?? node.innerHTML, response: node.hasAttribute("data-response") };
}

function restoreNode(node, saved) {
  if (node.matches("input, textarea, select")) node.value = saved.value ?? "";
  else node.innerHTML = saved.html ?? "";
}

function scopePresentationCss(css) {
  return css
    .replace(/--body/g, "--__ce-b-var")
    .replace(/:root/g, ":host")
    .replace(/\bhtml\b/g, ":host")
    .replace(/\bbody\b/g, ".worksheet-document")
    .replace(/--__ce-b-var/g, "--body");
}

async function installPackageFontImports(presentationCss) {
  document.head.querySelectorAll("link[data-case-package-font]").forEach(link => link.remove());
  const imports = [...presentationCss.matchAll(/@import\s+url\(["']?(https:\/\/fonts\.googleapis\.com\/[^"')]+)["']?\)\s*;/gi)]
    .map(match => match[1]);
  await Promise.all([...new Set(imports)].map(href => new Promise(resolve => {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = href;
    link.dataset.casePackageFont = "true";
    link.addEventListener("load", resolve, { once: true });
    link.addEventListener("error", resolve, { once: true });
    document.head.append(link);
  })));
}

function installWorksheet(sharedStyles, presentationCss, protectedComponentStyles, iconsText) {
  packageStyleText = [...sharedStyles, presentationCss, protectedComponentStyles];
  worksheetShadow = elements.worksheetHost.shadowRoot || elements.worksheetHost.attachShadow({ mode: "open" });
  const style = document.createElement("style");
  style.dataset.casePackagePresentation = `${casePackage.id}:v${casePackage.version}`;
  style.textContent = `${packageStyleText.map(scopePresentationCss).join("\n\n")}\n.worksheet-document{padding:0;background:transparent}\n@media print{.worksheet-document .page{box-shadow:none!important}}`;
  const editorLayoutStyle = document.createElement("style");
  editorLayoutStyle.dataset.editorWorkspaceLayout = "fixed-page-geometry";
  editorLayoutStyle.textContent = EDITOR_WORKSHEET_LAYOUT_CSS;
  worksheetDocument = document.createElement("div");
  worksheetDocument.className = "worksheet-document";
  worksheetDocument.dataset.standalone = "true";
  const icons = document.createElement("div");
  icons.className = "worksheet-icons";
  icons.setAttribute("aria-hidden", "true");
  icons.innerHTML = iconsText;
  elements.workspace = document.createElement("main");
  elements.workspace.id = "worksheetWorkspace";
  elements.workspace.className = "workspace";
  elements.workspace.setAttribute("aria-label", `${casePackage.title} worksheet pages`);
  worksheetDocument.append(icons, elements.workspace);
  worksheetShadow.replaceChildren(style, editorLayoutStyle, worksheetDocument);
}

function syncToolbarOffset() {
  const toolbar = elements.toolbarHost.querySelector(".toolbar");
  if (!toolbar) return;
  const height = toolbar.getBoundingClientRect().height;
  if (height > 0) document.documentElement.style.setProperty("--app-toolbar-offset", `${height}px`);
}

function observeToolbar(toolbar) {
  toolbarResizeObserver?.disconnect();
  if ("ResizeObserver" in window) {
    toolbarResizeObserver = new ResizeObserver(syncToolbarOffset);
    toolbarResizeObserver.observe(toolbar);
  }
  requestAnimationFrame(syncToolbarOffset);
  document.fonts?.ready.then(syncToolbarOffset);
}

function installToolbar(toolbarText) {
  const template = document.createElement("template");
  template.innerHTML = toolbarText.trim();
  const toolbar = template.content.querySelector(".toolbar");
  if (!toolbar) throw new Error("Shared shell toolbar is missing.");
  const download = toolbar.querySelector("#downloadButton");
  download.textContent = "Download Editable Copy";
  download.setAttribute("aria-describedby", "downloadEditableDescription");
  const roleDownload = document.createElement("button");
  roleDownload.id = "downloadRoleButton";
  roleDownload.type = "button";
  roleDownload.textContent = "Download Worksheet";
  roleDownload.setAttribute("aria-describedby", "downloadWorksheetDescription");
  download.after(roleDownload);
  const clear = toolbar.querySelector("#clearButton");
  clear.textContent = "Clear Responses";
  const reset = toolbar.querySelector("#resetButton");
  reset.textContent = "Reset This Case";
  const downloadEditableDescription = document.createElement("span");
  downloadEditableDescription.id = "downloadEditableDescription";
  downloadEditableDescription.className = "visually-hidden toolbar-description";
  downloadEditableDescription.textContent = "Downloads all roles with the editing toolbar and current changes.";
  const downloadWorksheetDescription = document.createElement("span");
  downloadWorksheetDescription.id = "downloadWorksheetDescription";
  downloadWorksheetDescription.className = "visually-hidden toolbar-description";
  downloadWorksheetDescription.textContent = "Downloads only the selected role as a clean HTML worksheet without editing controls.";
  download.closest(".toolbar-group").append(downloadEditableDescription, downloadWorksheetDescription);
  const boundaryControl = toolbar.querySelector("#boundaryControl");
  const boundaryLabel = boundaryControl.closest("label");
  boundaryLabel.replaceChildren(boundaryControl, document.createTextNode(" Page shadow"));
  boundaryControl.setAttribute("aria-describedby", "pageShadowDescription");
  const pageShadowDescription = document.createElement("span");
  pageShadowDescription.id = "pageShadowDescription";
  pageShadowDescription.className = "visually-hidden toolbar-description";
  pageShadowDescription.textContent = "Adds a screen-only shadow around each worksheet page for visual separation.";
  boundaryLabel.after(pageShadowDescription);
  const overflowStatus = toolbar.querySelector("#overflowStatus");
  overflowStatus.textContent = "Pages fit";
  overflowStatus.setAttribute("aria-describedby", "pageFitDescription");
  const pageFitDescription = document.createElement("span");
  pageFitDescription.id = "pageFitDescription";
  pageFitDescription.className = "visually-hidden toolbar-description";
  pageFitDescription.textContent = "A page is too full when content extends beyond its printable page area.";
  overflowStatus.after(pageFitDescription);
  toolbar.querySelector("#stateStatus").setAttribute("aria-live", "polite");
  overflowStatus.setAttribute("aria-live", "polite");
  toolbar.querySelector("#printButton").setAttribute("aria-describedby", "pdfNotice");
  toolbar.querySelector("#grayControl").setAttribute("aria-label", "Grayscale presentation");
  portableToolbarTemplate = toolbar.cloneNode(true);
  const roleControl = toolbar.querySelector("#roleControl");
  roleControl.closest("label")?.remove();
  elements.toolbarHost.replaceChildren(toolbar);
  elements.toolbarHost.setAttribute("aria-busy", "false");
  observeToolbar(toolbar);
}

function populateLibrary(selections) {
  const option = (value, text) => {
    const node = document.createElement("option");
    node.value = value;
    node.textContent = text;
    return node;
  };
  const curricula = [...new Map(selections.map(item => [item.curriculum.id, item.curriculum])).values()];
  const campaigns = [...new Map(selections.map(item => [`${item.curriculum.id}:${item.campaign.id}`, item.campaign])).values()];
  elements.curriculum.replaceChildren(...curricula.map(item => option(item.id, item.title)));
  elements.campaign.replaceChildren(...campaigns.map(item => option(item.id, item.title)));
  elements.caseSelect.replaceChildren(...selections.map(item => option(item.caseEntry.id, item.caseEntry.displayLabel)));
  elements.curriculum.disabled = curricula.length < 2;
  elements.campaign.disabled = campaigns.length < 2;
  elements.caseSelect.disabled = selections.length < 2;
  for (const selector of [elements.curriculum, elements.campaign, elements.caseSelect]) {
    selector.setAttribute("aria-disabled", String(selector.disabled));
  }
  if (!libraryBound) {
    for (const role of NAVIGATION_ROLES) {
      const label = document.createElement("label");
      label.className = "role-option";
      const input = document.createElement("input");
      input.type = "radio";
      input.name = "libraryRole";
      input.value = role;
      input.addEventListener("change", () => input.checked && setRole(role));
      label.append(input, document.createTextNode(ROLE_LABELS[role]));
      elements.roleLibrary.append(label);
    }
    elements.caseSelect.addEventListener("change", async event => {
      const selection = compatibleCases.find(item => item.caseEntry.id === event.target.value);
      if (!selection || selection === currentSelection) return;
      try { await loadCase(selection); } catch (error) { showError(error); }
    });
    libraryBound = true;
  }
}

function syncLibrarySelection(selection) {
  elements.curriculum.value = selection.curriculum.id;
  elements.campaign.value = selection.campaign.id;
  elements.caseSelect.value = selection.caseEntry.id;
  const isReleased = casePackage.status === "APPROVED_STABLE";
  elements.caseStatusLabel.textContent = isReleased ? "Current release" : "Development status";
  elements.caseStatus.textContent = isReleased
    ? `v${casePackage.version} · ${casePackage.status}`
    : `${casePackage.status} · ${casePackage.approval.status}`;
  elements.title.textContent = `${casePackage.title} · ${ROLE_LABELS[casePackage.defaultRole]}`;
  elements.pdfNotice.textContent = casePackage.accessibility.pdfNotice;
}

function currentRoleIdentity(role = state.role) { return role; }

function storageState() {
  return safeJson(safeStorageGet(stateKey), {});
}

function loadPersistentContent() {
  contentState = safeJson(safeStorageGet(contentKey), {});
  for (const node of $$("[data-persist-id]", elements.workspace)) {
    const saved = contentState[node.dataset.persistId];
    if (saved) restoreNode(node, saved);
  }
}

function setSaveStatus(text) {
  const toolbarStatus = $("#stateStatus");
  if (toolbarStatus) toolbarStatus.textContent = text;
  elements.saveMirror.textContent = text;
}

function setLoadStatus(visibleText, announcement = visibleText) {
  const visible = document.createElement("span");
  visible.setAttribute("aria-hidden", "true");
  visible.textContent = visibleText;
  const accessible = document.createElement("span");
  accessible.className = "visually-hidden";
  accessible.textContent = announcement;
  elements.loadStatus.replaceChildren(visible, accessible);
}

function formatPageFitStatus(count) {
  if (count === 0) return "Pages fit";
  if (count === 1) return "1 page too full";
  return `${count} pages too full`;
}

function setOverflowStatus(count) {
  const text = formatPageFitStatus(count);
  const toolbarStatus = $("#overflowStatus");
  if (toolbarStatus) {
    toolbarStatus.textContent = text;
    toolbarStatus.classList.toggle("toolbar-overflow", count > 0);
  }
  elements.overflowMirror.textContent = text;
  elements.overflowMirror.classList.toggle("page-fit-warning", count > 0);
}

function saveState(patch = {}) {
  state = { ...state, ...patch };
  safeStorageSet(stateKey, JSON.stringify(state));
  setSaveStatus("SAVED LOCALLY");
  applyState();
}

function persistElement(node) {
  const id = node.dataset.persistId;
  if (!id) return;
  contentState[id] = baselineValue(node);
  safeStorageSet(contentKey, JSON.stringify(contentState));
  setSaveStatus("SAVED LOCALLY");
}

function activeForNode(node) {
  const page = node.closest(".page[data-role]");
  return Boolean(page && page.dataset.role === currentRoleIdentity());
}

function applyEditable() {
  for (const node of $$("[data-editable]", elements.workspace)) {
    const active = activeForNode(node) && state.editMode;
    node.contentEditable = active ? "true" : "false";
    node.tabIndex = active ? 0 : -1;
    node.spellcheck = active;
  }
  for (const node of $$("[data-response]", elements.workspace)) {
    const active = activeForNode(node) && (state.fillMode || state.editMode);
    if (node.matches("input, textarea, select")) {
      node.disabled = !active;
      if ("readOnly" in node) node.readOnly = !active;
    } else {
      node.contentEditable = active ? "true" : "false";
      node.tabIndex = active ? 0 : -1;
      node.spellcheck = active;
    }
  }
}

function applyState() {
  const renderedRole = currentRoleIdentity();
  document.body.dataset.role = renderedRole;
  document.body.classList.toggle("edit-mode", state.editMode);
  document.body.classList.toggle("fill-mode", state.fillMode);
  document.body.classList.toggle("grayscale", state.grayscale);
  document.body.classList.toggle("show-guides", state.guides);
  document.body.classList.toggle("hide-boundaries", !state.boundaries);
  document.body.classList.remove("density-normal", "density-compact", "density-spacious");
  document.body.classList.add(`density-${state.density}`);
  worksheetDocument.dataset.role = renderedRole;
  worksheetDocument.classList.toggle("edit-mode", state.editMode);
  worksheetDocument.classList.toggle("fill-mode", state.fillMode);
  worksheetDocument.classList.toggle("grayscale", state.grayscale);
  worksheetDocument.classList.toggle("show-guides", state.guides);
  worksheetDocument.classList.toggle("hide-boundaries", !state.boundaries);
  worksheetDocument.classList.remove("density-normal", "density-compact", "density-spacious");
  worksheetDocument.classList.add(`density-${state.density}`);
  const rootStyle = worksheetDocument.style;
  for (const side of ["Top", "Right", "Bottom", "Left"]) {
    rootStyle.setProperty(`--margin-${side.toLowerCase()}`, `${state[`margin${side}`]}in`);
  }
  const values = {
    marginTop: state.marginTop,
    marginRight: state.marginRight,
    marginBottom: state.marginBottom,
    marginLeft: state.marginLeft,
    densityControl: state.density
  };
  for (const [id, value] of Object.entries(values)) if ($(`#${id}`)) $(`#${id}`).value = value;
  const checks = {
    fillControl: state.fillMode,
    editControl: state.editMode,
    grayControl: state.grayscale,
    guideControl: state.guides,
    boundaryControl: state.boundaries
  };
  for (const [id, value] of Object.entries(checks)) if ($(`#${id}`)) $(`#${id}`).checked = value;
  for (const input of $$("input[name=libraryRole]")) input.checked = input.value === state.role;
  for (const page of $$(".page[data-role]", elements.workspace)) {
    const visible = renderedRole === "all" || page.dataset.role === renderedRole;
    page.hidden = !visible;
    page.setAttribute("aria-hidden", String(!visible));
  }
  const roleName = ROLE_LABELS[state.role];
  const grayscaleLabel = state.grayscale ? " · Grayscale" : "";
  const editLabel = state.editMode ? "Edit Text mode" : (state.fillMode ? "Fill Responses mode" : "Preview mode");
  elements.title.textContent = `${casePackage.title} · ${roleName}${grayscaleLabel}`;
  elements.breadcrumb.textContent = `${casePackage.curriculum} → ${casePackage.campaign} → ${casePackage.title} → ${roleName}${grayscaleLabel}`;
  elements.mode.textContent = `${roleName} · ${editLabel} · Grayscale ${state.grayscale ? "on" : "off"}`;
  applyEditable();
  layoutController?.syncVisibility(renderedRole, state.editMode, !caseLoading);
  requestAnimationFrame(() => {
    if (layoutController) layoutController.refreshValidation();
    else checkOverflow();
  });
}

function announceSelection() {
  setLoadStatus(
    `${casePackage.title} · ${ROLE_LABELS[state.role]} ready`,
    `${casePackage.title} v${casePackage.version}. ${ROLE_LABELS[state.role]} selected. Grayscale ${state.grayscale ? "on" : "off"}.`
  );
}

function setRole(role) {
  if (!NAVIGATION_ROLES.includes(role)) throw new Error(`Unsupported navigation role: ${role}`);
  saveState({ role });
  announceSelection();
}

function checkOverflow() {
  let count = 0;
  for (const page of $$(".page", elements.workspace)) {
    if (page.hidden || getComputedStyle(page).display === "none") {
      page.classList.remove("has-overflow");
      continue;
    }
    const frame = page.querySelector(".page-frame");
    const content = page.querySelector(".content-area");
    const overflow = Boolean(frame && (
      frame.scrollHeight > frame.clientHeight + 2 || frame.scrollWidth > frame.clientWidth + 2 ||
      (content && (content.scrollHeight > content.clientHeight + 2 || content.scrollWidth > content.clientWidth + 2))
    ));
    page.classList.toggle("has-overflow", overflow);
    if (overflow) count += 1;
  }
  setOverflowStatus(count);
  return count;
}

function clearCurrentRole(force = false) {
  if (state.role === "all") {
    if (!force) alert("Choose one role before clearing responses.");
    return false;
  }
  if (!force && !confirm("Clear all responses in the current role?")) return false;
  const role = currentRoleIdentity();
  for (const node of $$(`.page[data-role="${role}"] [data-response]`, elements.workspace)) {
    if (node.matches("input, textarea, select")) node.value = "";
    else node.innerHTML = "";
    delete contentState[node.dataset.persistId];
  }
  safeStorageSet(contentKey, JSON.stringify(contentState));
  setSaveStatus("CURRENT ROLE CLEARED");
  checkOverflow();
  return true;
}

function resetSource(force = false) {
  if (!force && !confirm("Reset this case to its approved defaults?\n\nThis will remove all locally saved responses, instructional edits, and display settings for this case.")) return false;
  for (const node of $$("[data-persist-id]", elements.workspace)) {
    const baseline = sourceBaseline.get(node.dataset.persistId);
    if (baseline) restoreNode(node, baseline);
  }
  safeStorageRemove(stateKey);
  safeStorageRemove(contentKey);
  contentState = {};
  state = { ...defaultState };
  setSaveStatus("SOURCE RESET");
  applyState();
  return true;
}

function bindToolbar() {
  $("#fillControl").addEventListener("change", event => saveState({ fillMode: event.target.checked }));
  $("#editControl").addEventListener("change", event => saveState({ editMode: event.target.checked }));
  $("#grayControl").addEventListener("change", event => {
    saveState({ grayscale: event.target.checked });
    announceSelection();
  });
  $("#guideControl").addEventListener("change", event => saveState({ guides: event.target.checked }));
  $("#boundaryControl").addEventListener("change", event => saveState({ boundaries: event.target.checked }));
  $("#densityControl").addEventListener("change", event => saveState({ density: event.target.value }));
  for (const side of ["Top", "Right", "Bottom", "Left"]) {
    $(`#margin${side}`).addEventListener("change", event => {
      const value = Math.max(.25, Math.min(1, Number(event.target.value) || .5));
      saveState({ [`margin${side}`]: value });
    });
  }
  $("#marginReset").addEventListener("click", () => saveState({ marginTop: .5, marginRight: .5, marginBottom: .5, marginLeft: .5 }));
  $("#printButton").addEventListener("click", () => { void printCurrentRole().catch(showError); });
  $("#downloadButton").addEventListener("click", downloadPortableHTML);
  $("#downloadRoleButton").addEventListener("click", downloadCurrentRole);
  $("#clearButton").addEventListener("click", () => clearCurrentRole(false));
  $("#resetButton").addEventListener("click", () => resetSource(false));
  elements.workspace.addEventListener("input", event => {
    const node = event.target.closest("[data-persist-id]");
    if (node) persistElement(node);
  });
  if (!globalEventsBound) {
    window.addEventListener("resize", () => { syncToolbarOffset(); checkOverflow(); });
    window.addEventListener("beforeprint", () => { document.body.classList.add("print-preview"); checkOverflow(); });
    window.addEventListener("afterprint", () => document.body.classList.remove("print-preview"));
    globalEventsBound = true;
  }
}

function syncCloneValues(clone) {
  const liveById = new Map($$("[data-persist-id]", elements.workspace).map(node => [node.dataset.persistId, node]));
  for (const node of $$('[data-persist-id]', clone)) {
    const live = liveById.get(node.dataset.persistId);
    node.removeAttribute("contenteditable");
    node.removeAttribute("tabindex");
    node.removeAttribute("spellcheck");
    if (!live) continue;
    if (node.matches("input, textarea, select")) {
      node.value = live.value;
      node.setAttribute("value", live.value);
    } else node.innerHTML = layoutController?.cleanInnerHTML(live) ?? live.innerHTML;
  }
  for (const node of $$("[contenteditable],[tabindex],[spellcheck]", clone)) {
    node.removeAttribute("contenteditable");
    node.removeAttribute("tabindex");
    node.removeAttribute("spellcheck");
  }
  for (const page of $$(".page", clone)) {
    page.hidden = false;
    page.removeAttribute("hidden");
    page.removeAttribute("aria-hidden");
    page.classList.remove("has-overflow");
  }
  for (const warning of $$(".overflow-warning", clone)) warning.removeAttribute("aria-live");
  layoutController?.sanitizeClone(clone);
}

function cloneWorksheet(role = null) {
  const clone = elements.workspace.cloneNode(true);
  clone.id = "workspace";
  clone.setAttribute("aria-busy", "false");
  clone.setAttribute("aria-label", `${casePackage.title} worksheet pages`);
  syncCloneValues(clone);
  for (const asset of casePackage.assets) {
    if (!asset.selector || !asset.source || !assetSourceText.has(asset.source)) continue;
    const encoded = `data:${asset.type};charset=utf-8,${encodeURIComponent(assetSourceText.get(asset.source))}`;
    for (const node of $$(asset.selector, clone)) if (node.matches("img")) node.setAttribute("src", encoded);
  }
  if (role) {
    const wanted = role;
    for (const page of $$(".page[data-role]", clone)) if (page.dataset.role !== wanted) page.remove();
  }
  return clone;
}

function cloneToolbar() {
  const clone = portableToolbarTemplate.cloneNode(true);
  for (const control of $$('input, select', clone)) {
    const live = $(`#${control.id}`);
    if (control.matches('[type="checkbox"]')) {
      const checked = live ? live.checked : false;
      control.checked = checked;
      if (checked) control.setAttribute("checked", "");
      else control.removeAttribute("checked");
    } else {
      const value = control.id === "roleControl" ? state.role : live?.value;
      if (value == null) continue;
      control.value = value;
      for (const option of $$('option', control)) option.toggleAttribute("selected", option.value === value);
    }
  }
  clone.querySelector("#stateStatus").textContent = "EMBEDDED SOURCE";
  clone.querySelector("#overflowStatus").textContent = "Pages fit";
  clone.querySelector("#overflowStatus").classList.remove("toolbar-overflow");
  clone.querySelector("#downloadRoleButton").disabled = false;
  return clone;
}

function escapedJson(value) {
  return JSON.stringify(value).replace(/</g, "\\u003c").replace(/-->/g, "--\\u003e");
}

function portableConfig(role = null, grayscale = state.grayscale) {
  const sequence = `${Date.now()}-${++exportSequence}`;
  const initial = { ...state, grayscale };
  if (role) initial.role = role;
  return {
    schemaVersion: 2,
    documentKey: `${casePackage.documentKey}:portable:${sequence}`,
    title: casePackage.accessibility.documentTitle,
    initialState: initial,
    defaultState,
    roles: casePackage.supportedRoles,
    rolePageStructure: casePackage.rolePageStructure,
    outputs: casePackage.outputs,
    standaloneRole: role,
    responseReset: "clear"
  };
}

function buildPortableDocument(role = null, grayscale = state.grayscale, options = {}) {
  const printDocument = Boolean(options.printDocument);
  const roleName = role ? casePackage.rolePageStructure[role].documentRole : "Editable Worksheet";
  const worksheet = cloneWorksheet(role);
  const toolbar = role || printDocument ? "" : cloneToolbar().outerHTML;
  const config = printDocument ? null : portableConfig(role, grayscale);
  const renderedRole = role || currentRoleIdentity();
  const bodyClasses = printDocument ? [
    "standalone-role",
    grayscale ? "grayscale" : "",
    state.guides ? "show-guides" : "",
    "hide-boundaries",
    `density-${state.density}`,
    "print-document"
  ].filter(Boolean).join(" ") : [role ? "standalone-role" : "", grayscale ? "grayscale" : ""].filter(Boolean).join(" ");
  const metadata = [
    ["sss-case", casePackage.id],
    ["sss-case-version", casePackage.version],
    ["sss-case-package-schema", String(casePackage.schemaVersion)],
    ["sss-editor-shell", casePackage.shell.version],
    ["sss-export-kind", printDocument ? "isolated-role-print" : (role ? "current-role" : "complete-editable-html")],
    ["sss-presentation-grayscale", String(grayscale)]
  ].map(([name, content]) => `<meta name="${name}" content="${content}">`).join("\n");
  const styles = packageStyleText.join("\n\n") + "\n[hidden]{display:none!important}" + (printDocument ? PRINT_DOCUMENT_CSS : "");
  const runtime = portableRuntimeSource.replace(/<\/script/gi, "<\\/script");
  return `<!doctype html>
<html lang="${casePackage.accessibility.language}"${printDocument ? ` style="--margin-top:${state.marginTop}in;--margin-right:${state.marginRight}in;--margin-bottom:${state.marginBottom}in;--margin-left:${state.marginLeft}in"` : ""}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${casePackage.title} · ${roleName}${printDocument ? " · Print" : ""}</title>
${metadata}
<style>${styles}</style>
</head>
<body class="${bodyClasses}" data-role="${renderedRole}" data-standalone="${role ? "true" : "false"}"${printDocument ? " data-print-document=\"true\"" : ""}>
${printDocument ? "" : '<a class="visually-hidden" href="#workspace">Skip to curriculum pages</a>'}
${printDocument ? "" : `<p class="visually-hidden" id="pdfNotice">${casePackage.accessibility.pdfNotice}</p>`}
${printDocument ? `<div class="print-assets" aria-hidden="true">${elements.icons.innerHTML}</div>` : elements.icons.innerHTML}
${toolbar}
${worksheet.outerHTML}
${printDocument ? "" : `<script id="portableConfig" type="application/json">${escapedJson(config)}</script>`}
${printDocument ? "" : `<script>${runtime}</script>`}
</body>
</html>`;
}

function serializePortableHTML() { return buildPortableDocument(null); }
function serializeRoleHTML(role = state.role) {
  if (!NAVIGATION_ROLES.includes(role)) throw new Error("Choose one instructional role before exporting a current-role file.");
  return buildPortableDocument(role, state.grayscale);
}

function buildPrintDocument(role = state.role) {
  if (!NAVIGATION_ROLES.includes(role)) throw new Error("Choose one instructional role before printing.");
  return buildPortableDocument(role, state.grayscale, { printDocument: true });
}

function waitForPrintImage(image) {
  const decoded = () => typeof image.decode === "function" ? image.decode().catch(() => {}) : Promise.resolve();
  if (image.complete) return decoded();
  return new Promise(resolve => {
    const done = () => { image.removeEventListener("load", done); image.removeEventListener("error", done); resolve(); };
    image.addEventListener("load", done, { once: true });
    image.addEventListener("error", done, { once: true });
  }).then(decoded);
}

async function preparePrintFrame(role = state.role) {
  const frame = document.createElement("iframe");
  frame.className = "curriculum-print-frame";
  frame.title = `${casePackage.title} ${ROLE_LABELS[role]} print document`;
  frame.setAttribute("aria-hidden", "true");
  frame.style.cssText = "position:fixed;left:-20000px;top:0;width:1440px;height:1200px;border:0;pointer-events:none";
  const loaded = new Promise((resolve, reject) => {
    frame.addEventListener("load", resolve, { once: true });
    frame.addEventListener("error", () => reject(new Error("The isolated print document could not be loaded.")), { once: true });
  });
  frame.srcdoc = buildPrintDocument(role);
  document.body.append(frame);
  await loaded;
  const printDocument = frame.contentDocument;
  if (!printDocument) {
    frame.remove();
    throw new Error("The isolated print document is unavailable.");
  }
  await printDocument.fonts?.ready;
  await Promise.all($$("img", printDocument).map(waitForPrintImage));
  return frame;
}

async function printCurrentRole(options = {}) {
  const count = checkOverflow();
  if (count > 0 && options.confirmOnTooFull !== false && !confirm(`${formatPageFitStatus(count)}. Print anyway?`)) return null;
  const frame = await preparePrintFrame(state.role);
  if (options.invokePrint === false) return frame;
  const printWindow = frame.contentWindow;
  if (!printWindow) {
    frame.remove();
    throw new Error("The isolated print window is unavailable.");
  }
  let removed = false;
  const cleanup = () => {
    if (removed) return;
    removed = true;
    frame.remove();
  };
  printWindow.addEventListener("afterprint", () => setTimeout(cleanup, 0), { once: true });
  setTimeout(cleanup, options.cleanupFallbackMs ?? 60000);
  frame.contentDocument.body.tabIndex = -1;
  frame.contentDocument.body.focus({ preventScroll: true });
  printWindow.focus();
  printWindow.print();
  return frame;
}

function currentRoleOutput() {
  return { role: state.role, grayscale: state.grayscale, outputRole: state.role, filename: casePackage.outputs[state.role] };
}

function triggerDownload(html, filename) {
  const blob = new Blob([html], { type: "text/html;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function downloadPortableHTML() {
  triggerDownload(serializePortableHTML(), casePackage.outputs.complete);
}

function downloadCurrentRole() {
  const output = currentRoleOutput();
  triggerDownload(serializeRoleHTML(state.role), output.filename);
  return true;
}

function showError(error) {
  console.error(error);
  elements.error.hidden = false;
  elements.error.textContent = error.message || String(error);
  setLoadStatus("LOAD FAILED");
  elements.worksheetHost.setAttribute("aria-busy", "false");
  caseLoading = false;
  document.body.classList.remove("case-loading");
  document.body.classList.remove("layout-authoring-ready");
  elements.layoutPanel.hidden = true;
}

async function initialize() {
  registry = await fetchJson(REGISTRY_PATH);
  if (registry.schemaVersion !== 2) throw new Error(`Unsupported registry schema: ${registry.schemaVersion}`);
  compatibleCases = [];
  for (const curriculum of registry.curricula) {
    for (const campaign of curriculum.campaigns) {
      for (const caseEntry of campaign.cases) {
        if (caseEntry.editorPackage) compatibleCases.push({ curriculum, campaign, caseEntry });
      }
    }
  }
  for (const { caseEntry } of compatibleCases) {
    if (!Number.isInteger(caseEntry.displayOrder) || !caseEntry.displayLabel) {
      throw new Error(`Case registry display metadata is missing: ${caseEntry.id}`);
    }
  }
  if (new Set(compatibleCases.map(item => item.caseEntry.displayOrder)).size !== compatibleCases.length) {
    throw new Error("Case registry display order values must be unique.");
  }
  compatibleCases.sort((a, b) => a.caseEntry.displayOrder - b.caseEntry.displayOrder);
  if (!compatibleCases.length) throw new Error("No current editor-compatible case is discoverable.");
  populateLibrary(compatibleCases);
  const requestedCaseId = new URLSearchParams(location.search).get("case");
  const selectedId = requestedCaseId || safeStorageGet(SELECTED_CASE_KEY);
  const selected = compatibleCases.find(item => item.caseEntry.id === selectedId)
    || compatibleCases.find(item => item.caseEntry.id === "SSS-C1-CASE03")
    || compatibleCases[0];
  await loadCase(selected, true);
}

async function loadCase(selected, initial = false) {
  elements.layoutPanel.hidden = true;
  caseLoading = true;
  document.body.classList.add("case-loading");
  document.body.classList.remove("layout-authoring-ready");
  layoutController?.destroy();
  layoutController = null;
  elements.error.hidden = true;
  elements.error.textContent = "";
  elements.worksheetHost.setAttribute("aria-busy", "true");
  setLoadStatus(`Loading ${selected.caseEntry.title}…`, `Loading ${selected.caseEntry.title} v${selected.caseEntry.version}…`);
  casePackage = await fetchJson(selected.caseEntry.editorPackage);
  validatePackage(casePackage);
  if (selected.caseEntry.version !== casePackage.version || selected.caseEntry.status !== casePackage.status) {
    throw new Error("Registry and package version/status do not match.");
  }
  const sourcePaths = [
    casePackage.shell.toolbar,
    ...casePackage.shell.styles,
    casePackage.shell.icons,
    casePackage.taskRegistry.source,
    casePackage.layoutOverrides.source,
    casePackage.content.source,
    casePackage.presentation.source,
    PROTECTED_COMPONENT_STYLES_PATH,
    ...casePackage.assets.filter(item => item.source).map(item => item.source)
  ];
  const uniquePaths = [...new Set(sourcePaths)];
  const loaded = new Map(await Promise.all(uniquePaths.map(async path => [path, await fetchText(path)])));
  assetSourceText = new Map(casePackage.assets.filter(asset => asset.source).map(asset => [asset.source, loaded.get(asset.source)]));
  portableRuntimeSource = await fetch("portable-runtime.js", { cache: "no-store" }).then(response => {
    if (!response.ok) throw new Error("Portable export runtime is missing.");
    return response.text();
  });
  taskRegistry = parseTaskRegistry(loaded.get(casePackage.taskRegistry.source), casePackage.taskRegistry.global);
  await requireTextHash(loaded.get(casePackage.content.source), casePackage.sourceHashes.content, "Worksheet content");
  await requireTextHash(loaded.get(casePackage.presentation.source), casePackage.sourceHashes.presentation, "Presentation stylesheet");
  await requireTextHash(loaded.get(casePackage.taskRegistry.source), casePackage.sourceHashes.taskRegistry, "Task registry");
  await requireTextHash(loaded.get(casePackage.layoutOverrides.source), casePackage.sourceHashes.layoutOverrides, "Layout override metadata");
  if (casePackage.sourceHashes.icons) await requireTextHash(loaded.get(casePackage.shell.icons), casePackage.sourceHashes.icons, "Case icon sprite");
  await installPackageFontImports(loaded.get(casePackage.presentation.source));
  installToolbar(loaded.get(casePackage.shell.toolbar));
  elements.icons.innerHTML = loaded.get(casePackage.shell.icons);
  const sharedStyles = casePackage.presentation.sharedComponentStyles
    ? casePackage.shell.styles.map(path => loaded.get(path))
    : [];
  installWorksheet(sharedStyles, loaded.get(casePackage.presentation.source), loaded.get(PROTECTED_COMPONENT_STYLES_PATH), loaded.get(casePackage.shell.icons));
  prepareContent(loaded.get(casePackage.content.source));
  currentSelection = selected;
  syncLibrarySelection(selected);
  stateKey = `curriculum-editor:${casePackage.documentKey}:state`;
  contentKey = `curriculum-editor:${casePackage.documentKey}:content`;
  defaultState = { ...casePackage.defaultToolbarState };
  const saved = storageState();
  state = { ...defaultState, ...saved };
  const requestedRole = initial ? new URLSearchParams(location.search).get("role") : null;
  if (requestedRole && NAVIGATION_ROLES.includes(requestedRole)) state.role = requestedRole;
  if (!NAVIGATION_ROLES.includes(state.role)) state.role = defaultState.role;
  loadPersistentContent();
  bindToolbar();
  try {
    layoutManifest = JSON.parse(loaded.get(casePackage.layoutOverrides.source));
  } catch {
    throw new Error("Layout override metadata is invalid JSON.");
  }
  layoutController = await createVerticalResizeController({
    package: casePackage,
    manifest: layoutManifest,
    workspace: elements.workspace,
    worksheetDocument,
    checkOverflow,
    panel: elements.layoutPanel,
    reloadCase: () => loadCase(currentSelection)
  });
  setSaveStatus(Object.keys(contentState).length ? "AUTOSAVE RESTORED" : "LOCAL SAVE READY");
  applyState();
  await document.fonts?.ready;
  checkOverflow();
  elements.worksheetHost.setAttribute("aria-busy", "false");
  setLoadStatus(
    `${casePackage.title} · ${ROLE_LABELS[state.role]} ready`,
    `${casePackage.accessibility.loadAnnouncement} Grayscale ${state.grayscale ? "on" : "off"}.`
  );
  caseLoading = false;
  document.body.classList.remove("case-loading");
  layoutController.syncVisibility(state.role, state.editMode, true);
  document.body.classList.add("layout-authoring-ready");
  safeStorageSet(SELECTED_CASE_KEY, selected.caseEntry.id);
  window.__curriculumEditor = {
    getState: () => ({ ...state }),
    getPackage: () => structuredClone(casePackage),
    getTaskRegistry: () => structuredClone(taskRegistry),
    setRole,
    saveState,
    applyState,
    checkOverflow,
    clearCurrentRole,
    resetSource,
    serializePortableHTML,
    serializeRoleHTML,
    buildPrintDocument,
    preparePrintFrame,
    printCurrentRole,
    formatPageFitStatus,
    getCurrentRoleOutput: () => ({ ...currentRoleOutput() }),
    getWorkspace: () => elements.workspace,
    getWorksheetDocument: () => worksheetDocument,
    getCompatibleCases: () => compatibleCases.map(item => ({ id: item.caseEntry.id, displayOrder: item.caseEntry.displayOrder, displayLabel: item.caseEntry.displayLabel, title: item.caseEntry.title, version: item.caseEntry.version })),
    selectCase: async id => {
      const selection = compatibleCases.find(item => item.caseEntry.id === id);
      if (!selection) throw new Error(`Unknown editor-compatible case: ${id}`);
      await loadCase(selection);
      return casePackage.id;
    },
    syncToolbarOffset,
    persistElement,
    layout: layoutController,
    keys: { stateKey, contentKey }
  };
  window.dispatchEvent(new CustomEvent(initial ? "curriculum-editor-ready" : "curriculum-editor-case-ready", { detail: { caseId: casePackage.id, version: casePackage.version } }));
}

initialize().catch(showError);
