from tkinter import *
from tkinter import messagebox
import random, string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    N = random.randint(6,10)
    pass_input.delete(0, END)
    pwd = ''.join(random.choices(string.digits+string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase, k=N))
    pass_input.insert(0, pwd)
    pyperclip.copy(pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_text():
    website_input.delete(0, END)
    email_input.delete(0, END)
    pass_input.delete(0, END)


def save_data():
    website_data = website_input.get()
    email_data = email_input.get()
    pass_data = pass_input.get()
    if len(website_data)==0 or len(email_data)==0 or len(pass_data)==0:
        error_msg = messagebox.showerror(title="Error", message="Please fill all the fields")
        print(error_msg)
    else:
        if_ok = messagebox.askokcancel(title="Confirmation",
                                       message=f"Entered credentials are correct or not:\n Website: {website_data}\n Email: {email_data}\n Password: {pass_data}")
        if if_ok:
            with open("Saved Data.txt", "a") as saved_data:
                saved_data.write(f"\n {website_data}|{email_data}|{pass_data}")

    clear_text()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website :", bg="white")
website_label.grid(column=0, row=1)

email_label = Label()
email_label.config(text="Email/Username :", bg="white")
email_label.grid(column=0, row=2)

pass_label = Label()
pass_label.config(text="Password :", bg="white")
pass_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry(width=35)
pass_input.grid(column=1, row=3, columnspan=2)

generate_button = Button(width=15)
generate_button.config(text="Generate Password", command=generate_pass, highlightthickness=0)
generate_button.grid(column=2, row=3)

add_button = Button(width=36)
add_button.config(text="Add", command=save_data, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()