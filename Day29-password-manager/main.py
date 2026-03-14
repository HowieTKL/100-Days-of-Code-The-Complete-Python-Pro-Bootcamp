import json

import customtkinter as tk
import tkinter.messagebox as mb
import random
import pyperclip
from PIL import Image

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        mb.showerror("Error", "Please fill all fields")
    else:
        try:
            with open("passwords.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)
        with open("passwords.json", "w") as f:
            json.dump(data, f, indent=2)
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        website_entry.focus()

# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
        print(data[website])
    except FileNotFoundError:
        mb.showerror("Error", "Not found")
    except KeyError:
        mb.showerror("Error", "Not found")
    else:
        email_entry.delete(0, tk.END)
        email_entry.insert(0, data[website]["email"])
        password_entry.delete(0, tk.END)
        password_entry.insert(0, data[website]["password"])
        pyperclip.copy(data[website]["password"])

# ---------------------------- UI SETUP ------------------------------- #

#tk.set_appearance_mode("light")
window = tk.CTk()
window.title("My Password Manager")
window.config(padx=20, pady=20)

logo_image = tk.CTkImage(light_image=Image.open("logo.png"), dark_image=Image.open("logo.png"), size=(100, 100))
image_label = tk.CTkLabel(window, image=logo_image, text="")
image_label.grid(row=0, column=1)

website_label = tk.CTkLabel(window, text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.CTkEntry(window, width=21)
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()

search_button = tk.CTkButton(window, text="Search", command=search)
search_button.grid(row=1, column=2, sticky="ew")

email_label = tk.CTkLabel(window, text="E-mail/Username:")
email_label.grid(row=2, column=0)

email_entry = tk.CTkEntry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(tk.END, "praecognita@gmail.com")

password_label = tk.CTkLabel(window, text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.CTkEntry(window, width=21)
password_entry.grid(row=3, column=1, sticky="ew")

generate_password_button = tk.CTkButton(window, text="Gen Pwd", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")

add_button = tk.CTkButton(window, text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


window.mainloop()
