# password strength checker

import tkinter as tk
from tkinter import messagebox
import re

# password strength check conditions:
# min 8 chars, digit, uppercase, lowercase, special char

def check_password_strength(password):
    """
    Function to check the strength of a password.
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."

    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."

    return "Strong: Your password is secure!"

def evaluate_password():
    """
    GUI function to check password strength and display result.
    """
    password = entry.get()
    
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    
    result = check_password_strength(password)
    result_label.config(text=result)
    
    # Color code the result based on strength
    if "Strong" in result:
        result_label.config(fg="green")
    elif "Medium" in result:
        result_label.config(fg="orange")
    else:
        result_label.config(fg="red")

def clear_fields():
    """
    Clear the password entry and result label.
    """
    entry.delete(0, tk.END)
    result_label.config(text="")
    result_label.config(fg="black")

# Create GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#333333")
title_label.pack(pady=15)

# Instructions Label
instructions_label = tk.Label(root, text="Enter a password to check its strength", font=("Arial", 10), bg="#f4f4f4", fg="#666666")
instructions_label.pack(pady=5)

# Password Entry Label
label = tk.Label(root, text="Enter your password:", font=("Arial", 12, "bold"), bg="#f4f4f4")
label.pack(pady=10)

# Password Entry Field
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

# Button Frame for better layout
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=15)

# Check Button
check_button = tk.Button(button_frame, text="Check Strength", command=evaluate_password, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=15, pady=5)
check_button.pack(side=tk.LEFT, padx=5)

# Clear Button
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields, font=("Arial", 12, "bold"), bg="#ff9800", fg="white", padx=15, pady=5)
clear_button.pack(side=tk.LEFT, padx=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f4")
result_label.pack(pady=20)

# Criteria Label
criteria_text = """Password Criteria:
✓ Minimum 8 characters
✓ At least one number
✓ At least one uppercase letter
✓ At least one lowercase letter
✓ At least one special character (!@#$%^&*...)"""

criteria_label = tk.Label(root, text=criteria_text, font=("Arial", 9), bg="#f4f4f4", fg="#666666", justify=tk.LEFT)
criteria_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
