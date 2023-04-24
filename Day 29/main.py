from tkinter import *
import pandas

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    with open("Day 29/data.txt", "a") as data_file:
        entry = f"{user_website} | {user_email} | {user_password}\n"
        data_file.write(entry)
        data_file.close()

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")


password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons

password_btn = Button(text="Generate Password")
password_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


window.mainloop()
