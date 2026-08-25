# Part XIV: Sound, Animation & Interaction Design (Chapters 62 - 64)

def get_part14():
    return """
# PART XIV — SOUND DESIGN, ANIMATION & INTERACTION PHYSICS

---

## Chapter 62 — Psychoacoustic Sound Design & Web Audio API Synthesis

### 62.1 Zero-Dependency Procedural Audio
To avoid downloading large audio files, HRP Clinical synthesizes harmonic frequencies in real time using the browser's native **Web Audio API**:

```javascript
// Pure Web Audio Harmonic Synthesizer
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playClinicalChime(type) {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    
    if (type === 'success') {
        osc.frequency.setValueAtTime(523.25, audioCtx.currentTime); // C5
        osc.frequency.exponentialRampToValueAtTime(659.25, audioCtx.currentTime + 0.15); // E5
        gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.4);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.4);
    }
}
```

### 62.2 Acoustic Sound Library
* **Welcome Chime**: Gentle two-tone major third (C5 $\to$ E5, 400ms) confirming system readiness.
* **Telemedicine Ringtone**: Harmonic rhythmic pulse (440Hz $\leftrightarrow$ 554Hz) simulating medical phone ring.
* **Risk Calculation Pop**: Soft resonant tick confirming model inference completion.
* **Clinical Alert Ping**: Clear high-frequency chime alerting staff to acute vital deterioration.

---

### 62.3 Key Takeaways
1. Web Audio API synthesis produces zero-latency audio without external MP3 network requests.
2. Harmonic musical chords reduce auditory fatigue in clinical ward environments.
3. Users can mute or adjust sound effects in settings with instant global persistence.

---

## Chapter 63 — Micro-Interactions, State Transitions & Kinematic Physics

### 63.1 Kinematic Animation Standards
Every interactive component adheres to standardized physical motion durations:
* **Micro-interactions (Buttons, Toggles, Badges)**: **150ms – 200ms** (`cubic-bezier(0.4, 0.0, 0.2, 1)`).
* **Card Flips & Modals**: **300ms – 400ms** (`cubic-bezier(0.0, 0.0, 0.2, 1)`).
* **Page Transitions**: **250ms** subtle cross-fade with 4px vertical glide.

```
       ┌─────────────────────────────────────────────────────────┐
       │               COMPONENT INTERACTION STATES              │
       ├──────────────┬──────────────────────────────────────────┤
       │ Default      │ Resting elevation, subtle border         │
       │ Hover        │ +2dp elevation lift, color brightening   │
       │ Focus-Visible│ 2px high-contrast primary outline ring   │
       │ Active/Press │ -1dp compression, tactile click response │
       │ Disabled     │ 38% opacity, cursor-not-allowed          │
       │ Loading      │ Skeleton pulse with circular spinner     │
       └──────────────┴──────────────────────────────────────────┘
```

---

### 63.2 Key Takeaways
1. Predictable kinematic motion improves perceived system responsiveness and user satisfaction.
2. Standardized cubic-bezier easing curves prevent jarring or distracting visual transitions.
3. Every button supports all 10 distinct interaction and loading states.

---

## Chapter 64 — Haptic & Acoustic Feedback in Life-Critical Contexts

### 64.1 Multimodal Feedback Synergy
In noisy hospital wards or for visually impaired clinicians, combining visual badges, auditory chimes, and mobile device vibration (via the Web Vibration API `navigator.vibrate([40, 60, 40])`) guarantees critical alerts are never missed.

---

### 64.2 Key Takeaways
1. Multimodal feedback bridges visual, auditory, and tactile sensory channels.
2. Haptic vibration confirms emergency break-glass triggers on mobile devices.
3. Sound and vibration levels are customizable to prevent patient disturbance in sleep wards.
"""
