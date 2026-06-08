import random
import string
import os
import pyperclip

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_"
    all_chars = letters + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))
    pyperclip.copy(password)
    return password


def save_password(website, username, password, filename="data.txt"):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Website | Username | Password\n")

    with open(filename, "a") as file:
        file.write(f"{website} | {username} | {password}\n")

# try:
#     with open(filepath, "a") as file:
#         file.write(...)
# except Exception as e:
#     print(f"Error saving password: {e}")