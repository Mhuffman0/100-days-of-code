from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

PASSWORD_LEN = 14
LABEL_WIDTH = 13
DEFAULT_USERNAME = "test@test.com"
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!#$%&()*+"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    def generate_rand_list(min_num, max_num, char_list):
        return [
            random.choice(list(char_list))
            for _ in range(random.randint(min_num, max_num))
        ]

    letter_list = generate_rand_list(8, 10, LETTERS)
    symbol_list = generate_rand_list(2, 4, SYMBOLS)
    number_list = generate_rand_list(2, 4, NUMBERS)

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    fields = {
        website: {
            "username": username,
            "password": password,
        }
    }
    missing_fields = [field for field in fields[website] if not fields[website][field]]
    if missing_fields:
        messagebox.showwarning(
            title="Missing Entries",
            message=(
                "Values for the following fields are required:\n"
                f"{', '.join(missing_fields)}"
            ),
        )
    else:
        messagebox.askokcancel(
            title=website,
            message=(
                "Save the following password to file?\n"
                f"username: {fields[website]['username']}\n"
                f"password: {fields[website]['password']}"
            ),
        )
        with open("data.json", "r") as file:
            try:
                data = json.load(file)
                data.update(fields)
            except json.decoder.JSONDecodeError:
                data = {}
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        website_entry.delete(0, END)
        username_entry.delete(0, END)
        username_entry.insert(0, DEFAULT_USERNAME)
        password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    with open("data.json", "r") as file:
        passwords = json.load(file)
    try:
        username_entry.delete(0, END)
        username_entry.insert(0, passwords[website]['username'])
        password_entry.delete(0, END)
        password_entry.insert(0, passwords[website]['password'])
    except KeyError:
        messagebox.showwarning(
            title="Missing Password",
            message=(
                "Unable to find a password for this website."
            ),
        )

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", anchor="e", width=LABEL_WIDTH)
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", anchor="e", width=LABEL_WIDTH)
user_label.grid(column=0, row=2)

password_label = Label(text="Password:", anchor="e", width=LABEL_WIDTH)
password_label.grid(column=0, row=3)

# Entry Fields
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(END, DEFAULT_USERNAME)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
search_website_button = Button(text="Search Website", command=find_password)
search_website_button.grid(column=2, row=1, sticky="EW")

generate_password_button = Button(text="Generate Password", command=create_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_password_button = Button(text="Add Password", width=40, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
