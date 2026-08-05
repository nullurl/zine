const state = {
  skills: [],
  selectedSkill: null,
  filter: "visual",
  query: "",
  references: [],
  activeJob: null,
  pollTimer: null,
  currentPromptUrl: null,
  toastTimer: null,
};

const el = {};

document.addEventListener("DOMContentLoaded", () => {
  for (const id of [
    "serviceState", "serviceLabel", "skillPanel", "skillDrawerButton", "closeDrawerButton", "drawerScrim",
    "skillSearch", "skillFilters", "skillCount", "skillList", "selectedSkillName", "selectedSkillDescription",
    "referenceInput", "dropZone", "referenceGrid", "referenceCount", "referenceSkillButton", "selectedSkillIcon",
    "briefInput", "briefCount", "generateButton",
    "jobSection", "jobMessage", "cancelButton", "progressBar", "jobStatus", "jobProgress", "resultActions",
    "resultStage", "emptyResult", "resultImage", "promptButton", "downloadButton", "historyList",
    "refreshHistoryButton", "promptDialog", "closePromptButton", "promptText", "copyPromptButton", "toast",
  ]) el[id] = document.getElementById(id);

  bindEvents();
  Promise.all([loadHealth(), loadSkills(), loadHistory()]).catch((error) => showToast(error.message, true));
});

function bindEvents() {
  el.skillSearch.addEventListener("input", () => {
    state.query = el.skillSearch.value.trim().toLowerCase();
    renderSkills();
  });
  el.skillFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-filter]");
    if (!button) return;
    state.filter = button.dataset.filter;
    el.skillFilters.querySelectorAll("button").forEach((item) => item.classList.toggle("active", item === button));
    renderSkills();
  });
  el.skillDrawerButton.addEventListener("click", openDrawer);
  el.closeDrawerButton.addEventListener("click", closeDrawer);
  el.drawerScrim.addEventListener("click", closeDrawer);
  el.dropZone.addEventListener("click", () => el.referenceInput.click());
  el.referenceInput.addEventListener("change", () => addFiles(el.referenceInput.files));
  ["dragenter", "dragover"].forEach((name) => el.dropZone.addEventListener(name, (event) => {
    event.preventDefault();
    el.dropZone.classList.add("dragover");
  }));
  ["dragleave", "drop"].forEach((name) => el.dropZone.addEventListener(name, (event) => {
    event.preventDefault();
    el.dropZone.classList.remove("dragover");
  }));
  el.dropZone.addEventListener("drop", (event) => addFiles(event.dataTransfer.files));
  el.referenceSkillButton.addEventListener("click", openSkillList);
  el.briefInput.addEventListener("input", () => { el.briefCount.textContent = el.briefInput.value.length; });
  el.generateButton.addEventListener("click", startGeneration);
  el.cancelButton.addEventListener("click", cancelGeneration);
  el.refreshHistoryButton.addEventListener("click", loadHistory);
  el.promptButton.addEventListener("click", showPrompt);
  el.closePromptButton.addEventListener("click", () => el.promptDialog.close());
  el.copyPromptButton.addEventListener("click", copyPrompt);
  el.promptDialog.addEventListener("click", (event) => {
    if (event.target === el.promptDialog) el.promptDialog.close();
  });
}

async function api(path, options = {}) {
  const response = await fetch(path, options);
  let body;
  try { body = await response.json(); } catch { body = null; }
  if (!response.ok) throw new Error(body?.error || `请求失败 (${response.status})`);
  return body;
}

async function loadHealth() {
  try {
    const health = await api("/api/health");
    el.serviceState.classList.toggle("online", health.configured);
    el.serviceState.classList.toggle("error", !health.configured);
    el.serviceLabel.textContent = health.configured ? `${health.image_model} · 就绪` : "服务端未配置";
  } catch {
    el.serviceState.classList.add("error");
    el.serviceLabel.textContent = "服务不可用";
  }
}

async function loadSkills() {
  const data = await api("/api/skills");
  state.skills = data.skills || [];
  state.selectedSkill = null;
  renderSkills();
  renderSelectedSkill();
}

function filteredSkills() {
  return state.skills.filter((skill) => {
    const filterMatch = state.filter === "all"
      || (state.filter === "visual" && skill.visual)
      || (state.filter === "installed" && ["installed", "workspace"].includes(skill.source));
    const queryMatch = !state.query || `${skill.name} ${skill.description}`.toLowerCase().includes(state.query);
    return filterMatch && queryMatch;
  });
}

function renderSkills() {
  const skills = filteredSkills();
  el.skillCount.textContent = skills.length;
  el.skillList.replaceChildren();
  if (!skills.length) {
    const empty = document.createElement("div");
    empty.className = "list-empty";
    empty.textContent = "没有匹配的 Skill";
    el.skillList.append(empty);
    return;
  }
  const fragment = document.createDocumentFragment();
  skills.forEach((skill) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `skill-item${state.selectedSkill?.name === skill.name ? " active" : ""}`;
    button.setAttribute("role", "option");
    button.setAttribute("aria-selected", state.selectedSkill?.name === skill.name ? "true" : "false");
    const initials = skill.name.split("-").slice(0, 2).map((part) => part[0]).join("").toUpperCase();
    button.innerHTML = `
      <span class="skill-icon">${escapeHtml(initials)}</span>
      <span><span class="skill-name">${escapeHtml(skill.name)}</span><span class="skill-description">${escapeHtml(skill.description)}</span></span>
      <svg><use href="#i-chevron"/></svg>`;
    button.addEventListener("click", () => selectSkill(skill));
    fragment.append(button);
  });
  el.skillList.append(fragment);
}

function selectSkill(skill, { closeNavigation = true } = {}) {
  state.selectedSkill = skill;
  renderSkills();
  renderSelectedSkill();
  if (closeNavigation) closeDrawer();
}

function renderSelectedSkill() {
  const skill = state.selectedSkill;
  el.selectedSkillName.textContent = skill?.name || "尚未选择 Skill";
  el.selectedSkillDescription.textContent = skill?.description || "从 Skill Library 中选择本次生成使用的视觉工作流。";
  el.selectedSkillIcon.textContent = skill
    ? skill.name.split("-").slice(0, 2).map((part) => part[0]).join("").toUpperCase()
    : "SK";
  el.selectedSkillIcon.classList.toggle("active", Boolean(skill));
}

function openSkillList() {
  state.query = "";
  el.skillSearch.value = "";
  renderSkills();
  openDrawer();
  requestAnimationFrame(() => {
    el.skillList.querySelector(".skill-item.active")?.scrollIntoView({ block: "center" });
    el.skillSearch.focus({ preventScroll: true });
  });
}

function openDrawer() {
  el.skillPanel.classList.add("open");
  el.drawerScrim.classList.add("open");
}

function closeDrawer() {
  el.skillPanel.classList.remove("open");
  el.drawerScrim.classList.remove("open");
}

async function addFiles(fileList) {
  const available = 3 - state.references.length;
  const files = [...fileList].filter((file) => ["image/png", "image/jpeg", "image/webp"].includes(file.type));
  el.referenceInput.value = "";
  if (!available) return showToast("最多上传 3 张参考图", true);
  if (!files.length) return showToast("请选择 PNG、JPG 或 WEBP 图片", true);
  el.dropZone.disabled = true;
  try {
    const compressed = await Promise.all(files.slice(0, available).map(compressImage));
    state.references.push(...compressed);
    renderReferences();
    if (files.length > available) showToast(`已保留前 ${available} 张图片`);
  } catch (error) {
    showToast(error.message || "图片处理失败", true);
  } finally {
    el.dropZone.disabled = false;
  }
}

async function compressImage(file) {
  const bitmap = await createImageBitmap(file);
  const maxEdge = 1600;
  const scale = Math.min(1, maxEdge / Math.max(bitmap.width, bitmap.height));
  const width = Math.max(1, Math.round(bitmap.width * scale));
  const height = Math.max(1, Math.round(bitmap.height * scale));
  const canvas = document.createElement("canvas");
  canvas.width = width;
  canvas.height = height;
  const context = canvas.getContext("2d", { alpha: false });
  context.fillStyle = "#ffffff";
  context.fillRect(0, 0, width, height);
  context.drawImage(bitmap, 0, 0, width, height);
  bitmap.close();
  const data = canvas.toDataURL("image/jpeg", .88);
  if (estimateDataUrlBytes(data) > 8 * 1024 * 1024) throw new Error(`${file.name} 压缩后仍然过大`);
  return { name: file.name.slice(0, 120), data };
}

function estimateDataUrlBytes(data) {
  return Math.ceil((data.length - data.indexOf(",") - 1) * .75);
}

function renderReferences() {
  el.referenceCount.textContent = state.references.length;
  el.dropZone.hidden = state.references.length >= 3;
  el.referenceGrid.replaceChildren();
  state.references.forEach((reference, index) => {
    const item = document.createElement("div");
    item.className = "reference-item";
    item.innerHTML = `<img src="${reference.data}" alt="参考图 ${index + 1}"><span class="reference-name">${escapeHtml(reference.name)}</span><button type="button" aria-label="删除参考图" title="删除"><svg><use href="#i-trash"/></svg></button>`;
    item.querySelector("button").addEventListener("click", () => {
      state.references.splice(index, 1);
      renderReferences();
    });
    el.referenceGrid.append(item);
  });
}

async function startGeneration() {
  const brief = el.briefInput.value.trim();
  if (!state.references.length) {
    el.dropZone.focus();
    return showToast("请先上传参考素材", true);
  }
  if (!brief) {
    el.briefInput.focus();
    return showToast("请输入生成文案", true);
  }
  if (!state.selectedSkill) {
    openSkillList();
    return showToast("请从列表选择 Skill", true);
  }
  const size = document.querySelector('input[name="size"]:checked').value;
  const quality = document.querySelector('input[name="quality"]:checked').value;
  setGenerating(true);
  resetResult();
  try {
    const job = await api("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ skill: state.selectedSkill.name, brief, size, quality, images: state.references }),
    });
    state.activeJob = job;
    updateJob(job);
    pollJob(job.id);
  } catch (error) {
    setGenerating(false);
    showToast(error.message, true);
  }
}

function setGenerating(active) {
  el.generateButton.disabled = active;
  el.generateButton.querySelector("span").textContent = active ? "正在生成" : "开始生成";
  el.jobSection.hidden = !active;
}

async function pollJob(id) {
  clearTimeout(state.pollTimer);
  try {
    const job = await api(`/api/jobs/${id}`);
    if (state.activeJob?.id !== id) return;
    state.activeJob = job;
    updateJob(job);
    if (["completed", "failed", "cancelled"].includes(job.status)) return finishJob(job);
    state.pollTimer = setTimeout(() => pollJob(id), 1800);
  } catch (error) {
    setGenerating(false);
    showToast(error.message, true);
  }
}

function updateJob(job) {
  const progress = Number(job.progress || 0);
  el.jobMessage.textContent = localizeMessage(job.message);
  el.jobStatus.textContent = job.status;
  el.jobProgress.textContent = `${progress}%`;
  el.progressBar.style.width = `${progress}%`;
  el.cancelButton.hidden = !["queued", "running"].includes(job.status);
}

function localizeMessage(message) {
  const messages = {
    "Queued": "已进入队列",
    "Compiling Skill and references": "正在解析 Skill 与参考素材",
    "Saving generated image": "正在保存生成图",
    "Completed": "生成完成",
    "Cancelled": "已取消",
    "Generation failed": "生成失败",
  };
  return messages[message] || message || "处理中";
}

async function finishJob(job) {
  setGenerating(false);
  el.jobSection.hidden = false;
  if (job.status === "completed") {
    showResult(job);
    showToast("图片已生成");
    await loadHistory();
  } else if (job.status === "failed") {
    showToast(job.error || "生成失败", true);
  } else {
    showToast("任务已取消");
  }
}

async function cancelGeneration() {
  const id = state.activeJob?.id;
  if (!id) return;
  clearTimeout(state.pollTimer);
  try {
    const job = await api(`/api/jobs/${id}/cancel`, { method: "POST" });
    state.activeJob = job;
    updateJob({ ...job, progress: 100, message: "Cancelled" });
    setGenerating(false);
    el.jobSection.hidden = false;
  } catch (error) {
    showToast(error.message, true);
  }
}

function resetResult() {
  el.resultImage.hidden = true;
  el.resultImage.removeAttribute("src");
  el.emptyResult.hidden = false;
  el.resultActions.hidden = true;
  state.currentPromptUrl = null;
}

function showResult(item) {
  const cacheKey = encodeURIComponent(item.updated_at || Date.now());
  el.resultImage.src = `${item.result_url}?v=${cacheKey}`;
  el.resultImage.hidden = false;
  el.emptyResult.hidden = true;
  el.resultActions.hidden = false;
  el.downloadButton.href = item.result_url;
  el.downloadButton.download = `${item.skill || "zine-studio"}.png`;
  state.currentPromptUrl = item.prompt_url;
  el.resultStage.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

async function showPrompt() {
  if (!state.currentPromptUrl) return;
  try {
    const response = await fetch(state.currentPromptUrl);
    if (!response.ok) throw new Error("提示词读取失败");
    el.promptText.textContent = await response.text();
    el.promptDialog.showModal();
  } catch (error) {
    showToast(error.message, true);
  }
}

async function copyPrompt() {
  try {
    await navigator.clipboard.writeText(el.promptText.textContent);
    showToast("提示词已复制");
  } catch {
    showToast("无法访问剪贴板", true);
  }
}

async function loadHistory() {
  try {
    const data = await api("/api/history");
    renderHistory(data.items || []);
  } catch (error) {
    el.historyList.innerHTML = `<div class="history-empty">${escapeHtml(error.message)}</div>`;
  }
}

function renderHistory(items) {
  el.historyList.replaceChildren();
  if (!items.length) {
    el.historyList.innerHTML = '<div class="history-empty">暂无生成记录</div>';
    return;
  }
  items.slice(0, 8).forEach((item) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "history-item";
    const date = new Date(item.created_at).toLocaleString("zh-CN", { month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" });
    button.innerHTML = `<img src="${item.result_url}" alt=""><span><strong>${escapeHtml(item.skill || "Generated image")}</strong><span>${escapeHtml(date)} · ${escapeHtml(item.size || "")}</span></span><svg><use href="#i-chevron"/></svg>`;
    button.addEventListener("click", () => showResult(item));
    el.historyList.append(button);
  });
}

function showToast(message, error = false) {
  clearTimeout(state.toastTimer);
  el.toast.textContent = message;
  el.toast.classList.toggle("error", error);
  el.toast.classList.add("show");
  state.toastTimer = setTimeout(() => el.toast.classList.remove("show"), 3200);
}

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>'"]/g, (character) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;",
  })[character]);
}
