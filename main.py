import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

FONT = ("Arial", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = random_letters + random_numbers + random_symbols
    shuffle(password_list)

    password_input.delete(0, END)

    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
                                                              f"\nPassword: {password}\n Do you wish to save this details?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Update data with new_data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Update data with new_data
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                # Reset input fields
                email_input.delete(0, END)
                email_input.insert(0, "example@mail.com")
                password_input.delete(0, END)
                website_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        if website_input.get() in data:
            print("yes")
        else:
            print("There is no")


# ---------------------------- UI SETUP ------------------------------- #


#### Window ####
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#### Canvas ####
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

####Labels ####
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

#### Input Fields ####
website_input = Entry(width=23)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=43)
email_input.insert(END, "example@mail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=24)
password_input.grid(column=1, row=3)

#### Buttons ####
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=41, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(column=2, row=1)

window.mainloop()
