#!/usr/bin/env python3
"""
Fix database initialization issues by ensuring proper setup
"""
import os
import sys
from werkzeug.security import generate_password_hash

# Set required environment variables
os.environ['SESSION_SECRET'] = 'dev-secret-key-123'
os.environ['DATABASE_URL'] = 'sqlite:///shopbot.db'

# Import after setting environment variables
from app import app, db
from models import User, Product, ChatMessage, Order, OrderItem

def fix_database():
    """Fix database issues by recreating everything properly"""
    try:
        with app.app_context():
            print("Dropping all existing tables...")
            db.drop_all()
            
            print("Creating all tables with proper schema...")
            db.create_all()
            
            # Create sample user
            print("Creating sample users...")
            users = [
                User(
                    name='John Doe',
                    email='john@example.com',
                    password_hash=generate_password_hash('password123')
                ),
                User(
                    name='Jane Smith',
                    email='jane@example.com',
                    password_hash=generate_password_hash('password123')
                )
            ]
            
            for user in users:
                db.session.add(user)
            
            # Create sample products with all required fields
            print("Creating sample products...")
            products = [
                Product(
                    name='Dell XPS 13',
                    description='Ultra-portable laptop with excellent performance',
                    price=999.99,
                    category='Laptops',
                    brand='Dell',
                    sku='DELL-XPS-13',
                    stock_quantity=50,
                    in_stock=True,
                    rating=4.5,
                    reviews_count=123
                ),
                Product(
                    name='iPhone 15 Pro',
                    description='Latest iPhone with advanced camera system',
                    price=1199.99,
                    category='Smartphones',
                    brand='Apple',
                    sku='IPHONE-15-PRO',
                    stock_quantity=30,
                    in_stock=True,
                    rating=4.7,
                    reviews_count=89
                ),
                Product(
                    name='Sony WH-1000XM5',
                    description='Industry-leading noise canceling headphones',
                    price=399.99,
                    category='Headphones',
                    brand='Sony',
                    sku='SONY-WH-1000XM5',
                    stock_quantity=75,
                    in_stock=True,
                    rating=4.6,
                    reviews_count=234
                ),
                Product(
                    name='iPad Air',
                    description='Powerful tablet for work and creativity',
                    price=599.99,
                    category='Tablets',
                    brand='Apple',
                    sku='IPAD-AIR-2024',
                    stock_quantity=40,
                    in_stock=True,
                    rating=4.4,
                    reviews_count=156
                ),
                Product(
                    name='Samsung Galaxy Watch 6',
                    description='Advanced smartwatch with health monitoring',
                    price=329.99,
                    category='Smart Watches',
                    brand='Samsung',
                    sku='GALAXY-WATCH-6',
                    stock_quantity=60,
                    in_stock=True,
                    rating=4.3,
                    reviews_count=78
                )
            ]
            
            for product in products:
                db.session.add(product)
            
            db.session.commit()
            
            print("Database setup completed successfully!")
            print(f"Created {len(users)} users and {len(products)} products")
            print("Demo login: john@example.com / password123")
            return True
            
    except Exception as e:
        print(f"Error setting up database: {e}")
        return False

if __name__ == "__main__":
    success = fix_database()
    if success:
        print("\n✅ Database is now ready!")
        print("You can now run: python main.py")
    else:
        print("\n❌ Database setup failed")
        sys.exit(1)