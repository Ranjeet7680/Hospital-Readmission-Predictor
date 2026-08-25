/**
 * Precision Clinical Animation & Physics Easing Engine
 * Hospital Readmission Predictor (HRP Clinical)
 * Supports Spring Physics, Staggered Reveals, Gauge Sweeps, and Zero-Jank 60FPS CSS Transitions.
 */

class AnimationEngine {
    constructor() {
        this.reduceMotion = localStorage.getItem('hrp_reduce_motion') === 'true';
    }

    init() {
        if (this.reduceMotion) {
            document.documentElement.classList.add('reduce-motion');
        }
        this.initCountUps();
        this.initGauges();
        this.initScrollReveal();
        this.initButtonMicroInteractions();
        this.initCardHoverPhysics();
    }

    setReduceMotion(enabled) {
        this.reduceMotion = enabled;
        localStorage.setItem('hrp_reduce_motion', enabled ? 'true' : 'false');
        if (enabled) {
            document.documentElement.classList.add('reduce-motion');
        } else {
            document.documentElement.classList.remove('reduce-motion');
        }
    }

    /**
     * Staggered Scroll Observer for Cards and KPI Panels
     */
    initScrollReveal() {
        if (this.reduceMotion) return;
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, idx) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-revealed');
                    entry.target.style.transitionDelay = `${(idx % 4) * 60}ms`;
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.animate-on-scroll, .patient-card, .kpi-card, .metric-card').forEach(el => {
            el.classList.add('reveal-init');
            observer.observe(el);
        });
    }

    /**
     * Interactive Button Micro-Interactions & Acoustic Click Binding
     */
    initButtonMicroInteractions() {
        document.querySelectorAll('button, a.btn, [role="button"]').forEach(btn => {
            btn.addEventListener('mousedown', () => {
                if (!this.reduceMotion) {
                    btn.style.transform = 'scale(0.97)';
                }
            });
            btn.addEventListener('mouseup', () => {
                if (!this.reduceMotion) {
                    btn.style.transform = '';
                }
            });
            btn.addEventListener('mouseleave', () => {
                if (!this.reduceMotion) {
                    btn.style.transform = '';
                }
            });
        });
    }

    /**
     * Card Elevation & Hover Physics
     */
    initCardHoverPhysics() {
        if (this.reduceMotion) return;
        document.querySelectorAll('.hover-lift, .patient-card, .bento-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transition = 'transform 250ms cubic-bezier(0.16, 1, 0.3, 1), box-shadow 250ms ease';
                card.style.transform = 'translateY(-3px)';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0)';
            });
        });
    }

    /**
     * Physics-Calibrated Count-Up for Telemetry & Risk Numbers
     */
    initCountUps() {
        if (this.reduceMotion) return;
        document.querySelectorAll('[data-countup]').forEach(el => {
            const target = parseFloat(el.getAttribute('data-countup'));
            if (isNaN(target)) return;
            const isPct = el.getAttribute('data-is-pct') === 'true';
            const decimals = parseInt(el.getAttribute('data-decimals') || '0');
            const duration = 1200;
            const start = 0;
            const startTime = performance.now();

            const update = (now) => {
                const elapsed = now - startTime;
                const progress = Math.min(elapsed / duration, 1);
                // Ease-out cubic with slight deceleration
                const easeProgress = 1 - Math.pow(1 - progress, 3.5);
                const current = start + (target - start) * easeProgress;

                if (isPct) {
                    el.textContent = current.toFixed(decimals) + '%';
                } else if (decimals > 0) {
                    el.textContent = current.toFixed(decimals);
                } else {
                    el.textContent = Math.round(current).toLocaleString();
                }

                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                    el.textContent = isPct ? target.toFixed(decimals) + '%' : (decimals > 0 ? target.toFixed(decimals) : Math.round(target).toLocaleString());
                }
            };
            requestAnimationFrame(update);
        });
    }

    /**
     * Smooth Radial Gauge Sweep
     */
    initGauges() {
        document.querySelectorAll('.gauge-circle-animated, #gauge-circle').forEach(el => {
            const offset = parseFloat(el.getAttribute('data-dashoffset') || el.style.strokeDashoffset || '0');
            if (this.reduceMotion) {
                el.style.strokeDashoffset = offset;
            } else {
                el.style.transition = 'stroke-dashoffset 1.4s cubic-bezier(0.16, 1, 0.3, 1)';
                setTimeout(() => {
                    el.style.strokeDashoffset = offset;
                }, 100);
            }
        });
    }

    /**
     * Neural Particle Canvas Simulator (High-Contrast 60FPS)
     */
    animateNeuralFlow(canvasId) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        
        const resize = () => {
            const rect = canvas.getBoundingClientRect();
            canvas.width = rect.width || canvas.parentElement?.clientWidth || 600;
            canvas.height = rect.height || canvas.parentElement?.clientHeight || 190;
        };
        resize();
        window.addEventListener('resize', resize);

        const layers = [4, 6, 6, 2];
        const nodes = [];

        const updateNodes = () => {
            nodes.length = 0;
            const width = canvas.width;
            const height = canvas.height;
            layers.forEach((count, lIdx) => {
                const layerX = (lIdx / (layers.length - 1)) * (width - 80) + 40;
                for (let i = 0; i < count; i++) {
                    const nodeY = ((i + 0.5) / count) * (height - 40) + 20;
                    nodes.push({ x: layerX, y: nodeY, layer: lIdx });
                }
            });
        };
        updateNodes();

        const particles = [];
        for (let i = 0; i < 24; i++) {
            particles.push({
                fromLayer: 0,
                progress: Math.random(),
                speed: 0.008 + Math.random() * 0.009,
                fromNode: Math.floor(Math.random() * layers[0]),
                toNode: Math.floor(Math.random() * layers[1])
            });
        }

        const render = () => {
            if (this.reduceMotion) return;
            const width = canvas.width;
            const height = canvas.height;
            ctx.clearRect(0, 0, width, height);

            // Connective Synapse Lines
            ctx.strokeStyle = 'rgba(56, 189, 248, 0.2)';
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

            // Flowing AI Pulses (Glowing Cyan & Amber)
            particles.forEach(p => {
                p.progress += p.speed;
                if (p.progress >= 1) {
                    p.progress = 0;
                    p.fromLayer = (p.fromLayer + 1) % (layers.length - 1);
                    const currentLayerNodes = nodes.filter(n => n.layer === p.fromLayer);
                    const nextLayerNodes = nodes.filter(n => n.layer === p.fromLayer + 1);
                    p.fromNodeCoord = currentLayerNodes[Math.floor(Math.random() * currentLayerNodes.length)];
                    p.toNodeCoord = nextLayerNodes[Math.floor(Math.random() * nextLayerNodes.length)];
                }

                if (p.fromNodeCoord && p.toNodeCoord) {
                    const px = p.fromNodeCoord.x + (p.toNodeCoord.x - p.fromNodeCoord.x) * p.progress;
                    const py = p.fromNodeCoord.y + (p.toNodeCoord.y - p.fromNodeCoord.y) * p.progress;
                    ctx.fillStyle = '#22d3ee';
                    ctx.shadowColor = '#00d2ff';
                    ctx.shadowBlur = 8;
                    ctx.beginPath();
                    ctx.arc(px, py, 3.5, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }
            });

            // Neural Nodes
            nodes.forEach(node => {
                ctx.fillStyle = '#0284c7';
                ctx.beginPath();
                ctx.arc(node.x, node.y, 4.5, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth = 1.5;
                ctx.stroke();
            });

            requestAnimationFrame(render);
        };
        render();
    }
}

window.animationEngine = new AnimationEngine();
document.addEventListener('DOMContentLoaded', () => {
    window.animationEngine.init();
});
