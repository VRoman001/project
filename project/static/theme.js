const html = document.documentElement;
const btn = document.getElementById("themeToggle");

// Зберігання у localStorage
if (localStorage.getItem("theme")) {
    html.setAttribute("data-theme", localStorage.getItem("theme"));
}

btn.addEventListener("click", () => {
    let current = html.getAttribute("data-theme");
    let newTheme = current === "dark" ? "light" : "dark";

    html.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
});
