import re
import random
from datetime import datetime

def interpret_message(message):
    """
    Process user messages and return appropriate responses based on keywords and context.
    
    Args:
        message (str): The user's input message
        
    Returns:
        str: Bot response based on message interpretation
    """
    # Convert to lowercase for easier matching
    message_lower = message.lower().strip()
    
    # Define keyword patterns and responses
    patterns = {
        'greeting': {
            'keywords': ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening'],
            'responses': [
                "Hello! 👋 Welcome to ShopBot Assistant! How can I help you today?",
                "Hi there! I'm here to help you with your shopping needs. What are you looking for?",
                "Hey! Great to see you here. I can help you find products, check orders, or answer any shopping questions!"
            ]
        },
        'laptop': {
            'keywords': ['laptop', 'laptops', 'notebook', 'computer', 'pc'],
            'responses': [
                "🖥️ Looking for laptops? I can help you find the perfect one! What's your budget and intended use?",
                "Great choice! We have a wide selection of laptops. Are you looking for gaming, business, or general use?",
                "Laptops are one of our popular categories! What specifications are you looking for?"
            ]
        },
        'order_status': {
            'keywords': ['order', 'orders', 'my order', 'order status', 'track', 'tracking'],
            'responses': [
                "📦 I can help you track your order! Please provide your order number or email address.",
                "Let me help you check your order status. Do you have your order number handy?",
                "To track your order, I'll need either your order number or the email address used for the purchase."
            ]
        },
        'return_exchange': {
            'keywords': ['return', 'exchange', 'refund', 'send back'],
            'responses': [
                "🔄 I understand you'd like to return or exchange an item. Can you tell me more about the issue?",
                "Returns and exchanges are easy! What item would you like to return and what's the reason?",
                "I can help with returns and exchanges. Do you have your order number ready?"
            ]
        },
        'buy_purchase': {
            'keywords': ['buy', 'purchase', 'price', 'cost', 'how much'],
            'responses': [
                "💰 Ready to make a purchase? What product are you interested in?",
                "I can help you find pricing information! What item are you looking to buy?",
                "Great! What product would you like to purchase? I can provide details and pricing."
            ]
        },
        'recommendations': {
            'keywords': ['recommend', 'suggestion', 'what should', 'best', 'popular'],
            'responses': [
                "🌟 I'd love to give you personalized recommendations! What type of product are you looking for?",
                "For the best recommendations, tell me what you're shopping for and your preferences!",
                "I can suggest popular items based on your needs. What category interests you?"
            ]
        },
        'help': {
            'keywords': ['help', 'support', 'assistance', 'what can you do'],
            'responses': [
                """🤝 I'm here to help! I can assist you with:
• Finding and recommending products
• Checking order status and tracking
• Processing returns and exchanges
• Answering product questions
• Providing shopping guidance

What would you like help with?""",
                """I can help you with various shopping tasks:
• Product searches and recommendations
• Order tracking and status updates  
• Returns and exchanges
• Pricing and availability
• General shopping questions

How can I assist you today?"""
            ]
        }
    }
    
    # Check for specific patterns
    for category, data in patterns.items():
        for keyword in data['keywords']:
            if keyword in message_lower:
                return random.choice(data['responses'])
    
    # Handle specific product searches
    if any(word in message_lower for word in ['find', 'search', 'looking for', 'need']):
        return "🔍 I can help you find what you're looking for! Could you be more specific about the product or category you're interested in?"
    
    # Handle pricing questions
    if any(word in message_lower for word in ['price', 'cost', 'expensive', 'cheap', 'budget']):
        return "💲 I can help with pricing information! What specific product are you asking about?"
    
    # Handle availability questions
    if any(word in message_lower for word in ['available', 'in stock', 'stock']):
        return "📦 I can check product availability for you! Which item are you interested in?"
    
    # Handle shipping questions
    if any(word in message_lower for word in ['shipping', 'delivery', 'ship', 'deliver']):
        return "🚚 I can provide shipping information! Are you asking about delivery times, costs, or tracking?"
    
    # Handle payment questions
    if any(word in message_lower for word in ['payment', 'pay', 'credit card', 'paypal']):
        return "💳 We accept various payment methods including credit cards, PayPal, and more. What payment question can I help with?"
    
    # Handle warranty/guarantee questions
    if any(word in message_lower for word in ['warranty', 'guarantee', 'protection']):
        return "🛡️ I can provide warranty information! Which product are you asking about?"
    
    # Default response for unrecognized messages
    default_responses = [
        "I want to help you! Could you please rephrase your question or tell me more about what you're looking for?",
        "I'm not sure I understood that completely. Are you looking for products, need help with an order, or have other shopping questions?",
        "Let me help you better! Try asking about products, orders, returns, or use our quick action buttons above.",
        """I didn't quite catch that. Here's what I can help with:
• Product searches and recommendations
• Order tracking and status
• Returns and exchanges
• General shopping questions

What would you like assistance with?"""
    ]
    
    return random.choice(default_responses)

def get_quick_response(action):
    """
    Handle quick action responses for toolbar buttons
    
    Args:
        action (str): The quick action selected
        
    Returns:
        str: Appropriate response for the action
    """
    quick_responses = {
        'laptops': "🖥️ Here are our laptop categories:\n• Gaming Laptops\n• Business Laptops\n• Student Laptops\n• Ultrabooks\n\nWhich type interests you?",
        'my_orders': "📋 To view your orders, I'll need your email address or account information. You can also check your order status by providing an order number.",
        'track_order': "📦 I can help you track your order! Please provide:\n• Your order number, OR\n• Email address used for the purchase",
        'recommendations': "🌟 I'd love to recommend products for you! What are you shopping for today?\n• Electronics\n• Clothing\n• Home & Garden\n• Sports & Outdoors\n• Books & Media"
    }
    
    return quick_responses.get(action, "I can help you with that! Please tell me more about what you need.")
