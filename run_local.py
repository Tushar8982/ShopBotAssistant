#!/usr/bin/env python3
"""
Local development setup script for the ShopBot Assistant
"""
import os
import sys

def setup_environment():
    """Set up required environment variables for local development"""
    os.environ['SESSION_SECRET'] = 'dev-secret-key-local-123'
    os.environ['DATABASE_URL'] = 'sqlite:///shopbot.db'
    
def check_database():
    """Check if database exists and is properly set up"""
    db_file = 'shopbot.db'
    if not os.path.exists(db_file):
        print("Database not found. Creating new database...")
        return False
    return True

def main():
    """Main function to run the application locally"""
    print("Setting up ShopBot Assistant for local development...")
    
    # Set environment variables
    setup_environment()
    
    # Check if database exists
    if not check_database():
        print("Running database setup...")
        try:
            from fix_database import fix_database
            if not fix_database():
                print("Failed to set up database!")
                sys.exit(1)
        except ImportError:
            print("Database setup script not found!")
            sys.exit(1)
    
    # Import and run the Flask app
    try:
        from app import app
        print("\nStarting ShopBot Assistant...")
        print("Login credentials: john@example.com / password123")
        print("Access the application at: http://127.0.0.1:5000")
        print("Press Ctrl+C to stop the server")
        print("-" * 50)
        
        app.run(host='0.0.0.0', port=5000, debug=True)
        
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()