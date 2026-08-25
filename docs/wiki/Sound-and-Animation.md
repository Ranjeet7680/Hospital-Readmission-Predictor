# Sound & Animation Design

HRP Clinical features a native Web Audio API synthesizer and a GPU-accelerated interaction animation system.

---

## 1. Web Audio API Sound Synthesizer

Implemented in `static/js/sound_engine.js`:
- **Zero External Assets**: Pure programmatic audio synthesis using `AudioContext`, `OscillatorNode`, and `GainNode` with exponential ramps.
- **Sound Events**:
  - `playClick()`: Soft triangle wave ($800\text{Hz} \to 400\text{Hz}$) for interactive buttons.
  - `playSuccess()`: Ascending major triad ($C_5 \to E_5 \to G_5$) for successful submissions and approvals.
  - `playError()`: Low-frequency descending tone ($320\text{Hz} \to 180\text{Hz}$) for validation errors.
  - `playUploadChord()`: Multi-tone chord for document ingestion.
  - `playRingtone()`: Alternating two-tone harmonic ringtone for telemedicine call invitations.
- **Master Audio Mute**: Dedicated top-bar audio toggle button allows instant muting.

---

## 2. Animation & Interaction Utilities

Implemented in `static/js/animations.js`:
- **Count-Up Number Animations**: Smoothly interpolates KPI numbers (`0 \to 30,482`, `0% \to 93.7%`) on page load.
- **SVG Circular Risk Gauge**: Animates `stroke-dashoffset` from empty to target risk percentage (e.g., $68\%$).
- **Live Neural Network Data Flow**: HTML5 Canvas visualizing tensor activations moving between input, hidden, and output layers.
- **Accessible Reduce-Motion**: Honors user operating system preference `prefers-reduced-motion: reduce`.
