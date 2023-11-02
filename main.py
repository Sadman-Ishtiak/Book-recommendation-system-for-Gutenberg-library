# Required libraries for this section
import csv
import random
import sys

# Global Variables - Static prefarably
_books_ = []
_my_books_ = []
# Global Variables - Changing type 
retrun_query = []

# caching list user has read
with open("files\my_books.csv", "r", encoding="utf-8") as meh:
    catalog = csv.DictReader(meh)
    for i in catalog:
        _my_books_.append(i)

# reading and chaching the file
with open("files\pg_catalog.csv",'r',encoding='utf-8') as csvfile:
    catalog = csv.DictReader(csvfile)
    for line in catalog:
        if line["Language"] == 'en' and line["Type"] == 'Text' and line not in _my_books_:
            _books_.append(line)

# Defining the main function so that gui code can be added later
def main():
    print("WELCOME to a Gutenburg book recomendataion system CLI")
    while True:
        print("Enter one of the numbers which you want to use.")
        print("1. Give a random recommendation")
        print("2. Give a recommendation with favourite category")
        print("3. Read Own read list")
        print("0. Exit Program")
        
        flag = int(input())
        if flag == 0: break
        elif flag == 1:
            while True:
                book = rando_recommend(_books_)
                print_Book_CLI(book)
                print("Do you want to read this book? (y/n) : ", end="")
                usr_input = input()
                if usr_input == "y" or usr_input == "Y":
                    print("Please copy the link and use a browser to get the book : ", link_return(book))
                    print("Saved to file")
                    sys.exit()
                elif usr_input == "N" or usr_input == "n":
                    print("Another Random choice ?(y/n) : ", end="")
                    usr_input = input()
                    if usr_input == "n" or usr_input == "N" : break
        elif flag == 3 : 
            print_list_cli(_my_books_)
        else : break

def print_Book_CLI(a):
    x = "\n"
    print(f"Book name     : {a['Title'].replace(x, ' - ')}")
    print(f"Issue Date    : {a['Issued']}")
    print(f"Author's name : {a['Authors']}")
    print(f"Subjects      : {a['Subjects']}")

#Filtering books on to get randomized choices
def filter_tag(tag):
    retrun_query = []
    for i in _books_:
        if tag in i["Subjects"]:
            retrun_query.append(i)
    return retrun_query

# Random recommendation
def rando_recommend(list):
    return random.choice(list)

# Prints on the command line interface 
def print_list_cli(list_to_print):
    counter = 1
    for i in list_to_print : 
        name = i["Title"].replace("\n", "  -  ")
        print(counter, ".", name)
        counter += 1

# Add to the read file for user 
def add_book_to_read(book):
    _my_books_.append(book)
    try:
        _books_.pop(_books_.index(book))
    except: ...
    with open("files\my_books.csv", "a") as fp:
        writing = csv.DictWriter(fp)
        writing.writerow(book)

# This returns a list of books that have the same name as the author the user have put in
def author_query():
    ...

# This function is takes a string as input and returns a priority dictionary list
def book_search(Book_library, key):
    cache_result = {}
    key = key.split()
    n = len(key)
    for i in range(n+1):
        cache_result[i] = []
    
    return converted_to_list(cache_result)

# This converts Priority map to list
def converted_to_list(priority_dictionary):
    ret = []
    for i in priority_dictionary : 
        for j in i : 
            ret.append(j)
    return ret

# Link return for the book
def link_return(book):
    return "https://gutenberg.org/ebooks/" + str(book["Text"])

# Calling the main function if and only if this file opened is this one
if __name__ == "__main__":
    main()