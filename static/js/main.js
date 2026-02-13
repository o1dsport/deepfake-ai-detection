// =============================
// CUSTOM SMOOTH CURSOR
// =============================
const cursor = document.querySelector('.cursor');
let mouseX = 0;
let mouseY = 0;
let posX = 0;
let posY = 0;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

function animateCursor() {
    posX += (mouseX - posX) * 0.15;
    posY += (mouseY - posY) * 0.15;
    cursor.style.left = posX + "px";
    cursor.style.top = posY + "px";
    requestAnimationFrame(animateCursor);
}

animateCursor();

// Grow cursor on hover
document.querySelectorAll('a, button, input').forEach(el => {
    el.addEventListener('mouseenter', () => {
        cursor.style.transform = "scale(2)";
        cursor.style.background = "orange";
    });
    el.addEventListener('mouseleave', () => {
        cursor.style.transform = "scale(1)";
        cursor.style.background = "transparent";
    });
});


// =============================
// RIPPLE CLICK EFFECT
// =============================
document.addEventListener('click', function(e) {
    const ripple = document.createElement('span');
    ripple.classList.add("ripple");
    ripple.style.left = e.clientX + 'px';
    ripple.style.top = e.clientY + 'px';
    document.body.appendChild(ripple);

    setTimeout(() => {
        ripple.remove();
    }, 700);
});


// =============================
// GSAP HERO ANIMATION
// =============================
gsap.from(".hero-title", {
    y: -120,
    opacity: 0,
    duration: 1.5,
    ease: "power4.out"
});

gsap.from(".hero-subtitle", {
    opacity: 0,
    delay: 0.8,
    duration: 1.5
});

gsap.from(".hero-btn", {
    opacity: 0,
    delay: 1.2,
    duration: 1.2
});


// =============================
// SECTION FADE IN ON SCROLL
// =============================
gsap.utils.toArray(".section").forEach(section => {
    gsap.from(section, {
        scrollTrigger: {
            trigger: section,
            start: "top 80%"
        },
        y: 80,
        opacity: 0,
        duration: 1.2,
        ease: "power3.out"
    });
});


// =============================
// SMOOTH SCROLL
// =============================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});


// =============================
// MAGNETIC BUTTON EFFECT
// =============================
document.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("mousemove", function(e) {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        btn.style.transform = `translate(${x * 0.2}px, ${y * 0.2}px)`;
    });

    btn.addEventListener("mouseleave", function() {
        btn.style.transform = "translate(0px, 0px)";
    });
});
