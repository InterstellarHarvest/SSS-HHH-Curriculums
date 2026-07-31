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
  const baseline = new Map($$("[data-persist-id]").map(node => [node.dataset.persistId, node.matches("input,textarea,select") ? { value: node.value } : { html: node.innerHTML }]));
  let contentState = safeJson(safeGet(contentKey), {});
  let state = {
    ...config.defaultState,
    ...config.initialState,
    ...safeJson(safeGet(stateKey), {})
  };
  if (config.standaloneRole) state.role = config.standaloneRole;

  function sourceRole(role = state.role) {
    if (role === "all") return "all";
    return config.rolePageStructure[role]?.sourceRole || role;
  }

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
    return Boolean(page && (state.role === "all" || page.dataset.role === sourceRole()));
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
      output.textContent = `${count} overflow`;
      output.classList.toggle("toolbar-overflow", count > 0);
    }
    return count;
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
    for (const side of ["Top", "Right", "Bottom", "Left"]) {
      document.documentElement.style.setProperty(`--margin-${side.toLowerCase()}`, `${state[`margin${side}`]}in`);
    }
    const values = { roleControl: state.role, marginTop: state.marginTop, marginRight: state.marginRight, marginBottom: state.marginBottom, marginLeft: state.marginLeft, densityControl: state.density };
    for (const [id, value] of Object.entries(values)) if ($(`#${id}`)) $(`#${id}`).value = value;
    const checks = { fillControl: state.fillMode, editControl: state.editMode, grayControl: state.grayscale || state.role === "grayscale", guideControl: state.guides, boundaryControl: state.boundaries };
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
    const patch = { role };
    if (role === "grayscale") patch.grayscale = true;
    else if (state.role === "grayscale") patch.grayscale = false;
    saveState(patch);
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
    if (!force && !confirm("Clear responses for the current role only?")) return false;
    for (const node of $$(`.page[data-role="${sourceRole()}"] [data-response]`)) {
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
    if (!force && !confirm("Reset local edits, responses, and settings to this file's embedded source?")) return false;
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
    for (const page of $$(".page", clone)) {
      page.hidden = false;
      page.removeAttribute("hidden");
      page.removeAttribute("aria-hidden");
      page.classList.remove("has-overflow");
    }
    clone.body?.classList.remove("edit-mode", "print-preview");
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
    const wanted = config.rolePageStructure[role].sourceRole;
    for (const page of $$(".page[data-role]", clone)) if (page.dataset.role !== wanted) page.remove();
    clone.body.dataset.role = wanted;
    clone.body.dataset.standalone = "true";
    clone.body.classList.add("standalone-role");
    clone.body.classList.toggle("grayscale", Boolean(config.rolePageStructure[role].grayscale));
    const nextConfig = { ...config, initialState: { ...state, role }, standaloneRole: role, documentKey: `${config.documentKey}:${role}:${Date.now()}` };
    clone.querySelector("#portableConfig").textContent = JSON.stringify(nextConfig).replace(/</g, "\\u003c");
    return `<!doctype html>\n${clone.outerHTML}`;
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

  function bind() {
    $("#roleControl")?.addEventListener("change", event => setRole(event.target.value));
    $("#fillControl")?.addEventListener("change", event => saveState({ fillMode: event.target.checked }));
    $("#editControl")?.addEventListener("change", event => saveState({ editMode: event.target.checked }));
    $("#grayControl")?.addEventListener("change", event => saveState({ grayscale: event.target.checked, ...(state.role === "grayscale" && !event.target.checked ? { role: "student" } : {}) }));
    $("#guideControl")?.addEventListener("change", event => saveState({ guides: event.target.checked }));
    $("#boundaryControl")?.addEventListener("change", event => saveState({ boundaries: event.target.checked }));
    $("#densityControl")?.addEventListener("change", event => saveState({ density: event.target.value }));
    for (const side of ["Top", "Right", "Bottom", "Left"]) {
      $(`#margin${side}`)?.addEventListener("change", event => saveState({ [`margin${side}`]: Math.max(.25, Math.min(1, Number(event.target.value) || .5)) }));
    }
    $("#marginReset")?.addEventListener("click", () => saveState({ marginTop: .5, marginRight: .5, marginBottom: .5, marginLeft: .5 }));
    $("#printButton")?.addEventListener("click", () => { checkOverflow(); window.print(); });
    $("#downloadButton")?.addEventListener("click", () => download(serializePortableHTML(), config.outputs.complete));
    $("#downloadRoleButton")?.addEventListener("click", () => state.role !== "all" && download(serializeRoleHTML(), config.outputs[state.role]));
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
    serializePortableHTML,
    serializeRoleHTML,
    keys: { stateKey, contentKey }
  };
})();
