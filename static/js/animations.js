/**
 * Precision Clinical Animation & Physics Engine v3.0
 * Hospital Readmission Predictor (HRP Clinical)
 *
 * Features:
 *  - Spring-physics scroll reveals with stagger
 *  - Material Design 3 ripple effects
 *  - 3D perspective card tilt on mouse move
 *  - Slim page progress loader bar
 *  - Bouncy count-up with overshoot spring easing
 *  - Smooth gauge sweeps with halo ring
 *  - Neural particle canvas
 *  - Mobile swipe-to-close drawer
 */

class AnimationEngine {
    constructor() {
        this.reduceMotion = localStorage.getItem('hrp_reduce_motion') === 'true';
        this._pageLoaderTimer = null;
    }

    /* ──────────────────────────────────────────────
       INIT
    ────────────────────────────────────────────── */
    init() {
        if (this.reduceMotion) {
            document.documentElement.classList.add('reduce-motion');
        }
        this.injectPageLoader();
        this.initCountUps();
        this.initGauges();
        this.initScrollReveal();
        this.initButtonMicroInteractions();
        this.initCardHoverPhysics();
        this.initRipple();
        this.initMobileSwipeDrawer();
        this.initMobileBottomNavPill();
        this.initPageTransitionLinks();
    }

    setReduceMotion(enabled) {
        this.reduceMotion = enabled;
        localStorage.setItem('hrp_reduce_motion', enabled ? 'true' : 'false');
        document.documentElement.classList.toggle('reduce-motion', enabled);
    }

    /* ──────────────────────────────────────────────
       PAGE PROGRESS LOADER BAR
    ────────────────────────────────────────────── */
    injectPageLoader() {
        if (document.getElementById('page-progress-bar')) return;
        const bar = document.createElement('div');
        bar.id = 'page-progress-bar';
        document.body.prepend(bar);
    }

    startPageLoader() {
        if (this.reduceMotion) return;
        const bar = document.getElementById('page-progress-bar');
        if (!bar) return;
        bar.style.opacity = '1';
        bar.style.width = '0%';
        clearTimeout(this._pageLoaderTimer);

        // Quick jump to 30%, then slow crawl to 85%
        requestAnimationFrame(() => {
            bar.style.transition = 'width 300ms ease';
            bar.style.width = '30%';
            setTimeout(() => {
                bar.style.transition = 'width 4s cubic-bezier(0.1, 0, 0.2, 1)';
                bar.style.width = '85%';
            }, 320);
        });
    }

    finishPageLoader() {
        const bar = document.getElementById('page-progress-bar');
        if (!bar) return;
        bar.style.transition = 'width 250ms ease, opacity 350ms ease 200ms';
        bar.style.width = '100%';
        this._pageLoaderTimer = setTimeout(() => {
            bar.style.opacity = '0';
            setTimeout(() => { bar.style.width = '0%'; }, 400);
        }, 250);
    }

    initPageTransitionLinks() {
        if (this.reduceMotion) return;
        document.querySelectorAll('a[href]:not([target="_blank"]):not([href^="#"]):not([href^="mailto"])').forEach(link => {
            link.addEventListener('click', (e) => {
                const href = link.getAttribute('href');
                if (!href || href === '#' || href.startsWith('javascript')) return;
                this.startPageLoader();
            });
        });

        // Finish on DOM ready
        window.addEventListener('load', () => this.finishPageLoader());
        // Also finish on DOMContentLoaded in case 'load' already fired
        if (document.readyState === 'complete') this.finishPageLoader();
    }

    /* ──────────────────────────────────────────────
       MATERIAL DESIGN 3 RIPPLE
    ────────────────────────────────────────────── */
    initRipple() {
        const targets = document.querySelectorAll(
            'button, a.btn, [role="button"], .ripple-container, nav a, .mobile-nav-item'
        );
        targets.forEach(el => this._attachRipple(el));
    }

    _attachRipple(el) {
        // Avoid duplicate listeners
        if (el.dataset.rippleInit) return;
        el.dataset.rippleInit = 'true';

        if (!el.style.position || el.style.position === 'static') {
            el.style.position = 'relative';
        }
        el.style.overflow = 'hidden';

        el.addEventListener('pointerdown', (e) => {
            if (this.reduceMotion) return;
            const rect = el.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height) * 2;
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top  - size / 2;

            const wave = document.createElement('span');
            wave.className = 'ripple-wave';
            wave.style.cssText = `
                width:${size}px; height:${size}px;
                left:${x}px; top:${y}px;
            `;
            el.appendChild(wave);
            wave.addEventListener('animationend', () => wave.remove());
        });
    }

    /* ──────────────────────────────────────────────
       3D PERSPECTIVE CARD TILT
    ────────────────────────────────────────────── */
    initCardHoverPhysics() {
        if (this.reduceMotion) return;

        // Standard lift cards
        document.querySelectorAll('.hover-lift, .patient-card, .bento-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transition = 'transform 250ms cubic-bezier(0.16,1,0.3,1), box-shadow 250ms ease';
                card.style.transform = 'translateY(-4px)';
                card.style.boxShadow = '0 8px 30px rgba(0,91,191,0.12), 0 2px 8px rgba(0,0,0,0.06)';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0)';
                card.style.boxShadow = '';
            });
        });

        // 3D tilt cards
        document.querySelectorAll('.tilt-card, .kpi-card, .metric-card').forEach(card => {
            const MAX_TILT = 6; // degrees

            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const cx = rect.left + rect.width  / 2;
                const cy = rect.top  + rect.height / 2;
                const dx = (e.clientX - cx) / (rect.width  / 2);
                const dy = (e.clientY - cy) / (rect.height / 2);
                const rx = -dy * MAX_TILT;
                const ry =  dx * MAX_TILT;

                card.style.transition = 'transform 80ms linear, box-shadow 80ms linear';
                card.style.transform = `perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-3px)`;
                card.style.boxShadow = `
                    ${-ry * 1.5}px ${rx * 1.5}px 32px rgba(0,91,191,0.13),
                    0 2px 8px rgba(0,0,0,0.07)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transition = 'transform 400ms cubic-bezier(0.16,1,0.3,1), box-shadow 400ms ease';
                card.style.transform = 'perspective(800px) rotateX(0) rotateY(0) translateY(0)';
                card.style.boxShadow = '';
            });

            // Attach ripple too
            this._attachRipple(card);
        });
    }

    /* ──────────────────────────────────────────────
       STAGGERED SPRING SCROLL REVEAL
    ────────────────────────────────────────────── */
    initScrollReveal() {
        if (this.reduceMotion) return;

        const observer = new IntersectionObserver((entries) => {
            // Group all intersecting entries for stagger
            const visible = entries.filter(e => e.isIntersecting);
            visible.forEach((entry, idx) => {
                const delay = idx * 55; // 55ms stagger
                setTimeout(() => {
                    entry.target.classList.add('is-revealed');
                }, delay);
                observer.unobserve(entry.target);
            });
        }, { threshold: 0.08, rootMargin: '0px 0px -24px 0px' });

        document.querySelectorAll(
            '.animate-on-scroll, .patient-card, .kpi-card, .metric-card, .bento-card'
        ).forEach(el => {
            el.classList.add('reveal-init');
            observer.observe(el);
        });
    }

    /* ──────────────────────────────────────────────
       BUTTON MICRO-INTERACTIONS
    ────────────────────────────────────────────── */
    initButtonMicroInteractions() {
        document.querySelectorAll('button, a.btn, [role="button"]').forEach(btn => {
            btn.addEventListener('mousedown', () => {
                if (!this.reduceMotion) btn.style.transform = 'scale(0.96)';
            });
            ['mouseup', 'mouseleave'].forEach(evt => {
                btn.addEventListener(evt, () => {
                    if (!this.reduceMotion) btn.style.transform = '';
                });
            });
        });
    }

    /* ──────────────────────────────────────────────
       BOUNCY SPRING COUNT-UP (with overshoot)
    ────────────────────────────────────────────── */
    initCountUps() {
        if (this.reduceMotion) return;

        document.querySelectorAll('[data-countup]').forEach(el => {
            const target   = parseFloat(el.getAttribute('data-countup'));
            if (isNaN(target)) return;
            const isPct    = el.getAttribute('data-is-pct') === 'true';
            const decimals = parseInt(el.getAttribute('data-decimals') || '0');
            const duration = 1400;
            const startTime = performance.now();

            // Spring overshoot easing: goes slightly past target then settles
            const springEase = (t) => {
                const c4 = (2 * Math.PI) / 2.8;
                return t === 0 ? 0 : t === 1 ? 1
                    : Math.pow(2, -9 * t) * Math.sin((t * 10 - 0.75) * c4) + 1;
            };

            const update = (now) => {
                const t = Math.min((now - startTime) / duration, 1);
                const easedT = springEase(t);
                const current = target * easedT;

                el.textContent = isPct
                    ? current.toFixed(decimals) + '%'
                    : decimals > 0
                        ? current.toFixed(decimals)
                        : Math.max(0, Math.round(current)).toLocaleString();

                if (t < 1) {
                    requestAnimationFrame(update);
                } else {
                    el.textContent = isPct
                        ? target.toFixed(decimals) + '%'
                        : decimals > 0 ? target.toFixed(decimals) : Math.round(target).toLocaleString();
                }
            };
            requestAnimationFrame(update);
        });
    }

    /* ──────────────────────────────────────────────
       SMOOTH RADIAL GAUGE SWEEP
    ────────────────────────────────────────────── */
    initGauges() {
        document.querySelectorAll('.gauge-circle-animated, #gauge-circle').forEach(el => {
            const offset = parseFloat(
                el.getAttribute('data-dashoffset') || el.style.strokeDashoffset || '0'
            );
            if (this.reduceMotion) {
                el.style.strokeDashoffset = offset;
            } else {
                el.style.strokeDashoffset = '283';
                el.style.transition = 'stroke-dashoffset 1.4s cubic-bezier(0.16, 1, 0.3, 1)';
                requestAnimationFrame(() => {
                    setTimeout(() => { el.style.strokeDashoffset = offset; }, 100);
                });
            }
        });
    }

    /* ──────────────────────────────────────────────
       MOBILE SWIPE-TO-CLOSE DRAWER
    ────────────────────────────────────────────── */
    initMobileSwipeDrawer() {
        const drawer  = document.getElementById('mobile-drawer');
        const overlay = document.getElementById('mobile-drawer-overlay');
        if (!drawer || !overlay) return;

        let startX = 0;
        let currentX = 0;
        let isDragging = false;

        drawer.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            isDragging = true;
            drawer.style.transition = 'none';
        }, { passive: true });

        drawer.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            currentX = e.touches[0].clientX;
            const delta = Math.min(0, currentX - startX); // only allow left swipe
            drawer.style.transform = `translateX(${delta}px)`;
            // Fade overlay proportionally
            const progress = Math.abs(delta) / drawer.offsetWidth;
            overlay.style.opacity = 1 - progress;
        }, { passive: true });

        drawer.addEventListener('touchend', () => {
            isDragging = false;
            drawer.style.transition = '';
            const delta = currentX - startX;
            if (delta < -80) {
                // Close
                if (typeof closeMobileDrawer === 'function') closeMobileDrawer();
            } else {
                // Snap back
                drawer.style.transform = 'translateX(0)';
                overlay.style.opacity = '1';
            }
        });
    }

    /* ──────────────────────────────────────────────
       MOBILE BOTTOM NAV ACTIVE PILL ANIMATION
    ────────────────────────────────────────────── */
    initMobileBottomNavPill() {
        const activeItems = document.querySelectorAll('.mobile-nav-active-item');
        activeItems.forEach(item => {
            // Ensure pill indicator exists
            if (!item.querySelector('.mobile-nav-pill')) {
                const pill = document.createElement('span');
                pill.className = 'mobile-nav-pill';
                item.style.position = 'relative';
                item.appendChild(pill);
            }
        });
    }

    /* ──────────────────────────────────────────────
       NEURAL PARTICLE CANVAS SIMULATOR
    ────────────────────────────────────────────── */
    animateNeuralFlow(canvasId) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');

        const resize = () => {
            const rect = canvas.getBoundingClientRect();
            canvas.width  = rect.width  || canvas.parentElement?.clientWidth  || 600;
            canvas.height = rect.height || canvas.parentElement?.clientHeight || 190;
        };
        resize();
        window.addEventListener('resize', resize);

        const layers = [4, 6, 6, 2];
        const nodes  = [];

        const updateNodes = () => {
            nodes.length = 0;
            const { width, height } = canvas;
            layers.forEach((count, lIdx) => {
                const layerX = (lIdx / (layers.length - 1)) * (width - 80) + 40;
                for (let i = 0; i < count; i++) {
                    nodes.push({ x: layerX, y: ((i + 0.5) / count) * (height - 40) + 20, layer: lIdx });
                }
            });
        };
        updateNodes();

        const particles = [];
        for (let i = 0; i < 28; i++) {
            particles.push({
                fromLayer: 0,
                progress: Math.random(),
                speed: 0.007 + Math.random() * 0.009,
                fromNode: Math.floor(Math.random() * layers[0]),
                toNode: Math.floor(Math.random() * layers[1])
            });
        }

        const render = () => {
            if (this.reduceMotion) return;
            const { width, height } = canvas;
            ctx.clearRect(0, 0, width, height);

            // Synapse lines
            ctx.strokeStyle = 'rgba(56,189,248,0.18)';
            ctx.lineWidth = 1.2;
            for (let i = 0; i < nodes.length; i++) {
                for (let j = i + 1; j < nodes.length; j++) {
                    if (nodes[j].layer === nodes[i].layer + 1) {
                        ctx.beginPath();
                        ctx.moveTo(nodes[i].x, nodes[i].y);
                        ctx.lineTo(nodes[j].x, nodes[j].y);
                        ctx.stroke();
                    }
                }
            }

            // Flowing AI pulses
            particles.forEach(p => {
                p.progress += p.speed;
                if (p.progress >= 1) {
                    p.progress = 0;
                    p.fromLayer = (p.fromLayer + 1) % (layers.length - 1);
                    const cur  = nodes.filter(n => n.layer === p.fromLayer);
                    const next = nodes.filter(n => n.layer === p.fromLayer + 1);
                    p.fromNodeCoord = cur [Math.floor(Math.random() * cur.length)];
                    p.toNodeCoord   = next[Math.floor(Math.random() * next.length)];
                }
                if (p.fromNodeCoord && p.toNodeCoord) {
                    const px = p.fromNodeCoord.x + (p.toNodeCoord.x - p.fromNodeCoord.x) * p.progress;
                    const py = p.fromNodeCoord.y + (p.toNodeCoord.y - p.fromNodeCoord.y) * p.progress;

                    // Glow
                    const g = ctx.createRadialGradient(px, py, 0, px, py, 7);
                    g.addColorStop(0,   'rgba(34,211,238,0.9)');
                    g.addColorStop(1,   'rgba(34,211,238,0)');
                    ctx.fillStyle = g;
                    ctx.beginPath();
                    ctx.arc(px, py, 7, 0, Math.PI * 2);
                    ctx.fill();

                    ctx.fillStyle = '#22d3ee';
                    ctx.shadowColor = '#00d2ff';
                    ctx.shadowBlur = 8;
                    ctx.beginPath();
                    ctx.arc(px, py, 3, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }
            });

            // Nodes
            nodes.forEach(node => {
                const g = ctx.createRadialGradient(node.x, node.y, 0, node.x, node.y, 6);
                g.addColorStop(0, '#1a73e8');
                g.addColorStop(1, '#005bbf');
                ctx.fillStyle = g;
                ctx.beginPath();
                ctx.arc(node.x, node.y, 5, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = 'rgba(255,255,255,0.9)';
                ctx.lineWidth = 1.5;
                ctx.stroke();
            });

            requestAnimationFrame(render);
        };
        render();
    }

    /* ──────────────────────────────────────────────
       TOAST NOTIFICATION HELPER
    ────────────────────────────────────────────── */
    showToast(message, type = 'info', duration = 3500) {
        const colors = {
            info:    'bg-primary text-white',
            success: 'bg-green-600 text-white',
            warning: 'bg-amber-500 text-slate-900',
            error:   'bg-red-600 text-white',
        };
        const icons = { info: 'info', success: 'check_circle', warning: 'warning', error: 'error' };

        const container = document.getElementById('toast-container') || (() => {
            const c = document.createElement('div');
            c.id = 'toast-container';
            c.className = 'fixed bottom-20 md:bottom-6 right-4 z-[9999] flex flex-col gap-2 items-end';
            document.body.appendChild(c);
            return c;
        })();

        const toast = document.createElement('div');
        toast.className = `flex items-center gap-2.5 px-4 py-3 rounded-2xl shadow-xl text-sm font-semibold
            max-w-xs ${colors[type] || colors.info} animate-slide-up`;
        toast.innerHTML = `
            <span class="material-symbols-outlined text-[18px]">${icons[type] || 'info'}</span>
            <span>${message}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
            toast.style.transition = 'opacity 300ms, transform 300ms';
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(12px)';
            setTimeout(() => toast.remove(), 320);
        }, duration);
    }
}

window.animationEngine = new AnimationEngine();
document.addEventListener('DOMContentLoaded', () => {
    window.animationEngine.init();
});

// Expose showToast globally for convenience
window.showToast = (msg, type, duration) => window.animationEngine.showToast(msg, type, duration);

// Global graceful override of native window.alert to use modern Toast notifications
window.alert = function(msg) {
    if (typeof msg === 'string') {
        const lower = msg.toLowerCase();
        let type = 'info';
        if (lower.includes('success') || lower.includes('verified') || lower.includes('saved') || lower.includes('approved')) type = 'success';
        else if (lower.includes('error') || lower.includes('failed') || lower.includes('invalid') || lower.includes('deleted')) type = 'error';
        else if (lower.includes('warning') || lower.includes('pending') || lower.includes('caution')) type = 'warning';
        window.showToast(msg, type);
    } else {
        window.showToast(String(msg), 'info');
    }
};

// Global event delegation for click ripple & button press on dynamically created elements
document.addEventListener('pointerdown', (e) => {
    const btn = e.target.closest('button, a.btn, [role="button"], .btn-action');
    if (!btn || window.animationEngine.reduceMotion) return;
    
    // Scale effect
    btn.style.transform = 'scale(0.96)';
    const reset = () => { btn.style.transform = ''; cleanup(); };
    const cleanup = () => {
        btn.removeEventListener('pointerup', reset);
        btn.removeEventListener('pointerleave', reset);
        btn.removeEventListener('pointercancel', reset);
    };
    btn.addEventListener('pointerup', reset);
    btn.addEventListener('pointerleave', reset);
    btn.addEventListener('pointercancel', reset);

    // Ripple effect
    if (!btn.style.position || btn.style.position === 'static') {
        btn.style.position = 'relative';
    }
    btn.style.overflow = 'hidden';

    const rect = btn.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height) * 2;
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top  - size / 2;

    const wave = document.createElement('span');
    wave.className = 'ripple-wave';
    wave.style.cssText = `width:${size}px; height:${size}px; left:${x}px; top:${y}px;`;
    btn.appendChild(wave);
    wave.addEventListener('animationend', () => wave.remove());
});

// Interactive Confetti & Celebration Particle Burst
window.triggerCelebration = function() {
    if (window.animationEngine && window.animationEngine.reduceMotion) return;
    const colors = ['#005bbf', '#0284c7', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899'];
    for (let i = 0; i < 40; i++) {
        const p = document.createElement('div');
        p.style.position = 'fixed';
        p.style.top = '20%';
        p.style.left = `${Math.random() * 80 + 10}%`;
        p.style.width = `${Math.random() * 8 + 4}px`;
        p.style.height = `${Math.random() * 8 + 4}px`;
        p.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        p.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
        p.style.zIndex = '99999';
        p.style.pointerEvents = 'none';
        p.style.transform = 'translateY(0) rotate(0deg)';
        p.style.transition = `transform ${Math.random() * 1.5 + 1}s cubic-bezier(0.25, 1, 0.5, 1), opacity 1s ease`;
        document.body.appendChild(p);

        requestAnimationFrame(() => {
            const xDelta = (Math.random() - 0.5) * 300;
            const yDelta = Math.random() * 500 + 150;
            p.style.transform = `translate(${xDelta}px, ${yDelta}px) rotate(${Math.random() * 720}deg)`;
            p.style.opacity = '0';
        });

        setTimeout(() => p.remove(), 2500);
    }
};

