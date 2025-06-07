#!/usr/bin/env python3
"""
Script to populate the database with 100+ mock e-commerce products
for electronics category as specified in the case study requirements.
"""

import os
import sys
import json
from datetime import datetime, timedelta
import random

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models import Product, User, Order, OrderItem
from werkzeug.security import generate_password_hash

def create_sample_users():
    """Create sample users for testing"""
    users = [
        {
            'name': 'John Doe',
            'email': 'john@example.com',
            'password': 'password123'
        },
        {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'password': 'password123'
        },
        {
            'name': 'Mike Johnson',
            'email': 'mike@example.com',
            'password': 'password123'
        }
    ]
    
    for user_data in users:
        existing_user = User.query.filter_by(email=user_data['email']).first()
        if not existing_user:
            user = User(
                name=user_data['name'],
                email=user_data['email'],
                password_hash=generate_password_hash(user_data['password'])
            )
            db.session.add(user)
    
    db.session.commit()
    print("Sample users created successfully!")

def create_electronics_products():
    """Create 100+ electronics products across different categories"""
    
    # Define product categories and their specifications
    categories = {
        'Laptops': {
            'brands': ['Dell', 'HP', 'Lenovo', 'Apple', 'ASUS', 'Acer', 'MSI'],
            'base_price_range': (500, 3000),
            'specs_template': {
                'processor': ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9', 'AMD Ryzen 5', 'AMD Ryzen 7', 'Apple M1', 'Apple M2'],
                'ram': ['8GB', '16GB', '32GB', '64GB'],
                'storage': ['256GB SSD', '512GB SSD', '1TB SSD', '2TB SSD', '1TB HDD'],
                'display': ['13.3"', '14"', '15.6"', '17.3"'],
                'graphics': ['Integrated', 'NVIDIA GTX 1650', 'NVIDIA RTX 3060', 'NVIDIA RTX 4070']
            }
        },
        'Smartphones': {
            'brands': ['Apple', 'Samsung', 'Google', 'OnePlus', 'Xiaomi', 'Huawei'],
            'base_price_range': (200, 1500),
            'specs_template': {
                'display': ['5.4"', '6.1"', '6.4"', '6.7"', '6.8"'],
                'storage': ['64GB', '128GB', '256GB', '512GB', '1TB'],
                'camera': ['12MP', '48MP', '64MP', '108MP'],
                'battery': ['3000mAh', '4000mAh', '5000mAh']
            }
        },
        'Tablets': {
            'brands': ['Apple', 'Samsung', 'Microsoft', 'Lenovo', 'Amazon'],
            'base_price_range': (150, 1200),
            'specs_template': {
                'display': ['8"', '10.1"', '10.9"', '11"', '12.9"'],
                'storage': ['32GB', '64GB', '128GB', '256GB', '512GB'],
                'connectivity': ['Wi-Fi', 'Wi-Fi + Cellular']
            }
        },
        'Headphones': {
            'brands': ['Sony', 'Bose', 'Apple', 'Sennheiser', 'Audio-Technica', 'Beats'],
            'base_price_range': (50, 500),
            'specs_template': {
                'type': ['Over-ear', 'On-ear', 'In-ear', 'True Wireless'],
                'connectivity': ['Wired', 'Bluetooth 5.0', 'Bluetooth 5.2'],
                'features': ['Noise Cancelling', 'Water Resistant', 'Voice Assistant']
            }
        },
        'Smart Watches': {
            'brands': ['Apple', 'Samsung', 'Fitbit', 'Garmin', 'Fossil'],
            'base_price_range': (100, 800),
            'specs_template': {
                'display': ['1.4"', '1.6"', '1.9"'],
                'battery_life': ['1 day', '3 days', '7 days', '14 days'],
                'features': ['GPS', 'Heart Rate Monitor', 'Water Resistant', 'Sleep Tracking']
            }
        },
        'Gaming Consoles': {
            'brands': ['Sony', 'Microsoft', 'Nintendo'],
            'base_price_range': (200, 600),
            'specs_template': {
                'storage': ['512GB', '1TB', '2TB'],
                'resolution': ['1080p', '4K', '8K'],
                'features': ['Backwards Compatible', 'Online Gaming', 'Media Player']
            }
        },
        'Monitors': {
            'brands': ['Dell', 'LG', 'Samsung', 'ASUS', 'Acer', 'BenQ'],
            'base_price_range': (150, 1000),
            'specs_template': {
                'size': ['21"', '24"', '27"', '32"', '34"'],
                'resolution': ['1080p', '1440p', '4K'],
                'refresh_rate': ['60Hz', '75Hz', '144Hz', '240Hz'],
                'panel_type': ['IPS', 'VA', 'TN', 'OLED']
            }
        },
        'Keyboards': {
            'brands': ['Logitech', 'Corsair', 'Razer', 'SteelSeries', 'Keychron'],
            'base_price_range': (30, 300),
            'specs_template': {
                'type': ['Mechanical', 'Membrane', 'Wireless'],
                'layout': ['Full Size', 'TKL', '60%', '65%'],
                'switches': ['Cherry MX Red', 'Cherry MX Blue', 'Cherry MX Brown']
            }
        }
    }
    
    products_created = 0
    
    for category, config in categories.items():
        # Create 15-20 products per category
        products_per_category = random.randint(15, 20)
        
        for i in range(products_per_category):
            brand = random.choice(config['brands'])
            
            # Generate product name
            if category == 'Laptops':
                model_names = ['Pro', 'Air', 'Elite', 'Pavilion', 'ThinkPad', 'Inspiron', 'Spectre', 'Envy']
                model = random.choice(model_names)
                product_name = f"{brand} {model} {random.randint(13, 17)}"
            elif category == 'Smartphones':
                model_names = ['iPhone', 'Galaxy', 'Pixel', 'OnePlus', 'Mi', 'P']
                model = random.choice(model_names)
                product_name = f"{brand} {model} {random.randint(10, 15)}"
            else:
                product_name = f"{brand} {category[:-1]} {random.randint(100, 999)}"
            
            # Generate price
            min_price, max_price = config['base_price_range']
            price = round(random.uniform(min_price, max_price), 2)
            
            # Generate specifications
            specs = {}
            for spec_type, options in config['specs_template'].items():
                specs[spec_type] = random.choice(options)
            
            # Generate description
            description = f"High-quality {category[:-1].lower()} from {brand}. "
            description += " ".join([f"{k.replace('_', ' ').title()}: {v}" for k, v in specs.items()])
            
            # Generate other attributes
            stock_quantity = random.randint(0, 100)
            in_stock = stock_quantity > 0
            rating = round(random.uniform(3.5, 5.0), 1)
            reviews_count = random.randint(10, 500)
            
            # Generate SKU
            sku = f"{brand[:3].upper()}{category[:3].upper()}{random.randint(1000, 9999)}"
            
            # Create product
            product = Product(
                name=product_name,
                description=description,
                price=price,
                category=category,
                brand=brand,
                sku=sku,
                image_url=f"https://via.placeholder.com/300x300?text={category}",
                stock_quantity=stock_quantity,
                in_stock=in_stock,
                rating=rating,
                reviews_count=reviews_count,
                weight=round(random.uniform(0.1, 5.0), 2),
                dimensions=f"{random.randint(10, 50)}x{random.randint(10, 50)}x{random.randint(1, 10)}cm",
                specifications=json.dumps(specs)
            )
            
            db.session.add(product)
            products_created += 1
    
    db.session.commit()
    print(f"Created {products_created} products successfully!")
    return products_created

def create_sample_orders():
    """Create sample orders for testing"""
    users = User.query.all()
    products = Product.query.filter(Product.in_stock == True).limit(20).all()
    
    if not users or not products:
        print("No users or products found. Skipping order creation.")
        return
    
    order_statuses = ['pending', 'confirmed', 'shipped', 'delivered']
    
    for i in range(10):
        user = random.choice(users)
        
        # Create order
        order_number = f"ORD{datetime.now().strftime('%Y%m%d')}{random.randint(1000, 9999)}"
        order = Order(
            user_id=user.id,
            order_number=order_number,
            status=random.choice(order_statuses),
            total_amount=0.0,  # Will be calculated
            shipping_address=f"{random.randint(100, 999)} Main St, City {random.randint(10000, 99999)}",
            payment_method=random.choice(['Credit Card', 'PayPal', 'Bank Transfer']),
            payment_status='completed' if random.choice([True, False]) else 'pending',
            tracking_number=f"TRK{random.randint(100000, 999999)}" if random.choice([True, False]) else None,
            created_at=datetime.now() - timedelta(days=random.randint(1, 30))
        )
        
        db.session.add(order)
        db.session.flush()  # Get the order ID
        
        # Add order items
        num_items = random.randint(1, 3)
        total_amount = 0
        
        for _ in range(num_items):
            product = random.choice(products)
            quantity = random.randint(1, 3)
            unit_price = product.price
            item_total = unit_price * quantity
            total_amount += item_total
            
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                unit_price=unit_price,
                total_price=item_total
            )
            db.session.add(order_item)
        
        order.total_amount = round(total_amount, 2)
    
    db.session.commit()
    print("Sample orders created successfully!")

def main():
    """Main function to populate the database"""
    with app.app_context():
        print("Starting database population...")
        
        # Create tables if they don't exist
        db.create_all()
        
        # Create sample users
        create_sample_users()
        
        # Create products
        products_count = create_electronics_products()
        
        # Create sample orders
        create_sample_orders()
        
        print(f"\nDatabase population completed!")
        print(f"Total products created: {products_count}")
        print(f"Categories: Laptops, Smartphones, Tablets, Headphones, Smart Watches, Gaming Consoles, Monitors, Keyboards")
        print(f"Sample users: john@example.com, jane@example.com, mike@example.com (password: password123)")

if __name__ == "__main__":
    main()