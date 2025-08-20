class RAGChatbotWidget {
    constructor(config = {}) {
        try {
            this.config = {
                apiBaseUrl: config.apiBaseUrl || this.getApiBaseUrl(),
                position: config.position || 'bottom-right',
                ...config
            };

            this.isOpen = false;
            this.isTyping = false;
            this.recognition = null;
            this.isListening = false;

            console.log('Initializing RAG Chatbot Widget with config:', this.config);

            this.initializeElements();
            this.bindEvents();
            this.initializeSpeechRecognition();

            console.log('RAG Chatbot Widget initialized successfully');
        } catch (error) {
            console.error('Error initializing RAG Chatbot Widget:', error);
            throw error;
        }
    }

    getApiBaseUrl() {
        // Auto-detect API URL based on environment
        const hostname = window.location.hostname;

        if (hostname === 'localhost' || hostname === '127.0.0.1') {
            return 'http://localhost:8000';
        } else {
            // Replace with your actual backend URL on Render
            return 'https://ai-chat-bot-ote0.onrender.com';
        }
    }

    initializeElements() {
        this.toggle = document.getElementById('ragChatbotToggle');
        this.widget = document.getElementById('ragChatbotWidget');
        this.closeBtn = document.getElementById('ragChatbotClose');
        this.messages = document.getElementById('ragChatbotMessages');
        this.inputField = document.getElementById('ragChatbotInputField');
        this.sendBtn = document.getElementById('ragChatbotSendBtn');
        this.voiceBtn = document.getElementById('ragChatbotVoiceBtn');
        this.typing = document.getElementById('ragChatbotTyping');
    }

    bindEvents() {
        this.toggle.addEventListener('click', () => this.toggleWidget());
        this.closeBtn.addEventListener('click', () => this.closeWidget());
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.voiceBtn.addEventListener('click', () => this.toggleVoiceInput());

        this.inputField.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        this.inputField.addEventListener('input', () => {
            const hasText = this.inputField.value.trim().length > 0;
            this.sendBtn.classList.toggle('active', hasText);
        });
    }

    initializeSpeechRecognition() {
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            this.recognition = new SpeechRecognition();
            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = 'en-US';

            this.recognition.onresult = (event) => {
                const transcript = event.results[0][0].transcript;
                this.inputField.value = transcript;
                this.sendBtn.classList.add('active');
                this.stopListening();
            };

            this.recognition.onerror = () => {
                this.stopListening();
            };

            this.recognition.onend = () => {
                this.stopListening();
            };
        } else {
            this.voiceBtn.style.display = 'none';
        }
    }

    toggleWidget() {
        if (this.isOpen) {
            this.closeWidget();
        } else {
            this.openWidget();
        }
    }

    openWidget() {
        this.widget.classList.add('open');
        this.isOpen = true;
        this.inputField.focus();
    }

    closeWidget() {
        this.widget.classList.remove('open');
        this.isOpen = false;
    }

    toggleVoiceInput() {
        if (!this.recognition) return;

        if (this.isListening) {
            this.stopListening();
        } else {
            this.startListening();
        }
    }

    startListening() {
        if (!this.recognition) return;

        this.isListening = true;
        this.voiceBtn.style.background = '#ff4444';
        this.inputField.placeholder = 'Listening...';
        this.recognition.start();
    }

    stopListening() {
        this.isListening = false;
        this.voiceBtn.style.background = '';
        this.inputField.placeholder = 'Type your question here...';
        if (this.recognition) {
            this.recognition.stop();
        }
    }

    async sendMessage() {
        const message = this.inputField.value.trim();
        if (!message || this.isTyping) return;

        this.addMessage(message, 'user');
        this.inputField.value = '';
        this.sendBtn.classList.remove('active');

        this.showTyping();

        try {
            const response = await fetch(`${this.config.apiBaseUrl}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: message })
            });

            const data = await response.json();

            if (response.ok) {
                this.hideTyping();
                this.addMessage(data.response, 'bot');
            } else {
                throw new Error(data.detail || 'Failed to get response');
            }
        } catch (error) {
            this.hideTyping();
            this.addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            console.error('Chat error:', error);
        }
    }


    addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `rag-chatbot-message ${sender}`;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'rag-chatbot-message-content';
        contentDiv.textContent = text;

        messageDiv.appendChild(contentDiv);
        this.messages.insertBefore(messageDiv, this.typing);

        this.scrollToBottom();
    }

    showTyping() {
        this.isTyping = true;
        this.typing.classList.add('show');
        this.scrollToBottom();
    }

    hideTyping() {
        this.isTyping = false;
        this.typing.classList.remove('show');
    }

    scrollToBottom() {
        setTimeout(() => {
            this.messages.scrollTop = this.messages.scrollHeight;
        }, 100);
    }
}

// Initialize the widget when the page loads
document.addEventListener('DOMContentLoaded', function () {
    // You can customize the configuration here
    window.ragChatbot = new RAGChatbotWidget({
        // apiBaseUrl will be auto-detected by getApiBaseUrl() method
        position: 'bottom-right'
    });
});