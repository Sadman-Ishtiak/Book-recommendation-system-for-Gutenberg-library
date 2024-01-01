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
        if line["Language"] == 'en' and line not in _my_books_:
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


#Searches for book
def bookSearch(text, SearchOn) :
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
    # for i,j in enumerate(answerlist):
    #     print(i+1, j['Title'].replace('\n', '\t'))
    for widget in search_scrollable_frame.winfo_children():
        widget.destroy()
    for i in answerlist:
        book_print_GUI(i)

# Functions for search frame 
def searchfunction(choice):
    print(choice)      # This prints OK So this way we can det input
    print(sbar.get())  # This also works so we can use this as input as well
    text = sbar.get()
    if choice == 'Book Search' : bookSearch(text, "Title")
    if choice == 'Author Search' : bookSearch(text, "Authors")

def forget_frame(frame):
    frame.pack_forget()

# Add book to the wish list file
def addToWishlist(book,frame):
    if book in _wishList_ : pass
    else:
        _wishList_.append(book)
        with open("user-files\wishlist.csv", "a") as fp:
            writing = csv.DictWriter(fp, fieldnames=_fieldnames_, lineterminator="\n")
            writing.writerow(book)
    forget_frame(frame)


# Add to the read file for user 
def addToReadlist(book):
    _my_books_.append(book)
    _books_.remove(book)
    if book in _wishList_: deleteFromWishList(book)
    with open("user-files\my_books.csv", "a") as filePointer:
        writing = csv.DictWriter(filePointer, fieldnames=_fieldnames_, lineterminator="\n")
        writing.writerow(book)

# Delete book from the wishlist after user asks to put them on read list 
# Basically rewrites the entire wislist.csv to remove the book from the file
def deleteFromWishList(book, frame):
    if book in _wishList_: _wishList_.remove(book)
    with open("user-files\wishlist.csv", "w", encoding="utf-8", newline='') as filePointer:
        writing = csv.DictWriter(filePointer, fieldnames=_fieldnames_)
        writing.writeheader()
        for i in _wishList_:
            writing.writerow(i)
    forget_frame(frame)

# This opens the link of the book in the default browser of the device
def openBrowser(book):
    link = "https://gutenberg.org/ebooks/" + str(book["Text"])
    webbrowser.open(link, new=0, autoraise=True)

# This prints the book with the details of the book in the scrollable frame
def book_print_GUI(book):
    bookFrame = customtkinter.CTkFrame(search_scrollable_frame, width=1000)
    # bookFrame._set_appearance_mode("dark")
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Name", anchor="w")
    _dummy_.grid(row=1, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"], width=850,wraplength=800, anchor="w")
    bookTitle.grid(row=1, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Authors", anchor="w")
    _dummy_.grid(row=2, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=2, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Authors"], width=850, wraplength=800, anchor="w")
    bookAuthor.grid(row=2, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Issue Date", anchor="w")
    _dummy_.grid(row=3, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=3, column=2)
    bookIssued = customtkinter.CTkLabel(bookFrame, text=book["Issued"], anchor="w")
    bookIssued.grid(row=3, column=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="      Book type      ", anchor="w")
    _dummy_.grid(row=4, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=4, column=2)
    bookType = customtkinter.CTkLabel(bookFrame, text=book["Type"], anchor="w")
    bookType.grid(row=4, column=3)
    forget_button = customtkinter.CTkButton(bookFrame, text=f"Hide Book from this list", command=lambda f=bookFrame: forget_frame(f))
    AddToWishlistutton = customtkinter.CTkButton(bookFrame, text=f"Add to Wishlist", command=lambda f=bookFrame, book=book: addToWishlist(book, f))
    forget_button3 = customtkinter.CTkButton(bookFrame, text=f"Open Link in the web", command=lambda f=book: openBrowser(f))
    forget_button4 = customtkinter.CTkButton(bookFrame, text=f"Add To Readlist", command=lambda f=bookFrame, book=book: forget_frame(book, f))
    forget_button.grid(row=3, column=4, pady=1)
    AddToWishlistutton.grid(row=3, column=5)
    forget_button3.grid(row=4, column=4)
    forget_button4.grid(row=4, column=5)
    bookFrame.pack()
# Search frame 
sbar = customtkinter.CTkEntry(frame_search, placeholder_text="Enter text", width=800)
sbar.grid(row=1, column=1)
s_option = customtkinter.CTkOptionMenu(frame_search, values=['Book Search', 'Author Search'], width=200, command=searchfunction)
s_option.grid(row=1, column=2)

# This frame should contain all the book data after it is printed on the screen
search_scrollable_frame = customtkinter.CTkScrollableFrame(frame_search, width = 1000, height=550)
search_scrollable_frame.grid(row=2, column=1, columnspan=2, pady=5)












































app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop()