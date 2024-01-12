from tkinter import *
import customtkinter
import csv
import webbrowser
import random

# Global Variables - Static prefarably
_books_ = []      # This is to cache the book catalog from project Gutenburg
_my_books_ = []   # This is to cache the book list that user have identified to have already read
_wishList_ = []   # This is to cache the list of books that are in the user's wishList
_fieldnames_ = ["Text","Type","Issued","Title","Language","Authors","Subjects","LoCC","Bookshelves"] 

# Defining the app window 
app = customtkinter.CTk()
app.title("Book Recommendation System For Gutenberg Library")     # This goes to the title bar
customtkinter.set_appearance_mode("system")                       # 'light', 'dark', 'system'
customtkinter.set_default_color_theme("blue")                     # Themes: "blue", "green"


# Preprocessing all the required data
# caching the user read books list
with open("user-files\my_books.csv", "r", encoding="ISO-8859-1") as filePointer:
    catalog = csv.DictReader(filePointer)
    for i in catalog:
        _my_books_.append(i)
# caching the user wishlist
with open("user-files\wishlist.csv", "r", encoding="ISO-8859-1") as filePointer:
    catalog = csv.DictReader(filePointer)
    for i in catalog:
        _wishList_.append(i)
# caching the book caatalog
with open("files\pg_catalog.csv",'r',encoding='ISO-8859-1') as filePointer:
    catalog = csv.DictReader(filePointer)
    for line in catalog:
        if line["Language"] == 'en' and line["Type"] == "Text" and line not in _my_books_:
            _books_.append(line)


# Title of the program
TitleLabel = customtkinter.CTkLabel(app, width=1000, text="Book Recommendation System For Public Domain Books in Gutenburg Library", font=("ariel", 20))
TitleLabel.pack(pady=5)


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
                                                    width=1020, height=35,
                                                    command=segmented_button_callback,
                                                    dynamic_resizing=False,
                                                    corner_radius=10,
                                                    variable=segemented_button_var
                                                    )
# Packing the button in the screen
segemented_button.pack(pady=5) # Padding a little in the top to not touching the title bar

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
    clearFrame(search_scrollable_frame)
    for i in answerlist:
        book_print_GUI_search(i)

# This deletes all the widgets in a frame but keeps all the frame intact
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Functions for search frame 
def searchfunction(choice):
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
        with open("user-files\wishlist.csv", "a", encoding="ISO-8859-1") as fp:
            writing = csv.DictWriter(fp, fieldnames=_fieldnames_, lineterminator="\n")
            writing.writerow(book)
    forget_frame(frame)


# Add to the read file for user 
def addToReadlist(book, frame):
    _my_books_.append(book)
    if book in _books_ : _books_.remove(book)
    if book in _wishList_: deleteFromWishList(book, frame)
    with open("user-files\my_books.csv", "a", encoding="ISO-8859-1") as filePointer:
        writing = csv.DictWriter(filePointer, fieldnames=_fieldnames_, lineterminator="\n")
        writing.writerow(book)
    forget_frame(frame)

# Delete book from the wishlist after user asks to put them on read list 
# Basically rewrites the entire wislist.csv to remove the book from the file
def deleteFromWishList(book, frame):
    if book in _wishList_: _wishList_.remove(book)
    with open("user-files\wishlist.csv", "w", encoding="ISO-8859-1", newline='') as filePointer:
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
def book_print_GUI_search(book):
    bookFrame = customtkinter.CTkFrame(search_scrollable_frame, width=1000)
    # bookFrame._set_appearance_mode("dark")
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Name", anchor="w")
    _dummy_.grid(row=1, column=1, padx=20)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"], width=900,wraplength=800, anchor="w")
    bookTitle.grid(row=1, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Authors", anchor="w")
    _dummy_.grid(row=2, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=2, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Authors"], width=900, wraplength=800, anchor="w")
    bookAuthor.grid(row=2, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Issue Date", anchor="w")
    _dummy_.grid(row=3, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=3, column=2)
    bookIssued = customtkinter.CTkLabel(bookFrame, text=book["Issued"], anchor="w")
    bookIssued.grid(row=3, column=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Book type", anchor="w")
    _dummy_.grid(row=4, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=4, column=2)
    bookType = customtkinter.CTkLabel(bookFrame, text=book["Type"], anchor="w")
    bookType.grid(row=4, column=3)
    forget_button = customtkinter.CTkButton(bookFrame, text="Hide Book from this list", command=lambda f=bookFrame: forget_frame(f))
    AddToWishlistutton = customtkinter.CTkButton(bookFrame, text="Add to Wishlist", 
                                                 command=lambda f=bookFrame,book=book: addToWishlist(book, f))
    forget_button3 = customtkinter.CTkButton(bookFrame, text="Open Link in the web", command=lambda f=book: openBrowser(f))
    forget_button4 = customtkinter.CTkButton(bookFrame, text="Add To Readlist", command=lambda f=bookFrame, 
                                             book=book: addToReadlist(book, f))
    forget_button.grid(row=3, column=4, pady=1)
    AddToWishlistutton.grid(row=3, column=5)
    forget_button3.grid(row=4, column=4)
    forget_button4.grid(row=4, column=5)
    bookFrame.pack(pady=1)

# Opens a google link of the search bar 
def google_link_opener():
    link ="https://google.com/search?q=" +  sbar.get().replace(" ", "+")
    webbrowser.open(link)

# Search frame 
sbar = customtkinter.CTkEntry(frame_search, placeholder_text="Enter text to search", width=780)
sbar.grid(row=1, column=1)

image_path = "files/google.png"  # Replace with the actual path to your image file
image = PhotoImage(file=image_path)
image_button = Button(frame_search, image=image, command=google_link_opener)
image_button.grid(row=1, column=3)

s_option = customtkinter.CTkOptionMenu(frame_search, values=['Book Search', 'Author Search'], width=210, command=searchfunction)
s_option.grid(row=1, column=2)

# This frame should contain all the book data after it is printed on the screen
search_scrollable_frame = customtkinter.CTkScrollableFrame(frame_search, width = 1000, height=900)
search_scrollable_frame.grid(row=2, column=1, columnspan=3, pady=5)

def print_book_wishlist(book):
    bookFrame = customtkinter.CTkFrame(list_scrollable_frame, width=1000)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Name", anchor="w")
    _dummy_.grid(row=1, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"], width=900,wraplength=800, anchor="w")
    bookTitle.grid(row=1, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Authors", anchor="w")
    _dummy_.grid(row=2, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=2, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Authors"], width=900, wraplength=800, anchor="w")
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
    forget_button3 = customtkinter.CTkButton(bookFrame, text="Open Link in the web", command=lambda f=book: openBrowser(f))
    forget_button4 = customtkinter.CTkButton(bookFrame, text="Add To Readlist", command=lambda f=bookFrame, 
                                             book=book: addToReadlist(book, f))
    forget_button3.grid(row=4, column=4)
    forget_button4.grid(row=4, column=5)
    bookFrame.pack()

def print_book_readlist(book):
    bookFrame = customtkinter.CTkFrame(list_scrollable_frame, width=1000)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Name", anchor="w")
    _dummy_.grid(row=1, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"], width=900,wraplength=800, anchor="w")
    bookTitle.grid(row=1, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Authors", anchor="w")
    _dummy_.grid(row=2, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=2, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Authors"], width=900, wraplength=800, anchor="w")
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
    forget_button3 = customtkinter.CTkButton(bookFrame, text="Open Link in the web", command=lambda f=book: openBrowser(f))
    forget_button3.grid(row=4, column=4)
    bookFrame.pack(pady=1)

# This defines the function to print the list that is selected 
def show_list_button(value):
    if value == "Wishlist" :
        clearFrame(list_scrollable_frame)
        for i in _wishList_:
            print_book_wishlist(i)
    if value == "Read List" :
        clearFrame(list_scrollable_frame)
        for i in _my_books_:
            print_book_readlist(i)

show_list_var = customtkinter.StringVar(value=None)
show_list_segment_btn = customtkinter.CTkSegmentedButton(frame_list, values=["Wishlist", "Read List"],
                                                    width=1020, height=30,
                                                    command=show_list_button,
                                                    dynamic_resizing=False,
                                                    corner_radius=5,
                                                    variable=show_list_var
                                                    )
show_list_segment_btn.pack()

list_scrollable_frame = customtkinter.CTkScrollableFrame(frame_list, width=1000, height=900)
list_scrollable_frame.pack()


def bookfilter(bookList = _books_, catagory = None):
    returncatelogue = []
    for i in bookList:
        if catagory.lower() in i["Subjects"].lower():
            returncatelogue.append(i)
    return returncatelogue


def print10random(catalog):
    for _ in range(10):
        print_book_recommend(random.choice(catalog))

def printing(a):
    a = typebar.get()
    clearFrame(random_scrollable_frame)
    catalog = bookfilter(_books_, a)
    print10random(catalog)

def recommend_type(value):
    clearFrame(random_scrollable_frame)
    if value == optns[0]:
        print10random(_books_)
    if value == optns[1]:
        # clearFrame(random_scrollable_frame)
        typebar_var = StringVar()
        global typebar
        typebar = customtkinter.CTkEntry(random_scrollable_frame, 
                                         placeholder_text="Enter your Desired category of book that you want to read.", 
                                         width=1020, textvariable=typebar_var)
        typebar.bind('<Return>', printing)
        typebar.pack()


def print_book_recommend(book):
    bookFrame = customtkinter.CTkFrame(random_scrollable_frame, width=1000)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Name", anchor="w")
    _dummy_.grid(row=1, column=1, padx=20)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=1, column=2)
    bookTitle = customtkinter.CTkLabel(bookFrame, text=book["Title"], width=900,wraplength=800, anchor="w")
    bookTitle.grid(row=1, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Authors", anchor="w")
    _dummy_.grid(row=2, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=2, column=2)
    bookAuthor = customtkinter.CTkLabel(bookFrame, text=book["Authors"], width=900, wraplength=800, anchor="w")
    bookAuthor.grid(row=2, column=3, columnspan=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Issue Date", anchor="w")
    _dummy_.grid(row=3, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=3, column=2)
    bookIssued = customtkinter.CTkLabel(bookFrame, text=book["Issued"], anchor="w")
    bookIssued.grid(row=3, column=3)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text="Book type", anchor="w")
    _dummy_.grid(row=4, column=1)
    _dummy_ = customtkinter.CTkLabel(bookFrame, text='  :  ', anchor="w")
    _dummy_.grid(row=4, column=2)
    bookType = customtkinter.CTkLabel(bookFrame, text=book["Type"], anchor="w")
    bookType.grid(row=4, column=3)
    forget_button = customtkinter.CTkButton(bookFrame, text="Hide Book from this list", command=lambda f=bookFrame: forget_frame(f))
    AddToWishlistutton = customtkinter.CTkButton(bookFrame, text="Add to Wishlist", command=lambda f=bookFrame, 
                                                 book=book: addToWishlist(book, f))
    forget_button3 = customtkinter.CTkButton(bookFrame, text="Open Link in the web", command=lambda f=book: openBrowser(f))
    forget_button4 = customtkinter.CTkButton(bookFrame, text="Add To Readlist", command=lambda f=bookFrame, 
                                             book=book: addToReadlist(book, f))
    forget_button.grid(row=3, column=4, pady=1)
    AddToWishlistutton.grid(row=3, column=5)
    forget_button3.grid(row=4, column=4)
    forget_button4.grid(row=4, column=5)
    bookFrame.pack(pady=1)

# Recommendation page

optns = ["Random Recommend", "Categorized Random Recommend"]
random_recommend_segmented = customtkinter.CTkSegmentedButton(frame_recommend, values=optns, height=30, width=1020,
                                                              dynamic_resizing=False, command=recommend_type)
random_recommend_segmented.pack()
random_scrollable_frame = customtkinter.CTkScrollableFrame(frame_recommend, width=1000, height=900)
random_scrollable_frame.pack()


app.after(0, lambda:app.state('zoomed')) # Don't know how this works but this put file in full screen mode
app.mainloop() # This starts the mainloop that keeps the widgets in the screen
