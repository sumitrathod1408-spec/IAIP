import tkinter as tk
from tkinter import messagebox

# Dummy user credentials
username = "admin"
password = "1234"

balance = 0
transactions = []

# Login function
def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == username and pwd == password:
        messagebox.showinfo("Login Success", "Welcome to Online Banking System")
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Main banking window
def main_window():
    global balance

    window = tk.Tk()
    window.title("Online Banking System")
    window.geometry("400x400")

    def deposit():
        global balance
        try:
            amount = int(entry_amount.get())
            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: {amount}")
                messagebox.showinfo("Success", f"Deposited ₹{amount}")
            else:
                messagebox.showerror("Error", "Enter valid amount")
        except:
            messagebox.showerror("Error", "Invalid input")

    def withdraw():
        global balance
        try:
            amount = int(entry_amount.get())
            if amount > balance:
                messagebox.showerror("Error", "Insufficient Balance")
            else:
                balance -= amount
                transactions.append(f"Withdrawn: {amount}")
                messagebox.showinfo("Success", f"Withdrawn ₹{amount}")
        except:
            messagebox.showerror("Error", "Invalid input")

    def check_balance():
        messagebox.showinfo("Balance", f"Current Balance: ₹{balance}")

    def show_history():
        history = "\n".join(transactions)
        if history == "":
            history = "No transactions yet"
        messagebox.showinfo("Transaction History", history)

    tk.Label(window, text="Enter Amount").pack(pady=10)

    entry_amount = tk.Entry(window)
    entry_amount.pack()

    tk.Button(window, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(window, text="Withdraw", command=withdraw).pack(pady=5)
    tk.Button(window, text="Check Balance", command=check_balance).pack(pady=5)
    tk.Button(window, text="Transaction History", command=show_history).pack(pady=5)

    window.mainloop()

# Login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username").pack()
entry_user = tk.Entry(login_window)
entry_user.pack()

tk.Label(login_window, text="Password").pack()
entry_pass = tk.Entry(login_window, show="*")
entry_pass.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=10)

login_window.mainloop()
