document.addEventListener('DOMContentLoaded', () => {
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navList = document.querySelector('.nav-list');

    if (mobileNavToggle) {
        mobileNavToggle.addEventListener('click', () => {
            navList.classList.toggle('active');
            mobileNavToggle.classList.toggle('active');
        });
    }

    // Close mobile menu when a link is clicked
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navList.classList.contains('active')) {
                navList.classList.remove('active');
                mobileNavToggle.classList.remove('active');
            }
        });
    });
});
