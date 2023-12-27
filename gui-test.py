from tkinter import *
from PIL import ImageTk
import customtkinter
import cli
import random

app = customtkinter.CTk()
app.title("Book Recommendation System For Gutenberg Library")   # This goes to the title bar
customtkinter.set_appearance_mode("system")                       # 'light', 'dark', 'system'
customtkinter.set_default_color_theme("blue")                   # Themes: "blue", "green", "dark-blue"


search_scrollable_frame = customtkinter.CTkScrollableFrame(app, width = 1000, height=650)
search_scrollable_frame.pack()

def forget_frame(frame):
    frame.pack_forget()

def book_print_GUI(book):
    bookFrame = Frame(search_scrollable_frame, width=1000)
    # bookFrame._set_appearance_mode("dark")
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Name", anchor="w")
    _dummy_.grid(row=1, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"], width=1000,wraplength=1000, anchor="w")
    bookTitle.grid(row=1, column=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Authors", anchor="w")
    _dummy_.grid(row=2, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=2, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Authors"], width=1000, wraplength=1000, anchor="w")
    bookAuthor.grid(row=2, column=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Issue Date", anchor="w")
    _dummy_.grid(row=3, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=3, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Issued"], width=1000, wraplength=1000, anchor="w")
    bookAuthor.grid(row=3, column=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="      Book type      ", anchor="w")
    _dummy_.grid(row=4, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=4, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Type"], width=1000, wraplength=1000, anchor="w")
    bookAuthor.grid(row=4, column=3)
    forget_button = customtkinter.CTkButton(bookFrame, text=f"Forget Frame", command=lambda f=bookFrame: forget_frame(f))
    forget_button.grid(row=5, column=3)
    bookFrame.pack()

random.shuffle(cli._books_)
for i in cli._books_[:200]:
    book_print_GUI(i)

app.after(0, lambda:app.state('zoomed'))
app.mainloop()