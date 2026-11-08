/* Interações da página Seu Bem-estar */
document.addEventListener("DOMContentLoaded", () => {
  const checklist = document.querySelector("[data-habit-checklist]");
  if (checklist) {
    const boxes = [...checklist.querySelectorAll('input[type="checkbox"]')];
    const counter = checklist.querySelector("[data-checklist-count]");
    const update = () => {
      if (counter) counter.textContent = `${boxes.filter(box => box.checked).length} hábitos marcados`;
    };
    boxes.forEach(box => box.addEventListener("change", update));
    update();
  }

  document.querySelectorAll("[data-wellbeing-answer]").forEach(button => {
    button.addEventListener("click", () => {
      const feedback = button.closest("[data-wellbeing-quiz]")?.querySelector(".feedback");
      if (!feedback) return;
      feedback.textContent = button.dataset.wellbeingAnswer === "correct"
        ? "Isso mesmo. Conversar com um adulto de confiança pode ajudar a encontrar apoio."
        : "Pense em uma atitude segura: não é preciso enfrentar sentimentos difíceis sozinho.";
      feedback.setAttribute("role", "status");
    });
  });
});
