import re
import random
import json
from datetime import datetime
from sqlalchemy import or_

def search_products(query, category=None, limit=5):
    """Search for products in the database"""
    try:
        from models import Product
        
        # Build the search query
        search_query = Product.query.filter(Product.in_stock == True)
        
        if query:
            search_terms = query.lower().strip()
            search_query = search_query.filter(
                or_(
                    Product.name.ilike(f'%{search_terms}%'),
                    Product.description.ilike(f'%{search_terms}%'),
                    Product.category.ilike(f'%{search_terms}%'),
                    Product.brand.ilike(f'%{search_terms}%')
                )
            )
        
        if category:
            search_query = search_query.filter(Product.category.ilike(f'%{category}%'))
        
        products = search_query.limit(limit).all()
        return products
    except Exception as e:
        print(f"Error searching products: {e}")
        import traceback
        traceback.print_exc()
        return []

def format_product_results(products):
    """Format product search results for display"""
    if not products:
        return "I couldn't find any products matching your criteria. Try searching for laptops, smartphones, tablets, headphones, or other electronics."
    
    result = f"I found {len(products)} product{'s' if len(products) > 1 else ''} for you:\n\n"
    
    for product in products:
        result += f"🔹 **{product.name}**\n"
        result += f"   💰 ${product.price:.2f}\n"
        result += f"   📦 {product.category} by {product.brand}\n"
        if product.rating > 0:
            result += f"   ⭐ {product.rating}/5.0 ({product.reviews_count} reviews)\n"
        result += f"   📝 {product.description[:100]}{'...' if len(product.description) > 100 else ''}\n\n"
    
    if len(products) == 5:
        result += "💡 This is a limited preview. Use the Products page to see more options and filter results!"
    
    return result

def get_product_recommendations(category=None):
    """Get product recommendations"""
    try:
        from models import Product
        
        query = Product.query.filter(Product.in_stock == True)
        
        if category:
            query = query.filter(Product.category.ilike(f'%{category}%'))
        
        # Get top rated products
        products = query.filter(Product.rating >= 4.0).order_by(Product.rating.desc(), Product.reviews_count.desc()).limit(5).all()
        
        if not products:
            products = query.order_by(Product.created_at.desc()).limit(5).all()
        
        return products
    except Exception as e:
        print(f"Error getting recommendations: {e}")
        import traceback
        traceback.print_exc()
        return []

def get_recommendation_response():
    """Get personalized recommendations"""
    products = get_product_recommendations()
    if products:
        return "🌟 Here are my top recommendations based on popular and highly-rated products:\n\n" + format_product_results(products)
    else:
        return "🌟 I'd love to give you personalized recommendations! What type of product are you looking for? Try asking about laptops, smartphones, headphones, or other electronics."

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
    
    # Handle product searches with real database data
    product_keywords = ['laptop', 'laptops', 'smartphone', 'phone', 'tablet', 'headphone', 'headphones', 'watch', 'smartwatch', 'console', 'gaming', 'monitor', 'keyboard', 'mouse']
    
    # Check for product search keywords
    for keyword in product_keywords:
        if keyword in message_lower:
            if keyword in ['laptop', 'laptops']:
                products = search_products(message, 'Laptops')
                if products:
                    return format_product_results(products)
                else:
                    return "🖥️ I'd love to help you find laptops! Let me search our database... It seems we might be having connectivity issues. Please try again in a moment."
            
            elif keyword in ['smartphone', 'phone']:
                products = search_products(message, 'Smartphones')
                if products:
                    return format_product_results(products)
                else:
                    return "📱 Looking for smartphones? Let me check our inventory... Please try again in a moment."
            
            elif keyword in ['tablet']:
                products = search_products(message, 'Tablets')
                if products:
                    return format_product_results(products)
                else:
                    return "📱 I can help you find tablets! Let me search our database..."
            
            elif keyword in ['headphone', 'headphones']:
                products = search_products(message, 'Headphones')
                if products:
                    return format_product_results(products)
                else:
                    return "🎧 Looking for headphones? Let me find some great options for you..."
            
            elif keyword in ['watch', 'smartwatch']:
                products = search_products(message, 'Smart Watches')
                if products:
                    return format_product_results(products)
                else:
                    return "⌚ I can help you find smartwatches! Checking our inventory..."
            
            elif keyword in ['console', 'gaming']:
                products = search_products(message, 'Gaming')
                if products:
                    return format_product_results(products)
                else:
                    return "🎮 Looking for gaming equipment? Let me search our collection..."
            
            elif keyword in ['monitor']:
                products = search_products(message, 'Monitors')
                if products:
                    return format_product_results(products)
                else:
                    return "🖥️ I can help you find monitors! Searching our database..."
            
            elif keyword in ['keyboard']:
                products = search_products(message, 'Keyboards')
                if products:
                    return format_product_results(products)
                else:
                    return "⌨️ Looking for keyboards? Let me check what we have available..."

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
            'responses': []
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
                if category == 'recommendations':
                    return get_recommendation_response()
                else:
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
