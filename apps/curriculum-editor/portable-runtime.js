(() => {
  "use strict";
  const configNode = document.querySelector("#portableConfig");
  if (!configNode) return;
  const config = JSON.parse(configNode.textContent);
  const stateKey = `${config.documentKey}:state`;
  const contentKey = `${config.documentKey}:content`;
  const $ = selector => document.querySelector(selector);
  const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
  const safeGet = key => { try { return localStorage.getItem(key); } catch { return null; } };
  const safeSet = (key, value) => { try { localStorage.setItem(key, value); return true; } catch { return false; } };
  const safeRemove = key => { try { localStorage.removeItem(key); } catch { /* recovery storage is optional */ } };
  const safeJson = (value, fallback) => { try { return value ? JSON.parse(value) : fallback; } catch { return fallback; } };
  const continuationRoleLabels = {
    student: "Student Mission · Continued",
    teacher: "Teacher Guide · Continued",
    answer: "Answer Key · Continued",
    accessible: "Accessible Mission · Continued"
  };
  for (const page of $$('.page[data-role] [data-page-identity="continuation"]')) {
    const role = page.closest('.page[data-role]')?.dataset.role;
    const label = page.querySelector('.continuation-role');
    if (label && continuationRoleLabels[role]) label.textContent = continuationRoleLabels[role];
  }
  const baseline = new Map($$("[data-persist-id]").map(node => [node.dataset.persistId, node.matches("input,textarea,select") ? { value: node.value } : { html: node.innerHTML }]));
  let contentState = safeJson(safeGet(contentKey), {});
  let state = {
    ...config.defaultState,
    ...config.initialState,
    ...safeJson(safeGet(stateKey), {})
  };
  if (config.standaloneRole) state.role = config.standaloneRole;
  const printProtection = document.createElement("style");
  printProtection.id = "portablePrintProtection";
  printProtection.textContent = "@media print{.page{box-shadow:none!important}}";
  document.head.append(printProtection);

  function formatPageFitStatus(count) {
    if (count === 0) return "Pages fit";
    if (count === 1) return "1 page too full";
    return `${count} pages too full`;
  }

  function currentRoleIdentity(role = state.role) { return role; }

  function restore(node, saved) {
    if (node.matches("input,textarea,select")) node.value = saved.value ?? "";
    else node.innerHTML = saved.html ?? "";
  }

  function loadContent() {
    for (const node of $$("[data-persist-id]")) {
      if (contentState[node.dataset.persistId]) restore(node, contentState[node.dataset.persistId]);
    }
  }

  function setStatus(text) {
    const node = $("#stateStatus");
    if (node) node.textContent = text;
  }

  function active(node) {
    const page = node.closest(".page[data-role]");
    return Boolean(page && (state.role === "all" || page.dataset.role === currentRoleIdentity()));
  }

  function applyEditable() {
    for (const node of $$("[data-editable]")) {
      const enabled = active(node) && state.editMode;
      node.contentEditable = enabled ? "true" : "false";
      node.tabIndex = enabled ? 0 : -1;
    }
    for (const node of $$("[data-response]")) {
      const enabled = active(node) && (state.fillMode || state.editMode);
      if (node.matches("input,textarea,select")) {
        node.disabled = !enabled;
        if ("readOnly" in node) node.readOnly = !enabled;
      } else {
        node.contentEditable = enabled ? "true" : "false";
        node.tabIndex = enabled ? 0 : -1;
      }
    }
  }

  function checkOverflow() {
    let count = 0;
    for (const page of $$(".page")) {
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
    const output = $("#overflowStatus");
    if (output) {
      output.textContent = formatPageFitStatus(count);
      output.classList.toggle("toolbar-overflow", count > 0);
    }
    return count;
  }

  function applyState() {
    const renderedRole = currentRoleIdentity();
    document.body.dataset.role = renderedRole;
    document.body.classList.toggle("edit-mode", state.editMode);
    document.body.classList.toggle("grayscale", state.grayscale);
    document.body.classList.toggle("show-guides", state.guides);
    document.body.classList.toggle("hide-boundaries", !state.boundaries);
    document.body.classList.remove("density-normal", "density-compact", "density-spacious");
    document.body.classList.add(`density-${state.density}`);
    for (const side of ["Top", "Right", "Bottom", "Left"]) {
      document.documentElement.style.setProperty(`--margin-${side.toLowerCase()}`, `${state[`margin${side}`]}in`);
    }
    const values = { roleControl: state.role, marginTop: state.marginTop, marginRight: state.marginRight, marginBottom: state.marginBottom, marginLeft: state.marginLeft, densityControl: state.density };
    for (const [id, value] of Object.entries(values)) if ($(`#${id}`)) $(`#${id}`).value = value;
    const checks = { fillControl: state.fillMode, editControl: state.editMode, grayControl: state.grayscale, guideControl: state.guides, boundaryControl: state.boundaries };
    for (const [id, value] of Object.entries(checks)) if ($(`#${id}`)) $(`#${id}`).checked = value;
    for (const page of $$(".page[data-role]")) {
      const visible = renderedRole === "all" || page.dataset.role === renderedRole;
      page.hidden = !visible;
      page.setAttribute("aria-hidden", String(!visible));
    }
    if ($("#downloadRoleButton")) $("#downloadRoleButton").disabled = state.role === "all";
    applyEditable();
    requestAnimationFrame(checkOverflow);
  }

  function saveState(patch = {}) {
    state = { ...state, ...patch };
    safeSet(stateKey, JSON.stringify(state));
    setStatus("SAVED LOCALLY");
    applyState();
  }

  function setRole(role) {
    if (config.standaloneRole) return;
    saveState({ role });
  }

  function persist(node) {
    contentState[node.dataset.persistId] = node.matches("input,textarea,select") ? { value: node.value } : { html: node.innerHTML };
    safeSet(contentKey, JSON.stringify(contentState));
    setStatus("SAVED LOCALLY");
  }

  function clearCurrentRole(force = false) {
    if (state.role === "all") {
      if (!force) alert("Choose one role before clearing responses.");
      return false;
    }
    if (!force && !confirm("Clear all responses in the current role?")) return false;
    for (const node of $$(`.page[data-role="${currentRoleIdentity()}"] [data-response]`)) {
      if (node.matches("input,textarea,select")) node.value = "";
      else node.innerHTML = "";
      delete contentState[node.dataset.persistId];
    }
    safeSet(contentKey, JSON.stringify(contentState));
    setStatus("CURRENT ROLE CLEARED");
    checkOverflow();
    return true;
  }

  function resetSource(force = false) {
    if (!force && !confirm("Reset this case to its approved defaults?\n\nThis will remove all locally saved responses, instructional edits, and display settings for this case.")) return false;
    for (const node of $$("[data-persist-id]")) {
      const saved = baseline.get(node.dataset.persistId);
      if (!saved) continue;
      if (config.responseReset === "clear" && node.hasAttribute("data-response")) {
        restore(node, node.matches("input,textarea,select") ? { value: "" } : { html: "" });
      } else restore(node, saved);
    }
    safeRemove(stateKey);
    safeRemove(contentKey);
    contentState = {};
    state = { ...config.defaultState };
    if (config.standaloneRole) state.role = config.standaloneRole;
    setStatus("SOURCE RESET");
    applyState();
    return true;
  }

  function cleanClone(clone) {
    const liveById = new Map($$("[data-persist-id]").map(node => [node.dataset.persistId, node]));
    for (const node of $$("[data-persist-id]", clone)) {
      const live = liveById.get(node.dataset.persistId);
      if (live) {
        if (node.matches("input,textarea,select")) {
          node.value = live.value;
          node.setAttribute("value", live.value);
        } else node.innerHTML = live.innerHTML;
      }
      node.removeAttribute("contenteditable");
      node.removeAttribute("tabindex");
      node.removeAttribute("spellcheck");
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
    clone.querySelector("body")?.classList.remove("edit-mode", "print-preview");
  }

  function serializePortableHTML() {
    const clone = document.documentElement.cloneNode(true);
    cleanClone(clone);
    const nextConfig = { ...config, initialState: state, documentKey: `${config.documentKey}:copy:${Date.now()}` };
    clone.querySelector("#portableConfig").textContent = JSON.stringify(nextConfig).replace(/</g, "\\u003c");
    return `<!doctype html>\n${clone.outerHTML}`;
  }

  function serializeRoleHTML(role = state.role) {
    if (role === "all") throw new Error("Choose one role before exporting.");
    const clone = document.documentElement.cloneNode(true);
    cleanClone(clone);
    clone.querySelector(".toolbar")?.remove();
    const wanted = role;
    for (const page of $$(".page[data-role]", clone)) if (page.dataset.role !== wanted) page.remove();
    const cloneBody = clone.querySelector("body");
    cloneBody.dataset.role = wanted;
    cloneBody.dataset.standalone = "true";
    cloneBody.classList.add("standalone-role");
    cloneBody.classList.toggle("grayscale", state.grayscale);
    const nextConfig = { ...config, initialState: { ...state, role, grayscale: state.grayscale }, standaloneRole: role, documentKey: `${config.documentKey}:${role}:${Date.now()}` };
    clone.querySelector("#portableConfig").textContent = JSON.stringify(nextConfig).replace(/</g, "\\u003c");
    return `<!doctype html>\n${clone.outerHTML}`;
  }

  function buildPrintDocument(role = state.role) {
    if (role === "all" || !config.rolePageStructure[role]) throw new Error("Choose one instructional role before printing.");
    const clone = document.documentElement.cloneNode(true);
    cleanClone(clone);
    for (const selector of [".toolbar", "#editorToolbarHost", ".library-rail", ".workspace-header", ".editor-statuses", ".skip-link", "#pdfNotice", "#portableConfig", "script"]) {
      for (const node of $$(selector, clone)) node.remove();
    }
    for (const link of $$('a[href="#workspace"]', clone)) link.remove();
    const wanted = role;
    for (const page of $$(".page[data-role]", clone)) if (page.dataset.role !== wanted) page.remove();
    const cloneBody = clone.querySelector("body");
    cloneBody.dataset.role = wanted;
    cloneBody.dataset.standalone = "true";
    cloneBody.dataset.printDocument = "true";
    cloneBody.className = ["standalone-role", "print-document", "hide-boundaries", `density-${state.density}`, state.grayscale ? "grayscale" : "", state.guides ? "show-guides" : ""].filter(Boolean).join(" ");
    for (const side of ["top", "right", "bottom", "left"]) clone.style.setProperty(`--margin-${side}`, `${state[`margin${side[0].toUpperCase()}${side.slice(1)}`]}in`);
    const style = clone.ownerDocument.createElement("style");
    style.id = "isolatedPrintDocumentStyles";
    style.textContent = `
html,body{min-height:0!important;margin:0!important;padding:0!important;background:#fff!important}
body.print-document{display:block!important;min-height:0!important;background:#fff!important}
body.print-document .workspace{display:block!important;min-height:0!important;margin:0!important;padding:0!important;background:transparent!important}
body.print-document .page{display:block!important;margin:0 auto!important;box-shadow:none!important;break-after:page!important;page-break-after:always!important}
body.print-document .page:last-child{break-after:auto!important;page-break-after:auto!important}
body.print-document .overflow-warning{display:none!important}
@media print{html,body,body.print-document,body.print-document .workspace{min-height:0!important;margin:0!important;padding:0!important;background:#fff!important}body.print-document .page{box-shadow:none!important}}`;
    clone.querySelector("head").append(style);
    return `<!doctype html>\n${clone.outerHTML}`;
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
    frame.title = `${config.title} print document`;
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

  function download(html, filename) {
    const url = URL.createObjectURL(new Blob([html], { type: "text/html;charset=utf-8" }));
    const link = document.createElement("a");
    link.href = url;
    link.download = filename;
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  function currentRoleOutput() {
    return { role: state.role, grayscale: state.grayscale, outputRole: state.role, filename: config.outputs[state.role] };
  }

  function bind() {
    $("#roleControl")?.addEventListener("change", event => setRole(event.target.value));
    $("#fillControl")?.addEventListener("change", event => saveState({ fillMode: event.target.checked }));
    $("#editControl")?.addEventListener("change", event => saveState({ editMode: event.target.checked }));
    $("#grayControl")?.addEventListener("change", event => saveState({ grayscale: event.target.checked }));
    $("#guideControl")?.addEventListener("change", event => saveState({ guides: event.target.checked }));
    $("#boundaryControl")?.addEventListener("change", event => saveState({ boundaries: event.target.checked }));
    $("#densityControl")?.addEventListener("change", event => saveState({ density: event.target.value }));
    for (const side of ["Top", "Right", "Bottom", "Left"]) {
      $(`#margin${side}`)?.addEventListener("change", event => saveState({ [`margin${side}`]: Math.max(.25, Math.min(1, Number(event.target.value) || .5)) }));
    }
    $("#marginReset")?.addEventListener("click", () => saveState({ marginTop: .5, marginRight: .5, marginBottom: .5, marginLeft: .5 }));
    $("#printButton")?.addEventListener("click", () => {
      void printCurrentRole().catch(error => setStatus(`PRINT FAILED: ${error.message || error}`));
    });
    $("#downloadButton")?.addEventListener("click", () => download(serializePortableHTML(), config.outputs.complete));
    $("#downloadRoleButton")?.addEventListener("click", () => state.role !== "all" && download(serializeRoleHTML(), currentRoleOutput().filename));
    $("#clearButton")?.addEventListener("click", () => clearCurrentRole(false));
    $("#resetButton")?.addEventListener("click", () => resetSource(false));
    document.addEventListener("input", event => {
      const node = event.target.closest?.("[data-persist-id]");
      if (node) persist(node);
    });
    window.addEventListener("resize", checkOverflow);
    window.addEventListener("beforeprint", checkOverflow);
  }

  loadContent();
  bind();
  applyState();
  window.__curriculumPortable = {
    getState: () => ({ ...state }),
    setRole,
    saveState,
    clearCurrentRole,
    resetSource,
    checkOverflow,
    formatPageFitStatus,
    serializePortableHTML,
    serializeRoleHTML,
    buildPrintDocument,
    preparePrintFrame,
    printCurrentRole,
    getCurrentRoleOutput: () => ({ ...currentRoleOutput() }),
    keys: { stateKey, contentKey }
  };
})();
