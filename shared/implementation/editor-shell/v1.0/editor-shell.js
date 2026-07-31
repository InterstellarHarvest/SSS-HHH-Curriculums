(() => {
  "use strict";

  const configNode = document.getElementById("sssEditorShellCaseConfig");
  if (!configNode) throw new Error("Missing #sssEditorShellCaseConfig.");
  const config = JSON.parse(configNode.textContent);
  const shellVersion = "1.0";
  if (config.shellVersion !== shellVersion) {
    throw new Error(`Editor shell mismatch: expected ${shellVersion}, found ${String(config.shellVersion)}.`);
  }

  const controls = Object.fromEntries([
    "roleSelect", "fillToggle", "editToggle",
    "marginTop", "marginRight", "marginBottom", "marginLeft", "marginReset",
    "densitySelect", "grayToggle", "guidesToggle", "boundariesToggle",
    "printBtn", "downloadMasterBtn", "downloadRoleBtn", "clearRoleBtn", "resetSourceBtn",
    "localSaveStatus", "overflowStatus"
  ].map((id) => [id, document.getElementById(id)]));

  const authorNodes = () => [...document.querySelectorAll("[data-editable], [data-response]")];
  const responseNodes = () => [...document.querySelectorAll("[data-response]")];
  const editableNodes = () => [...document.querySelectorAll("[data-editable]")];
  const pageNodes = () => [...document.querySelectorAll(".page[data-role]")];
  const embeddedSource = new Map(authorNodes().map((node) => [node.dataset.persistId, node.innerHTML]));
  const defaultState = structuredClone(config.defaults);
  let state = structuredClone(defaultState);
  let saveTimer = 0;

  function storageKey(suffix) {
    return `sss-editor-shell:${config.documentKey}:${suffix}`;
  }

  function safeJSON(value, fallback) {
    if (value === null || value === "") return fallback;
    try {
      const parsed = JSON.parse(value);
      return parsed === null ? fallback : parsed;
    } catch (_) {
      return fallback;
    }
  }

  function selectedRole() {
    return controls.roleSelect ? controls.roleSelect.value : (config.standaloneRole || state.role);
  }

  function pageIsActive(page) {
    const role = selectedRole();
    return role === "all" || page.dataset.role === role;
  }

  function setStatus(message) {
    if (controls.localSaveStatus) controls.localSaveStatus.textContent = message;
  }

  function saveLocalState() {
    if (config.standaloneRole) return;
    localStorage.setItem(storageKey("state"), JSON.stringify(state));
    const content = Object.fromEntries(authorNodes().map((node) => [node.dataset.persistId, node.innerHTML]));
    localStorage.setItem(storageKey("content"), JSON.stringify(content));
    setStatus("Local save: saved");
  }

  function scheduleSave() {
    setStatus("Local save: saving…");
    clearTimeout(saveTimer);
    saveTimer = window.setTimeout(saveLocalState, 150);
  }

  function loadLocalState() {
    if (!config.standaloneRole) {
      state = {
        ...structuredClone(defaultState),
        ...safeJSON(localStorage.getItem(storageKey("state")), {})
      };
      const content = safeJSON(localStorage.getItem(storageKey("content")), {});
      authorNodes().forEach((node) => {
        if (Object.prototype.hasOwnProperty.call(content, node.dataset.persistId)) {
          node.innerHTML = content[node.dataset.persistId];
        }
      });
    }
    applyState();
    return structuredClone(state);
  }

  function applyModes() {
    const standaloneFill = Boolean(config.standaloneRole);
    responseNodes().forEach((node) => {
      const enabled = standaloneFill || state.fillResponses || state.editText;
      node.contentEditable = enabled ? "true" : "false";
      node.tabIndex = enabled ? 0 : -1;
      node.setAttribute("role", "textbox");
      if (node.tagName !== "INPUT") node.setAttribute("aria-multiline", "true");
    });
    editableNodes().forEach((node) => {
      const enabled = !config.standaloneRole && state.editText;
      node.contentEditable = enabled ? "true" : "false";
      node.tabIndex = enabled ? 0 : -1;
    });
    document.body.classList.toggle("shell-edit-text", !config.standaloneRole && state.editText);
  }

  function applyState() {
    if (controls.roleSelect) controls.roleSelect.value = state.role;
    if (controls.fillToggle) controls.fillToggle.checked = state.fillResponses;
    if (controls.editToggle) controls.editToggle.checked = state.editText;
    ["Top", "Right", "Bottom", "Left"].forEach((side) => {
      const key = `margin${side}`;
      const control = controls[key];
      if (control) control.value = state[key];
      document.documentElement.style.setProperty(`--shell-margin-${side.toLowerCase()}`, `${state[key]}in`);
    });
    if (controls.densitySelect) controls.densitySelect.value = state.density;
    if (controls.grayToggle) controls.grayToggle.checked = state.grayscale;
    if (controls.guidesToggle) controls.guidesToggle.checked = state.guides;
    if (controls.boundariesToggle) controls.boundariesToggle.checked = state.boundaries;
    document.body.classList.toggle("shell-grayscale", state.grayscale);
    document.body.classList.toggle("shell-guides", state.guides);
    document.body.classList.toggle("shell-boundaries", state.boundaries);
    document.body.classList.toggle("shell-density-compact", state.density === "compact");
    document.body.classList.toggle("shell-density-roomy", state.density === "roomy");
    pageNodes().forEach((page) => {
      page.hidden = !pageIsActive(page);
      page.setAttribute("aria-hidden", String(!pageIsActive(page)));
    });
    applyModes();
    requestAnimationFrame(checkOverflow);
  }

  function setRole(role) {
    if (!config.roles.includes(role) && role !== "all") throw new RangeError(`Unknown role: ${role}`);
    state.role = role;
    applyState();
    scheduleSave();
  }

  function checkOverflow() {
    let count = 0;
    pageNodes().forEach((page) => {
      const content = page.querySelector(".page-frame") || page;
      const overflow = !page.hidden && content.scrollHeight > content.clientHeight + 2;
      page.classList.toggle("has-overflow", overflow);
      if (overflow) count += 1;
    });
    if (controls.overflowStatus) controls.overflowStatus.textContent = `Overflow: ${count}`;
    return count;
  }

  function clearCurrentRole(confirmed = false) {
    const role = selectedRole();
    if (role === "all") return false;
    if (!confirmed && !window.confirm(`Clear response and note fields for ${role} only?`)) return false;
    responseNodes().filter(
      (node) => node.closest(`.page[data-role="${role}"]`) && !node.classList.contains("id-field")
    ).forEach((node) => {
      node.innerHTML = "";
      node.dispatchEvent(new InputEvent("input", { bubbles: true, inputType: "deleteContent" }));
    });
    saveLocalState();
    return true;
  }

  function resetSource(confirmed = false) {
    if (!confirmed && !window.confirm("Reset this file to its embedded source and clear its local autosave?")) return false;
    authorNodes().forEach((node) => {
      node.innerHTML = embeddedSource.get(node.dataset.persistId) || "";
    });
    if (!config.standaloneRole) {
      localStorage.removeItem(storageKey("state"));
      localStorage.removeItem(storageKey("content"));
    }
    state = structuredClone(defaultState);
    applyState();
    setStatus("Local save: reset to embedded source");
    return true;
  }

  function scrubClone(root) {
    const body = root.querySelector("body");
    [
      "shell-edit-text", "shell-guides", "shell-boundaries",
      "shell-density-compact", "shell-density-roomy"
    ].forEach((name) => body.classList.remove(name));
    root.querySelectorAll(".has-overflow").forEach((node) => node.classList.remove("has-overflow"));
    root.querySelectorAll("[data-editable], [data-response]").forEach((node) => {
      node.setAttribute("contenteditable", "false");
      node.removeAttribute("tabindex");
    });
  }

  function cloneWithCurrentSource() {
    const root = document.documentElement.cloneNode(true);
    scrubClone(root);
    const cloneConfigNode = root.querySelector("#sssEditorShellCaseConfig");
    const cloneConfig = JSON.parse(cloneConfigNode.textContent);
    cloneConfig.documentKey = `${config.documentKey}:custom:${Date.now()}`;
    cloneConfig.defaults = structuredClone(state);
    cloneConfig.standaloneRole = null;
    cloneConfigNode.textContent = JSON.stringify(cloneConfig);
    return root;
  }

  function serializeRoot(root) {
    return `<!doctype html>\n${root.outerHTML}`;
  }

  function serializeEditedMasterHTML() {
    return serializeRoot(cloneWithCurrentSource());
  }

  function serializeCurrentRoleHTML(roleOverride = null) {
    const role = roleOverride || selectedRole();
    if (role === "all" || !config.roles.includes(role)) throw new RangeError("Select one role before export.");
    const root = cloneWithCurrentSource();
    root.querySelector(".toolbar")?.remove();
    root.querySelectorAll(`.page[data-role]:not([data-role="${role}"])`).forEach((page) => page.remove());
    root.querySelectorAll(".page[data-role]").forEach((page) => {
      page.hidden = false;
      page.removeAttribute("aria-hidden");
    });
    const cloneConfigNode = root.querySelector("#sssEditorShellCaseConfig");
    const cloneConfig = JSON.parse(cloneConfigNode.textContent);
    cloneConfig.documentKey = `${config.documentKey}:role:${role}:${Date.now()}`;
    cloneConfig.standaloneRole = role;
    cloneConfig.defaults.role = role;
    cloneConfig.defaults.fillResponses = true;
    cloneConfig.defaults.editText = false;
    cloneConfigNode.textContent = JSON.stringify(cloneConfig);
    const meta = root.ownerDocument.createElement("meta");
    meta.setAttribute("name", "sss-standalone-role");
    meta.setAttribute("content", role);
    root.querySelector("head").append(meta);
    root.querySelector("body").classList.add("standalone-role");
    return serializeRoot(root);
  }

  function downloadText(filename, text) {
    const link = document.createElement("a");
    link.href = URL.createObjectURL(new Blob([text], { type: "text/html;charset=utf-8" }));
    link.download = filename;
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(link.href), 1000);
  }

  function bind() {
    authorNodes().forEach((node) => node.addEventListener("input", scheduleSave));
    controls.roleSelect?.addEventListener("change", () => setRole(controls.roleSelect.value));
    controls.fillToggle?.addEventListener("change", () => {
      state.fillResponses = controls.fillToggle.checked;
      applyState();
      scheduleSave();
    });
    controls.editToggle?.addEventListener("change", () => {
      state.editText = controls.editToggle.checked;
      applyState();
      scheduleSave();
    });
    ["Top", "Right", "Bottom", "Left"].forEach((side) => {
      controls[`margin${side}`]?.addEventListener("change", () => {
        state[`margin${side}`] = Number(controls[`margin${side}`].value);
        applyState();
        scheduleSave();
      });
    });
    controls.marginReset?.addEventListener("click", () => {
      ["Top", "Right", "Bottom", "Left"].forEach((side) => {
        state[`margin${side}`] = defaultState[`margin${side}`];
      });
      applyState();
      scheduleSave();
    });
    controls.densitySelect?.addEventListener("change", () => {
      state.density = controls.densitySelect.value;
      applyState();
      scheduleSave();
    });
    controls.grayToggle?.addEventListener("change", () => {
      state.grayscale = controls.grayToggle.checked;
      applyState();
      scheduleSave();
    });
    controls.guidesToggle?.addEventListener("change", () => {
      state.guides = controls.guidesToggle.checked;
      applyState();
      scheduleSave();
    });
    controls.boundariesToggle?.addEventListener("change", () => {
      state.boundaries = controls.boundariesToggle.checked;
      applyState();
      scheduleSave();
    });
    controls.printBtn?.addEventListener("click", () => window.print());
    controls.downloadMasterBtn?.addEventListener("click", () => {
      downloadText(config.editedMasterFilename, serializeEditedMasterHTML());
    });
    controls.downloadRoleBtn?.addEventListener("click", () => {
      const role = selectedRole();
      downloadText(config.roleFilenames[role], serializeCurrentRoleHTML(role));
    });
    controls.clearRoleBtn?.addEventListener("click", () => clearCurrentRole(false));
    controls.resetSourceBtn?.addEventListener("click", () => resetSource(false));
    window.addEventListener("resize", checkOverflow);
    window.addEventListener("beforeprint", checkOverflow);
  }

  window.SSSEditorShell = Object.freeze({
    shellVersion,
    loadLocalState,
    saveLocalState,
    serializeEditedMasterHTML,
    serializeCurrentRoleHTML,
    clearCurrentRole,
    resetSource,
    setRole,
    checkOverflow
  });

  bind();
  loadLocalState();
  setStatus(config.standaloneRole ? "Embedded role source" : "Local save: ready");
})();
