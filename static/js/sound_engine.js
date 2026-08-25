/**
 * Web Audio API Sound Synthesizer for Hospital Readmission Predictor (HRP Clinical)
 * Pure client-side Web Audio API - Zero external audio file dependencies, zero latency.
 */

class SoundEngine {
    constructor() {
        this.audioCtx = null;
        this.muted = localStorage.getItem('hrp_sound_muted') === 'true';
        this.soundMode = localStorage.getItem('hrp_sound_mode') || 'all'; // 'all', 'essential', 'muted'
        this.volume = parseFloat(localStorage.getItem('hrp_sound_vol') || '0.35');
    }

    init() {
        if (!this.audioCtx) {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (AudioContext) {
                this.audioCtx = new AudioContext();
            }
        }
        if (this.audioCtx && this.audioCtx.state === 'suspended') {
            this.audioCtx.resume();
        }
    }

    setMuted(mute) {
        this.muted = mute;
        localStorage.setItem('hrp_sound_muted', mute ? 'true' : 'false');
    }

    setMode(mode) {
        this.soundMode = mode;
        localStorage.setItem('hrp_sound_mode', mode);
        if (mode === 'muted') this.setMuted(true);
        else this.setMuted(false);
    }

    playTone(freq, type = 'sine', duration = 0.1, gainVal = 0.2, delay = 0) {
        if (this.muted || this.soundMode === 'muted') return;
        this.init();
        if (!this.audioCtx) return;

        setTimeout(() => {
            try {
                const osc = this.audioCtx.createOscillator();
                const gain = this.audioCtx.createGain();

                osc.type = type;
                osc.frequency.setValueAtTime(freq, this.audioCtx.currentTime);

                const finalGain = gainVal * this.volume;
                gain.gain.setValueAtTime(finalGain, this.audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.0001, this.audioCtx.currentTime + duration);

                osc.connect(gain);
                gain.connect(this.audioCtx.destination);

                osc.start(this.audioCtx.currentTime);
                osc.stop(this.audioCtx.currentTime + duration);
            } catch (e) {
                console.warn('Audio play error:', e);
            }
        }, delay * 1000);
    }

    // 1. Button Press (Short soft click)
    click() {
        if (this.soundMode === 'essential') return;
        this.playTone(800, 'triangle', 0.04, 0.15);
    }

    // 2. Success (Harmonic two-tone chime)
    success() {
        this.playTone(523.25, 'sine', 0.12, 0.25, 0);       // C5
        this.playTone(659.25, 'sine', 0.20, 0.25, 0.09);    // E5
        this.playTone(783.99, 'sine', 0.35, 0.25, 0.18);    // G5
    }

    // 3. Error / Warning (Soft low-frequency alert)
    error() {
        this.playTone(280, 'sawtooth', 0.15, 0.20, 0);
        this.playTone(220, 'sawtooth', 0.25, 0.20, 0.12);
    }

    // 4. Upload Complete (Short pleasant chord)
    uploadComplete() {
        this.playTone(440, 'sine', 0.1, 0.2, 0);
        this.playTone(554.37, 'sine', 0.15, 0.2, 0.08);
        this.playTone(659.25, 'sine', 0.25, 0.2, 0.16);
    }

    // 5. Prediction Complete (Professional non-alarming completion chime)
    predictionReady() {
        this.playTone(392.00, 'sine', 0.15, 0.25, 0);     // G4
        this.playTone(523.25, 'sine', 0.18, 0.25, 0.10);    // C5
        this.playTone(659.25, 'sine', 0.30, 0.30, 0.20);    // E5
        this.playTone(1046.50, 'sine', 0.45, 0.25, 0.30);   // C6
    }

    // 6. New Message / Notification (Soft ping)
    message() {
        this.playTone(880, 'sine', 0.08, 0.2, 0);
        this.playTone(1318.51, 'sine', 0.18, 0.2, 0.06);
    }

    // 7. Medical Attention Alert (Subtle, professional non-alarming tone)
    medicalAlert() {
        this.playTone(440, 'triangle', 0.15, 0.25, 0);
        this.playTone(349.23, 'triangle', 0.25, 0.25, 0.15);
    }

    // 8. Incoming Video Call (Professional rhythmic ringtone)
    startRingtone() {
        if (this.ringInterval) clearInterval(this.ringInterval);
        const ringPattern = () => {
            this.playTone(587.33, 'sine', 0.15, 0.25, 0);
            this.playTone(739.99, 'sine', 0.15, 0.25, 0.12);
            this.playTone(880.00, 'sine', 0.25, 0.25, 0.24);
        };
        ringPattern();
        this.ringInterval = setInterval(ringPattern, 2200);
    }

    stopRingtone() {
        if (this.ringInterval) {
            clearInterval(this.ringInterval);
            this.ringInterval = null;
        }
    }

    // 9. Call Connected
    callConnected() {
        this.stopRingtone();
        this.playTone(440, 'sine', 0.1, 0.2, 0);
        this.playTone(880, 'sine', 0.2, 0.2, 0.08);
    }

    // 10. Call Ended
    callEnded() {
        this.stopRingtone();
        this.playTone(440, 'sine', 0.12, 0.2, 0);
        this.playTone(330, 'sine', 0.20, 0.2, 0.10);
    }
}

window.soundEngine = new SoundEngine();

// Auto-attach sound handlers to buttons
document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('click', (e) => {
        const target = e.target.closest('button, a, input[type="checkbox"], input[type="radio"], select');
        if (target) {
            window.soundEngine.click();
        }
    }, { passive: true });
});
