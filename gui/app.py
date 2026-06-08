import tkinter as tk
from tkinter import messagebox
from core.password_manager import generate_password, save_password


class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")
        master.config(padx=40, pady=40)

        tk.Label(master, text="Company:").grid(row=0, column=0)
        tk.Label(master, text="Email/Username:").grid(row=1, column=0)
        tk.Label(master, text="Password:").grid(row=2, column=0)

        self.website_entry = tk.Entry(master, width=35)
        self.website_entry.grid(row=0, column=1, columnspan=2)

        self.user_entry = tk.Entry(master, width=35)
        self.user_entry.grid(row=1, column=1, columnspan=2)

        self.password_entry = tk.Entry(master, width=21)
        self.password_entry.grid(row=2, column=1)

        tk.Button(master, text="Generate Password", command=self.handle_generate).grid(row=2, column=2)
        tk.Button(master, text="Add", width=36, command=self.handle_save).grid(row=3, column=1, columnspan=2)
        tk.Button(master, text="View Saved Passwords", width=36, command=self.handle_view).grid(row=4, column=1, columnspan=2)

    def handle_generate(self):
        password = generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        messagebox.showinfo("Copied", "Password generated!")

    def handle_save(self):
        website = self.website_entry.get()
        username = self.user_entry.get()
        password = self.password_entry.get()

        if not website or not username or not password:
            messagebox.showwarning("Error", "Please fill all fields.")
            return

        save_password(website, username, password)

        self.website_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo("Saved", "Password saved successfully!")

    def handle_view(self):
        try:
            with open("data.txt", "r") as file:
                data = file.readlines()
        except FileNotFoundError:
            messagebox.showinfo("No Data", "No passwords saved yet.")
            return

        window = tk.Toplevel(self.master)
        window.title("Saved Passwords")

        for i, line in enumerate(data):
            tk.Label(window, text=line.strip()).grid(row=i, column=0, sticky="w")