# Required libraries for this section
import csv
import random

# Global Variables 
books = []
retrun_query = []

# reading and chaching the file
with open("pg_catalog.csv",'r',encoding='utf-8') as csvfile:
    catalog = csv.DictReader(csvfile)
    for line in catalog:
            books.append(line)

# Defining the main function so that gui code can be added later
def main():
    print("WELCOME to a Gutenburg book recomendataion system CLI")
    print("Enter one of the numbers ")

# This returns a list of books that have the same name as the author the user have put in
def author_query():
    ...

# This function is takes a string as input and returns a priority dictionary list
def book_search():
    ...

# This function should take user's choice of book subject and types and later return a shuffled list
def randomized_choice():
    ...

# Link return for the book
def link_return():
    ...

# Calling the main function if and only if the file opened is this one
if __name__ == "__main__":
    main()