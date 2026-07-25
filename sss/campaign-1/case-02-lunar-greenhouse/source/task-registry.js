/**
 * Space Sprout Sleuth — Campaign 1, Case 02
 * Canonical task registry
 *
 * Student and Accessible headings, Teacher cross-references, Answer Key
 * headings, controlled Markdown, and regression tests must use these exact
 * identifiers and visible titles.
 */

export const CASE_ID = "SSS-C1-CASE02";
export const CASE_SLUG = "case-02-lunar-greenhouse";
export const CASE_TITLE = "Lunar Greenhouse";
export const STUDENT_IDENTITY = "Process Modeler";
export const REGISTRY_VERSION = "1.0";

export const TASKS = Object.freeze([
  Object.freeze({ id: 1, slug: "vocabulary", title: "Vocabulary", keyable: false, answerKeyParts: Object.freeze([]) }),
  Object.freeze({ id: 2, slug: "initial-thinking", title: "Initial thinking", keyable: false, answerKeyParts: Object.freeze([]) }),
  Object.freeze({ id: 3, slug: "model-the-pollination-sequence", title: "Model the pollination sequence", keyable: true, answerKeyParts: Object.freeze(["completed-process-model"]) }),
  Object.freeze({ id: 4, slug: "identify-the-failed-step", title: "Identify the failed step", keyable: true, answerKeyParts: Object.freeze(["failed-step", "case-evidence", "downstream-effect"]) }),
  Object.freeze({ id: 5, slug: "test-the-competing-explanations", title: "Test the competing explanations", keyable: true, answerKeyParts: Object.freeze(["competing-explanations"]) }),
  Object.freeze({ id: 6, slug: "diagnose-and-reject-an-alternative", title: "Diagnose and reject an alternative", keyable: true, answerKeyParts: Object.freeze(["diagnosis", "rejected-alternative"]) }),
  Object.freeze({ id: 7, slug: "claim-evidence-reasoning", title: "Claim-Evidence-Reasoning", keyable: true, answerKeyParts: Object.freeze(["claim", "evidence", "reasoning"]) }),
  Object.freeze({ id: 8, slug: "design-a-reliable-pollination-support", title: "Design a reliable pollination support", keyable: true, answerKeyParts: Object.freeze(["design", "criterion", "constraint", "mechanism-check"]) }),
  Object.freeze({ id: 9, slug: "exit-ticket", title: "Exit ticket", keyable: true, answerKeyParts: Object.freeze(["exit-ticket"]) }),
]);

export const ANSWER_KEY_TASK_IDS = Object.freeze(TASKS.filter((task) => task.keyable).map((task) => task.id));

export function getTask(taskId) {
  const id = Number(taskId);
  const task = TASKS.find((entry) => entry.id === id);
  if (!task) throw new RangeError(`Unknown ${CASE_ID} task id: ${String(taskId)}`);
  return task;
}

export function taskLabel(taskId) {
  const task = getTask(taskId);
  return `${task.id} · ${task.title}`;
}

export function getAnswerKeyTasks() {
  return TASKS.filter((task) => task.keyable);
}

export function validateTaskRegistry() {
  const errors = [];
  const ids = TASKS.map((task) => task.id);
  const slugs = TASKS.map((task) => task.slug);
  if (new Set(ids).size !== TASKS.length) errors.push("Task ids must be unique.");
  if (new Set(slugs).size !== TASKS.length) errors.push("Task slugs must be unique.");
  TASKS.forEach((task, index) => {
    const expectedId = index + 1;
    if (task.id !== expectedId) errors.push(`Task sequence error: expected ${expectedId}, found ${task.id}.`);
    if (!task.title.trim()) errors.push(`Task ${task.id} must have a title.`);
    if (task.keyable && task.answerKeyParts.length === 0) errors.push(`Task ${task.id} is keyable but has no Answer Key parts.`);
    if (!task.keyable && task.answerKeyParts.length !== 0) errors.push(`Task ${task.id} is not keyable but declares Answer Key parts.`);
  });
  const expectedAnswerIds = [3, 4, 5, 6, 7, 8, 9];
  if (ANSWER_KEY_TASK_IDS.length !== expectedAnswerIds.length || expectedAnswerIds.some((id, index) => id !== ANSWER_KEY_TASK_IDS[index])) {
    errors.push("Answer Key task ids must remain 3, 4, 5, 6, 7, 8, 9.");
  }
  return Object.freeze({ valid: errors.length === 0, errors: Object.freeze(errors) });
}

const registryCheck = validateTaskRegistry();
if (!registryCheck.valid) throw new Error(`Invalid ${CASE_ID} task registry:
- ${registryCheck.errors.join("
- ")}`);
