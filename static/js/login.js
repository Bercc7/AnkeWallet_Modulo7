const passwordInput = document.getElementById("password");
const togglePasswordBtn = document.getElementById("togglePassword");

togglePasswordBtn.addEventListener("click", () => {
  const isPassword = passwordInput.type === "password";
  passwordInput.type = isPassword ? "text" : "password";
  togglePasswordBtn.textContent = isPassword ? "Ocultar" : "Mostrar";
  togglePasswordBtn.setAttribute("aria-pressed", String(isPassword));
  togglePasswordBtn.setAttribute(
    "aria-label",
    isPassword ? "Ocultar contraseña" : "Mostrar contraseña"
  );
});