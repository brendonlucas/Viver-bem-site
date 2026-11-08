/* Interações opcionais do catálogo de quizzes */
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-coming-soon]").forEach(link => {
    link.addEventListener("click", event => {
      if (link.getAttribute("href") === "#quiz-habitos") {
        event.preventDefault();
        const status = link.closest(".quiz-catalog-card")?.querySelector(".quiz-status");
        if (status) status.textContent = "Conteúdo em preparação";
      }
    });
  });
});
