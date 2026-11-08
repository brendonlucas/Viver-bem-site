/* Scripts compartilhados — Viver Bem de Verdade */
document.addEventListener("DOMContentLoaded", () => {
  // Marca o link de navegação da página atual quando o template usa aria-current="page".
  document.querySelectorAll('.navbar .nav-link[aria-current="page"]').forEach(link => {
    link.classList.add("active");
  });
});
