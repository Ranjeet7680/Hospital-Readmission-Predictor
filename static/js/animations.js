/**
 * Premium Animation & Interaction Utilities
 * Hospital Readmission Predictor (HRP Clinical)
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

    initCountUps() {
        if (this.reduceMotion) return;
        document.querySelectorAll('[data-countup]').forEach(el => {
            const target = parseFloat(el.getAttribute('data-countup'));
            const isPct = el.getAttribute('data-is-pct') === 'true';
            const decimals = parseInt(el.getAttribute('data-decimals') || '0');
            const duration = 1200;
            const start = 0;
            const startTime = performance.now();

            const update = (now) => {
                const elapsed = now - startTime;
                const progress = Math.min(elapsed / duration, 1);
                // Ease-out cubic
                const easeProgress = 1 - Math.pow(1 - progress, 3);
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
                }
            };
            requestAnimationFrame(update);
        });
    }

    initGauges() {
        document.querySelectorAll('.gauge-circle-animated').forEach(el => {
            const offset = parseFloat(el.getAttribute('data-dashoffset') || '0');
            if (this.reduceMotion) {
                el.style.strokeDashoffset = offset;
            } else {
                setTimeout(() => {
                    el.style.strokeDashoffset = offset;
                }, 150);
            }
        });
    }

    animateNeuralFlow(canvasId) {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        let width = canvas.width = canvas.parentElement.clientWidth || 400;
        let height = canvas.height = canvas.parentElement.clientHeight || 180;

        const layers = [4, 6, 6, 2];
        const nodes = [];

        // Build node coords
        layers.forEach((count, lIdx) => {
            const layerX = (lIdx / (layers.length - 1)) * (width - 60) + 30;
            for (let i = 0; i < count; i++) {
                const nodeY = ((i + 0.5) / count) * (height - 40) + 20;
                nodes.push({ x: layerX, y: nodeY, layer: lIdx });
            }
        });

        const particles = [];
        for (let i = 0; i < 16; i++) {
            particles.push({
                fromLayer: 0,
                progress: Math.random(),
                speed: 0.008 + Math.random() * 0.006,
                fromNode: Math.floor(Math.random() * layers[0]),
                toNode: Math.floor(Math.random() * layers[1])
            });
        }

        const render = () => {
            if (this.reduceMotion) return;
            ctx.clearRect(0, 0, width, height);

            // Draw connection lines
            ctx.strokeStyle = '#dde0e6';
            ctx.lineWidth = 1;
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

            // Draw animated particles
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
                    ctx.fillStyle = '#005bbf';
                    ctx.beginPath();
                    ctx.arc(px, py, 3, 0, Math.PI * 2);
                    ctx.fill();
                }
            });

            // Draw nodes
            nodes.forEach(node => {
                ctx.fillStyle = '#1a73e8';
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
