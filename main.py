from tkinter import *
from tkinter import messagebox
from randomGenerator import generate_random_password
import pyperclip

# ---------------------------- PASSWORD GENERATOR -------------------------------


def generate_password():
    password_input.delete(0, END)
    password = generate_random_password()
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUser: {username} \n"
                                       f"Password:{password} \nIs it ok to save?")
        if is_ok:
            website_input.delete(0, END)
            password_input.delete(0, END)
            data = f"{website} | {username} | {password}"
            with open("data.txt", "a") as data_file:
                data_file.write(f"{data}\n")
            messagebox.showinfo(title="Success", message="Data Saved!")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=51)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_input = Entry(width=51)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "defaultUser@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=33)
password_input.grid(row=3, column=1)
password_generate_btn = Button(text="Generate Password", command=generate_password)
password_generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=28, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
