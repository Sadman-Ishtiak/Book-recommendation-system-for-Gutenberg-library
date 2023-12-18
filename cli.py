import csv
import random
import sys

# Global Variables - Static prefarably
_books_ = []      # This is to cache the book catalog from project Gutenburg
_my_books_ = []   # This is to cache the book list that user have identified to have already read
_fieldnames_ = ["Text","Type","Issued","Title","Language","Authors","Subjects","LoCC","Bookshelves"]



def main():
    print("Welcome to book recommendation system for project Gutenburg.")
    print("Please select one of the options-")
    print("1. Random Recommend")
    print("2. Catagorized Random Recommend")
    print("3. Search for a book")
    print("4. Search book of an author")
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
    for i,j in enumerate(answerlist):
        print(i+1, j['Title'].replace('\n', '\t'))
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
    pass














































































# File Operation
# Add book to the wish list file
def addToWishlist(book):
    with open("user-files\wishlist.csv", "a") as fp:
        writing = csv.DictWriter(fp, fieldnames=_fieldnames_, lineterminator="\n")
        writing.writerow(book)

# Add to the read file for user 
def addToReadlist(book):
    _my_books_.append(book)
    try:
        _books_.pop(_books_.index(book))
    except: ...
    with open("user-files\my_books.csv", "a") as fp:
        writing = csv.DictWriter(fp, fieldnames=_fieldnames_, lineterminator="\n")
        writing.writerow(book)


# Preprocessing all the required data
# caching the user read books list
with open("user-files\my_books.csv", "r", encoding="utf-8") as meh:
    catalog = csv.DictReader(meh)
    for i in catalog:
        _my_books_.append(i)

# caching the book caatalog
with open("files\pg_catalog.csv",'r',encoding='utf-8') as csvfile:
    catalog = csv.DictReader(csvfile)
    for line in catalog:
        if line["Language"] == 'en' and line["Type"] == 'Text' and line not in _my_books_:
            _books_.append(line)


# calling the main
if __name__ == "__main__":
    main()