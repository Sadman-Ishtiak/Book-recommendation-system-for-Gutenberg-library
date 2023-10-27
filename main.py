# Required libraries for this section
import csv
import random
import sys

# Global Variables
books = []
retrun_query = []
readed_book = []

# reading and chaching the file
with open("files\pg_catalog.csv",'r',encoding='utf-8') as csvfile:
    catalog = csv.DictReader(csvfile)
    for line in catalog:
        if line["Language"] == 'en' and line["Type"] == 'Text':
            books.append(line)

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
                book = rando_recommend(books)
                print_Book_CLI(book)
                print("Do you want to read this book? (y/n) : ", end="")
                ran = input()
                if ran == "y" or ran == "Y":
                    print("Please copy the link and use a browser to get the book : ", link_return(book))
                    print("Saved to file")
                    sys.exit()
                elif ran == "N" or ran == "n":
                    print("Another Random choice ?(y/n) : ", end="")
                    ran = input()
                    if ran == "n" or ran == "N" : break
        else : break

def print_Book_CLI(a):
    print(f"Book name     : {a['Title']}")
    print(f"Issue Date    : {a['Issued']}")
    print(f"Author's name : {a['Authors']}")
    print(f"Subjects      : {a['Subjects']}")

# Random recommendation
def rando_recommend(list):
    return random.choice(list)

# This returns a list of books that have the same name as the author the user have put in
def author_query():
    ...

# This function is takes a string as input and returns a priority dictionary list
def book_search():
    ...

# Link return for the book
def link_return(book):
    return "https://gutenberg.org/ebooks/" + str(book["Text"])

# Calling the main function if and only if the file opened is this one
if __name__ == "__main__":
    main()