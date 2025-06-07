# ShopBot Assistant - E-commerce Sales Chatbot

A comprehensive full-stack e-commerce chatbot application built with Flask, featuring real-time product search, user authentication, order tracking, and intelligent conversational AI for customer assistance.

## 🚀 Project Overview

ShopBot Assistant is an advanced e-commerce sales chatbot designed to enhance the shopping experience by enabling efficient search, exploration, and purchase processes. The application provides a modern, responsive interface with real-time chat capabilities, comprehensive product management, and secure user authentication.

### Key Features

- **🤖 Intelligent Chatbot**: Natural language processing with real-time product search and recommendations
- **🔐 User Authentication**: Secure login/registration system with session management
- **📱 Responsive Design**: Mobile-first design compatible with desktop, tablet, and mobile devices
- **🛍️ Product Catalog**: Advanced search and filtering with 100+ electronics products
- **📦 Order Management**: Order tracking and history with detailed status timelines
- **💬 Chat Management**: Session continuity, conversation reset, and chat history
- **🎯 Quick Actions**: One-click shortcuts for common queries

## 🛠️ Technology Stack

### Backend
- **Python 3.11**: Core programming language
- **Flask**: Lightweight web application framework
- **SQLAlchemy**: Object-Relational Mapping (ORM)
- **PostgreSQL**: Production-grade relational database
- **Gunicorn**: WSGI HTTP Server for production deployment

### Frontend
- **HTML5**: Modern semantic markup
- **CSS3**: Custom styling with CSS Grid and Flexbox
- **Bootstrap 5.3**: Responsive UI component framework
- **JavaScript ES6+**: Interactive functionality and AJAX communication
- **Font Awesome**: Icon library for enhanced UX

### Database Schema
- **User Management**: Authentication and profile data
- **Product Catalog**: Comprehensive product information with specifications
- **Order System**: Complete order lifecycle management
- **Chat History**: Persistent conversation storage with session tracking

## 📁 Project Structure

```
shopbot-assistant/
├── app.py                 # Main Flask application
├── main.py               # Application entry point
├── models.py             # Database models and relationships
├── populate_data.py      # Database population script
├── requirements.txt      # Python dependencies
├── chatbot/
│   ├── __init__.py      # Package initialization
│   └── logic.py         # Chatbot intelligence and product search
├── static/
│   ├── css/
│   │   └── style.css    # Custom styling
│   └── js/
│       └── chat.js      # Chat functionality and UI interactions
├── templates/
│   ├── index.html       # Main chat interface
│   ├── login.html       # User authentication
│   ├── register.html    # User registration
│   ├── products.html    # Product catalog page
│   └── orders.html      # Order management page
└── README.md            # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- PostgreSQL database
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shopbot-assistant
   ```

2. **Set up environment variables**
   ```bash
   export SESSION_SECRET="your-secret-key-here"
   export DATABASE_URL="postgresql://user:password@localhost/shopbot_db"
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python populate_data.py
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the application**
   - Open your browser to `http://localhost:5000`
   - Use demo credentials: `john@example.com` / `password123`

## 💾 Database Population

The application includes a comprehensive data population script that creates:

- **139 Electronics Products** across 8 categories:
  - Laptops (Dell, HP, Lenovo, Apple, ASUS, Acer, MSI)
  - Smartphones (Apple, Samsung, Google, OnePlus, Xiaomi)
  - Tablets (Apple, Samsung, Microsoft, Lenovo, Amazon)
  - Headphones (Sony, Bose, Apple, Sennheiser, Audio-Technica)
  - Smart Watches (Apple, Samsung, Fitbit, Garmin, Fossil)
  - Gaming Consoles (Sony, Microsoft, Nintendo)
  - Monitors (Dell, LG, Samsung, ASUS, Acer, BenQ)
  - Keyboards (Logitech, Corsair, Razer, SteelSeries, Keychron)

- **Sample Users** for testing authentication
- **Order History** with various status states
- **Realistic Product Data** including specifications, pricing, and ratings

## 🤖 Chatbot Capabilities

### Intelligent Product Search
- Real-time database queries based on natural language input
- Category-specific recommendations
- Price range filtering and availability checking
- Brand and specification matching

### Conversation Management
- Session continuity across page refreshes
- Chat history persistence
- Conversation reset functionality
- Contextual response generation

### Supported Queries
- Product searches: "Show me laptops under $1000"
- Order tracking: "Track my order ORD20250607001"
- Recommendations: "What are your best smartphones?"
- General assistance: "Help me find gaming equipment"

## 🔧 API Endpoints

### Authentication
- `POST /login` - User authentication
- `POST /register` - New user registration
- `GET /logout` - User logout

### Chat Interface
- `POST /chat` - Process chat messages
- `GET /api/chat/history` - Retrieve chat history
- `POST /api/chat/reset` - Reset chat session

### Product Management
- `GET /api/products` - Search and filter products
- Support for pagination, category filtering, price ranges

## 🎨 User Interface Design

### Design Principles
- **Modern & Clean**: Minimalist design with intuitive navigation
- **Responsive Layout**: Optimized for all device sizes
- **Accessibility**: WCAG compliant with keyboard navigation
- **Performance**: Optimized loading and smooth animations

### Color Scheme
- Primary: `#0d6efd` (Bootstrap Blue)
- Secondary: `#6c757d` (Neutral Gray)
- Success: `#198754` (Green)
- Warning: `#ffc107` (Amber)
- Background: `#f0f2f5` (Light Gray)

### Interactive Elements
- Smooth hover transitions
- Loading indicators
- Typing animations
- Real-time message timestamps
- Responsive button states

## 🧪 Testing & Quality Assurance

### Manual Testing Scenarios
1. **User Registration/Login Flow**
2. **Product Search Functionality**
3. **Chat Interface Responsiveness**
4. **Order Tracking System**
5. **Session Management**
6. **Mobile Device Compatibility**

### Error Handling
- Graceful database connection failures
- Invalid user input validation
- Network connectivity issues
- Session timeout management

## 🚀 Deployment Considerations

### Production Setup
- Configure PostgreSQL for production workloads
- Set up SSL/TLS encryption
- Implement rate limiting
- Configure logging and monitoring
- Set secure session keys

### Performance Optimization
- Database query optimization with indexing
- Image optimization and CDN integration
- Caching strategies for frequent queries
- Frontend asset minification

## 🔮 Future Enhancements

### Planned Features
- **Shopping Cart**: Add to cart and checkout functionality
- **Payment Integration**: Stripe/PayPal payment processing
- **Advanced Filters**: More granular product filtering
- **Wishlist System**: Save favorite products
- **Review System**: Customer product reviews and ratings
- **Live Chat**: Real-time agent assistance
- **Mobile App**: Native iOS/Android applications

### Technical Improvements
- **Elasticsearch**: Advanced product search capabilities
- **Redis Caching**: Improved performance for frequent queries
- **API Documentation**: Swagger/OpenAPI integration
- **Unit Testing**: Comprehensive test coverage
- **CI/CD Pipeline**: Automated testing and deployment

## 🐛 Known Issues & Limitations

1. **Order Creation**: Currently displays sample orders (demo data)
2. **Payment Processing**: Not implemented in current version
3. **Email Notifications**: Order status notifications pending
4. **Advanced Search**: Full-text search could be enhanced

## 📞 Support & Contribution

### Getting Help
- Check the documentation and README
- Review the codebase for implementation details
- Test with provided demo credentials

### Development Guidelines
- Follow PEP 8 style guidelines for Python code
- Use semantic HTML5 and modern CSS practices
- Implement responsive design principles
- Maintain comprehensive error handling
- Write clear, documented code

## 📄 License

This project is developed as part of an internship case study for Uplyft and demonstrates full-stack web development capabilities with modern technologies.

---

**ShopBot Assistant** - Enhancing e-commerce through intelligent conversation and seamless user experience.