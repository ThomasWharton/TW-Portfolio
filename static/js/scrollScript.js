document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".nav-link");
    const navbarToggler = document.querySelector(".navbar-toggler");

    navLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
        const targetId = this.getAttribute("href");
        const targetSection = document.querySelector(targetId);

        if (targetSection) {
        event.preventDefault(); // Prevent default anchor behavior

        // Close navbar on small screens
        if (window.innerWidth < 786) {
            navbarToggler.click();
        }

        const collapseElement = targetSection.querySelector(".collapse");

        if (collapseElement) {
          // If section is collapsed, expand it first
            if (!collapseElement.classList.contains("show")) {
            const bsCollapse = new bootstrap.Collapse(collapseElement, {
                toggle: true,
            });

            // Wait for collapse animation to complete before scrolling
            collapseElement.addEventListener(
                "shown.bs.collapse",
                function () {
                smoothScroll(targetSection);
            },
              { once: true } // Ensure it only fires once
            );
            } else {
            // If already expanded, just scroll
            smoothScroll(targetSection);
            }
        } else {
          // If no collapsible content, just scroll
            smoothScroll(targetSection);
        }
        }
    });
    });

    function smoothScroll(section) {
        const targetPosition =
        section.offsetTop - document.querySelector(".navbar").offsetHeight;
        window.scrollTo({ top: targetPosition, behavior: "smooth" });
    }
});
