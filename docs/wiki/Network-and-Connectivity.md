# Network & Connectivity Documentation

This section describes network telemetry, offline status detection, and video stream connection quality handlers.

---

## 1. Network Diagnostics & Offline State

- **Connection Monitoring**: Uses `navigator.onLine` and window online/offline event listeners to detect connection loss.
- **Offline Banner**: In offline states, an accessible non-blocking alert appears, disabling active server predictions while preserving local patient and report viewing.
- **Upload Retry Queue**: Medical document uploads that fail due to temporary network interruptions are automatically queued for retry when connectivity restores.
- **Telemedicine Network Telemetry**: Video consultation monitors packet loss and bandwidth, automatically switching to audio-only fallback mode if throughput degrades below $150\text{ kbps}$.
- **Security Notice**: Network diagnostics do not store, scan, or expose Wi-Fi passwords or local network credentials.
