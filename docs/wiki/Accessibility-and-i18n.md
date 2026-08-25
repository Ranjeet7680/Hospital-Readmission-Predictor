# Accessibility & Internationalization (i18n)

HRP Clinical is built to ensure universal accessibility, contrast compliance, and real-time multi-lingual clinical understanding.

---

## 1. Bilingual Engine: English ↔ हिन्दी

Implemented in `static/js/i18n.js`:
- Client-side reactive translation engine scanning `data-i18n` attributes across all DOM elements.
- Instant switching without page reloads.
- Translates navigation links, risk badges, clinical recommendations, lab explanations, and telemedicine captions.

---

## 2. Accessibility & Reduced Motion

Implemented in `static/js/animations.js` and `templates/settings.html`:
- **Reduce-Motion Toggle**: Disables SVG gauge spinning, pulse effects, and neural net background canvas when activated.
- **High-Contrast Google Material 3 Palette**: Complies with WCAG 2.1 AA color contrast standards.
- **ARIA Tags & Keyboard Navigation**: Full keyboard tab navigation support across forms, modals, and prediction wizards.
