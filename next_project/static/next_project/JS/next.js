document.addEventListener("DOMContentLoaded", () => {

    // --- Utility: get CSRF token from cookie ---
    const getCookie = name => {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
        return '';
    };

    // 1. Reverse header
    const header = document.querySelector("h1.color");
    if (header) {
        header.addEventListener("click", () => {
            header.textContent = header.textContent.split("").reverse().join("");
        });
    }
});
