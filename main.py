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
    Main function to take user input and check password strength.
    """
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Thank you for using the Password Strength Checker! Goodbye!")
            break

        result = check_password_strength(password)
        print(result)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")
root.configure(bg="#f4f4f4")


label = tk.Label(root, text="Enter your password:", font=("Arial", 12, "bold"), bg="#f4f4f4")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f4")
result_label.pack(pady=10)


root.mainloop()