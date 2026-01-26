document.addEventListener("DOMContentLoaded", function () {
    console.log("AUTH JS LOADED ✅");

    // Password toggle logic (login + register)
    const passwordFields = document.querySelectorAll(".password-field");

    passwordFields.forEach(field => {
        const input = field.querySelector("input[type='password'], input[type='text']");
        const toggle = field.querySelector(".password-toggle");

        if (input && toggle) {
            toggle.addEventListener("click", function () {
                const type = input.getAttribute("type") === "password" ? "text" : "password";
                input.setAttribute("type", type);

                const icon = toggle.querySelector("i");
                if (icon) {
                    icon.classList.toggle("fa-eye");
                    icon.classList.toggle("fa-eye-slash");
                }
            });
        }
    });
});