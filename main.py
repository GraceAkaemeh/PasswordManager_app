import tkinter as tk
from tkinter import messagebox
import pyperclip  # for clipboard copy
import os
import random
import string

# --------------------- PASSWORD FUNCTIONS --------------------- #
def generate_password(length=12):
    """Generate a random secure password."""
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_"
    all_chars = letters + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))
    pyperclip.copy(password)  # copy password to clipboard automatically
    return password

def save_password(website, username, password, filename="data.txt"):
    """Save password to a text file."""
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Website | Username | Password\n")
    with open(filename, "a") as file:
        file.write(f"{website} | {username} | {password}\n")

# ------------------------- PASSWORD MANAGER CLASS ------------------------ #
class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")
        master.config(padx=40, pady=40)

        # Labels
        tk.Label(master, text="Company:").grid(row=0, column=0)
        tk.Label(master, text="Email/Username:").grid(row=1, column=0)
        tk.Label(master, text="Password:").grid(row=2, column=0)

        # Entries
        self.website_entry = tk.Entry(master, width=35)
        self.website_entry.grid(row=0, column=1, columnspan=2)
        self.website_entry.focus()

        self.user_entry = tk.Entry(master, width=35)
        self.user_entry.grid(row=1, column=1, columnspan=2)

        self.password_entry = tk.Entry(master, width=21)
        self.password_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(master, text="Generate Password", command=self.handle_generate).grid(row=2, column=2)
        tk.Button(master, text="Add", width=36, command=self.handle_save).grid(row=3, column=1, columnspan=2)
        tk.Button(master, text="View Saved Passwords", width=36, command=self.handle_view).grid(row=4, column=1, columnspan=2)

    # ---------------------- BUTTON FUNCTIONS ---------------------- #
    def handle_generate(self):
        password = generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        messagebox.showinfo("Copied", "Password generated and copied to clipboard!")

    def handle_save(self):
        website = self.website_entry.get()
        username = self.user_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showwarning(title="Error", message="Please fill in all fields.")
            return

        save_password(website, username, password)
        self.website_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo(title="Saved", message="Password saved successfully!")

    def handle_view(self):
        """Display all saved passwords in a new window."""
        try:
            with open("data.txt", "r") as file:
                data = file.readlines()
        except FileNotFoundError:
            messagebox.showinfo("No Data", "No passwords saved yet.")
            return

        view_window = tk.Toplevel(self.master)
        view_window.title("Saved Passwords")
        view_window.config(padx=20, pady=20)

        for i, line in enumerate(data):
            tk.Label(view_window, text=line.strip()).grid(row=i, column=0, sticky="w")

# ----------------------- START PROGRAM ------------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
