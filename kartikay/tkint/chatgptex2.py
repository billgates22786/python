from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, Listbox
import json

# Initialize users dictionary
users = {}

# Load users from file if exists
def load_users():
    global users
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

# Save users to file
def save_users():
    global users
    with open("users.json", "w") as f:
        json.dump(users, f)

# Register new user
def register():
    def save_user():
        email = email_entry.get()
        password = password_entry.get()
        if email and password:
            if email in users:
                messagebox.showerror("Error", "User already exists")
            else:
                users[email] = password
                save_users()
                messagebox.showinfo("Success", "User registered successfully")
                register_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    register_window = Toplevel(root)
    register_window.title("Register")
    Label(register_window, text="Email:").grid(row=0, column=0, padx=10, pady=10)
    email_entry = Entry(register_window)
    email_entry.grid(row=0, column=1, padx=10, pady=10)
    Label(register_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = Entry(register_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)
    Button(register_window, text="Register", command=save_user).grid(row=2, columnspan=2, pady=10)

# Login user
def login():
    email = email_entry.get()
    password = password_entry.get()
    if email in users and users[email] == password:
        if email == "kartikayjain@gmail.com" and password == "admin123":
            show_all_users()
        else:
            messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Show all users (Admin view)
def show_all_users():
    admin_window = Toplevel(root)
    admin_window.title("Admin View")
    listbox = Listbox(admin_window, width=50)
    listbox.pack(padx=10, pady=10)
    for user, pwd in users.items():
        listbox.insert("end", f"Email: {user} | Password: {pwd}")

# Initialize main window
root = Tk()
root.title("Login/Register")

# Login form
Label(root, text="Email:").grid(row=0, column=0, padx=10, pady=10)
email_entry = Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login and Register buttons
Button(root, text="Login", command=login).grid(row=2, column=0, pady=10)
Button(root, text="Register", command=register).grid(row=2, column=1, pady=10)

# Load users from the file
load_users()

# Start the main loop
root.mainloop()
