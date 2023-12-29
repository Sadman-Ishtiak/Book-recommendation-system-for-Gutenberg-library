from tkinter import *
from PIL import ImageTk
import customtkinter
import csv
import webbrowser

# Global Variables - Static prefarably
_books_ = []      # This is to cache the book catalog from project Gutenburg
_my_books_ = []   # This is to cache the book list that user have identified to have already read
_wishList_ = []   # This is to cache the list of books that are in the user's wishList
_fieldnames_ = ["Text","Type","Issued","Title","Language","Authors","Subjects","LoCC","Bookshelves"] 

# Preprocessing all the required data
# caching the user read books list
with open("user-files\my_books.csv", "r", encoding="utf-8") as filePointer:
    catalog = csv.DictReader(filePointer)
    for i in catalog:
        _my_books_.append(i)
# caching the user wishlist
with open("user-files\wishlist.csv", "r", encoding="utf-8") as filePointer:
    catalog = csv.DictReader(filePointer)
    for i in catalog:
        _wishList_.append(i)
# caching the book caatalog
with open("files\pg_catalog.csv",'r',encoding='utf-8') as filePointer:
    catalog = csv.DictReader(filePointer)
    for line in catalog:
        if line["Language"] == 'en' and line["Type"] == 'Text' and line not in _my_books_:
            _books_.append(line)


# Defining the app window 
app = customtkinter.CTk()
app.title("Book Recommendation System For Gutenberg Library")   # This goes to the title bar
customtkinter.set_appearance_mode("dark")                       # 'light', 'dark', 'system'
customtkinter.set_default_color_theme("blue")                   # Themes: "blue", "green", "dark-blue"
# Other themes do work but the dark theme and blue appearance looks better in my opinion.

# This function is checking which main segmented_button is selected in the mainloop and
# it is forgetting all the other except the selected frame and packing that frame in the center of the screen.
def segmented_button_callback(value):
    if value == "Search":
        frame_search.pack()
        frame_list.pack_forget()
        frame_recommend.pack_forget()
    if value == "List":
        frame_search.pack_forget()
        frame_list.pack()
        frame_recommend.pack_forget()
    if value == "Recommend":
        frame_search.pack_forget()
        frame_list.pack_forget()
        frame_recommend.pack()

# This stringVariable takes input from the segmented button and this returns value without needing to use a lambda function
segemented_button_var = customtkinter.StringVar(value=None)
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Search", "List", "Recommend"],
                                                    width=1000, height=35,
                                                    command=segmented_button_callback,
                                                    dynamic_resizing=False,
                                                    corner_radius=10,
                                                    variable=segemented_button_var
                                                    )
# Packing the button in the screen
segemented_button.pack(pady=10) # Padding a little in the top to not touching the title bar

# Setting up the three frames for search list and recommend respectively
frame_search    = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_list      = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)
frame_recommend = customtkinter.CTkFrame(app, width=1920, height=900, corner_radius=30)

# Testing to see if the code works or not.
lab2 = customtkinter.CTkLabel(frame_list, text="List")
lab3 = customtkinter.CTkLabel(frame_recommend, text="Recommend")
lab4 = customtkinter.CTkLabel(frame_recommend, text="not Recommend")
lab4.grid(row=2, column=2)
lab2.grid(row=1, column=1)
lab3.grid(row=1, column=1)

# Functions for search frame 
def searchfunction(choice):
    print(choice)      # This prints OK So this way we can det input
    print(sbar.get())  # This also works so we can use this as input as well

def bookSearch(text, SearchOn = 'Text') : 
    answerdictionary = {}
    text = text.split()
    for i in range(len(text)):
        answerdictionary[i] = []
    for i in _books_:
        x = 0
        for j in text:
            if j.lower() in i[SearchOn].lower():
                x += 1
        if x!= 0:
            answerdictionary[len(answerdictionary) - x].append(i)
    answerlist = []
    for i in sorted(answerdictionary.keys()):
        for j in answerdictionary[i][:int(100/(i+1))]:
            answerlist.append(j)
            # print(i, j["Title"].replace('\n', '\t')) # For debugging purposes
    print()
    for i,j in enumerate(answerlist):
        print(i+1, j['Title'].replace('\n', '\t'))

# Search frame 
sbar = customtkinter.CTkEntry(frame_search, placeholder_text="Enter text", width=800)
sbar.grid(row=1, column=1)
s_option = customtkinter.CTkOptionMenu(frame_search, values=['Book Search', 'Author Search'], width=200, command=searchfunction)
s_option.grid(row=1, column=2)

# This frame should contain all the book data after it is printed on the screen
search_scrollable_frame = customtkinter.CTkFrame(frame_search, width = 1000, height=550)
search_scrollable_frame.grid(row=2, column=1, columnspan=2, pady=5)












































app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop()