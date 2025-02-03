from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import re


# ---------------------------- PASSWORD STRENGTH CHECKER ------------------------------- #
def check_password_strength():
    password = password_entry.get()
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Length should be 8+ chars")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase")

    if re.search(r"[!@#$%^&*()+]", password):
        strength += 1
    else:
        feedback.append("Add symbols")

    strength_text = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    strength_colors = ["red", "red", "orange", "light green", "green"]

    if password:
        strength_label.config(text=f"Strength: {strength_text[min(strength, 4)]}",
                              fg=strength_colors[min(strength, 4)])
        feedback_label.config(text="Suggestions: " + ", ".join(feedback) if feedback else "")
    else:
        strength_label.config(text="")
        feedback_label.config(text="")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = (
        [choice(letters) for _ in range(randint(8, 10))] +
        [choice(symbols) for _ in range(randint(2, 4))] +
        [choice(numbers) for _ in range(randint(2, 4))]
    )
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    check_password_strength()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        strength_label.config(text="")
        feedback_label.config(text="")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            search_email = data[website]['email']
            search_password = data[website]['password']
            messagebox.showinfo(title=website.title(), message=f"Email: {search_email}\nPassword: {search_password}")
    except (FileNotFoundError, KeyError):
        messagebox.showerror(title="Error", message="No details for the website exist.")


# ---------------------------- CLEAR INFO ------------------------------- #
def clear_info():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    strength_label.config(text="")
    feedback_label.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
strength_label = Label(text="", font=("Arial", 10))
strength_label.grid(row=5, column=1, columnspan=2)
feedback_label = Label(text="", font=("Arial", 8))
feedback_label.grid(row=6, column=1, columnspan=2)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "amit@messi.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
password_entry.bind('<KeyRelease>', lambda event: check_password_strength())

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)
add_button = Button(text="Save Info", command=save)
add_button.grid(row=4, column=1, columnspan=2)
clear_button = Button(text="Clear Info", command=clear_info)
clear_button.grid(row=2, column=2)

window.mainloop()
