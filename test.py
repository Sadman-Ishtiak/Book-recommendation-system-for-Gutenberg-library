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

for i in range(10):
    a = random.choice(main.books)
    print((a["Authors"]))