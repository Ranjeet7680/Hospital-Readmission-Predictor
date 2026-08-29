/**
 * HRP Clinical Enterprise Client Library & Global Toast System v5.0
 * Hospital Readmission Predictor & CareAI Platform
 */

// Global Toast Notification System
window.showToast = function(message, type = 'info', duration = 3800) {
    let container = document.getElementById('hrp-toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'hrp-toast-container';
        container.className = 'fixed top-5 right-5 z-[9999] flex flex-col gap-2.5 pointer-events-none max-w-sm w-full px-4';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'pointer-events-auto flex items-start gap-3 p-3.5 rounded-2xl shadow-2xl border backdrop-blur-xl transition-all duration-300 transform translate-y-[-20px] opacity-0 text-xs font-medium';

    let icon = 'info';
    let bgStyle = 'background: rgba(255, 255, 255, 0.96); border-color: rgba(0, 91, 191, 0.2); color: #003366;';
    let iconColor = '#005bbf';

    if (type === 'success') {
        icon = 'check_circle';
        bgStyle = 'background: rgba(240, 253, 244, 0.98); border-color: rgba(34, 197, 94, 0.35); color: #14532d;';
        iconColor = '#16a34a';
    } else if (type === 'error' || type === 'emergency') {
        icon = 'error';
        bgStyle = 'background: rgba(254, 242, 242, 0.98); border-color: rgba(239, 68, 68, 0.35); color: #7f1d1d;';
        iconColor = '#dc2626';
    } else if (type === 'warning') {
        icon = 'warning';
        bgStyle = 'background: rgba(254, 252, 232, 0.98); border-color: rgba(234, 179, 8, 0.35); color: #713f12;';
        iconColor = '#ca8a04';
    }

    toast.setAttribute('style', bgStyle);
    toast.innerHTML = `
        <span class="material-symbols-outlined text-[20px] shrink-0" style="color: ${iconColor};">${icon}</span>
        <div class="flex-1 pr-2">
            <p class="leading-relaxed font-semibold">${message}</p>
        </div>
        <button onclick="this.parentElement.remove()" class="shrink-0 p-1 hover:opacity-75 transition-opacity text-slate-400 hover:text-slate-700">
            <span class="material-symbols-outlined text-[16px]">close</span>
        </button>
    `;

    container.appendChild(toast);

    // Animate In
    requestAnimationFrame(() => {
        toast.classList.remove('translate-y-[-20px]', 'opacity-0');
        toast.classList.add('translate-y-0', 'opacity-100');
    });

    // Auto Dismiss
    setTimeout(() => {
        toast.classList.add('translate-y-[-10px]', 'opacity-0');
        setTimeout(() => toast.remove(), 300);
    }, duration);
};

// Global Sound Engine
window.soundEngine = {
    playTone(freq = 440, type = 'sine', duration = 0.1) {
        try {
            const AudioCtx = window.AudioContext || window.webkitAudioContext;
            if (!AudioCtx) return;
            const ctx = new AudioCtx();
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = type;
            osc.frequency.setValueAtTime(freq, ctx.currentTime);
            gain.gain.setValueAtTime(0.08, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start();
            osc.stop(ctx.currentTime + duration);
        } catch(e) {}
    },
    click() { this.playTone(600, 'triangle', 0.05); },
    success() {
        this.playTone(523.25, 'sine', 0.08);
        setTimeout(() => this.playTone(659.25, 'sine', 0.12), 80);
    },
    error() {
        this.playTone(300, 'sawtooth', 0.15);
    },
    uploadComplete() {
        this.playTone(440, 'sine', 0.06);
        setTimeout(() => this.playTone(880, 'sine', 0.1), 60);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    console.log("HRP Clinical v5.0 Enterprise Core Loaded.");
});
