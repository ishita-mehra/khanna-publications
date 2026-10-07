/* ============ Navbar scroll ============ */
const header = document.getElementById('site-header');
const onScroll = () => header?.classList.toggle('scrolled', window.scrollY > 20);
onScroll();
window.addEventListener('scroll', onScroll, { passive: true });

/* ============ Mobile menu ============ */
const toggle = document.getElementById('menu-toggle');
const menu = document.getElementById('mobile-menu');
let menuOpen = false;

toggle?.addEventListener('click', () => {
  menuOpen = !menuOpen;
  menu.style.maxHeight = menuOpen ? menu.scrollHeight + 'px' : '0px';
});
document.querySelectorAll('#mobile-menu a').forEach(a =>
  a.addEventListener('click', () => {
    menuOpen = false;
    menu.style.maxHeight = '0px';
  })
);

/* ============ Reveal on scroll ============ */
const io = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      }
    });
  },
  { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
);
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

/* ============ Binding option pills ============ */
document.querySelectorAll('.opt-pill').forEach((pill) => {
  pill.addEventListener('click', () => {
    pill.parentElement
      .querySelectorAll('.opt-pill')
      .forEach((p) => p.classList.remove('opt-active'));
    pill.classList.add('opt-active');
  });
});

/* ============ Smooth anchor scroll ============ */
document.querySelectorAll('a[href*="#"]').forEach((link) => {
  link.addEventListener('click', (e) => {
    const href = link.getAttribute('href');
    if (!href.includes('#')) return;
    const id = '#' + href.split('#')[1];
    if (id === '#' || id.length < 2) return;
    const target = document.querySelector(id);
    if (!target) return;
    e.preventDefault();
    const y = target.getBoundingClientRect().top + window.scrollY - 84;
    window.scrollTo({ top: y, behavior: 'smooth' });
  });
});

/* ============ Order button → WhatsApp ============ */
/* TODO: replace the empty string below with the real number (e.g. "919876543210") */
const WHATSAPP_NUMBER = "";
const WA_BASE = WHATSAPP_NUMBER ? `https://wa.me/${WHATSAPP_NUMBER}` : "https://wa.me/";

document.querySelectorAll('.order-btn').forEach((btn) => {
  btn.addEventListener('click', () => {
    const product = btn.dataset.product || 'a product';
    const text = `Hi Khanna Notebooks! I'd like to order: ${product}. Here are my customization details:`;
    const url = `${WA_BASE}?text=${encodeURIComponent(text)}`;
    window.open(url, '_blank', 'noopener');
  });
});