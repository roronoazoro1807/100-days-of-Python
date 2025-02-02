from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import re


# ---------------------------- PASSWORD STRENGTH CHECKER ------------------------------- #
def check_password_strength():
    password = password_entry.get()
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Length should be 8+ chars")

    # Number check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add numbers")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase")

    # Symbol check
    if re.search(r"[!@#$%^&*()+]", password):
        strength += 1
    else:
        feedback.append("Add symbols")

    # Update strength label
    strength_text = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    strength_colors = ["red", "red", "orange", "light green", "green"]

    if password:
        strength_label.config(text=f"Strength: {strength_text[min(strength, 4)]}",
                              fg=strength_colors[min(strength, 4)] )
        if feedback:
            feedback_label.config(text="Suggestions: " + ", ".join(feedback))
        else:
            feedback_label.config(text="")
    else:
        strength_label.config(text="")
        feedback_label.config(text="")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)  # Clear the entry first

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    check_password_strength()  # Check strength of generated password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                strength_label.config(text="")  # Clear strength label
                feedback_label.config(text="")  # Clear feedback label


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

# Strength Labels
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

# Bind password entry to strength checker
password_entry.bind('<KeyRelease>', lambda event: check_password_strength())

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
