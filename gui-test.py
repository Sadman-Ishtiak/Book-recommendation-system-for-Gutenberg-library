from tkinter import *
from PIL import ImageTk
import customtkinter
import webbrowser
import main


app = customtkinter.CTk()
app.title("Book Recommendation System For Gutenberg Library")

def book_print_GUI(book):
    bookFrame = customtkinter.CTkFrame(app, width=1000)
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
    
for i in range(1,10):
    book_print_GUI(main.rando_recommend(main._books_))








































































app.after(0, lambda:app.state('zoomed'))
app.mainloop()