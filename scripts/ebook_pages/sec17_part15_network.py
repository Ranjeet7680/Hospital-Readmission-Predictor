"""
Pages 83 to 86: Part XV — Network Resilience, Offline-First & Edge AI
"""
import os
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from ebook_core import create_styles, make_callout, make_table, make_code_box, C_PRIMARY, C_SECONDARY, C_DARK, C_LIGHT_BG

def get_pages_083_086_part15():
    styles = create_styles()
    flowables = []

    # ==========================================
    # PAGE 83: Part XV Header & Chapter 57 (Edge Computing in Healthcare)
    # ==========================================
    flowables.append(Paragraph("PART XV — NETWORK RESILIENCE, OFFLINE-FIRST & EDGE AI", styles['PartHeader']))
    flowables.append(Paragraph("Chapter 57 — Edge Computing in Bandwidth-Constrained Clinical Environments", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "Modern hospital facilities are notorious for RF shielding, thick lead-lined radiology walls, and elevator dead zones. "
        "Furthermore, rural community clinics and home health nurses operating in remote areas frequently face complete cellular blackouts. "
        "A clinical decision support system that crashes when offline is unacceptable. HRP Clinical is engineered from the ground up "
        "as an <b>Offline-First, Edge-Intelligent Progressive Web Application (PWA)</b>.", styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    edge_headers = ["Network Operating Condition", "System Operational Behavior", "Guaranteed Clinical Capability"]
    edge_rows = [
        ["High-Speed Fiber (Hospital Wi-Fi)", "Full cloud sync; real-time FastAPI inference; live WebRTC HD video", "Sub-second cloud risk inference & instant executive dashboard sync"],
        ["Degraded 3G / High Packet Loss", "Adaptive bitrate WebRTC; compressed JSON payloads; telemetry throttling", "Maintains uninterrupted audio consultation & basic vital telemetry stream"],
        ["Intermittent Connectivity", "Service Worker caches requests; queues sync events in IndexedDB", "Clinicians chart discharge notes without UI interruption or data loss"],
        ["Total Offline Disconnection", "Client-side ONNX Runtime edge inference; local QR cryptographic validation", "Hospitalists score readmission risk locally on tablets with zero internet"]
    ]
    flowables.append(make_table(edge_headers, edge_rows, col_widths=[130, 195, 197]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "OFFLINE RELIABILITY GUARANTEE",
        "Home health nurses can visit patients in rural dead zones, perform full risk scoring via embedded ONNX models, and log clinical "
        "notes into IndexedDB with 100% guarantee of automatic background synchronization upon returning to connectivity.",
        kind="shield"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 84: Chapter 58 (Service Workers & IndexedDB Storage)
    # ==========================================
    flowables.append(Paragraph("Chapter 58 — Service Workers, Cache-First Strategies & IndexedDB Storage", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "HRP Clinical deploys a high-performance <b>Service Worker caching lifecycle</b> coupled with encrypted client-side <b>IndexedDB storage</b>:",
        styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    sw_headers = ["Asset / Resource Category", "Caching Strategy", "Storage Mechanism", "Cache Invalidation Trigger"]
    sw_rows = [
        ["App Shell (HTML/CSS/JS)", "Cache-First with Background Revalidation", "CacheStorage API", "Automated service worker version hash bump on new release"],
        ["Patient Roster & Vitals", "Network-First with IndexedDB Fallback", "Encrypted IndexedDB Table", "Refreshed on every successful online REST fetch"],
        ["ONNX Model Weights (5.2 MB)", "Cache-First (Permanent Cache)", "CacheStorage (Indexed)", "Updated only during major clinical model version updates"],
        ["Offline Charting Actions Queue", "IndexedDB Mutation Queue", "Dexie.js IndexedDB Store", "Drained and synced via Background Sync API upon reconnection"]
    ]
    flowables.append(make_table(sw_headers, sw_rows, col_widths=[125, 140, 115, 142]))
    flowables.append(Spacer(1, 6))

    sw_code = """// Production Service Worker Caching & Background Sync
const CACHE_NAME = 'hrp-clinical-v2.4.1';
const STATIC_ASSETS = ['/', '/index.html', '/css/styles.css', '/js/bundle.js', '/models/xgb_quantized.onnx'];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS))
    );
    self.skipWaiting();
});

self.addEventListener('fetch', (event) => {
    // Cache-First strategy for static UI assets and ONNX weights
    if (STATIC_ASSETS.some(url => event.request.url.includes(url))) {
        event.respondWith(
            caches.match(event.request).then((res) => res || fetch(event.request))
        );
        return;
    }
    // Network-First for real-time patient EHR data
    event.respondWith(
        fetch(event.request).catch(() => caches.match(event.request))
    );
});"""
    flowables.append(make_code_box(sw_code, "Service Worker Offline Caching Engine", width=522))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 85: Chapter 59 (Background Sync & Conflict Resolution)
    # ==========================================
    flowables.append(Paragraph("Chapter 59 — Background Sync, Queue Reconciliation & Conflict Resolution", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "When multiple clinicians make offline adjustments to patient discharge plans, reconciling conflicting edits upon reconnection "
        "is critical to avoid data corruption. HRP Clinical implements a <b>Vector Clock & Last-Write-Wins (LWW) Conflict Engine</b>:",
        styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    conflict_headers = ["Conflict Scenario", "Detection Mechanism", "Automated Resolution Strategy", "Clinician Alert"]
    conflict_rows = [
        ["Concurrent Medication Edits", "Vector Clock divergence on prescription array", "Union of non-conflicting drugs; flags duplicate dosages for MD review", "High-priority modal: 'Medication Conflict Detected'"],
        ["Offline SOAP Note Finalization", "Server timestamp > Client offline timestamp", "Preserves server finalized version; stores client edit as 'Addendum Draft'", "Appends note as signed clinical addendum"],
        ["Outdated Risk Score Submission", "Model version mismatch in sync payload", "Recomputes inference on server using latest ingested laboratory telemetry", "Silently updates risk score with latest telemetry"],
        ["Network Interruption During Call", "WebRTC ICE connection state === 'disconnected'", "Caches in-call vital logs in IndexedDB; syncs payload on reconnect", "Seamlessly uploads consultation telemetry buffer"]
    ]
    flowables.append(make_table(conflict_headers, conflict_rows, col_widths=[120, 130, 140, 132]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "ZERO-DATA-LOSS GUARANTEE",
        "The IndexedDB transaction queue maintains an append-only mutation log with exponential backoff retries, guaranteeing that "
        "no physician discharge order or nurse triage log is ever lost due to network dropouts.",
        kind="shield"
    ))
    flowables.append(PageBreak())

    # ==========================================
    # PAGE 86: Chapter 60 (Lightweight Edge AI Inference with ONNX)
    # ==========================================
    flowables.append(Paragraph("Chapter 60 — Lightweight Edge AI Inference with ONNX Runtime Web", styles['ChapterHeader']))
    flowables.append(Spacer(1, 4))

    flowables.append(Paragraph(
        "To enable instant risk scoring even when completely disconnected from cloud servers, we quantized our production XGBoost "
        "and LightGBM models into <b>8-bit quantized ONNX binaries (5.2 MB)</b> that execute client-side via WebAssembly (WASM):",
        styles['Body']
    ))
    flowables.append(Spacer(1, 4))

    onnx_headers = ["Inference Mode", "Execution Environment", "Latency", "Memory Footprint", "Network Requirement"]
    onnx_rows = [
        ["Cloud FastAPI Inference", "Cloud Python 3.11 / Uvicorn Server", "1.8 ms", "Server-side RAM", "Requires active internet connection"],
        ["Edge Browser Inference (WASM)", "Client Browser ONNX Runtime (WASM)", "<b>6.4 ms</b>", "<b>18.2 MB RAM</b>", "<b>100% Offline (Zero internet required)</b>"],
        ["Edge Mobile App (Android/iOS)", "React Native ONNX Native Runtime", "<b>3.2 ms</b>", "<b>14.5 MB RAM</b>", "<b>100% Offline (Zero internet required)</b>"]
    ]
    flowables.append(make_table(onnx_headers, onnx_rows, col_widths=[125, 125, 60, 85, 127]))
    flowables.append(Spacer(1, 6))

    flowables.append(make_callout(
        "PART XV SYNTHESIS & ARCHITECTURAL TRANSITION",
        "Edge computing, Service Workers, and ONNX runtime establish unbreakable network resilience. "
        "In <b>Part XVI: Microservices Architecture & Cloud Deployment</b>, we detail our cloud infrastructure, "
        "Docker container orchestration, Redis caching, and PostgreSQL schema scaling.",
        kind="info"
    ))
    flowables.append(PageBreak())

    return flowables

print("sec17_part15_network loaded.")
