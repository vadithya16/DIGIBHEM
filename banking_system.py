import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class BankingSystem:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.data_file = "banking_data.json"
        self.load_data()
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("💳 Online Banking System")
        self.root.geometry("900x650")
        self.root.configure(bg="#f8f9fa")
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.create_login_screen()
    
    def load_data(self):
        """Load user data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.users = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.users = {}
    
    def save_data(self):
        """Save user data to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
    
    def create_login_screen(self):
        """Create the login interface"""
        self.clear_screen()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = tk.Label(main_frame, text="🏦 Online Banking System", 
                              font=("Segoe UI", 28, "bold"), bg="#f8f9fa", fg="#2c3e50")
        title_label.pack(pady=40)
        
        # Login form frame
        login_frame = tk.Frame(main_frame, bg="white", relief="flat", bd=0)
        login_frame.pack(pady=30, padx=100, fill='x')
        
        # Add subtle shadow effect
        shadow_frame = tk.Frame(main_frame, bg="#e9ecef", height=2)
        shadow_frame.place(x=102, y=142, width=696, height=2)
        
        tk.Label(login_frame, text="🔐 Login", font=("Segoe UI", 20, "bold"), 
                bg="white", fg="#495057").pack(pady=25)
        
        # Username field
        tk.Label(login_frame, text="👤 Username:", font=("Segoe UI", 12), 
                bg="white", fg="#6c757d").pack(anchor='w', padx=30, pady=(5, 0))
        self.username_entry = tk.Entry(login_frame, font=("Segoe UI", 12), width=35,
                                     relief="flat", bd=5, bg="#f8f9fa")
        self.username_entry.pack(pady=(8, 15), padx=30)
        
        # Password field
        tk.Label(login_frame, text="🔒 Password:", font=("Segoe UI", 12), 
                bg="white", fg="#6c757d").pack(anchor='w', padx=30, pady=(5, 0))
        self.password_entry = tk.Entry(login_frame, font=("Segoe UI", 12), 
                                      width=35, show="*", relief="flat", bd=5, bg="#f8f9fa")
        self.password_entry.pack(pady=(8, 25), padx=30)
        
        # Buttons frame
        button_frame = tk.Frame(login_frame, bg="white")
        button_frame.pack(pady=25)
        
        login_btn = tk.Button(button_frame, text="🚀 Login", font=("Segoe UI", 12, "bold"),
                             bg="#007bff", fg="white", width=12, relief="flat", 
                             pady=8, command=self.login)
        login_btn.pack(side='left', padx=15)
        
        register_btn = tk.Button(button_frame, text="✨ Register", font=("Segoe UI", 12, "bold"),
                                bg="#28a745", fg="white", width=12, relief="flat",
                                pady=8, command=self.show_register)
        register_btn.pack(side='left', padx=15)
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.login())
    
    def show_register(self):
        """Show registration screen"""
        self.clear_screen()
        
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(expand=True, fill='both')
        
        title_label = tk.Label(main_frame, text="📝 Create New Account", 
                              font=("Segoe UI", 24, "bold"), bg="#f8f9fa", fg="#2c3e50")
        title_label.pack(pady=35)
        
        # Registration form
        reg_frame = tk.Frame(main_frame, bg="white", relief="flat", bd=0)
        reg_frame.pack(pady=25, padx=80, fill='x')
        
        # Username
        tk.Label(reg_frame, text="👤 Username:", font=("Segoe UI", 12), 
                bg="white", fg="#6c757d").pack(anchor='w', padx=25, pady=(25, 5))
        self.reg_username = tk.Entry(reg_frame, font=("Segoe UI", 12), width=35,
                                   relief="flat", bd=5, bg="#f8f9fa")
        self.reg_username.pack(padx=25, pady=(0, 10))
        
        # Password
        tk.Label(reg_frame, text="🔒 Password:", font=("Segoe UI", 12), 
                bg="white", fg="#6c757d").pack(anchor='w', padx=25, pady=(5, 5))
        self.reg_password = tk.Entry(reg_frame, font=("Segoe UI", 12), 
                                    width=35, show="*", relief="flat", bd=5, bg="#f8f9fa")
        self.reg_password.pack(padx=25, pady=(0, 10))
        
        # Confirm Password
        tk.Label(reg_frame, text="🔐 Confirm Password:", font=("Segoe UI", 12), 
                bg="white", fg="#6c757d").pack(anchor='w', padx=25, pady=(5, 5))
        self.reg_confirm = tk.Entry(reg_frame, font=("Segoe UI", 12), 
                                   width=35, show="*", relief="flat", bd=5, bg="#f8f9fa")
        self.reg_confirm.pack(padx=25, pady=(0, 10))
        
        # Initial Deposit
        tk.Label(reg_frame, text="💰 Initial Deposit (minimum ₹100):", font=("Segoe UI", 12), 
                bg="white", fg="#6c757d").pack(anchor='w', padx=25, pady=(5, 5))
        self.initial_deposit = tk.Entry(reg_frame, font=("Segoe UI", 12), width=35,
                                      relief="flat", bd=5, bg="#f8f9fa")
        self.initial_deposit.pack(padx=25, pady=(0, 15))
        
        # Buttons
        button_frame = tk.Frame(reg_frame, bg="white")
        button_frame.pack(pady=(25, 30))
        
        create_btn = tk.Button(button_frame, text="📝 Create Account", 
                              font=("Segoe UI", 12, "bold"), bg="#28a745", fg="white", 
                              width=15, command=self.register, cursor="hand2", relief="flat",
                              activebackground="#218838", activeforeground="white")
        create_btn.pack(side='left', padx=15)
        
        back_btn = tk.Button(button_frame, text="← Back", font=("Segoe UI", 12, "bold"),
                            bg="#6c757d", fg="white", width=12, 
                            command=self.create_login_screen, cursor="hand2", relief="flat",
                            activebackground="#5a6268", activeforeground="white")
        back_btn.pack(side='left', padx=15)
    
    def register(self):
        """Register a new user"""
        username = self.reg_username.get().strip()
        password = self.reg_password.get()
        confirm = self.reg_confirm.get()
        initial = self.initial_deposit.get().strip()
        
        # Validation
        if not username or not password:
            messagebox.showerror("Error", "Username and password are required!")
            return
        
        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if len(password) < 4:
            messagebox.showerror("Error", "Password must be at least 4 characters!")
            return
        
        try:
            initial_amount = float(initial)
            if initial_amount < 100:
                messagebox.showerror("Error", "Initial deposit must be at least ₹100!")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid initial deposit amount!")
            return
        
        # Create new user
        self.users[username] = {
            'password': password,
            'balance': initial_amount,
            'transactions': [{
                'type': 'Initial Deposit',
                'amount': initial_amount,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'balance': initial_amount
            }]
        }
        
        self.save_data()
        messagebox.showinfo("Success", "Account created successfully!")
        self.create_login_screen()
    
    def login(self):
        """Authenticate user login"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password!")
            return
        
        if username in self.users and self.users[username]['password'] == password:
            self.current_user = username
            self.create_main_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password!")
    
    def create_main_screen(self):
        """Create the main banking interface"""
        self.clear_screen()
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Header
        header_frame = tk.Frame(main_frame, bg="#2c3e50", height=90)
        header_frame.pack(fill='x', pady=(0, 15))
        header_frame.pack_propagate(False)
        
        welcome_label = tk.Label(header_frame, text=f"👋 Welcome, {self.current_user}!", 
                                font=("Segoe UI", 20, "bold"), bg="#2c3e50", fg="white")
        welcome_label.pack(side='left', padx=25, pady=25)
        
        logout_btn = tk.Button(header_frame, text="🚪 Logout", font=("Segoe UI", 12, "bold"),
                              bg="#dc3545", fg="white", command=self.logout,
                              cursor="hand2", relief="flat", padx=20, pady=8,
                              activebackground="#c82333", activeforeground="white")
        logout_btn.pack(side='right', padx=25, pady=25)
        
        # Balance display
        balance_frame = tk.Frame(main_frame, bg="white", relief="flat", bd=0)
        balance_frame.pack(fill='x', pady=(0, 15))
        
        tk.Label(balance_frame, text="💰 Current Balance", font=("Segoe UI", 16, "bold"),
                bg="white", fg="#495057").pack(pady=(15, 8))
        
        balance = self.users[self.current_user]['balance']
        self.balance_label = tk.Label(balance_frame, text=f"₹{balance:.2f}", 
                                     font=("Segoe UI", 28, "bold"), bg="white", fg="#28a745")
        self.balance_label.pack(pady=(0, 15))
        
        # Action buttons
        action_frame = tk.Frame(main_frame, bg="#f8f9fa")
        action_frame.pack(fill='x', pady=(0, 15))
        
        deposit_btn = tk.Button(action_frame, text="💵 Deposit", font=("Segoe UI", 14, "bold"),
                               bg="#28a745", fg="white", width=14, height=2,
                               command=self.show_deposit, cursor="hand2", relief="flat",
                               activebackground="#218838", activeforeground="white")
        deposit_btn.pack(side='left', padx=8)
        
        withdraw_btn = tk.Button(action_frame, text="💸 Withdraw", font=("Segoe UI", 14, "bold"),
                                bg="#fd7e14", fg="white", width=14, height=2,
                                command=self.show_withdraw, cursor="hand2", relief="flat",
                                activebackground="#e8680b", activeforeground="white")
        withdraw_btn.pack(side='left', padx=8)
        
        history_btn = tk.Button(action_frame, text="📊 Transaction History", 
                               font=("Segoe UI", 14, "bold"), bg="#007bff", fg="white", 
                               width=18, height=2, command=self.show_history,
                               cursor="hand2", relief="flat",
                               activebackground="#0056b3", activeforeground="white")
        history_btn.pack(side='left', padx=8)
        
        # Quick info
        info_frame = tk.Frame(main_frame, bg="white", relief="flat", bd=0)
        info_frame.pack(fill='both', expand=True)
        
        tk.Label(info_frame, text="📋 Account Information", font=("Segoe UI", 18, "bold"),
                bg="white", fg="#495057").pack(pady=(15, 10))
        
        info_text = f"""🏦 Account Holder: {self.current_user}
💳 Account Type: Savings Account  
📈 Total Transactions: {len(self.users[self.current_user]['transactions'])}
🕒 Last Login: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"""
        
        tk.Label(info_frame, text=info_text, font=("Segoe UI", 12), bg="white",
                justify='left', fg="#6c757d").pack(pady=(10, 20))
    
    def show_deposit(self):
        """Show deposit dialog"""
        self.show_transaction_dialog("Deposit", self.process_deposit)
    
    def show_withdraw(self):
        """Show withdrawal dialog"""
        self.show_transaction_dialog("Withdraw", self.process_withdraw)
    
    def show_transaction_dialog(self, title, callback):
        """Generic transaction dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("400x200")
        dialog.configure(bg="white")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 200, 
                                   self.root.winfo_rooty() + 150))
        
        tk.Label(dialog, text=f"💰 {title} Amount", font=("Segoe UI", 18, "bold"),
                bg="white", fg="#495057").pack(pady=(25, 15))
        
        tk.Label(dialog, text="Enter amount:", font=("Segoe UI", 12),
                bg="white", fg="#6c757d").pack()
        
        amount_entry = tk.Entry(dialog, font=("Segoe UI", 14), width=25,
                               relief="flat", bd=5, bg="#f8f9fa")
        amount_entry.pack(pady=(10, 20))
        amount_entry.focus()
        
        button_frame = tk.Frame(dialog, bg="white")
        button_frame.pack(pady=(10, 25))
        
        confirm_btn = tk.Button(button_frame, text="✅ Confirm", font=("Segoe UI", 12, "bold"),
                               bg="#28a745" if title == "Deposit" else "#fd7e14", 
                               fg="white", width=12, cursor="hand2", relief="flat",
                               activebackground="#218838" if title == "Deposit" else "#e8680b",
                               activeforeground="white",
                               command=lambda: callback(amount_entry.get(), dialog))
        confirm_btn.pack(side='left', padx=15)
        
        cancel_btn = tk.Button(button_frame, text="❌ Cancel", font=("Segoe UI", 12, "bold"),
                              bg="#6c757d", fg="white", width=12, cursor="hand2", relief="flat",
                              activebackground="#5a6268", activeforeground="white",
                              command=dialog.destroy)
        cancel_btn.pack(side='left', padx=15)
        
        # Bind Enter key
        dialog.bind('<Return>', lambda event: callback(amount_entry.get(), dialog))
    
    def process_deposit(self, amount_str, dialog):
        """Process deposit transaction"""
        try:
            amount = float(amount_str.strip())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0!")
                return
            
            # Update balance
            self.users[self.current_user]['balance'] += amount
            
            # Add transaction record
            transaction = {
                'type': 'Deposit',
                'amount': amount,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'balance': self.users[self.current_user]['balance']
            }
            self.users[self.current_user]['transactions'].append(transaction)
            
            self.save_data()
            self.update_balance_display()
            
            messagebox.showinfo("Success", f"₹{amount:.2f} deposited successfully!")
            dialog.destroy()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")
    
    def process_withdraw(self, amount_str, dialog):
        """Process withdrawal transaction"""
        try:
            amount = float(amount_str.strip())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than 0!")
                return
            
            current_balance = self.users[self.current_user]['balance']
            if amount > current_balance:
                messagebox.showerror("Error", "Insufficient funds!")
                return
            
            # Update balance
            self.users[self.current_user]['balance'] -= amount
            
            # Add transaction record
            transaction = {
                'type': 'Withdrawal',
                'amount': amount,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'balance': self.users[self.current_user]['balance']
            }
            self.users[self.current_user]['transactions'].append(transaction)
            
            self.save_data()
            self.update_balance_display()
            
            messagebox.showinfo("Success", f"₹{amount:.2f} withdrawn successfully!")
            dialog.destroy()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")
    
    def show_history(self):
        """Show transaction history window"""
        history_window = tk.Toplevel(self.root)
        history_window.title("📊 Transaction History")
        history_window.geometry("750x550")
        history_window.configure(bg="#f8f9fa")
        
        # Title
        tk.Label(history_window, text="📊 Transaction History", 
                font=("Segoe UI", 20, "bold"), bg="#f8f9fa", fg="#495057").pack(pady=(15, 10))
        
        # Create treeview for transactions
        tree_frame = tk.Frame(history_window, bg="#f8f9fa")
        tree_frame.pack(fill='both', expand=True, padx=25, pady=(10, 15))
        
        columns = ('Date', 'Type', 'Amount', 'Balance')
        tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=15)
        
        # Define headings
        for col in columns:
            tree.heading(col, text=col)
            if col == 'Date':
                tree.column(col, width=150)
            elif col == 'Type':
                tree.column(col, width=120)
            else:
                tree.column(col, width=100)
        
        # scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        # Pack treeview and scrollbar
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Insert transaction data
        transactions = self.users[self.current_user]['transactions']
        for transaction in reversed(transactions):  # Show most recent first
            tree.insert('', 'end', values=(
                transaction['date'],
                transaction['type'],
                f"₹{transaction['amount']:.2f}",
                f"₹{transaction['balance']:.2f}"
            ))
        
        # Close button
        close_btn = tk.Button(history_window, text="❌ Close", font=("Segoe UI", 12, "bold"),
                             bg="#6c757d", fg="white", width=12, cursor="hand2", relief="flat",
                             activebackground="#5a6268", activeforeground="white",
                             command=history_window.destroy)
        close_btn.pack(pady=(15, 20))
    
    def update_balance_display(self):
        """Update the balance display on main screen"""
        balance = self.users[self.current_user]['balance']
        self.balance_label.config(text=f"₹{balance:.2f}")
    
    def logout(self):
        """Logout current user"""
        self.current_user = None
        self.create_login_screen()
    
    def clear_screen(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def run(self):
        """Start the banking system"""
        self.root.mainloop()

# Run the banking system
if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.run()