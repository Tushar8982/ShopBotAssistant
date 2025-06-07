// Chat functionality for ShopBot Assistant
class ChatBot {
    constructor() {
        this.chatWindow = document.getElementById('chatWindow');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.typingIndicator = document.getElementById('typingIndicator');
        this.quickActionButtons = document.querySelectorAll('.quick-action');
        
        this.init();
    }
    
    init() {
        // Event listeners
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        // Quick action buttons
        this.quickActionButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                const action = e.currentTarget.dataset.action;
                this.handleQuickAction(action);
            });
        });
        
        // Auto-focus on input
        this.messageInput.focus();
    }
    
    async sendMessage() {
        const message = this.messageInput.value.trim();
        if (!message) return;
        
        // Disable input while sending
        this.toggleInputState(false);
        
        // Add user message to chat
        this.addMessage(message, 'user');
        
        // Clear input
        this.messageInput.value = '';
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            // Send message to backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            // Hide typing indicator
            this.hideTypingIndicator();
            
            if (data.status === 'success') {
                // Add bot response to chat
                this.addMessage(data.response, 'bot');
            } else {
                // Handle error response
                this.addMessage(data.error || 'Sorry, something went wrong. Please try again.', 'bot', true);
            }
            
        } catch (error) {
            console.error('Error sending message:', error);
            this.hideTypingIndicator();
            this.addMessage('Sorry, I\'m having trouble connecting right now. Please check your internet connection and try again.', 'bot', true);
        } finally {
            // Re-enable input
            this.toggleInputState(true);
            this.messageInput.focus();
        }
    }
    
    addMessage(content, sender, isError = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = sender === 'bot' ? '<i class="fas fa-robot"></i>' : '<i class="fas fa-user"></i>';
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        
        const bubble = document.createElement('div');
        bubble.className = `message-bubble ${sender}-bubble`;
        
        if (isError) {
            bubble.classList.add('error-message');
        }
        
        // Format content with line breaks and preserve formatting
        bubble.innerHTML = this.formatMessage(content);
        
        const time = document.createElement('div');
        time.className = 'message-time';
        time.textContent = this.getCurrentTime();
        
        messageContent.appendChild(bubble);
        messageContent.appendChild(time);
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        
        this.chatWindow.appendChild(messageDiv);
        this.scrollToBottom();
    }
    
    formatMessage(message) {
        // Convert line breaks to HTML and preserve formatting
        return message
            .replace(/\n/g, '<br>')
            .replace(/•/g, '•')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>');
    }
    
    handleQuickAction(action) {
        // Map actions to messages
        const actionMessages = {
            'laptops': 'Show me laptops',
            'my_orders': 'I want to check my orders',
            'track_order': 'I need to track my order',
            'recommendations': 'Can you give me some recommendations?'
        };
        
        const message = actionMessages[action];
        if (message) {
            this.messageInput.value = message;
            this.sendMessage();
        }
    }
    
    showTypingIndicator() {
        this.typingIndicator.style.display = 'flex';
        this.scrollToBottom();
    }
    
    hideTypingIndicator() {
        this.typingIndicator.style.display = 'none';
    }
    
    toggleInputState(enabled) {
        this.messageInput.disabled = !enabled;
        this.sendButton.disabled = !enabled;
        
        if (enabled) {
            this.sendButton.classList.remove('loading');
        } else {
            this.sendButton.classList.add('loading');
        }
    }
    
    scrollToBottom() {
        setTimeout(() => {
            this.chatWindow.scrollTop = this.chatWindow.scrollHeight;
        }, 100);
    }
    
    getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }
}

// Initialize chat when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ChatBot();
});

// Add some additional utility functions
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth hover effects to quick action buttons
    const quickActions = document.querySelectorAll('.quick-action');
    quickActions.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Add ripple effect to send button
    const sendBtn = document.getElementById('sendButton');
    sendBtn.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');
        
        this.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
    
    // Auto-resize textarea functionality for future enhancements
    const messageInput = document.getElementById('messageInput');
    messageInput.addEventListener('input', function() {
        // Could add auto-resize functionality here if needed
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
});

// Add CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
