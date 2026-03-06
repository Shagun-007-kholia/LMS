from models.book import Book
from File_handler import *

library ={} #library named dictionary with some entries
load_books_from_file(library)

def add_book():
    book_id = int(input("Enter Book ID : "))

    if book_id in library:
        print("Book Already Exists!")
        return

    title = input("Enter Title : ")
    author = input("Enter Author : ")

    library[book_id] = Book(book_id,title,author)

    save_books_to_file(library)   # 🔥

    print("Book Added Successfully")

def view_all_books():
    if not library:
        print("Library is Empty")
        return
    
    print("\n==========Library_Books==========")
    
    for book in library.values(): # here we have used values() method of dictionary which will return a collection of all of the values(i.e objects in our case) of Library dictionary.Library = {1 : obj1, 2 : obj2,...},we have 3 main methods of dictionary obj_dict.keys(),.values() and .items()
        book.show_details()

def issue_book():
    book_id = int(input("Enter Book ID to issue: "))

    if book_id in library:
        library[book_id].issue_book()
        save_books_to_file(library)   # 🔥
    else:
        print("Book not found!")

def return_book():
    book_id = int(input("Enter Book ID to return: "))

    if book_id in library:
        library[book_id].return_book()
        save_books_to_file(library)   # 🔥
    else:
        print("Book ID not found.")