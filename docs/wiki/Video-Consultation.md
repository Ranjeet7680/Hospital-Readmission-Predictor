# Telemedicine Video Consultation

Located at `/consultation/careai`, the Video Consultation system connects patients and healthcare providers through an encrypted, AI-augmented clinical consultation interface.

---

## 1. Consultation Lifecycle

```mermaid
sequenceDiagram
    autonumber
    actor Patient as Patient (Eleanor Vance)
    actor Doctor as Doctor (Dr. J. Aris)
    participant Platform as Video Gateway
    participant CareAI as CareAI Copilot

    Patient->>Platform: Join Telemedicine Session
    Doctor->>Platform: Connect & Authenticate Call
    Platform->>Platform: Trigger Web Audio Ringtone
    Platform->>CareAI: Stream Audio / Transcript
    CareAI-->>Doctor: Display 68% Readmission Risk & PPO Care Action
    CareAI-->>Platform: Emit Real-time Dual Captions (EN / HI)
    Doctor->>Platform: Edit & Sign Clinical Encounter Note
    Platform-->>Patient: Save Consultation Record to Patient Portal
```

---

## 2. Key Interface Features

1. **Simulated WebRTC Video Stream**: High-definition video with camera, microphone, screen sharing, and full-screen controls.
2. **Web Audio Ringtone**: Custom harmonic synthesizer tone announcing incoming clinical connections.
3. **Dual Live Subtitles**: Real-time line-by-line synchronized English and Hindi subtitles for accessibility and ESL patients.
4. **CareAI Sidebar**: Live patient summary, longitudinal risk history chart, vital signs, and PPO decision-support recommendations.
5. **Encounter Documentation**: Real-time editable clinical note pane with one-click EHR persistence.
