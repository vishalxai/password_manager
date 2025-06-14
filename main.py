from tkinter import *
from tkinter import messagebox
import random
import string
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits+ symbols
    password = "".join(random.choice(all_chars) for _ in range(12))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }


# Checking if any field is empty
    if len(website)==0 or len(email) ==0 or len(password)==0:
        messagebox.showwarning(title="Oops",message="Please don't leave any field empty !")
    else:
        try:
            with open("test_data.json", "r")as data_file :
                #load existing data
                data = json.load(data_file)
        except FileNotFoundError:
            #create new file if it doenst exist
            with open("test_data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            #updata existing data with new entries
            data.update(new_data)
            with open("test_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height = 200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(row=0, column=1)

#  Need to create website widget(width= 35) email/username password(width = 21) and generate password and last add button(width 36)
#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "myemail@gmail.com")  #Entered most used email
email_entry.grid(row=2,column=1,columnspan=2)

# password entry
password_entry = Entry(width= 21,show="*")
password_entry.grid(row=3, column=1)
#Buttons
generate_password_button= Button(text="Generate Password ",command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add",width=40,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()