from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# --- SEARCH --- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data:
            messagebox.showinfo(title=website,
                                    message=f"Email: {data[website]['email']}\n"
                                            f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exist")


# --- PASSWORD GENERATOR --- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = random_letters + random_numbers + random_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # Pyperclip auto copies password to clipboard
    pyperclip.copy(password)

# --- SAVE PASSWORD --- #
def save():
    # Get entry values
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check that fields are completed
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Create new file and add new data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --- UI SETUP --- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=("Arial", 14, "normal"))
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=("Arial", 14, "normal"))
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=("Arial", 14, "normal"))
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "happyharping@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
gen_password_btn = Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn = Button(text="Search", width=13, command=find_password)
search_btn.grid(row=1, column=2)


window.mainloop()
