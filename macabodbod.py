import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Shanrick" and password == "password":
        custom_messagebox("Login Successful", "Welcome, Mr. Lance!",
                          "padlock.png")  # Change "padlock.png" to your padlock icon file path
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def custom_messagebox(title, message, icon_path):
    top = tk.Toplevel()
    top.title(title)
    top.geometry("250x100")

    icon = Image.open("C:\\Users\\creen\\Downloads\\fcb428cc-cdf5-4b76-a26d-26a3ac100d10.png")
    icon = icon.resize((20, 20), Image.Resampling.LANCZOS)
    icon = ImageTk.PhotoImage(icon)

    label = tk.Label(top, text=message)
    label.pack(side=tk.LEFT, padx=5)

    icon_label = tk.Label(top, image=icon)
    icon_label.image = icon  # Keep a reference to avoid garbage collection
    icon_label.pack(side=tk.LEFT, padx=5)

    button = tk.Button(top, text="OK", command=top.destroy)
    button.pack(side=tk.LEFT, pady=5)


root = tk.Tk()
root.title("Login Form")

# Open and resize the image
image = Image.open("C:\\Users\\creen\\Downloads\\login-button-png-member-login-button-png-photos-574.png")  # Change "your_image.jpg" to your image file path
image = image.resize((400, 100), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Convert the image to a format compatible with tkinter
header_image = ImageTk.PhotoImage(image)

# Create a label to display the image
header_label = tk.Label(root, image=header_image)
header_label.image = header_image  # Keep a reference to avoid garbage collection
header_label.grid(row=0, columnspan=2, pady=10)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=15, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=15, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
