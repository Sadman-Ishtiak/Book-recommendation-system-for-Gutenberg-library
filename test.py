import customtkinter
import random
from tkinter import *
from cli import _books_
# from main import search_scrollable_frame,forget_frame, addToReadlist, addToWishlist, openBrowser, _books_

app = customtkinter.CTk()
app.title("Top Level Window")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def openBookDetails(book):
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
            "Text"    :"Gutenburg Book ID"
            }
    for i in dcnry:
        title = customtkinter.CTkLabel(top, text=f"{dcnry[i]}", width=80)
        title.grid(row=number, column=0, padx=10)
        dash = customtkinter.CTkLabel(top, text=":", width=20)
        dash.grid(row=number, column=1)
        data = customtkinter.CTkLabel(top, text=book[i], width=780, wraplength=780)
        data.grid(row=number, column=2)
        number += 1


search_scrollable_frame = customtkinter.CTkScrollableFrame(app, width = 1000, height=1000)
search_scrollable_frame.pack()

def book_print_GUI_search(book, count):
    bookFrame = customtkinter.CTkFrame(search_scrollable_frame, width=1000)
    btn = customtkinter.CTkButton(bookFrame, text=count, width=100, anchor="center", command=lambda book = book : openBookDetails(book))
    btn.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"].replace('\n',' - '), width=800,wraplength=800, anchor="w")
    bookTitle.grid(row=1, column=1)
    bookFrame.pack()





# btn = customtkinter.CTkButton(app, text="Hello", command=lambda book = random.choice(cli._books_) : openBookDetails(book))
# btn.pack()
for i in range(500):
    count = str(i+1)
    book_print_GUI_search(random.choice(_books_), count)







# app.after(0, lambda:app.state('zoomed'))
app.mainloop()