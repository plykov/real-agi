/* ============================================================
   Zuurdesem — interactions
   - 3D parallax hero (mouse + scroll driven)
   - tilt-on-hover cards
   - scroll reveals + animated counters
   - nav state + scroll progress
   ============================================================ */

(function () {
  "use strict";

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const layers = Array.from(document.querySelectorAll(".layer"));

  /* ---------- HERO PARALLAX (mouse + scroll) ---------- */
  // each layer has data-depth (mouse strength) and data-scroll (scroll strength).
  let pointerX = 0, pointerY = 0;   // -0.5 .. 0.5
  let scrollY = 0;

  function applyParallax() {
    for (const layer of layers) {
      const depth = parseFloat(layer.dataset.depth || "0");
      const scrollK = parseFloat(layer.dataset.scroll || "0");
      const mx = pointerX * depth * 60;          // px shift from mouse
      const my = pointerY * depth * 45;
      const sy = scrollY * scrollK * 0.35;       // px shift from scroll
      const tz = depth * 60;                     // real Z depth for the 3D feel
      layer.style.transform =
        `translate3d(${mx}px, ${my - sy}px, ${tz}px) rotateX(${pointerY * depth * -6}deg) rotateY(${pointerX * depth * 8}deg)`;
    }
  }

  if (!reduceMotion) {
    window.addEventListener("mousemove", (e) => {
      pointerX = e.clientX / window.innerWidth - 0.5;
      pointerY = e.clientY / window.innerHeight - 0.5;
      requestAnimationFrame(applyParallax);
    }, { passive: true });

    // touch tilt for mobile
    window.addEventListener("deviceorientation", (e) => {
      if (e.gamma == null || e.beta == null) return;
      pointerX = Math.max(-0.5, Math.min(0.5, e.gamma / 45));
      pointerY = Math.max(-0.5, Math.min(0.5, (e.beta - 45) / 45));
      requestAnimationFrame(applyParallax);
    }, { passive: true });
  }

  /* ---------- SCROLL: progress bar, nav, hero parallax ---------- */
  const progress = document.getElementById("scrollProgress");
  const nav = document.getElementById("nav");
  const heroHeight = () => document.querySelector(".hero").offsetHeight;

  function onScroll() {
    scrollY = window.scrollY;
    const docH = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = (scrollY / docH) * 100 + "%";
    if (nav) nav.classList.toggle("is-scrolled", scrollY > 40);
    if (!reduceMotion && scrollY < heroHeight()) applyParallax();
  }
  window.addEventListener("scroll", () => requestAnimationFrame(onScroll), { passive: true });
  onScroll();

  /* ---------- TILT CARDS ---------- */
  if (!reduceMotion) {
    document.querySelectorAll("[data-tilt]").forEach((card) => {
      card.addEventListener("mousemove", (e) => {
        const r = card.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width - 0.5;
        const py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform =
          `rotateY(${px * 12}deg) rotateX(${py * -12}deg) translateY(-6px)`;
      });
      card.addEventListener("mouseleave", () => {
        card.style.transform = "";
      });
    });
  }

  /* ---------- SCROLL REVEALS ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
          countUp(entry.target);
        }
      });
    }, { threshold: 0.16 });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  /* ---------- ANIMATED COUNTERS ---------- */
  function countUp(scope) {
    scope.querySelectorAll("[data-count]").forEach((el) => {
      const target = parseInt(el.dataset.count, 10);
      if (reduceMotion) { el.textContent = target; return; }
      const duration = 1400;
      const start = performance.now();
      function tick(now) {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased);
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  }
})();
