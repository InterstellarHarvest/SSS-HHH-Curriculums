const REGISTRY_PATH = "/shared/implementation/case-registry.v1.json";
const SUPPORTED_PACKAGE_SCHEMA = 1;
const ROLE_LABELS = {
  student: "Student",
  teacher: "Teacher",
  answer: "Answer Key",
  accessible: "Accessible",
  grayscale: "Grayscale",
  all: "All Pages"
};

const elements = {
  toolbarHost: document.querySelector("#editorToolbarHost"),
  icons: document.querySelector("#packageIcons"),
  workspace: document.querySelector("#worksheetWorkspace"),
  curriculum: document.querySelector("#curriculumSelect"),
  campaign: document.querySelector("#campaignSelect"),
  caseSelect: document.querySelector("#caseSelect"),
  caseStatus: document.querySelector("#caseStatus"),
  roleLibrary: document.querySelector("#roleLibrary"),
  title: document.querySelector("#workspaceTitle"),
  breadcrumb: document.querySelector("#caseBreadcrumb"),
  mode: document.querySelector("#modeIndicator"),
  loadStatus: document.querySelector("#loadStatus"),
  saveMirror: document.querySelector("#saveStatusMirror"),
  overflowMirror: document.querySelector("#overflowStatusMirror"),
  error: document.querySelector("#editorError"),
  pdfNotice: document.querySelector("#pdfNotice")
};

let registry;
let casePackage;
let taskRegistry;
let state;
let defaultState;
let stateKey;
let contentKey;
let sourceBaseline = new Map();
let contentState = {};
let packageStyleText = [];
let portableRuntimeSource = "";
let exportSequence = 0;

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
    "schemaVersion", "id", "curriculum", "campaign", "title", "version", "status",
    "documentKey", "supportedRoles", "defaultRole", "shell", "taskRegistry", "content",
    "styles", "assets", "rolePageStructure", "outputs", "defaultToolbarState", "accessibility"
  ], "Case package");
  if (pkg.schemaVersion !== SUPPORTED_PACKAGE_SCHEMA) {
    throw new Error(`Unsupported case-package schema version: ${pkg.schemaVersion}`);
  }
  const requiredRoles = ["student", "teacher", "answer", "accessible", "grayscale"];
  for (const role of requiredRoles) {
    if (!pkg.supportedRoles.includes(role) || !pkg.rolePageStructure[role] || !pkg.outputs[role]) {
      throw new Error(`Case package is missing role definition: ${role}`);
    }
    const structure = pkg.rolePageStructure[role];
    if (!Number.isInteger(structure.pageCount) || structure.pageCount < 1 || !structure.sourceRole) {
      throw new Error(`Invalid page structure for role: ${role}`);
    }
  }
  if (!pkg.supportedRoles.includes(pkg.defaultRole)) throw new Error("Default role is not supported.");
  if (pkg.shell.version !== "1.0") throw new Error(`Unsupported editor shell: ${pkg.shell.version}`);
  if (!Array.isArray(pkg.shell.styles) || !pkg.shell.styles.length) throw new Error("Shared shell styles are missing.");
  if (!Array.isArray(pkg.styles) || !pkg.styles.length) throw new Error("Case-specific styles are missing.");
  if (/master\//i.test(pkg.content.source)) throw new Error("A case package may not use an approved master as content.");
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
  return { html: node.innerHTML, response: node.hasAttribute("data-response") };
}

function restoreNode(node, saved) {
  if (node.matches("input, textarea, select")) node.value = saved.value ?? "";
  else node.innerHTML = saved.html ?? "";
}

function installStyles(styleEntries) {
  for (const old of $$("style[data-case-package-style]")) old.remove();
  packageStyleText = styleEntries.map(entry => entry.text);
  styleEntries.forEach((entry, index) => {
    const style = document.createElement("style");
    style.dataset.casePackageStyle = String(index + 1);
    style.dataset.source = entry.path;
    style.textContent = entry.text;
    document.head.append(style);
  });
}

function installToolbar(toolbarText) {
  const template = document.createElement("template");
  template.innerHTML = toolbarText.trim();
  const toolbar = template.content.querySelector(".toolbar");
  if (!toolbar) throw new Error("Shared shell toolbar is missing.");
  const download = toolbar.querySelector("#downloadButton");
  const roleDownload = document.createElement("button");
  roleDownload.id = "downloadRoleButton";
  roleDownload.type = "button";
  roleDownload.textContent = "Download Current Role";
  download.after(roleDownload);
  const roleControl = toolbar.querySelector("#roleControl");
  const allOption = roleControl.querySelector('option[value="all"]');
  const grayscale = document.createElement("option");
  grayscale.value = "grayscale";
  grayscale.textContent = "Grayscale";
  roleControl.insertBefore(grayscale, allOption);
  toolbar.querySelector("#stateStatus").setAttribute("aria-live", "polite");
  toolbar.querySelector("#overflowStatus").setAttribute("aria-live", "polite");
  toolbar.querySelector("#printButton").setAttribute("aria-describedby", "pdfNotice");
  elements.toolbarHost.replaceChildren(toolbar);
  elements.toolbarHost.setAttribute("aria-busy", "false");
}

function populateLibrary(curriculum, campaign, caseEntry) {
  const option = (value, text) => {
    const node = document.createElement("option");
    node.value = value;
    node.textContent = text;
    return node;
  };
  elements.curriculum.replaceChildren(option(curriculum.id, curriculum.title));
  elements.campaign.replaceChildren(option(campaign.id, campaign.title));
  elements.caseSelect.replaceChildren(option(caseEntry.id, `${caseEntry.title} · v${caseEntry.version}`));
  elements.curriculum.disabled = elements.campaign.disabled = elements.caseSelect.disabled = true;
  for (const role of casePackage.supportedRoles) {
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
  elements.caseStatus.textContent = casePackage.status;
  elements.title.textContent = `${casePackage.title} · ${ROLE_LABELS[casePackage.defaultRole]}`;
  elements.pdfNotice.textContent = casePackage.accessibility.pdfNotice;
}

function sourceRole(role = state.role) {
  if (role === "all") return "all";
  return casePackage.rolePageStructure[role]?.sourceRole || role;
}

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

function setOverflowStatus(count) {
  const text = `${count} overflow`;
  const toolbarStatus = $("#overflowStatus");
  if (toolbarStatus) {
    toolbarStatus.textContent = text;
    toolbarStatus.classList.toggle("toolbar-overflow", count > 0);
  }
  elements.overflowMirror.textContent = text;
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
  return Boolean(page && (state.role === "all" || page.dataset.role === sourceRole()));
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
  const renderedRole = sourceRole();
  document.body.dataset.role = renderedRole;
  document.body.classList.toggle("edit-mode", state.editMode);
  document.body.classList.toggle("grayscale", state.grayscale || state.role === "grayscale");
  document.body.classList.toggle("show-guides", state.guides);
  document.body.classList.toggle("hide-boundaries", !state.boundaries);
  document.body.classList.remove("density-normal", "density-compact", "density-spacious");
  document.body.classList.add(`density-${state.density}`);
  const rootStyle = document.documentElement.style;
  for (const side of ["Top", "Right", "Bottom", "Left"]) {
    rootStyle.setProperty(`--margin-${side.toLowerCase()}`, `${state[`margin${side}`]}in`);
  }
  const values = {
    roleControl: state.role,
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
    grayControl: state.grayscale || state.role === "grayscale",
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
  elements.title.textContent = `${casePackage.title} · ${roleName}`;
  elements.breadcrumb.textContent = `${casePackage.curriculum} → ${casePackage.campaign} → ${casePackage.title} → ${roleName}`;
  elements.mode.textContent = state.editMode ? "Edit Text mode" : (state.fillMode ? "Fill Responses mode" : "Preview mode");
  $("#downloadRoleButton").disabled = state.role === "all";
  applyEditable();
  requestAnimationFrame(checkOverflow);
}

function setRole(role) {
  const valid = [...casePackage.supportedRoles, "all"];
  if (!valid.includes(role)) throw new Error(`Unsupported role: ${role}`);
  const patch = { role };
  if (role === "grayscale") patch.grayscale = true;
  else if (state.role === "grayscale") patch.grayscale = false;
  saveState(patch);
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
  if (!force && !confirm("Clear responses for the current role only?")) return false;
  const role = sourceRole();
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
  if (!force && !confirm("Reset all local edits, responses, and settings to the loaded case package?")) return false;
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
  $("#roleControl").addEventListener("change", event => setRole(event.target.value));
  $("#fillControl").addEventListener("change", event => saveState({ fillMode: event.target.checked }));
  $("#editControl").addEventListener("change", event => saveState({ editMode: event.target.checked }));
  $("#grayControl").addEventListener("change", event => {
    const patch = { grayscale: event.target.checked };
    if (!event.target.checked && state.role === "grayscale") patch.role = "student";
    saveState(patch);
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
  $("#printButton").addEventListener("click", () => { checkOverflow(); window.print(); });
  $("#downloadButton").addEventListener("click", downloadPortableHTML);
  $("#downloadRoleButton").addEventListener("click", downloadCurrentRole);
  $("#clearButton").addEventListener("click", () => clearCurrentRole(false));
  $("#resetButton").addEventListener("click", () => resetSource(false));
  elements.workspace.addEventListener("input", event => {
    const node = event.target.closest("[data-persist-id]");
    if (node) persistElement(node);
  });
  window.addEventListener("resize", checkOverflow);
  window.addEventListener("beforeprint", () => { document.body.classList.add("print-preview"); checkOverflow(); });
  window.addEventListener("afterprint", () => document.body.classList.remove("print-preview"));
}

function syncCloneValues(clone) {
  const liveById = new Map($$("[data-persist-id]", elements.workspace).map(node => [node.dataset.persistId, node]));
  for (const node of $$('[data-persist-id]', clone)) {
    const live = liveById.get(node.dataset.persistId);
    if (!live) continue;
    if (node.matches("input, textarea, select")) {
      node.value = live.value;
      node.setAttribute("value", live.value);
    } else node.innerHTML = live.innerHTML;
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
}

function cloneWorksheet(role = null) {
  const clone = elements.workspace.cloneNode(true);
  clone.id = "workspace";
  clone.setAttribute("aria-busy", "false");
  clone.setAttribute("aria-label", `${casePackage.title} worksheet pages`);
  syncCloneValues(clone);
  if (role) {
    const wanted = casePackage.rolePageStructure[role].sourceRole;
    for (const page of $$(".page[data-role]", clone)) if (page.dataset.role !== wanted) page.remove();
  }
  return clone;
}

function cloneToolbar() {
  const clone = $(".toolbar").cloneNode(true);
  for (const control of $$('input, select', clone)) {
    const live = $(`#${control.id}`);
    if (!live) continue;
    if (control.matches('[type="checkbox"]')) {
      control.checked = live.checked;
      if (live.checked) control.setAttribute("checked", "");
      else control.removeAttribute("checked");
    } else {
      control.value = live.value;
      for (const option of $$('option', control)) option.toggleAttribute("selected", option.value === live.value);
    }
  }
  clone.querySelector("#stateStatus").textContent = "EMBEDDED SOURCE";
  clone.querySelector("#overflowStatus").textContent = "0 overflow";
  clone.querySelector("#downloadRoleButton").disabled = state.role === "all";
  return clone;
}

function escapedJson(value) {
  return JSON.stringify(value).replace(/</g, "\\u003c").replace(/-->/g, "--\\u003e");
}

function portableConfig(role = null) {
  const sequence = `${Date.now()}-${++exportSequence}`;
  const initial = { ...state };
  if (role) initial.role = role;
  return {
    schemaVersion: 1,
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

function buildPortableDocument(role = null) {
  const roleName = role ? ROLE_LABELS[role] : "Editable Worksheet";
  const worksheet = cloneWorksheet(role);
  const toolbar = role ? "" : cloneToolbar().outerHTML;
  const config = portableConfig(role);
  const grayscale = Boolean(role ? casePackage.rolePageStructure[role].grayscale : (state.grayscale || state.role === "grayscale"));
  const renderedRole = role ? casePackage.rolePageStructure[role].sourceRole : sourceRole();
  const bodyClasses = [role ? "standalone-role" : "", grayscale ? "grayscale" : ""].filter(Boolean).join(" ");
  const metadata = [
    ["sss-case", casePackage.id],
    ["sss-case-version", casePackage.version],
    ["sss-case-package-schema", String(casePackage.schemaVersion)],
    ["sss-editor-shell", casePackage.shell.version],
    ["sss-export-kind", role ? "current-role" : "complete-editable-html"]
  ].map(([name, content]) => `<meta name="${name}" content="${content}">`).join("\n");
  const styles = packageStyleText.join("\n\n") + "\n[hidden]{display:none!important}";
  const runtime = portableRuntimeSource.replace(/<\/script/gi, "<\\/script");
  return `<!doctype html>
<html lang="${casePackage.accessibility.language}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${casePackage.title} · ${roleName}</title>
${metadata}
<style>${styles}</style>
</head>
<body class="${bodyClasses}" data-role="${renderedRole}" data-standalone="${role ? "true" : "false"}">
<a class="visually-hidden" href="#workspace">Skip to curriculum pages</a>
${elements.icons.innerHTML}
${toolbar}
${worksheet.outerHTML}
<script id="portableConfig" type="application/json">${escapedJson(config)}</script>
<script>${runtime}</script>
</body>
</html>`;
}

function serializePortableHTML() { return buildPortableDocument(null); }
function serializeRoleHTML(role = state.role) {
  if (role === "all") throw new Error("Choose one role before exporting a current-role file.");
  return buildPortableDocument(role);
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
  if (state.role === "all") {
    alert("Choose one role before downloading a current-role file.");
    return false;
  }
  triggerDownload(serializeRoleHTML(state.role), casePackage.outputs[state.role]);
  return true;
}

function showError(error) {
  console.error(error);
  elements.error.hidden = false;
  elements.error.textContent = error.message || String(error);
  elements.loadStatus.textContent = "LOAD FAILED";
  elements.workspace.setAttribute("aria-busy", "false");
}

async function initialize() {
  registry = await fetchJson(REGISTRY_PATH);
  if (registry.schemaVersion !== 1) throw new Error(`Unsupported registry schema: ${registry.schemaVersion}`);
  const compatible = [];
  for (const curriculum of registry.curricula) {
    for (const campaign of curriculum.campaigns) {
      for (const caseEntry of campaign.cases) {
        if (caseEntry.editorPackage) compatible.push({ curriculum, campaign, caseEntry });
      }
    }
  }
  const selected = compatible.find(item => item.caseEntry.id === "SSS-C1-CASE03");
  if (!selected) throw new Error("Case 03 is not discoverable through an editor package.");
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
    casePackage.content.source,
    ...casePackage.styles.map(item => item.source),
    ...casePackage.assets.filter(item => item.source).map(item => item.source)
  ];
  const uniquePaths = [...new Set(sourcePaths)];
  const loaded = new Map(await Promise.all(uniquePaths.map(async path => [path, await fetchText(path)])));
  portableRuntimeSource = await fetch("portable-runtime.js", { cache: "no-store" }).then(response => {
    if (!response.ok) throw new Error("Portable export runtime is missing.");
    return response.text();
  });
  taskRegistry = parseTaskRegistry(loaded.get(casePackage.taskRegistry.source), casePackage.taskRegistry.global);
  installStyles([
    ...casePackage.shell.styles.map(path => ({ path, text: loaded.get(path) })),
    ...casePackage.styles.map(item => ({ path: item.source, text: loaded.get(item.source) }))
  ]);
  installToolbar(loaded.get(casePackage.shell.toolbar));
  elements.icons.innerHTML = loaded.get(casePackage.shell.icons);
  prepareContent(loaded.get(casePackage.content.source));
  populateLibrary(selected.curriculum, selected.campaign, selected.caseEntry);
  stateKey = `curriculum-editor:${casePackage.documentKey}:state`;
  contentKey = `curriculum-editor:${casePackage.documentKey}:content`;
  defaultState = { ...casePackage.defaultToolbarState };
  const saved = storageState();
  state = { ...defaultState, ...saved };
  if (![...casePackage.supportedRoles, "all"].includes(state.role)) state.role = defaultState.role;
  loadPersistentContent();
  bindToolbar();
  setSaveStatus(Object.keys(contentState).length ? "AUTOSAVE RESTORED" : "LOCAL SAVE READY");
  applyState();
  elements.workspace.setAttribute("aria-busy", "false");
  elements.loadStatus.textContent = casePackage.accessibility.loadAnnouncement;
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
    persistElement,
    keys: { stateKey, contentKey }
  };
  window.dispatchEvent(new CustomEvent("curriculum-editor-ready"));
}

initialize().catch(showError);
