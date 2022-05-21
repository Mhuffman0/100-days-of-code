from tkinter import *
import random

LABEL_WIDTH = 13
DEFAULT_USERNAME = "test@test.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    fields = [website.get(), username.get(), password.get()]
    with open("data.txt", "a") as file:
        file.write(" | ".join(fields) + "\n")
    website.delete(0, END)
    username.delete(0, END)
    username.insert(0, DEFAULT_USERNAME)
    password.delete(0, END)


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
website = Entry()
website.grid(column=1, row=1, columnspan=2, sticky="EW")
website.focus()

username = Entry()
username.grid(column=1, row=2, columnspan=2, sticky="EW")
username.insert(END, DEFAULT_USERNAME)

password = Entry()
password.grid(column=1, row=3, sticky="EW")

# Buttons
create_password_button = Button(text="Generate Password")
create_password_button.grid(column=2, row=3, sticky="EW")

add_password_button = Button(text="Add Password", width=40, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
