import tkinter as tk
from gui.app import PasswordManagerApp

# ----------------------- START PROGRAM ------------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
