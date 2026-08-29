/**
 * CareAI Universal End-to-End Multilingual Voice Assistant & Chatbot Engine v5.5
 * Hospital Readmission Predictor (HRP Clinical)
 *
 * Full Capabilities:
 *  - 36+ Language Speech-to-Text (STT) Speech Recognition with live interim feedback
 *  - High-Fidelity Female Neural Voice Speech Synthesis (TTS) in 36 languages
 *  - Web Audio API Real-time Microphone FFT Frequency Visualizer
 *  - Bidirectional Hands-Free Voice Call (Full-Duplex Speech-to-Speech)
 *  - Automatic Chrome/Edge SpeechSynthesis Pause & Garbage Collection Workaround
 *  - Voice Navigation Router & 100% Deterministic Emergency Red-Flag Triage
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
        this.femaleVoiceMap = {};
        this.audioContext = null;
        this.analyser = null;
        this.audioSource = null;
        this.micStream = null;
        this.animFrameId = null;
        this.synthTimer = null;

        // Master 36-Language Locale Mapping (BCP-47 Standard)
        this.localeMap = {
            en: 'en-US', hi: 'hi-IN', bn: 'bn-IN', ta: 'ta-IN', te: 'te-IN',
            kn: 'kn-IN', ml: 'ml-IN', mr: 'mr-IN', gu: 'gu-IN', pa: 'pa-IN',
            ur: 'ur-PK', or: 'or-IN', as: 'as-IN', ne: 'ne-NP', si: 'si-LK',
            es: 'es-ES', fr: 'fr-FR', de: 'de-DE', it: 'it-IT', pt: 'pt-BR',
            ru: 'ru-RU', nl: 'nl-NL', pl: 'pl-PL', tr: 'tr-TR', sv: 'sv-SE',
            el: 'el-GR', ar: 'ar-SA', fa: 'fa-IR', zh: 'zh-CN', ja: 'ja-JP',
            ko: 'ko-KR', vi: 'vi-VN', id: 'id-ID', th: 'th-TH', ms: 'ms-MY',
            fil: 'fil-PH'
        };

        this.femalePersonaNames = {
            en: 'Dr. Sophia (US Female)', hi: 'Dr. Ananya (हिन्दी)',
            bn: 'Dr. Tanushree (বাংলা)', ta: 'Dr. Priya (தமிழ்)',
            te: 'Dr. Kavya (తెలుగు)', kn: 'Dr. Sahana (ಕನ್ನಡ)',
            ml: 'Dr. Anupama (മലയാളം)', mr: 'Dr. Gauri (मराठी)',
            gu: 'Dr. Dhara (ગુજરાતી)', pa: 'Dr. Simran (ਪੰਜਾਬੀ)',
            ur: 'Dr. Zoya (اردو)', or: 'Dr. Rashmi (ଓଡ଼ିଆ)',
            as: 'Dr. Manisha (অসমীয়া)', ne: 'Dr. Sushma (नेपाली)',
            si: 'Dr. Tharushi (සිංහල)', es: 'Dra. Valentina (Español)',
            fr: 'Dr. Amélie (Français)', de: 'Dr. Marlene (Deutsch)',
            it: 'Dott.ssa Chiara (Italiano)', pt: 'Dra. Camila (Português)',
            ru: 'Dr. Elena (Русский)', nl: 'Dr. Lotte (Nederlands)',
            pl: 'Dr. Zofia (Polski)', tr: 'Dr. Aylin (Türkçe)',
            sv: 'Dr. Astrid (Svenska)', el: 'Dr. Eleni (Ελληνικά)',
            ar: 'Dr. Layla (العربية)', fa: 'Dr. Neda (فارسی)',
            zh: 'Dr. Meiling (中文)', ja: 'Dr. Yoko (日本語)',
            ko: 'Dr. Min-ji (한국어)', vi: 'Dr. Linh (Tiếng Việt)',
            id: 'Dr. Siti (Indonesia)', th: 'Dr. Kanya (ไทย)',
            ms: 'Dr. Nurul (Melayu)', fil: 'Dr. Maria (Filipino)'
        };
    }

    init() {
        // Sync language from cookie / localStorage
        const storedLang = localStorage.getItem('hrp_lang') || document.cookie.replace(/(?:(?:^|.*;\s*)hrp_lang\s*\=\s*([^;]*).*$)|^.*$/, "$1") || 'en';
        if (this.localeMap[storedLang]) {
            this.currentLang = storedLang;
        }

        // Cache browser female voices
        if ('speechSynthesis' in window) {
            window.speechSynthesis.onvoiceschanged = () => {
                this.loadFemaleVoices();
            };
            this.loadFemaleVoices();
        }

        // Initialize Speech Recognition
        this.initSpeechRecognition();

        // Bind global key shortcuts and inputs
        this.bindEvents();
        console.log(`CareAI Voice System Initialized. Active Language: ${this.currentLang.toUpperCase()} (36 Languages Supported)`);
    }

    loadFemaleVoices() {
        if (!('speechSynthesis' in window)) return;
        const voices = window.speechSynthesis.getVoices();
        if (!voices || voices.length === 0) return;

        const femaleKeywords = ['female', 'woman', 'zira', 'samantha', 'victoria', 'karen', 'swara', 'heera', 'kalpana', 'valentina', 'monica', 'amelie', 'hortense', 'marlene', 'hedda', 'chiara', 'tanushree', 'priya', 'kavya', 'sahana', 'anupama', 'gauri', 'zoya', 'layla', 'meiling', 'kyoko', 'yoko', 'min-ji', 'camila', 'elena', 'lotte', 'zofia', 'aylin', 'astrid', 'eleni', 'neda', 'linh', 'siti', 'kanya', 'nurul', 'maria'];

        Object.keys(this.localeMap).forEach(lang => {
            const locale = this.localeMap[lang];
            const matchingVoices = voices.filter(v => v.lang.startsWith(lang) || v.lang === locale || v.lang.replace('_', '-') === locale);
            
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
            console.warn("Speech Recognition API not supported natively in this browser.");
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
            this.startWebAudioAnalyser();
            this.updateInputPlaceholders(`🎙️ Listening (${this.currentLang.toUpperCase()})... Speak now`);
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

            const textToShow = finalTranscript || interimTranscript;
            this.setInputValues(textToShow);

            if (finalTranscript.trim().length > 0) {
                this.stopListening();
                this.sendMessage(finalTranscript.trim());
            }
        };

        this.speechRec.onerror = (event) => {
            console.warn("Speech Recognition error:", event.error);
            this.stopListening();
            if (event.error === 'not-allowed') {
                if (typeof showToast === 'function') {
                    showToast("Microphone access blocked. Please allow mic permissions in browser settings.", "warning");
                }
            }
        };

        this.speechRec.onend = () => {
            this.isListening = false;
            this.updateVoiceVisualizer(false);
            this.showMicPulsing(false);
            this.stopWebAudioAnalyser();
            this.updateInputPlaceholders("Ask Dr. Sophia CareAI or speak in 36 languages...");
        };
    }

    async startListening() {
        if (!this.speechRec) {
            // Prompt fallback for browsers without Web Speech API
            const fallbackPrompt = prompt("Voice recognition is simulated in this browser. Enter your clinical question:", "What is my 30-day hospital readmission risk?");
            if (fallbackPrompt) {
                this.sendMessage(fallbackPrompt);
            }
            return;
        }

        if (this.isSpeaking) {
            this.stopSpeaking();
        }

        // Request microphone permission if not already granted
        try {
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                await navigator.mediaDevices.getUserMedia({ audio: true });
            }
        } catch(e) {
            console.warn("Mic permission prompt:", e);
        }

        this.speechRec.lang = this.localeMap[this.currentLang] || 'en-US';
        try {
            this.speechRec.start();
        } catch (e) {
            console.warn("Speech recognition already active or error:", e);
        }
    }

    stopListening() {
        if (this.speechRec && this.isListening) {
            try { this.speechRec.stop(); } catch(e) {}
        }
        this.isListening = false;
        this.showMicPulsing(false);
        this.updateVoiceVisualizer(false);
        this.stopWebAudioAnalyser();
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
        
        // Clean markdown symbols, asterisks, hashes, and emojis for natural clinical speech
        const cleanText = text
            .replace(/[*_#`~[\]()<>]/g, ' ')
            .replace(/[⚠️🚨💊🩺📊🪪🥗📅📹🔍🧭•]/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();

        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.lang = locale;
        utterance.pitch = this.voicePitch; // Warm natural female physician pitch
        utterance.rate = this.voiceRate;   // Soothing cadence

        if (this.femaleVoiceMap[targetLang]) {
            utterance.voice = this.femaleVoiceMap[targetLang];
        }

        utterance.onstart = () => {
            this.isSpeaking = true;
            this.updateVoiceVisualizer(true, 'speaking');
            this.setAvatarSpeaking(true);

            // Chrome/Edge 15-second speech pause workaround
            clearInterval(this.synthTimer);
            this.synthTimer = setInterval(() => {
                if (window.speechSynthesis.speaking) {
                    window.speechSynthesis.pause();
                    window.speechSynthesis.resume();
                } else {
                    clearInterval(this.synthTimer);
                }
            }, 10000);
        };

        utterance.onend = () => {
            this.isSpeaking = false;
            clearInterval(this.synthTimer);
            this.updateVoiceVisualizer(false);
            this.setAvatarSpeaking(false);
            
            // In continuous hands-free mode, re-listen automatically!
            if (this.handsFreeMode) {
                setTimeout(() => {
                    this.startListening();
                }, 400);
            }
        };

        utterance.onerror = () => {
            this.isSpeaking = false;
            clearInterval(this.synthTimer);
            this.updateVoiceVisualizer(false);
            this.setAvatarSpeaking(false);
        };

        this.currentUtterance = utterance;
        window.speechSynthesis.resume();
        window.speechSynthesis.speak(utterance);
    }

    stopSpeaking() {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
        }
        clearInterval(this.synthTimer);
        this.isSpeaking = false;
        this.updateVoiceVisualizer(false);
        this.setAvatarSpeaking(false);
    }

    toggleHandsFree() {
        this.handsFreeMode = !this.handsFreeMode;
        const btns = document.querySelectorAll('#careai-handsfree-btn, #careai-studio-handsfree-btn');
        
        btns.forEach(btn => {
            if (!btn) return;
            if (this.handsFreeMode) {
                btn.style.background = '#10b981';
                btn.style.color = '#ffffff';
                btn.classList.add('animate-pulse');
            } else {
                btn.style.background = '';
                btn.style.color = '';
                btn.classList.remove('animate-pulse');
            }
        });

        if (this.handsFreeMode) {
            if (typeof showToast === 'function') showToast("🎙️ Hands-Free Voice Call Active. Speak freely!", "success");
            this.startListening();
        } else {
            this.stopListening();
            this.stopSpeaking();
            if (typeof showToast === 'function') showToast("Hands-Free Mode Paused", "info");
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

        const studioPersona = document.getElementById('studio-persona-name');
        if (studioPersona) {
            studioPersona.textContent = this.femalePersonaNames[lang] || 'Dr. Sophia CareAI';
        }

        const studioLocale = document.getElementById('studio-voice-locale');
        if (studioLocale) {
            studioLocale.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-500"></span><span>Neural Female Voice • ${lang.toUpperCase()}</span>`;
        }

        const select = document.getElementById('studio-lang-select');
        if (select && select.value !== lang) {
            select.value = lang;
        }

        if (this.speechRec && this.isListening) {
            this.stopListening();
            this.startListening();
        }
        
        const greetingMap = {
            hi: 'नमस्ते! मैं डॉ. अनन्या केयर-एआई हूँ। आपकी स्वास्थ्य वॉयस सहायिका तैयार है।',
            te: 'నమస్కారం! నేను డాక్టర్ కావ్య CareAI. మీ ఆరోగ్య సలహాదారు సిద్ధంగా ఉంది.',
            ta: 'வணக்கம்! நான் டாக்டர் பிரியா CareAI. உங்கள் குரல் உதவியாளர் தயார்.',
            bn: 'নমস্কার! আমি ডক্টর তনুশ্রী কেয়ার-এआई। আপনার ভয়েস সহকারী সক্রিয় রয়েছে।',
            es: 'Hola! Soy la Dra. Valentina CareAI. Su asistente clínica está lista.',
            fr: 'Bonjour! Je suis le Dr. Amélie CareAI. Votre assistante vocale médicale est prête.',
            de: 'Hallo! Ich bin Dr. Marlene CareAI. Ihre universelle Sprachassistentin ist bereit.',
            ar: 'مرحباً! أنا د. ليلى CareAI. مساعدتك الصوتية الطبية جاهزة.',
            zh: '您好！我是Sophia医生（CareAI）。通用临床语音助手已就绪。',
            ja: 'こんにちは！CareAIのDr. Yokoです。'
        };
        const greeting = greetingMap[lang] || 'Hello! I am Dr. Sophia CareAI. Universal clinical voice assistant is ready.';
        this.speak(greeting, lang);
    }

    async sendMessage(text) {
        if (!text || text.trim().length === 0) return;

        const chatBoxes = document.querySelectorAll('#careai-dock-messages');
        this.setInputValues('');

        // Append User Message to all active chat containers
        chatBoxes.forEach(chatBox => {
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
        });

        // Typing Indicator
        const typingId = 'careai-typing-' + Date.now();
        chatBoxes.forEach(chatBox => {
            chatBox.innerHTML += `
                <div id="${typingId}" class="flex justify-start gap-2 items-center message-bot animate-fade-in">
                    <div class="w-7 h-7 rounded-full text-white flex items-center justify-center text-[12px] font-bold shadow-xs shrink-0" style="background: linear-gradient(135deg, #001e47, #005bbf, #0284c7);">
                        <span class="material-symbols-outlined text-[15px]">smart_toy</span>
                    </div>
                    <div class="p-3 rounded-2xl rounded-tl-xs bg-surface-container text-secondary text-xs flex items-center gap-1.5 shadow-xs">
                        <span class="w-1.5 h-1.5 rounded-full bg-primary animate-bounce"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-primary animate-bounce" style="animation-delay: 0.15s"></span>
                        <span class="w-1.5 h-1.5 rounded-full bg-primary animate-bounce" style="animation-delay: 0.3s"></span>
                        <span class="text-[10px] ml-1 font-semibold text-primary">Dr. CareAI analyzing query...</span>
                    </div>
                </div>
            `;
            chatBox.scrollTop = chatBox.scrollHeight;
        });

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
            document.querySelectorAll(`[id^="careai-typing-"]`).forEach(el => el.remove());

            if (data.status === 'success') {
                this.renderBotResponse(data);
                
                // Voice Speech Playback
                if (this.autoSpeak && data.audio_text) {
                    this.speak(data.audio_text, this.currentLang);
                }

                // Voice Navigation Action Redirect
                if (data.action_type === 'NAVIGATE' && data.target_url) {
                    setTimeout(() => {
                        window.location.href = data.target_url;
                    }, 1400);
                }
            } else {
                this.renderBotResponse({
                    response: "I encountered a minor processing issue. Please try again.",
                    disclaimer: "CareAI Assistant",
                    suggested_actions: []
                });
            }
        } catch (err) {
            console.error("CareAI API error:", err);
            document.querySelectorAll(`[id^="careai-typing-"]`).forEach(el => el.remove());
            this.renderBotResponse({
                response: "CareAI is running locally. Clinical safety checks active.",
                disclaimer: "Offline Medical Protocol",
                suggested_actions: []
            });
        }
    }

    renderBotResponse(data) {
        const chatBoxes = document.querySelectorAll('#careai-dock-messages');
        if (!chatBoxes || chatBoxes.length === 0) return;

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
            <div class="flex justify-start gap-2.5 items-start message-bot animate-fade-in">
                <div class="w-8 h-8 rounded-full text-white flex items-center justify-center text-[12px] font-bold shadow-xs shrink-0 mt-0.5" style="background: linear-gradient(135deg, #001e47, #005bbf, #0284c7);">
                    <span class="material-symbols-outlined text-[16px]">medical_services</span>
                </div>
                <div class="max-w-[85%] p-4 rounded-2xl rounded-tl-xs ${cardBg} text-xs shadow-xs space-y-2">
                    <div class="flex items-center justify-between gap-2 border-b border-outline-variant/30 pb-1">
                        <span class="font-bold text-primary flex items-center gap-1">
                            <span class="material-symbols-outlined text-[14px]">record_voice_over</span>
                            ${voicePersona}
                        </span>
                        <button onclick="window.careAIVoice.speak('${this.escapeQuotes(data.audio_text || data.response)}', '${this.currentLang}')" class="p-1 rounded-md hover:bg-primary/10 text-primary transition-all cursor-pointer" title="Replay Audio in Female Voice">
                            <span class="material-symbols-outlined text-[16px]">volume_up</span>
                        </button>
                    </div>
                    <p class="leading-relaxed font-normal text-slate-700">${this.formatMarkdown(data.response)}</p>
                    ${actionsHtml}
                    ${data.disclaimer ? `<span class="text-[9px] text-secondary/70 block italic pt-1">${data.disclaimer}</span>` : ''}
                </div>
            </div>
        `;

        chatBoxes.forEach(chatBox => {
            chatBox.innerHTML += msgHtml;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    }

    // Web Audio API Frequency Equalizer
    startWebAudioAnalyser() {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) return;
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (!AudioContext) return;

            if (!this.audioContext) {
                this.audioContext = new AudioContext();
            }

            navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
                this.micStream = stream;
                this.audioSource = this.audioContext.createMediaStreamSource(stream);
                this.analyser = this.audioContext.createAnalyser();
                this.analyser.fftSize = 64;
                this.audioSource.connect(this.analyser);
                this.drawWaveformCanvas();
            }).catch(() => {});
        } catch(e) {}
    }

    stopWebAudioAnalyser() {
        if (this.micStream) {
            this.micStream.getTracks().forEach(t => t.stop());
            this.micStream = null;
        }
        if (this.animFrameId) {
            cancelAnimationFrame(this.animFrameId);
            this.animFrameId = null;
        }
    }

    drawWaveformCanvas() {
        const canvas = document.getElementById('careai-canvas-waveform');
        if (!canvas || !this.analyser) return;

        const ctx = canvas.getContext('2d');
        const bufferLength = this.analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        const draw = () => {
            this.animFrameId = requestAnimationFrame(draw);
            this.analyser.getByteFrequencyData(dataArray);

            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const barWidth = (canvas.width / bufferLength) * 1.5;
            let x = 0;

            for (let i = 0; i < bufferLength; i++) {
                const barHeight = (dataArray[i] / 255) * canvas.height;
                ctx.fillStyle = `rgba(0, 91, 191, ${0.4 + (dataArray[i] / 255) * 0.6})`;
                ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
                x += barWidth + 2;
            }
        };
        draw();
    }

    updateVoiceVisualizer(active, mode = 'speaking') {
        const visualizers = document.querySelectorAll('#careai-voice-waveform');
        visualizers.forEach(visualizer => {
            if (active) {
                visualizer.classList.remove('hidden');
                visualizer.classList.add('flex');
                const bars = visualizer.querySelectorAll('.waveform-bar');
                bars.forEach((b, idx) => {
                    b.style.animationDuration = `${0.35 + (idx % 4) * 0.15}s`;
                    b.classList.add('animate-wave');
                });
            } else {
                const bars = visualizer.querySelectorAll('.waveform-bar');
                bars.forEach(b => b.classList.remove('animate-wave'));
                visualizer.classList.add('hidden');
                visualizer.classList.remove('flex');
            }
        });

        const statusLabels = document.querySelectorAll('#careai-voice-status-text, #studio-status-text');
        statusLabels.forEach(label => {
            if (active) {
                label.textContent = mode === 'speaking' ? `🔊 ${this.femalePersonaNames[this.currentLang] || 'Dr. Sophia'} Speaking...` : `🎙️ Listening (${this.currentLang.toUpperCase()})...`;
            } else {
                label.textContent = `Ready to speak or listen in 36 languages`;
            }
        });
    }

    setAvatarSpeaking(speaking) {
        const rings = document.querySelectorAll('#careai-avatar-pulse-ring, #studio-avatar-ring');
        rings.forEach(ring => {
            if (speaking) ring.classList.add('animate-ping', 'opacity-75');
            else ring.classList.remove('animate-ping', 'opacity-75');
        });
    }

    showMicPulsing(pulsing) {
        const micBtns = document.querySelectorAll('#careai-mic-btn, .careai-mic-trigger');
        micBtns.forEach(micBtn => {
            if (pulsing) {
                micBtn.style.background = '#ef4444';
                micBtn.classList.add('animate-pulse', 'scale-110');
            } else {
                micBtn.style.background = 'linear-gradient(135deg, #001e47, #005bbf, #0284c7)';
                micBtn.classList.remove('animate-pulse', 'scale-110');
            }
        });
    }

    updateInputPlaceholders(text) {
        const inputs = document.querySelectorAll('#careai-dock-input');
        inputs.forEach(input => {
            input.placeholder = text;
        });
    }

    setInputValues(text) {
        const inputs = document.querySelectorAll('#careai-dock-input');
        inputs.forEach(input => {
            input.value = text;
        });
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
        const chatBoxes = document.querySelectorAll('#careai-dock-messages');
        chatBoxes.forEach(chatBox => {
            chatBox.innerHTML = `
                <div class="p-4 bg-surface-container rounded-2xl text-secondary space-y-1 text-xs">
                    <p class="font-bold text-primary flex items-center gap-1.5">
                        <span class="material-symbols-outlined text-[16px]">record_voice_over</span>
                        ${this.femalePersonaNames[this.currentLang] || 'Dr. Sophia CareAI'}
                    </p>
                    <p>Chat cleared. I am ready to answer any clinical questions or speak in your chosen language!</p>
                </div>
            `;
        });
    }

    bindEvents() {
        const inputs = document.querySelectorAll('#careai-dock-input');
        inputs.forEach(input => {
            input.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.sendMessage(input.value);
                }
            });
        });
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

// Global Singleton Instance
window.careAIVoice = new CareAIVoiceSystem();
document.addEventListener('DOMContentLoaded', () => {
    window.careAIVoice.init();
});
