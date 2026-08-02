const SNAP_PX = 4;
const AUTHORING_SELECTOR = "[data-layout-resize-ui]";

function cloneRecord(value) {
  return JSON.parse(JSON.stringify(value));
}

function roundPx(value) {
  return Math.max(16, Math.round(value));
}

function snapPx(value) {
  return Math.round(value / SNAP_PX) * SNAP_PX;
}

export function sourcePixelsFromPointer(screenPixels, renderedScale) {
  return screenPixels / Math.max(renderedScale, .01);
}

function setHeightStyle(node, height) {
  if (height == null) {
    for (const property of ["height", "min-height", "max-height", "flex-basis"]) node.style.removeProperty(property);
    node.removeAttribute("data-layout-height-active");
    return;
  }
  const value = `${height}px`;
  node.style.setProperty("height", value, "important");
  node.style.setProperty("min-height", value, "important");
  node.style.setProperty("max-height", value, "important");
  node.style.setProperty("flex-basis", value, "important");
  node.dataset.layoutHeightActive = String(height);
}

function downloadJson(value, filename) {
  const blob = new Blob([`${JSON.stringify(value, null, 2)}\n`], { type: "application/json;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function safeStorageKeys() {
  try { return Array.from({ length: localStorage.length }, (_, index) => localStorage.key(index)).filter(Boolean); } catch { return []; }
}

function storedJson(key, fallback = null) {
  try { return JSON.parse(localStorage.getItem(key) || "null") ?? fallback; } catch { return fallback; }
}

export async function createVerticalResizeController(options) {
  const { package: casePackage, manifest, workspace, worksheetDocument, checkOverflow, panel, reloadCase } = options;
  if (!manifest || manifest.schemaVersion !== 1 || manifest.caseId !== casePackage.id || manifest.edition !== "accessible" || manifest.stepPx !== SNAP_PX) {
    throw new Error("Accessible layout override metadata does not match the loaded package.");
  }
  const controls = {
    body: panel.querySelector("#layoutChangesBody"),
    count: panel.querySelector("#layoutChangeCount"),
    status: panel.querySelector("#layoutChangeStatus"),
    undo: panel.querySelector("#layoutUndo"),
    redo: panel.querySelector("#layoutRedo"),
    resetPage: panel.querySelector("#layoutResetPage"),
    export: panel.querySelector("#layoutExport"),
    apply: panel.querySelector("#layoutApply"),
    stale: panel.querySelector("#layoutStaleDraft"),
    staleSummary: panel.querySelector("#layoutStaleSummary"),
    staleInspect: panel.querySelector("#layoutStaleInspect"),
    staleExport: panel.querySelector("#layoutStaleExport"),
    staleDiscard: panel.querySelector("#layoutStaleDiscard"),
    dialog: document.querySelector("#layoutApplyDialog"),
    preview: document.querySelector("#layoutApplyPreview"),
    confirm: document.querySelector("#layoutApplyConfirm"),
    cancel: document.querySelector("#layoutApplyCancel")
  };
  const areas = new Map();
  const pending = new Map();
  const selected = new Set();
  const history = [];
  const future = [];
  let activePageId = manifest.areas[0]?.pageId || null;
  let repositoryContext = null;
  let draftKey = null;
  let staleDrafts = [];
  let applying = false;

  panel.hidden = false;
  panel.dataset.caseId = casePackage.id;

  function canonicalHeight(area) {
    return manifest.overrides[area.id]?.heightPx ?? area.sourceHeightPx;
  }

  function currentHeight(area) {
    return pending.get(area.id)?.heightPx ?? canonicalHeight(area);
  }

  function capturePending() {
    return Object.fromEntries([...pending].map(([id, value]) => [id, { ...value }]));
  }

  function installPending(snapshot, save = true) {
    pending.clear();
    for (const [id, value] of Object.entries(snapshot || {})) if (areas.has(id)) pending.set(id, value);
    selected.clear();
    for (const id of pending.keys()) selected.add(id);
    for (const area of areas.values()) {
      setHeightStyle(area.node, pending.get(area.id)?.heightPx ?? manifest.overrides[area.id]?.heightPx ?? null);
    }
    validateAll();
    render();
    if (save) saveDraft();
  }

  function recordHistory() {
    history.push(capturePending());
    if (history.length > 100) history.shift();
    future.length = 0;
  }

  function pageSpace(area) {
    const page = area.node.closest(".page");
    const frame = page?.querySelector(".page-frame") || page;
    const footer = page?.querySelector("[data-publication-footer],.publication-footer,footer");
    const nodeRect = area.node.getBoundingClientRect();
    const scale = page && page.offsetHeight ? page.getBoundingClientRect().height / page.offsetHeight : 1;
    const bottomLimit = footer ? footer.getBoundingClientRect().top - 6 * scale : frame.getBoundingClientRect().bottom - 6 * scale;
    return Math.floor((bottomLimit - nodeRect.bottom) / Math.max(scale, .01));
  }

  function dynamicMax(area) {
    return Math.max(area.minPx, Math.min(area.maxPx, snapPx(currentHeight(area) + Math.max(0, pageSpace(area)))));
  }

  function validateArea(area) {
    const proposed = currentHeight(area);
    const page = area.node.closest(".page");
    const frame = page?.querySelector(".page-frame");
    const footer = page?.querySelector("[data-publication-footer],.publication-footer,footer");
    const nodeRect = area.node.getBoundingClientRect();
    const footerRect = footer?.getBoundingClientRect();
    const overflow = Boolean(page && (
      page.classList.contains("has-overflow") ||
      (frame && (frame.scrollHeight > frame.clientHeight + 2 || frame.scrollWidth > frame.clientWidth + 2)) ||
      (footerRect && nodeRect.bottom > footerRect.top - 2)
    ));
    let status = "valid";
    let message = "Fits within the current page";
    if (proposed < area.minPx || proposed > area.maxPx || proposed % SNAP_PX) {
      status = "invalid";
      message = `Outside ${area.minPx}–${area.maxPx}px / 4px snap`;
    } else if (overflow) {
      status = "invalid";
      message = "Would overflow or overlap the page/footer";
    } else if (pageSpace(area) < 28) {
      status = "approaching";
      message = "Approaching the safe page boundary";
    }
    const item = pending.get(area.id);
    if (item) Object.assign(item, { status, message });
    area.node.dataset.layoutValidation = status;
    return { status, message };
  }

  function validateAll() {
    checkOverflow();
    for (const area of areas.values()) validateArea(area);
  }

  function updateArea(area, requested, source = "editor") {
    const bounded = Math.max(area.minPx, Math.min(area.maxPx, snapPx(requested)));
    const before = currentHeight(area);
    if (bounded === before) return false;
    recordHistory();
    activePageId = area.pageId;
    if (bounded === canonicalHeight(area)) pending.delete(area.id);
    else pending.set(area.id, {
      id: area.id,
      heightPx: bounded,
      sourceHeightPx: canonicalHeight(area),
      source,
      status: "valid",
      message: "Pending validation"
    });
    setHeightStyle(area.node, pending.has(area.id) ? bounded : manifest.overrides[area.id]?.heightPx ?? null);
    if (pending.has(area.id)) selected.add(area.id); else selected.delete(area.id);
    validateAll();
    render();
    saveDraft();
    return true;
  }

  function resetArea(area) {
    if (!pending.has(area.id)) return;
    recordHistory();
    pending.delete(area.id);
    selected.delete(area.id);
    setHeightStyle(area.node, manifest.overrides[area.id]?.heightPx ?? null);
    validateAll();
    render();
    saveDraft();
  }

  function resetPage(pageId) {
    const ids = [...pending.keys()].filter(id => areas.get(id)?.pageId === pageId);
    if (!ids.length) return;
    recordHistory();
    for (const id of ids) {
      pending.delete(id);
      selected.delete(id);
      const area = areas.get(id);
      setHeightStyle(area.node, manifest.overrides[id]?.heightPx ?? null);
    }
    validateAll();
    render();
    saveDraft();
  }

  function undo() {
    if (!history.length) return;
    future.push(capturePending());
    installPending(history.pop());
  }

  function redo() {
    if (!future.length) return;
    history.push(capturePending());
    installPending(future.pop());
  }

  function draftValue() {
    return {
      schemaVersion: 1,
      repositoryId: repositoryContext?.repositoryId || "service-unavailable",
      repositoryLabel: repositoryContext?.repositoryLabel || "unknown",
      revision: repositoryContext?.revision || "unknown",
      caseId: casePackage.id,
      edition: "accessible",
      sourceHashes: {
        contentSha256: casePackage.sourceHashes.content,
        presentationSha256: casePackage.sourceHashes.presentation,
        layoutOverridesSha256: casePackage.sourceHashes.layoutOverrides
      },
      changes: [...pending.values()].map(item => ({ ...item }))
    };
  }

  function saveDraft() {
    if (!draftKey) return;
    if (!pending.size) localStorage.removeItem(draftKey);
    else localStorage.setItem(draftKey, JSON.stringify(draftValue()));
    const indexKey = `layout-resize:index:v1:${repositoryContext.repositoryId}:${casePackage.id}`;
    const keys = JSON.parse(localStorage.getItem(indexKey) || "[]").filter(key => key !== draftKey && localStorage.getItem(key));
    if (pending.size) keys.push(draftKey);
    localStorage.setItem(indexKey, JSON.stringify([...new Set(keys)]));
  }

  function loadDrafts() {
    if (!repositoryContext) return;
    draftKey = [
      "layout-resize", "v1", repositoryContext.repositoryId, casePackage.id, "accessible",
      casePackage.sourceHashes.content, casePackage.sourceHashes.presentation, casePackage.sourceHashes.layoutOverrides
    ].join(":");
    const current = storedJson(draftKey);
    if (current?.changes) {
      const snapshot = Object.fromEntries(current.changes.filter(item => areas.has(item.id)).map(item => [item.id, item]));
      installPending(snapshot, false);
    }
    const prefix = `layout-resize:v1:${repositoryContext.repositoryId}:${casePackage.id}:accessible:`;
    staleDrafts = safeStorageKeys().filter(key => key.startsWith(prefix) && key !== draftKey).map(key => ({ key, value: storedJson(key) })).filter(item => item.value);
    renderStale();
  }

  function renderStale() {
    controls.stale.hidden = staleDrafts.length === 0;
    if (!staleDrafts.length) return;
    controls.staleSummary.textContent = `${staleDrafts.length} stale draft${staleDrafts.length === 1 ? "" : "s"} found. Source hashes changed; drafts were not rebased.`;
    controls.staleInspect.textContent = JSON.stringify(staleDrafts.map(item => item.value), null, 2);
  }

  function render() {
    controls.body.replaceChildren();
    for (const item of pending.values()) {
      const area = areas.get(item.id);
      const row = document.createElement("tr");
      row.dataset.status = item.status;
      const choose = document.createElement("input");
      choose.type = "checkbox";
      choose.checked = selected.has(item.id);
      choose.setAttribute("aria-label", `Select ${area.label} for source apply`);
      choose.addEventListener("change", () => { choose.checked ? selected.add(item.id) : selected.delete(item.id); render(); });
      const reset = document.createElement("button");
      reset.type = "button";
      reset.textContent = "Reset area";
      reset.addEventListener("click", () => resetArea(area));
      for (const value of [choose, area.pageId, `Task ${area.taskId}`, area.label, `${item.sourceHeightPx}px`, `${item.heightPx}px`, item.message, reset]) {
        const cell = document.createElement("td");
        if (value instanceof Node) cell.append(value); else cell.textContent = value;
        row.append(cell);
      }
      controls.body.append(row);
    }
    controls.count.textContent = `${pending.size} pending`;
    controls.status.textContent = !repositoryContext ? "Source service unavailable; export remains available." : pending.size ? "Draft stored locally; source unchanged." : "No pending layout changes.";
    controls.undo.disabled = !history.length;
    controls.redo.disabled = !future.length;
    controls.resetPage.disabled = !activePageId || ![...pending.keys()].some(id => areas.get(id)?.pageId === activePageId);
    controls.export.disabled = !pending.size;
    const selectedItems = [...selected].map(id => pending.get(id)).filter(Boolean);
    controls.apply.disabled = applying || !repositoryContext || !selectedItems.length || selectedItems.some(item => item.status === "invalid");
    for (const area of areas.values()) {
      area.handle.textContent = `↕ ${currentHeight(area)}px${pending.has(area.id) ? " •" : ""}`;
      area.handle.setAttribute("aria-label", `Resize ${area.label} vertically. Current height ${currentHeight(area)} pixels. Arrow keys change by 4 pixels.`);
    }
  }

  function exportedDraft(items = [...pending.values()]) {
    return { ...draftValue(), changes: items.map(item => ({ ...item })) };
  }

  function openApplyPreview() {
    const changes = [...selected].map(id => pending.get(id)).filter(Boolean);
    controls.preview.replaceChildren(...changes.map(change => {
      const area = areas.get(change.id);
      const item = document.createElement("li");
      item.textContent = `${area.pageId} · Task ${area.taskId} · ${area.label}: ${change.sourceHeightPx}px → ${change.heightPx}px (${change.status})`;
      return item;
    }));
    controls.dialog.showModal();
  }

  async function applySelected() {
    const changes = [...selected].map(id => pending.get(id)).filter(Boolean);
    if (!changes.length || changes.some(item => item.status === "invalid")) return;
    applying = true;
    let reloaded = false;
    controls.confirm.disabled = true;
    render();
    try {
      const response = await fetch("/__authoring/apply-layout-overrides", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          schemaVersion: 1,
          repositoryId: repositoryContext.repositoryId,
          caseId: casePackage.id,
          edition: "accessible",
          preconditions: draftValue().sourceHashes,
          changes: changes.map(({ id, heightPx, sourceHeightPx }) => ({ id, heightPx, sourceHeightPx }))
        })
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || `Source apply failed (${response.status}).`);
      const unselected = [...pending.values()].filter(item => !selected.has(item.id));
      if (unselected.length) localStorage.setItem(draftKey, JSON.stringify(exportedDraft(unselected)));
      else localStorage.removeItem(draftKey);
      controls.dialog.close();
      controls.status.textContent = `Applied ${result.applied.length} change${result.applied.length === 1 ? "" : "s"}; focused validation passed. Reloading source…`;
      await reloadCase();
      reloaded = true;
    } catch (error) {
      controls.status.textContent = error.message;
      controls.dialog.close();
      throw error;
    } finally {
      applying = false;
      controls.confirm.disabled = false;
      if (!reloaded) render();
    }
  }

  function createHandle(area) {
    const handle = document.createElement("button");
    handle.type = "button";
    handle.className = "layout-resize-handle";
    handle.dataset.layoutResizeUi = "handle";
    handle.contentEditable = "false";
    let drag = null;
    handle.addEventListener("pointerdown", event => {
      if (!worksheetDocument.classList.contains("edit-mode") || worksheetDocument.dataset.role !== "accessible") return;
      event.preventDefault();
      activePageId = area.pageId;
      const page = area.node.closest(".page");
      const scale = page?.offsetHeight ? page.getBoundingClientRect().height / page.offsetHeight : 1;
      drag = { y: event.clientY, height: currentHeight(area), scale, max: dynamicMax(area) };
      handle.setPointerCapture(event.pointerId);
    });
    handle.addEventListener("pointermove", event => {
      if (!drag || !handle.hasPointerCapture(event.pointerId)) return;
      const proposed = drag.height + sourcePixelsFromPointer(event.clientY - drag.y, drag.scale);
      updateArea(area, Math.min(drag.max, proposed), "pointer");
    });
    const stop = event => {
      if (drag && handle.hasPointerCapture(event.pointerId)) handle.releasePointerCapture(event.pointerId);
      drag = null;
    };
    handle.addEventListener("pointerup", stop);
    handle.addEventListener("pointercancel", stop);
    handle.addEventListener("keydown", event => {
      if (!worksheetDocument.classList.contains("edit-mode") || worksheetDocument.dataset.role !== "accessible") return;
      if (!["ArrowUp", "ArrowDown", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      activePageId = area.pageId;
      const amount = event.shiftKey ? 20 : SNAP_PX;
      if (event.key === "ArrowUp") updateArea(area, currentHeight(area) - amount, "keyboard");
      if (event.key === "ArrowDown") updateArea(area, Math.min(dynamicMax(area), currentHeight(area) + amount), "keyboard");
      if (event.key === "Home") updateArea(area, area.minPx, "keyboard");
      if (event.key === "End") updateArea(area, dynamicMax(area), "keyboard");
    });
    return handle;
  }

  for (const definition of manifest.areas) {
    const matches = workspace.querySelectorAll(`[data-persist-id="${CSS.escape(definition.persistId)}"]`);
    if (matches.length !== 1) throw new Error(`Eligible response locator is missing or ambiguous: ${definition.id}`);
    const node = matches[0];
    const page = node.closest(".page[data-role]");
    if (!page || page.dataset.role !== "accessible" || page.dataset.pageId !== definition.pageId || node.closest('[class*="cer"],[data-cer-contract]')) {
      throw new Error(`Protected or mismatched response in layout registry: ${definition.id}`);
    }
    const priorRole = worksheetDocument.dataset.role;
    const hadHidden = page.hasAttribute("hidden");
    const priorAriaHidden = page.getAttribute("aria-hidden");
    const priorDisplay = page.style.getPropertyValue("display");
    const priorDisplayPriority = page.style.getPropertyPriority("display");
    worksheetDocument.dataset.role = "accessible";
    page.removeAttribute("hidden");
    page.setAttribute("aria-hidden", "false");
    page.style.setProperty("display", "block", "important");
    const measuredHeight = node.getBoundingClientRect().height;
    if (hadHidden) page.setAttribute("hidden", "");
    if (priorAriaHidden == null) page.removeAttribute("aria-hidden"); else page.setAttribute("aria-hidden", priorAriaHidden);
    if (priorDisplay) page.style.setProperty("display", priorDisplay, priorDisplayPriority); else page.style.removeProperty("display");
    if (priorRole == null) delete worksheetDocument.dataset.role; else worksheetDocument.dataset.role = priorRole;
    const area = { ...definition, node, sourceHeightPx: roundPx(measuredHeight) };
    area.handle = createHandle(area);
    node.dataset.layoutResizable = definition.id;
    node.append(area.handle);
    areas.set(area.id, area);
  }

  for (const [id, override] of Object.entries(manifest.overrides)) {
    const area = areas.get(id);
    if (!area) throw new Error(`Sparse override has no eligible response: ${id}`);
    setHeightStyle(area.node, override.heightPx);
  }

  controls.undo.onclick = undo;
  controls.redo.onclick = redo;
  controls.resetPage.onclick = () => resetPage(activePageId);
  controls.export.onclick = () => downloadJson(exportedDraft(), `${casePackage.id}_ACCESSIBLE_LAYOUT_CHANGES.json`);
  controls.apply.onclick = openApplyPreview;
  controls.cancel.onclick = () => controls.dialog.close();
  controls.confirm.onclick = () => void applySelected().catch(error => console.error(error));
  controls.staleExport.onclick = () => downloadJson({ schemaVersion: 1, staleDrafts: staleDrafts.map(item => item.value) }, `${casePackage.id}_STALE_ACCESSIBLE_LAYOUT_DRAFTS.json`);
  controls.staleDiscard.onclick = () => {
    for (const item of staleDrafts) localStorage.removeItem(item.key);
    staleDrafts = [];
    renderStale();
  };

  try {
    const response = await fetch("/__authoring/context", { cache: "no-store" });
    if (response.ok) repositoryContext = await response.json();
  } catch { /* read-only static hosting keeps preview/export available */ }
  loadDrafts();
  validateAll();
  render();

  return {
    getAreas: () => [...areas.values()].map(area => ({ ...definitionView(area), heightPx: currentHeight(area) })),
    getPending: () => cloneRecord(capturePending()),
    getDraftKey: () => draftKey,
    getRepositoryContext: () => repositoryContext ? { ...repositoryContext } : null,
    setHeight: (id, height) => updateArea(areas.get(id), height, "test"),
    resizeByPointer: (id, screenDelta, renderedScale) => {
      const area = areas.get(id);
      return updateArea(area, currentHeight(area) + sourcePixelsFromPointer(screenDelta, renderedScale), "pointer");
    },
    resetArea: id => resetArea(areas.get(id)),
    resetPage,
    undo,
    redo,
    validateAll,
    exportValue: exportedDraft,
    sourcePixelsFromPointer,
    sanitizeClone(clone) {
      clone.querySelectorAll(AUTHORING_SELECTOR).forEach(node => node.remove());
      for (const area of areas.values()) {
        const node = clone.querySelector(`[data-persist-id="${CSS.escape(area.persistId)}"]`);
        if (!node) continue;
        setHeightStyle(node, manifest.overrides[area.id]?.heightPx ?? null);
        node.removeAttribute("data-layout-resizable");
        node.removeAttribute("data-layout-validation");
      }
    },
    cleanInnerHTML(node) {
      const clone = node.cloneNode(true);
      clone.querySelectorAll(AUTHORING_SELECTOR).forEach(item => item.remove());
      return clone.innerHTML;
    },
    destroy() {
      for (const area of areas.values()) area.handle.remove();
      panel.hidden = true;
    }
  };
}

function definitionView(area) {
  const { node, handle, ...value } = area;
  return value;
}
