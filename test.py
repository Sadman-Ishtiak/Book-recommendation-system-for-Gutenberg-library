import pytest
import random
import main

def count_test():
    eng = 0
    noneng = 0
    for i in main.books:
        if i["Language"] == 'en': eng += 1
        else : noneng += 1
    print(eng, '+', noneng,'=', eng+noneng)


a = random.choice(main.books)
print(a)
print(f"Book name : {a['Title']}")
print(f"Issue Date : {a['Issued']}")
print(f"Author's name : {a['Authors']}")
print(f"Subjects : {a['Subjects']}")