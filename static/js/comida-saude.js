/* Interações da página Comida & Saúde */
document.addEventListener("DOMContentLoaded", () => {
  const quiz = document.querySelector("[data-hydration-quiz]");
  if (!quiz) return;
  const feedback = quiz.querySelector(".feedback");
  quiz.querySelectorAll("[data-answer]").forEach(button => {
    button.addEventListener("click", () => {
      const correct = button.dataset.answer === "correct";
      feedback.textContent = correct
        ? "Isso! A água é uma ótima escolha para hidratar o corpo."
        : "Tente novamente: pense na bebida indicada para a hidratação diária.";
      feedback.setAttribute("role", "status");
    });
  });
});
