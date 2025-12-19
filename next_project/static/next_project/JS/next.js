document.addEventListener("DOMContentLoaded", () => {
  // --- Utility: get CSRF token from cookie ---
  const getCookie = (name) => {
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + "=")) {
        return decodeURIComponent(cookie.substring(name.length + 1));
      }
    }
    return "";
  };

  // 1. Reverse header
  const header = document.querySelector("h1.color");
  if (header) {
    header.addEventListener("click", () => {
      header.textContent = header.textContent.split("").reverse().join("");
    });
  }

  // 2. Nav toggle
  const toggleButton = document.getElementById("navToggle");
  const navLinks = document.getElementById("navLinks");

  if (toggleButton && navLinks) {
    toggleButton.addEventListener("click", () => {
      navLinks.classList.toggle("open");
    });
  }

  document.querySelectorAll(".reaction-btn").forEach((btn) => {
    btn.addEventListener("click", () => {

      if (!window.userAuthenticated) {
        alert("You must be logged in to like or dilike a comment.")
      }
      const commentId = btn.dataset.commentId;
      const reaction = btn.dataset.reaction;
      const csrftoken = getCookie("csrftoken");

      fetch(`/toggle-reaction/${commentId}/${reaction}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrftoken,
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) return;

          const bar = btn.closest(".reaction-bar");
          bar.querySelector(".like-count").textContent = data.likes;
          bar.querySelector(".dislike-count").textContent = data.dislikes;
        });
    });
  });

  // Translation dictionary
  const translations = {
    en: {
      about_title: "About Page",
      about_content: "This page tells you about our project",

      who_title: "Who we are",
      who_content: "This section tells you who we are",

      detail_title: "The details page",
      detail_content: "This is the page of details",

      login_title: "The login page",
      login_content: "This is the page lets you login",

      logout_title: "The logout page",
      logout_content: "This is the page lets you logout",

      confrim_logout_title: "Confirm logout page",
      confirm_logout_content: "This page confirms you want to logout",

      register_title: "The register page",
      register_content: "This is the page for registration",

      button: "Español",
    },
    es: {
      about_title: "Página sobre nosotros",
      about_content: "Esta página te cuenta sobre nuestro proyecto",

      who_title: "De quiénes somos",
      who_content: "Esta sección te dice quiénes somos",

      detail_title: "La pagina de detalles",
      detail_content: "Este es la pagina de detalles",

      login_title: "La pagina de iniciar",
      login_content: "Este es la pagina para permitarse iniciar",

      logout_title: "La pagina de cerrar",
      logout_content: "Este es la pagina para permitarse cerrar",

      confrim_logout_title: "La pagina para confirmerse cerrar",
      confirm_logout_content:
        "Este pagina es para permitirse cerrar la seccion",

      register_title: "La pagina de registracion",
      register_content: "Este es la pagina para registracion",

      button: "English",
    },
  };

  function updatePageLanguage(lang) {
    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      if (translations[lang][key]) {
        el.textContent = translations[lang][key];
      }
    });
  }

  let currentLang = "en";

  document.getElementById("switch-lang").addEventListener("click", () => {
    currentLang = currentLang === "en" ? "es" : "en";
    updatePageLanguage(currentLang);
  });
});
