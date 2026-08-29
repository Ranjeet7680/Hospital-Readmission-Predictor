/**
 * CareAI End-to-End Multilingual Voice & Chatbot Engine v4.2
 * Hospital Readmission Predictor (HRP Clinical)
 *
 * Features:
 *  - 18+ Language Text-to-Speech (TTS) with optimized Natural Female Voice Selection
 *  - Real-time Speech-to-Text (STT) Voice Recognition across all supported languages
 *  - Continuous Hands-Free Live Voice Conversation Mode (Speech-to-Speech)
 *  - Animated Voice Waveform & Sound Pulse Audio Visualizer
 *  - Multi-Turn Medical Conversational Memory & Quick Action Triggers
 *  - Audio Replay, Pitch, Rate, and Persona Controls
 */

class CareAIVoiceSystem {
    constructor() {
        this.currentLang = 'en';
        this.isSpeaking = false;
        this.isListening = false;
        this.autoSpeak = true;
        this.handsFreeMode = false;
        this.voicePitch = 1.08;
        this.voiceRate = 0.98;
        this.speechRec = null;
        this.currentUtterance = null;
        this.voicesLoaded = false;
        this.femaleVoiceMap = {};

        this.localeMap = {
            en: 'en-US', hi: 'hi-IN', es: 'es-ES', fr: 'fr-FR', de: 'de-DE',
            bn: 'bn-IN', ta: 'ta-IN', te: 'te-IN', kn: 'kn-IN', ml: 'ml-IN',
            mr: 'mr-IN', gu: 'gu-IN', pa: 'pa-IN', ar: 'ar-SA', zh: 'zh-CN',
            ja: 'ja-JP', pt: 'pt-BR', ru: 'ru-RU'
        };

        this.femalePersonaNames = {
            en: 'Dr. Sophia (US Female)',
            hi: 'Dr. Ananya (हिन्दी Female)',
            es: 'Dra. Valentina (Español)',
            fr: 'Dr. Amélie (Français)',
            de: 'Dr. Marlene (Deutsch)',
            bn: 'Dr. Tanushree (বাংলা)',
            ta: 'Dr. Priya (தமிழ்)',
            te: 'Dr. Kavya (తెలుగు)',
            kn: 'Dr. Sahana (ಕನ್ನಡ)',
            ml: 'Dr. Anupama (മലയാളം)',
            mr: 'Dr. Gauri (मराठी)',
            ar: 'Dr. Layla (العربية)',
            zh: 'Dr. Meiling (中文)',
            ja: 'Dr. Yoko (日本語)',
            pt: 'Dra. Camila (Português)',
            ru: 'Dr. Elena (Русский)'
        };
    }

    init() {
        // 1. Sync language from cookie / localStorage or i18n
        const storedLang = localStorage.getItem('hrp_lang') || document.cookie.replace(/(?:(?:^|.*;\s*)hrp_lang\s*\=\s*([^;]*).*$)|^.*$/, "$1") || 'en';
        if (this.localeMap[storedLang]) {
            this.currentLang = storedLang;
        }

        // 2. Load and cache browser female voices
        if ('speechSynthesis' in window) {
            window.speechSynthesis.onvoiceschanged = () => {
                this.loadFemaleVoices();
            };
            this.loadFemaleVoices();
        }

        // 3. Initialize Web Speech Recognition
        this.initSpeechRecognition();

        // 4. Bind UI elements
        this.bindEvents();
        console.log("CareAI End-to-End Female Voice System initialized in", this.currentLang.toUpperCase());
    }

    loadFemaleVoices() {
        if (!('speechSynthesis' in window)) return;
        const voices = window.speechSynthesis.getVoices();
        if (!voices || voices.length === 0) return;

        this.voicesLoaded = true;
        const femaleKeywords = ['female', 'woman', 'zira', 'samantha', 'victoria', 'karen', 'swara', 'heera', 'kalpana', 'valentina', 'monica', 'amelie', 'hortense', 'marlene', 'hedda', 'tanushree', 'priya', 'kavya', 'sahana', 'anupama', 'gauri', 'layla', 'meiling', 'kyoko', 'yoko', 'camila', 'elena'];

        Object.keys(this.localeMap).forEach(lang => {
            const locale = this.localeMap[lang];
            const matchingVoices = voices.filter(v => v.lang.startsWith(lang) || v.lang === locale || v.lang.replace('_', '-') === locale);
            
            // Prioritize explicitly female voices
            let bestFemale = matchingVoices.find(v => {
                const nameLower = v.name.toLowerCase();
                return femaleKeywords.some(k => nameLower.includes(k));
            });

            if (!bestFemale && matchingVoices.length > 0) {
                bestFemale = matchingVoices[0];
            }
            if (bestFemale) {
                this.femaleVoiceMap[lang] = bestFemale;
            }
        });
    }

    initSpeechRecognition() {
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRec) {
            console.warn("Speech Recognition API not supported in this browser.");
            return;
        }

        this.speechRec = new SpeechRec();
        this.speechRec.continuous = false;
        this.speechRec.interimResults = true;
        this.speechRec.maxAlternatives = 1;

        this.speechRec.onstart = () => {
            this.isListening = true;
            this.updateVoiceVisualizer(true, 'listening');
            this.showMicPulsing(true);
            const input = document.getElementById('careai-dock-input');
            if (input) input.placeholder = `🎙️ Listening (${this.currentLang.toUpperCase()})... Speak now`;
        };

        this.speechRec.onresult = (event) => {
            let interimTranscript = '';
            let finalTranscript = '';

            for (let i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                    finalTranscript += event.results[i][0].transcript;
                } else {
                    interimTranscript += event.results[i][0].transcript;
                }
            }

            const input = document.getElementById('careai-dock-input');
            if (input) {
                input.value = finalTranscript || interimTranscript;
            }

            if (finalTranscript.trim().length > 0) {
                this.stopListening();
                this.sendMessage(finalTranscript.trim());
            }
        };

        this.speechRec.onerror = (event) => {
            console.warn("Speech Recognition error:", event.error);
            this.stopListening();
        };

        this.speechRec.onend = () => {
            this.isListening = false;
            this.updateVoiceVisualizer(false);
            this.showMicPulsing(false);
            const input = document.getElementById('careai-dock-input');
            if (input) input.placeholder = "Ask Dr. Sophia CareAI or tap mic to speak...";
        };
    }

    startListening() {
        if (!this.speechRec) {
            if (typeof showToast === 'function') {
                showToast("Voice input is not supported in this browser.", "warning");
            }
            return;
        }

        if (this.isSpeaking) {
            this.stopSpeaking();
        }

        this.speechRec.lang = this.localeMap[this.currentLang] || 'en-US';
        try {
            this.speechRec.start();
        } catch (e) {
            console.warn("Speech recognition already running or error:", e);
        }
    }

    stopListening() {
        if (this.speechRec && this.isListening) {
            try { this.speechRec.stop(); } catch(e) {}
        }
        this.isListening = false;
        this.showMicPulsing(false);
        this.updateVoiceVisualizer(false);
    }

    toggleListening() {
        if (this.isListening) {
            this.stopListening();
        } else {
            this.startListening();
        }
    }

    speak(text, lang = null) {
        if (!('speechSynthesis' in window)) return;
        this.stopSpeaking();

        if (!text || text.trim().length === 0) return;

        const targetLang = lang || this.currentLang;
        const locale = this.localeMap[targetLang] || 'en-US';
        
        // Clean text for speech synthesis (remove markdown markers and emojis for clean speech)
        const cleanText = text
            .replace(/[*_#`~[\]()<>]/g, ' ')
            .replace(/[⚠️🚨💊🩺📊🪪🥗📅📹🔍]/g, '')
            .replace(/\s+/g, ' ')
            .trim();

        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = locale;
        utterance.pitch = this.voicePitch; // Warm, gentle female pitch (1.08)
        utterance.rate = this.voiceRate;   // Soothing cadence (0.98)

        // Bind female voice if available
        if (this.femaleVoiceMap[targetLang]) {
            utterance.voice = this.femaleVoiceMap[targetLang];
        }

        utterance.onstart = () => {
            this.isSpeaking = true;
            this.updateVoiceVisualizer(true, 'speaking');
            this.setAvatarSpeaking(true);
        };

        utterance.onend = () => {
            this.isSpeaking = false;
            this.updateVoiceVisualizer(false);
            this.setAvatarSpeaking(false);
            
            // If in continuous hands-free mode, re-listen automatically!
            if (this.handsFreeMode) {
                setTimeout(() => {
                    this.startListening();
                }, 400);
            }
        };

        utterance.onerror = () => {
            this.isSpeaking = false;
            this.updateVoiceVisualizer(false);
            this.setAvatarSpeaking(false);
        };

        this.currentUtterance = utterance;
        window.speechSynthesis.speak(utterance);
    }

    stopSpeaking() {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
        }
        this.isSpeaking = false;
        this.updateVoiceVisualizer(false);
        this.setAvatarSpeaking(false);
    }

    toggleHandsFree() {
        this.handsFreeMode = !this.handsFreeMode;
        const btn = document.getElementById('careai-handsfree-btn');
        if (btn) {
            if (this.handsFreeMode) {
                btn.classList.add('bg-emerald-500', 'text-white', 'animate-pulse');
                btn.classList.remove('bg-surface-variant', 'text-secondary');
                if (typeof showToast === 'function') showToast("🎙️ Hands-Free Live Voice Call Mode Active", "success");
                this.startListening();
            } else {
                btn.classList.remove('bg-emerald-500', 'text-white', 'animate-pulse');
                btn.classList.add('bg-surface-variant', 'text-secondary');
                this.stopListening();
                this.stopSpeaking();
                if (typeof showToast === 'function') showToast("Hands-Free Mode Paused", "info");
            }
        }
    }

    setLanguage(lang) {
        if (!this.localeMap[lang]) return;
        this.currentLang = lang;
        localStorage.setItem('hrp_lang', lang);
        document.cookie = `hrp_lang=${lang}; path=/; max-age=31536000`;

        const badge = document.getElementById('careai-current-lang-badge');
        if (badge) badge.textContent = lang.toUpperCase();

        const personaLabel = document.getElementById('careai-persona-label');
        if (personaLabel) {
            personaLabel.textContent = this.femalePersonaNames[lang] || 'Dr. Sophia (CareAI Female)';
        }

        if (this.speechRec && this.isListening) {
            this.stopListening();
            this.startListening();
        }
        
        // Notify user in the female voice
        const greeting = lang === 'hi' ? 'नमस्ते, मैं डॉ. अनन्या केयर-एआई हूँ।' : (lang === 'es' ? 'Hola, soy la Dra. Valentina CareAI.' : 'Hello, I am Dr. Sophia CareAI.');
        this.speak(greeting, lang);
    }

    async sendMessage(text) {
        if (!text || text.trim().length === 0) return;

        const chatBox = document.getElementById('careai-dock-messages');
        const input = document.getElementById('careai-dock-input');
        if (input) input.value = '';

        // Append User Message to UI
        if (chatBox) {
            chatBox.innerHTML += `
                <div class="flex justify-end gap-2 items-start message-user animate-fade-in">
                    <div class="max-w-[82%] p-3 rounded-2xl rounded-tr-xs bg-primary text-white text-xs shadow-xs">
                        <p class="font-medium">${this.escapeHtml(text)}</p>
                        <span class="text-[9px] text-white/70 block mt-1 text-right">${new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</span>
                    </div>
                    <div class="w-6 h-6 rounded-full bg-primary-fixed text-primary flex items-center justify-center text-[11px] font-bold shrink-0">You</div>
                </div>
            `;
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        // Show typing indicator
        const typingId = 'careai-typing-' + Date.now();
        if (chatBox) {
            chatBox.innerHTML += `
                <div id="${typingId}" class="flex justify-start gap-2 items-center message-bot animate-fade-in">
                    <div class="w-7 h-7 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-400 text-white flex items-center justify-center text-[12px] font-bold shadow-xs">
                        <span class="material-symbols-outlined text-[15px]">smart_toy</span>
                    </div>
                    <div class="p-3 rounded-2xl rounded-tl-xs bg-surface-container text-secondary text-xs flex items-center gap-1.5 shadow-xs">
                        <span class="w-1.5 h-1.5 rounded-full bg-primary animate-bounce"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-primary animate-bounce" style="animation-delay: 0.15s"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-primary animate-bounce" style="animation-delay: 0.3s"></span>
                        <span class="text-[10px] ml-1 font-semibold text-primary">Dr. CareAI analyzing...</span>
                    </div>
                </div>
            `;
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        try {
            const resp = await fetch('/api/careai/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: text,
                    lang: this.currentLang,
                    voice_enabled: this.autoSpeak
                })
            });

            const data = await resp.json();
            const typingEl = document.getElementById(typingId);
            if (typingEl) typingEl.remove();

            if (data.status === 'success') {
                this.renderBotResponse(data);
                if (this.autoSpeak && data.audio_text) {
                    this.speak(data.audio_text, this.currentLang);
                }
            } else {
                this.renderBotResponse({
                    response: "I encountered a minor network issue. Please try again.",
                    disclaimer: "CareAI Assistant",
                    suggested_actions: []
                });
            }
        } catch (err) {
            console.error("CareAI API error:", err);
            const typingEl = document.getElementById(typingId);
            if (typingEl) typingEl.remove();
            this.renderBotResponse({
                response: "CareAI is temporarily offline. Local safety checks remain active.",
                disclaimer: "Offline Protocol",
                suggested_actions: []
            });
        }
    }

    renderBotResponse(data) {
        const chatBox = document.getElementById('careai-dock-messages');
        if (!chatBox) return;

        const isEmergency = data.urgency === 'CRITICAL_RED';
        const cardBg = isEmergency ? 'bg-red-50 border border-red-200 text-red-900' : 'bg-surface-container-lowest border border-outline-variant text-on-surface';
        const voicePersona = data.female_voice || this.femalePersonaNames[this.currentLang] || 'Dr. Sophia CareAI';

        let actionsHtml = '';
        if (data.suggested_actions && data.suggested_actions.length > 0) {
            actionsHtml = `<div class="flex flex-wrap gap-1.5 pt-2 border-t border-outline-variant/40 mt-2">`;
            data.suggested_actions.forEach(act => {
                if (act.type === 'call') {
                    actionsHtml += `<a href="${act.action}" class="px-2.5 py-1 rounded-lg bg-primary text-white text-[11px] font-bold hover:bg-primary-container transition-all flex items-center gap-1"><span class="material-symbols-outlined text-[13px]">videocam</span> ${act.label}</a>`;
                } else if (act.type === 'emergency') {
                    actionsHtml += `<a href="${act.action}" class="px-2.5 py-1 rounded-lg bg-red-600 text-white text-[11px] font-extrabold hover:bg-red-700 transition-all flex items-center gap-1 animate-pulse"><span class="material-symbols-outlined text-[13px]">emergency</span> ${act.label}</a>`;
                } else {
                    actionsHtml += `<a href="${act.action}" class="px-2.5 py-1 rounded-lg bg-surface-variant text-primary text-[11px] font-semibold hover:bg-primary-fixed transition-all">${act.label}</a>`;
                }
            });
            actionsHtml += `</div>`;
        }

        const msgHtml = `
            <div class="flex justify-start gap-2 items-start message-bot animate-fade-in">
                <div class="w-7 h-7 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-400 text-white flex items-center justify-center text-[12px] font-bold shadow-xs shrink-0 mt-0.5">
                    <span class="material-symbols-outlined text-[15px]">medical_services</span>
                </div>
                <div class="max-w-[85%] p-3.5 rounded-2xl rounded-tl-xs ${cardBg} text-xs shadow-xs space-y-1.5">
                    <div class="flex items-center justify-between gap-2 border-b border-outline-variant/30 pb-1">
                        <span class="font-bold text-primary flex items-center gap-1">
                            <span class="material-symbols-outlined text-[14px]">record_voice_over</span>
                            ${voicePersona}
                        </span>
                        <button onclick="window.careAIVoice.speak('${this.escapeQuotes(data.audio_text || data.response)}', '${this.currentLang}')" class="p-1 rounded-md hover:bg-primary/10 text-primary transition-all" title="Replay Audio in Female Voice">
                            <span class="material-symbols-outlined text-[14px]">volume_up</span>
                        </button>
                    </div>
                    <p class="leading-relaxed font-normal">${this.formatMarkdown(data.response)}</p>
                    ${actionsHtml}
                    ${data.disclaimer ? `<span class="text-[9px] text-secondary/70 block italic pt-1">${data.disclaimer}</span>` : ''}
                </div>
            </div>
        `;

        chatBox.innerHTML += msgHtml;
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    updateVoiceVisualizer(active, mode = 'speaking') {
        const visualizer = document.getElementById('careai-voice-waveform');
        if (!visualizer) return;

        if (active) {
            visualizer.classList.remove('hidden');
            visualizer.classList.add('flex');
            const bars = visualizer.querySelectorAll('.waveform-bar');
            bars.forEach((b, idx) => {
                b.style.animationDuration = `${0.35 + (idx % 4) * 0.15}s`;
                b.classList.add('animate-wave');
            });
            const statusLabel = document.getElementById('careai-voice-status-text');
            if (statusLabel) {
                statusLabel.textContent = mode === 'speaking' ? '🔊 Dr. CareAI Speaking (Female Voice)...' : '🎙️ Listening to your voice...';
            }
        } else {
            const bars = visualizer.querySelectorAll('.waveform-bar');
            bars.forEach(b => b.classList.remove('animate-wave'));
            visualizer.classList.add('hidden');
            visualizer.classList.remove('flex');
        }
    }

    setAvatarSpeaking(speaking) {
        const ring = document.getElementById('careai-avatar-pulse-ring');
        if (ring) {
            if (speaking) ring.classList.add('animate-ping', 'opacity-75');
            else ring.classList.remove('animate-ping', 'opacity-75');
        }
    }

    showMicPulsing(pulsing) {
        const micBtn = document.getElementById('careai-mic-btn');
        if (micBtn) {
            if (pulsing) {
                micBtn.classList.add('bg-red-500', 'text-white', 'animate-pulse');
                micBtn.classList.remove('bg-surface-variant', 'text-primary');
            } else {
                micBtn.classList.remove('bg-red-500', 'text-white', 'animate-pulse');
                micBtn.classList.add('bg-surface-variant', 'text-primary');
            }
        }
    }

    openDock() {
        const dock = document.getElementById('careai-floating-dock');
        if (dock) {
            dock.classList.remove('hidden');
            dock.classList.add('flex');
            const input = document.getElementById('careai-dock-input');
            if (input) input.focus();
        }
    }

    closeDock() {
        const dock = document.getElementById('careai-floating-dock');
        if (dock) {
            dock.classList.add('hidden');
            dock.classList.remove('flex');
        }
        this.stopSpeaking();
        this.stopListening();
    }

    toggleDock() {
        const dock = document.getElementById('careai-floating-dock');
        if (dock && !dock.classList.contains('hidden')) {
            this.closeDock();
        } else {
            this.openDock();
        }
    }

    clearChat() {
        const chatBox = document.getElementById('careai-dock-messages');
        if (chatBox) {
            chatBox.innerHTML = `
                <div class="p-3.5 bg-surface-container rounded-2xl text-secondary space-y-1 text-xs">
                    <p class="font-bold text-primary flex items-center gap-1">
                        <span class="material-symbols-outlined text-[15px]">record_voice_over</span>
                        ${this.femalePersonaNames[this.currentLang] || 'Dr. Sophia CareAI'}
                    </p>
                    <p>Chat cleared. I am ready to answer any questions in your preferred language!</p>
                </div>
            `;
        }
    }

    bindEvents() {
        const input = document.getElementById('careai-dock-input');
        if (input) {
            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.sendMessage(input.value);
                }
            });
        }
    }

    formatMarkdown(text) {
        if (!text) return '';
        return text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/`(.*?)`/g, '<code class="px-1 py-0.5 rounded bg-primary/10 text-primary font-mono text-[11px]">$1</code>')
            .replace(/\n/g, '<br/>');
    }

    escapeHtml(str) {
        return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    escapeQuotes(str) {
        return str.replace(/'/g, "\\'").replace(/"/g, '&quot;');
    }
}

// Instantiate global singleton
window.careAIVoice = new CareAIVoiceSystem();
document.addEventListener('DOMContentLoaded', () => {
    window.careAIVoice.init();
});
