const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");
const navLinks = document.querySelectorAll(".nav-menu a");
const revealItems = document.querySelectorAll(".reveal");
const counters = document.querySelectorAll("[data-counter]");
const contactForm = document.querySelector("#contactForm");
const formStatus = document.querySelector("#formStatus");
const cursorDot = document.querySelector(".cursor-dot");
const canvas = document.querySelector("#heroCanvas");
const ctx = canvas.getContext("2d");

let particles = [];
let hasCounted = false;

navToggle.addEventListener("click", () => {
  const isOpen = navMenu.classList.toggle("open");
  navToggle.setAttribute("aria-expanded", String(isOpen));
});

navLinks.forEach((link) => {
  link.addEventListener("click", () => {
    navMenu.classList.remove("open");
    navToggle.setAttribute("aria-expanded", "false");
  });
});

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  { threshold: 0.18 }
);

revealItems.forEach((item) => revealObserver.observe(item));

const counterObserver = new IntersectionObserver(
  (entries) => {
    if (hasCounted) return;

    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        hasCounted = true;
        counters.forEach(animateCounter);
      }
    });
  },
  { threshold: 0.5 }
);

if (counters.length > 0) {
  counterObserver.observe(counters[0]);
}

function animateCounter(counter) {
  const target = Number(counter.dataset.counter);
  const duration = 1200;
  const start = performance.now();

  function update(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    counter.textContent = Math.round(target * eased);

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

window.addEventListener("scroll", () => {
  const scrollPosition = window.scrollY + 120;

  navLinks.forEach((link) => {
    const section = document.querySelector(link.getAttribute("href"));
    if (!section) return;

    const top = section.offsetTop;
    const bottom = top + section.offsetHeight;
    link.classList.toggle("active", scrollPosition >= top && scrollPosition < bottom);
  });
});

contactForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(contactForm);
  const name = String(formData.get("name")).trim();
  const email = String(formData.get("email")).trim();
  const project = String(formData.get("project")).trim();
  const message = String(formData.get("message")).trim();

  if (!name || !email || !project || !message) {
    formStatus.textContent = "Completa todos los campos para enviar tu consulta.";
    formStatus.style.color = "#ef4444";
    return;
  }

  formStatus.textContent = "Mensaje preparado. Puedes conectar este formulario a EmailJS, Formspree o tu backend.";
  formStatus.style.color = "#9cc2ff";
  contactForm.reset();
});

window.addEventListener("pointermove", (event) => {
  if (!cursorDot) return;
  cursorDot.style.left = `${event.clientX}px`;
  cursorDot.style.top = `${event.clientY}px`;
});

document.querySelectorAll("a, button, input, select, textarea").forEach((element) => {
  element.addEventListener("pointerenter", () => {
    if (!cursorDot) return;
    cursorDot.style.width = "34px";
    cursorDot.style.height = "34px";
  });

  element.addEventListener("pointerleave", () => {
    if (!cursorDot) return;
    cursorDot.style.width = "18px";
    cursorDot.style.height = "18px";
  });
});

function resizeCanvas() {
  const ratio = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  canvas.width = Math.floor(rect.width * ratio);
  canvas.height = Math.floor(rect.height * ratio);
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  createParticles(rect.width, rect.height);
}

function createParticles(width, height) {
  const particleCount = Math.min(72, Math.floor(width / 18));

  particles = Array.from({ length: particleCount }, () => ({
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (Math.random() - 0.5) * 0.45,
    vy: (Math.random() - 0.5) * 0.45,
    radius: Math.random() * 2 + 1,
  }));
}

function drawCanvas() {
  const width = canvas.clientWidth;
  const height = canvas.clientHeight;

  ctx.clearRect(0, 0, width, height);

  const gradient = ctx.createLinearGradient(0, 0, width, height);
  gradient.addColorStop(0, "#070b14");
  gradient.addColorStop(0.45, "#0c1424");
  gradient.addColorStop(1, "#071b1d");
  ctx.fillStyle = gradient;
  ctx.fillRect(0, 0, width, height);

  particles.forEach((particle) => {
    particle.x += particle.vx;
    particle.y += particle.vy;

    if (particle.x < 0 || particle.x > width) particle.vx *= -1;
    if (particle.y < 0 || particle.y > height) particle.vy *= -1;

    ctx.beginPath();
    ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(79, 140, 255, 0.36)";
    ctx.fill();
  });

  for (let i = 0; i < particles.length; i += 1) {
    for (let j = i + 1; j < particles.length; j += 1) {
      const dx = particles[i].x - particles[j].x;
      const dy = particles[i].y - particles[j].y;
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance < 125) {
        ctx.beginPath();
        ctx.moveTo(particles[i].x, particles[i].y);
        ctx.lineTo(particles[j].x, particles[j].y);
        ctx.strokeStyle = `rgba(40, 217, 196, ${0.2 - distance / 850})`;
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }
  }

  requestAnimationFrame(drawCanvas);
}

resizeCanvas();
drawCanvas();
window.addEventListener("resize", resizeCanvas);
