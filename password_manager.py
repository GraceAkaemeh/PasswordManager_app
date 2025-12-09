import random
import string
import os

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!#$%&()*+"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def save_password(website, username, password):
    filepath = os.path.join(os.path.dirname(__file__), "data.txt")
    with open(filepath, "a") as file:
        file.write(f"{website} | {username} | {password}\n")
