document.addEventListener("DOMContentLoaded", function () {
const navLinks = document.querySelectorAll(".nav-link");
const navbarToggler = document.querySelector(".navbar-toggler");
const navbarCollapse = document.querySelector(".navbar-collapse");

navLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
    // Only apply custom scrolling on small screens (when navbar-toggler is visible)
    if (window.innerWidth < 786) {
        event.preventDefault(); // Prevent default anchor link behavior
        
        const targetId = this.getAttribute("href"); // Get the target section ID
        const targetSection = document.querySelector(targetId);

        if (targetSection) {
        navbarToggler.click(); // Close the menu
        
        // Wait for the menu to fully collapse before scrolling
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
