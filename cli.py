import csv
import random
import sys


# Global Variables - Static prefarably
_books_ = []      # This is to cache the book catalog from project Gutenburg
_my_books_ = []   # This is to cache the book list that user have identified to have already read
_wishList_ = []   # This is to cache the list of books that are in the user's wishList
_fieldnames_ = ["Text","Type","Issued","Title","Language","Authors","Subjects","LoCC","Bookshelves"] 


def main():
    print("Welcome to book recommendation system for project Gutenburg.")
    print("Please select one of the options-")
    print("1. Random Recommend")
    print("2. Catagorized Random Recommend")
    print("3. Search for a book")
    print("4. Search book of an author")
    print("5. Print read book list.")
    print("6. Read a book from the wishlist.")
    inp = input("Enter Your choice(integer) :")
    try:
        inp = int(inp)
    except ValueError or TypeError:
        print(f"user input {inp} was not an integer.")
    if inp == 1:
        randomBookChoice(_books_)
    if inp == 2:
        catagory = input("Please input a single word category: ").strip()
        newcatalog = bookfilter(_books_, catagory)
        randomBookChoice(newcatalog)
    if inp == 3:
        text = input("Enter to search : ").strip()
        bookSearch(text, 'Title')
    if inp == 4:
        text = input("Enter author name : ")
        bookSearch(text, 'Authors')
    if inp == 5:
        showList(_my_books_)
        userInput = input("Do you want to know any book data(y/n): ")
        if userInput == 'y' or userInput == 'Y':
            while bool(userInput):
                userInput = input('Enter the index for detail: ')
                try: print_Book_CLI(_my_books_[int(userInput)-1])
                except ValueError:
                    print("Not an integer.")
                    userInput = False
                except IndexError:
                    print("book not in index.")
                    userInput = False
    if inp == 6:
        showList(_wishList_)
        userInput = True
        while userInput:
            userInput = input("Enter the index of a book : ")
            try:
                print_Book_CLI(_wishList_[int(userInput) - 1])
            except ValueError:
                print("Input was not an integer.")
                userInput = False
            except IndexError:
                print("Book not in index. Please try again.")
            userInput = input('1. Add to read list')
            if userInput.strip() == '1':
                addToReadlist(_wishList_[int(userInput) - 1])
                sys.exit()


# This function is called if the user is calling one of the random choices
def randomBookChoice(listOfBooks):
    bookchoice = random.choice(listOfBooks)
    print_Book_CLI(bookchoice)
    print("1. Add to wishlist")
    print("2. Already Read it.")
    print("Next Choice.")
    a = input("Enter Your Choice :").strip()
    if a == "1":
        addToWishlist(bookchoice)
    elif a == "2":
        addToReadlist(bookchoice)
    else : 
        listOfBooks.remove(bookchoice)
        randomBookChoice(listOfBooks)


# Code to print the data of the book on the console screen 
def print_Book_CLI(a):
    x = "\n"
    print(x)
    print(f"Book name     : {a['Title'].replace(x, ' - ')}")
    print(f"Issue Date    : {a['Issued']}")
    print(f"Author's name : {a['Authors']}")
    print(f"Subjects      : {a['Subjects']}")
    print(f"Book Link     : {'https://gutenberg.org/ebooks/'+ a['Text']}")
    print(x)


# This is used for the category filtering
def bookfilter(bookList = _books_, catagory = None):
    returncatelogue = []
    for i in bookList:
        if catagory.lower() in i["Subjects"].lower():
            returncatelogue.append(i)
    return returncatelogue

#This searches the book and prints and the entierety of the task of the searching Of CLI options
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
    print()
    userInput = False
    while True:
        userInput = userInput if bool(userInput) else input("Enter the number beside the book you want to learn about : ")
        try :
            print_Book_CLI(answerlist[int(userInput) - 1])
            print("x. Add book to read list.")
            print("y. Add book to the wishlist.")
            print("Enter an index to check another book.")
            chosen_book = int(userInput)-1
            userInput = input("Enter your choice : ")
            if userInput.strip() == 'x' or userInput.strip() == 'X':
                addToReadlist(answerlist[chosen_book])
                sys.exit()
            if userInput.strip() == 'y' or userInput.strip() == 'Y':
                addToWishlist(answerlist[chosen_book])
                sys.exit()
        except ValueError:
            print("Not an integer. Please try again.")
            userInput = False
        except IndexError:
            print("book not in index. Please try again")
            userInput = False
    # print(text)
    # print(answerlist)


def showList(ListName):
    print()
    for i, BookData in enumerate(ListName) :
        print(i+1, BookData['Title'].replace('\n', '\t'))
    print()


# File Operations
# Add book to the wish list file
def addToWishlist(book):
    if book in _wishList_ : pass
    else:
        _wishList_.append(book)
        with open("user-files\wishlist.csv", "a") as fp:
            writing = csv.DictWriter(fp, fieldnames=_fieldnames_, lineterminator="\n")
            writing.writerow(book)


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
def deleteFromWishList(book):
    if book in _wishList_: _wishList_.remove(book)
    with open("user-files\wishlist.csv", "w", encoding="utf-8", newline='') as filePointer:
        writing = csv.DictWriter(filePointer, fieldnames=_fieldnames_)
        writing.writeheader()
        for i in _wishList_:
            writing.writerow(i)
    

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


# calling the main
if __name__ == "__main__":
    try : main()
    except EOFError: print("Exit program.")