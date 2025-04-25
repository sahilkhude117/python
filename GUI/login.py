import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Main Window
root = tk.Tk()
root.title("Login & Register System")
root.geometry("450x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Fonts and Colors
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 12)
btn_color = "#4CAF50"
entry_bg = "#ffffff"
highlight = "#222222"

# Frame Setup
frame_register = tk.Frame(root, bg="white")
frame_login = tk.Frame(root, bg="white")

for frame in (frame_register, frame_login):
    frame.place(x=0, y=0, width=450, height=400)

# REGISTER PAGE
def register_user():
    username = reg_username.get()
    password = reg_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")
        reg_username.set("")
        reg_password.set("")
        show_login()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

def show_login():
    frame_register.place_forget()
    frame_login.place(x=0, y=0, width=450, height=400)

def show_register():
    frame_login.place_forget()
    frame_register.place(x=0, y=0, width=450, height=400)

reg_username = tk.StringVar()
reg_password = tk.StringVar()

tk.Label(frame_register, text="Register", font=font_title, bg="white", fg=highlight).pack(pady=20)
tk.Label(frame_register, text="Username", font=font_label, bg="white").pack(pady=5)
tk.Entry(frame_register, textvariable=reg_username, bg=entry_bg, width=30).pack()
tk.Label(frame_register, text="Password", font=font_label, bg="white").pack(pady=5)
tk.Entry(frame_register, textvariable=reg_password, bg=entry_bg, show="*", width=30).pack()
tk.Button(frame_register, text="Register", command=register_user, bg=btn_color, fg="white", width=20).pack(pady=20)
tk.Button(frame_register, text="Already have an account? Login", command=show_login, bg="white", fg="blue", bd=0).pack()

# LOGIN PAGE
def login_user():
    username = login_username.get()
    password = login_password.get()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

login_username = tk.StringVar()
login_password = tk.StringVar()

tk.Label(frame_login, text="Login", font=font_title, bg="white", fg=highlight).pack(pady=20)
tk.Label(frame_login, text="Username", font=font_label, bg="white").pack(pady=5)
tk.Entry(frame_login, textvariable=login_username, bg=entry_bg, width=30).pack()
tk.Label(frame_login, text="Password", font=font_label, bg="white").pack(pady=5)
tk.Entry(frame_login, textvariable=login_password, bg=entry_bg, show="*", width=30).pack()
tk.Button(frame_login, text="Login", command=login_user, bg=btn_color, fg="white", width=20).pack(pady=20)
tk.Button(frame_login, text="New user? Register here", command=show_register, bg="white", fg="blue", bd=0).pack()

# Start on Register page
show_register()

root.mainloop()

