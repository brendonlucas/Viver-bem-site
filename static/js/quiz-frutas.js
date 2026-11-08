/* Interação da página do Quiz das Frutas */
document.addEventListener("DOMContentLoaded", () => {
  const questions = [...document.querySelectorAll(".question")];
  const form = document.getElementById("fruitQuiz");
  if (!questions.length || !form) return;
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const finishBtn = document.getElementById("finishBtn");
  const counter = document.getElementById("questionCounter");
  const percent = document.getElementById("progressPercent");
  const progressBar = document.getElementById("progressBar");
  const progressTrack = document.getElementById("progressTrack");
  let current = 0;
  let advanceTimer;

  function updateScreen() {
    questions.forEach((question, index) => {
      const active = index === current;
      question.classList.toggle("active", active);
      question.setAttribute("aria-hidden", String(!active));
    });
    const total = questions.length;
    const percentage = Math.round(((current + 1) / total) * 100);
    counter.textContent = `Pergunta ${current + 1} de ${total}`;
    percent.textContent = `${percentage}%`;
    progressBar.style.width = `${percentage}%`;
    progressTrack.setAttribute("aria-valuenow", percentage);
    prevBtn.disabled = current === 0;
    nextBtn.hidden = current === total - 1;
    finishBtn.hidden = current !== total - 1;
  }

  function currentAnswered() {
    return Boolean(questions[current].querySelector('input[type="radio"]:checked'));
  }
  function showValidationMessage() {
    const input = questions[current].querySelector('input[type="radio"]');
    input.setCustomValidity("Escolha uma alternativa para continuar.");
    input.reportValidity();
    input.setCustomValidity("");
  }

  nextBtn.addEventListener("click", () => {
    if (!currentAnswered()) return showValidationMessage();
    if (current < questions.length - 1) { current++; updateScreen(); }
  });
  prevBtn.addEventListener("click", () => {
    if (current > 0) { current--; updateScreen(); }
  });

  questions.forEach(question => {
    question.querySelectorAll('input[type="radio"]').forEach(input => {
      input.addEventListener("change", () => {
        window.clearTimeout(advanceTimer);
        if (current < questions.length - 1) {
          advanceTimer = window.setTimeout(() => {
            if (input.checked && current === Number(question.dataset.index)) {
              current++;
              updateScreen();
            }
          }, 220);
        }
      });
    });
  });

  form.addEventListener("submit", event => {
    const unanswered = questions.findIndex(question =>
      !question.querySelector('input[type="radio"]:checked')
    );
    if (unanswered !== -1) {
      event.preventDefault();
      current = unanswered;
      updateScreen();
      showValidationMessage();
    }
  });
  updateScreen();
});
