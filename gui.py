import tkinter as tk
from tkinter import messagebox
import pyperclip

from generator import generate_password
from checker import check_strength


# ---- Function to generate password ----
def generate_pw():
    try:
        length = int(entry_length.get())

        # call generator function
        pw = generate_password(length)

        # put in textbox
        entry_password.delete(0, tk.END)
        entry_password.insert(0, pw)

        # copy to clipboard
        pyperclip.copy(pw)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")


# ---- Function to check strength ----
def check_pw():
    pw = entry_password.get()

    if pw.strip() == "":
        messagebox.showwarning("Warning", "Generate or enter a password first.")
        return

    label, score = check_strength(pw)
    messagebox.showinfo("Strength Result", f"Strength: {label}\nScore: {score}")


# ---------- GUI WINDOW ----------
root = tk.Tk()
root.title("Password Manager")
root.geometry("350x300")

# ---------- Title ----------
title = tk.Label(root, text="🔐 Password Generator & Checker", font=("Arial", 12, "bold"))
title.pack(pady=10)

# ---------- Input for Length ----------
tk.Label(root, text="Enter password length:").pack()
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Button to generate
btn_generate = tk.Button(root, text="Generate Password", command=generate_pw)
btn_generate.pack(pady=10)

# Textbox for the password
tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

# Button to check
btn_check = tk.Button(root, text="Check Strength", command=check_pw)
btn_check.pack(pady=10)

# Start GUI
root.mainloop()