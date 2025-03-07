document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".nav-link");
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navLinks.forEach((link) => {
        link.addEventListener("click", function (event) {
        const targetId = this.getAttribute("href"); // Get the target section ID
        const targetSection = document.querySelector(targetId);

        if (targetSection) {
            // If section has a collapsible element, open it
            const collapseElement = targetSection.querySelector(".collapse");
            if (collapseElement && !collapseElement.classList.contains("show")) {
            new bootstrap.Collapse(collapseElement, {
                toggle: true,
            });
            }

            // Only apply custom scrolling on small screens
            if (window.innerWidth < 786) {
            event.preventDefault(); // Prevent default anchor link behavior
            navbarToggler.click(); // Close the menu

            setTimeout(() => {
                const navbarHeight = document.querySelector(".navbar").offsetHeight;
                const targetPosition = targetSection.offsetTop - navbarHeight;

                window.scrollTo({
                top: targetPosition,
                behavior: "smooth",
                });
            }, 300); // Delay scrolling slightly to allow menu to close
            }
        }
        });
    });
});
