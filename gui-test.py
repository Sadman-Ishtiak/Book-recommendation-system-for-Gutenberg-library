from tkinter import *
from PIL import ImageTk
import customtkinter


app = customtkinter.CTk()
app.title("Book Recommendation System For Gutenberg Library")
# app._set_appearance_mode("dark")

def book_print_GUI(book):
    bookFrame = customtkinter.CTkFrame(app, width=1000)
    # bookFrame._set_appearance_mode("dark")
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Name", anchor="w")
    _dummy_.grid(row=1, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"].replace('\n', ' - '), width=1000,wraplength=1000, anchor="w")
    bookTitle.grid(row=1, column=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Authors", anchor="w")
    _dummy_.grid(row=2, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=2, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Authors"], width=1000, wraplength=1000, anchor="w")
    bookAuthor.grid(row=2, column=3)
    bookFrame.pack()


app.after(0, lambda:app.state('zoomed'))
app.mainloop()