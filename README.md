# 💳 Online Banking System

A modern, user-friendly banking application built with Python and Tkinter that provides essential banking operations with a beautiful graphical interface.

## 🌟 Features

### 🔐 Authentication System
- **User Registration** - Create new accounts with secure validation
- **User Login** - Secure authentication with username and password
- **Password Security** - Minimum 4-character password requirement
- **Session Management** - Secure logout functionality

### 💰 Banking Operations
- **Account Balance Display** - Real-time balance updates in Indian Rupees (₹)
- **Deposit Money** - Add funds to your account
- **Withdraw Money** - Withdraw funds with insufficient balance protection
- **Transaction History** - View detailed transaction records with dates and amounts
- **Initial Deposit** - Minimum ₹100 deposit requirement for new accounts

## 🛠️ Technology Stack

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Data Storage**: JSON file-based persistence
- **Date/Time**: Python datetime module
- **Styling**: Custom Tkinter styling with modern color schemes

## 📋 Requirements

- Python 3.6 or higher
- Tkinter
- No additional dependencies required

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/vadithya16/DIGIBHEM.git
   cd DIGIBHEM
   ```

2. **Run the application**
   ```bash
   python banking_system.py
   ```

3. **First-time setup**
   - The application will create a `banking_data.json` file to store user data
   - Register a new account to get started

## 📖 Usage Guide

### Getting Started
1. **Launch the application** by running `python banking_system.py`
2. **Register a new account**:
   - Click "✨ Register" on the login screen
   - Enter your desired username and password
   - Confirm your password
   - Make an initial deposit (minimum ₹100)
3. **Login** with your credentials

### Banking Operations
- **Deposit**: Click "💵 Deposit" and enter the amount
- **Withdraw**: Click "💸 Withdraw" and enter the amount
- **View History**: Click "📊 Transaction History" to see all transactions
- **Check Balance**: Your current balance is always displayed on the main screen

## 🗂️ Project Structure

```
DIGIBHEM/
│
├── banking_system.py      # Main application file
├── banking_data.json      # User data storage (created automatically)
└── README.md              # Project documentation
```

## 🎯 Key Components

### Classes and Methods

#### `BankingSystem`
- `__init__()` - Initialize the application
- `load_data()` - Load user data from JSON file
- `save_data()` - Save user data to JSON file
- `create_login_screen()` - Create login interface
- `show_register()` - Display registration form
- `register()` - Handle new user registration
- `login()` - Authenticate user login
- `create_main_screen()` - Main banking interface
- `show_deposit()` - Deposit dialog
- `show_withdraw()` - Withdrawal dialog
- `process_deposit()` - Handle deposit transactions
- `process_withdraw()` - Handle withdrawal transactions
- `show_history()` - Transaction history window
- `update_balance_display()` - Update balance on screen
- `logout()` - User logout functionality
- `clear_screen()` - Clear UI widgets

## 🔒 Security Features

- **Password Protection** - All accounts are password protected
- **Session Management** - Users must login to access banking features
- **Data Validation** - Input validation for all user entries
- **Balance Protection** - Prevents overdraft situations
- **Secure Storage** - User data stored in local JSON file

## 💾 Data Storage

The application uses JSON file storage with the following structure:

```json
{
  "username": {
    "password": "user_password",
    "balance": 1000.00,
    "transactions": [
      {
        "type": "Initial Deposit",
        "amount": 1000.00,
        "date": "2025-07-15 10:30:00",
        "balance": 1000.00
      }
    ]
  }
}
```

## ‍💻 Author

**V Adithya**
- GitHub: [@vadithya16](https://github.com/vadithya16)
- Repository: [DIGIBHEM](https://github.com/vadithya16/DIGIBHEM)
- Email: vadithya16@gmail.com
