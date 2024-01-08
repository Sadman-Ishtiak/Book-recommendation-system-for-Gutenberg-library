import customtkinter
import random
from tkinter import *
import cli

app = customtkinter.CTk()
app.title("Top Level Window")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def openBookDetails(book):
    book = random.choice(cli._books_)
    
    top = customtkinter.CTkToplevel(app)
    top.title(f"{book['Title']}")
    number = 0
    print(book)
    dcnry = {"Title"  : "Book Name", 
            "Authors":"Authors",
            "Language":"Language", 
            "Type"    :"Book Type",
            "Subjects":"Category",
            "Issued"  :"Uploaded on gutenburg",
            }
    for i in dcnry:
        title = customtkinter.CTkLabel(top, text=f"{dcnry[i]}", width=80)
        title.grid(row=number, column=0)
        dash = customtkinter.CTkLabel(top, text=":", width=20)
        dash.grid(row=number, column=1)
        data = customtkinter.CTkLabel(top, text=book[i], width=800, wraplength=780)
        data.grid(row=number, column=2)
        number += 1
    

# btn = customtkinter.CTkButton(app, text="Hello", command=lambda book = random.choice(cli._books_) : openBookDetails(book))
# btn.pack()
for i in range(1000):
    openBookDetails(None)








app.after(0, lambda:app.state('zoomed'))
app.mainloop()