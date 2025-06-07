# ShopBot Assistant - Local Setup Guide

## Quick Start

1. **Set Environment Variable** (required):
   ```bash
   set SESSION_SECRET=dev-secret-key-123
   ```

2. **Create Database** (first time only):
   ```bash
   python fix_database.py
   ```

3. **Start Application**:
   ```bash
   python run_local.py
   ```

4. **Access Application**:
   - Open browser to: `http://127.0.0.1:5000`
   - Login with: `john@example.com` / `password123`

## Troubleshooting

**If you get database errors:**
1. Delete existing database: `del shopbot.db`
2. Run database setup: `python fix_database.py`
3. Start application: `python run_local.py`

**If you get "Flask app not registered" errors:**
- Make sure SESSION_SECRET environment variable is set
- Use `run_local.py` instead of `python app.py` directly

## Demo Features

- Login/Register users
- Chatbot with product search
- Product catalog browsing
- Order management
- Chat history persistence

## Sample Data Included

- 2 demo users (john@example.com, jane@example.com)
- 5 sample products across different categories
- Login password for all demo users: `password123`