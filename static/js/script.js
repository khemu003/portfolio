// Smooth fade-in animations on scroll
document.addEventListener('DOMContentLoaded', () => {
    const faders = document.querySelectorAll('.fade-in, .fade-in-delay, .zoom-in');
    const options = {
        threshold: 0.2,
    };

    const appearOnScroll = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('appear');
            observer.unobserve(entry.target);
        });
    }, options);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});
