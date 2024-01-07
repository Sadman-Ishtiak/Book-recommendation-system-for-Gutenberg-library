# Book-recommendation-system-for-Gutenberg-library
"The book recommendation system for Gutenburg library" is a project for extreme level readers who has reached to a point that it is no longer quick and easy for an user to look through the book catalog of Gutenburg Library but still want to read the public domain books that are readily available in Gutenburg.


## Introduction
This project is created as a Uni project by [Sadman Ishtiak](https://github.com/Sadman-Ishtiak) and [Jahid Hasan Khan Ornob](https://github.com/ornobkhan20). The target of the project is to get book choice when the user has read a substantioal number of books from [Gutenburg Library](https://gutenberg.org/). And the user wants to read more from the library but doesn't want to go through the book catalog as the user can only get the catalog as the most downloaded list. But that list consists of books that most bookworms have already read and it is truly a shame that from over 50,000 books in different formats with over 78,000 versions and we can only get like 50-ish books that most readers have already read. So if you already have read a lot of books and want to read more from these public domain books or if you are interested in these classics and want to read more books of the simmilar era. You can easily get help from this project to get some choice of books that you probably never heard before.


## Features
1. Search book by title
2. Search book by author name
3. Contains a wishlist that you haven't read yet but want to read
4. Contains a readlist for book that you have completed
5. Get Random recommendation.
6. Get Category Recommendation


## Installation
To get an use of this project you may need to do some task beforehand for your device. This project is tested and created in Windows 11. And due to constraints we can only give you a guide for windows 11. 

So first you need to have python installed. you can download python 3.10 or above and install python in your device from [Python website](https://www.python.org/downloads) . 

Next step is to install all the requirements for this. please use the code in your terminal to install all the required libraries using pip.
```
pip install customtkinter
```
we have only used one external library (module) here so you can directly use this from this moment foreward


## User Documentation
We have two kinds of interfaces. one is Command Line Interface. and another is a Graphical User Interface. If you do not need the graphical user interface you can even not install the customtkinter module.

### Command Line Interface guide
Will be available soon
### Graphical User Interface guide
Will be available soon
## Current Issues
1. We used linear search to write the code faster as we still are learning. It is slow.
2. Customtkinter is slow. It is used only because it is much easier to implement than other.
3. Currently The Graphical User Interface is not working as it is still in the developement stage.
4. In the CLI there are no arguments used. So, Quick arguments to get the work done is not possible
5. The user may frequently need to use (**CTRL+Z**) to escape from the command loop to exit. The command line interface is not well made with different scenarios in mind.