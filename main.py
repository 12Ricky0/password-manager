from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    l = [random.choice(letters) for _ in range(random.randint(8, 10))]
    n = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    s = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = l + n + s
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_input():
    site = website_entry.get()
    user_name = email_entry.get()
    password = password_entry.get()

    if site == '' or user_name == '' or password == '':
        messagebox.showerror(title='Error', message='Please enter all fields')

    else:
        is_ok = messagebox.askokcancel(title=site,
                                       message=f"Please confirm your details:\nEmail:{user_name}\nPassword:{password}")
        if is_ok:
            data = {site: {"email": user_name, "password": password}}
            try:
                with open("data.json", "r") as f1:
                    data1 = json.load(f1)
                    data1.update(data)
                with open("data.json", 'w') as f:
                    json.dump(data1, f, indent=4)

            except FileNotFoundError:
                with open("data.json", 'w') as f:
                    json.dump(data, f, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)


def find_password():
    site = website_entry.get()
    try:
        with open("data.json", "r") as data:
            data = json.load(data)
        print(data.get(site))
        messagebox.showinfo(title=site, message=f"Email: {data.get(site)["email"]}\nPassword: {data.get(site)["password"]}")

    except FileNotFoundError:
        messagebox.showerror(title='Error', message='Please')

    except TypeError:
        messagebox.showinfo(title='Error', message='No data file found')

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

canvas = Canvas(windows, width=200, height=200)
myimg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=1, row=0)

# Labels

Label(windows, text="Email/Username:", font="15").grid(column=0, row=2)
Label(windows, text="Website:", font="15").grid(column=0, row=1)
Label(windows, text="Password:", font="15").grid(column=0, row=3)

# Entries

website_entry = Entry(windows, width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(windows, width=38)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(windows, width=21)
password_entry.grid(column=1, row=3)
# Buttons

Button(windows, text="Generate Password", font="15", command=generate_password).grid(row=3, column=2)
Button(windows, text="Add", font="15", width=36, command=save_input).grid(row=4, column=1, columnspan=2)
Button(windows, text="Search", font="15", width=13, command=find_password).grid(column=2, row=1)
windows.mainloop()
