import tkinter as tk
from tkinter import ttk

# Initialize the ATM balance
balance = 1000

# Function to check account balance
def check_balance():
    balance_label.config(text=f"Your account balance is ${balance}")

# Function to deposit money
def deposit_money():
    global balance
    amount = float(deposit_entry.get())
    if amount > 0:
        balance += amount
        deposit_entry.delete(0, tk.END)
        check_balance()
        output_tab.select(0)
        output_text.insert(tk.END, f"${amount} has been deposited successfully.\n")
    else:
        output_tab.select(0)
        output_text.insert(tk.END, "Invalid amount. Please enter a positive number.\n")

# Function to withdraw money
def withdraw_money():
    global balance
    amount = float(withdraw_entry.get())
    if amount > 0:
        if amount <= balance:
            balance -= amount
            withdraw_entry.delete(0, tk.END)
            check_balance()
            output_tab.select(0)
            output_text.insert(tk.END, f"${amount} has been withdrawn successfully.\n")
        else:
            output_tab.select(0)
            output_text.insert(tk.END, "Insufficient funds.\n")
    else:
        output_tab.select(0)
        output_text.insert(tk.END, "Invalid amount. Please enter a positive number.\n")

# Create a Tkinter window
window = tk.Tk()
window.title("ATM Simulator")

# Create tabs for input and output
tab_control = ttk.Notebook(window)
input_tab = ttk.Frame(tab_control)
output_tab = ttk.Frame(tab_control)
tab_control.add(input_tab, text="Input")
tab_control.add(output_tab, text="Output")
tab_control.pack(expand=1, fill="both")

# Create input widgets
deposit_label = tk.Label(input_tab, text="Enter the amount to deposit:")
deposit_entry = tk.Entry(input_tab)
deposit_button = tk.Button(input_tab, text="Deposit", command=deposit_money)

withdraw_label = tk.Label(input_tab, text="Enter the amount to withdraw:")
withdraw_entry = tk.Entry(input_tab)
withdraw_button = tk.Button(input_tab, text="Withdraw", command=withdraw_money)

# Position input widgets
deposit_label.grid(row=0, column=0)
deposit_entry.grid(row=0, column=1)
deposit_button.grid(row=0, column=2)

withdraw_label.grid(row=1, column=0)
withdraw_entry.grid(row=1, column=1)
withdraw_button.grid(row=1, column=2)
# Create output text widget
output_text = tk.Text(output_tab, wrap=tk.WORD)
output_text.pack(fill="both", expand=True)
# Create a label for account balance
balance_label = tk.Label(input_tab, text="")
balance_label.grid(row=2, columnspan=3)
# Main loop
window.mainloop()
