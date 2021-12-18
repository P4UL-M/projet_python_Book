from functions.others_functions import *
from functions.books_function import *
from functions.user_function import *
import os

directory = os.path.dirname(os.path.realpath(__file__))
verif_is_file("readers.txt")
verif_is_file("books.txt")
verif_is_file("booksread.txt")
if not verif_is_file("notes.txt"):
    init_notes()

matrix=compute_matrix()

running=True

while running:
    command=input("Enter a command : ").lower()
    if command=="help":
        print("""Everythings that follow a 'Input' in the descriptions bellow will be asked in the command prompt. 
Here is the list of all commands :
    - add a reader       : Inrecoput : Name, gender, age and reading style   | Output : A new client will be signed in
    - remove a reader    : Input : Name                                  | Output : The client is removed from the database
    - view a reader      : Input : Name                                  | Output : The description of the reader
    - edit a reader      : Input : Name, new attributes                  | Output : The user will be modify with the new attributes
    - display books      : Input :                                       | Output : All books with their coresponding numbers
    - add a book         : Input : Book's name                           | Output : A new book will be registered
    - edit a book        : Input : number of the book, new name          | Output : The book's name will be modify
    - delete a book      : Input :                                       | Output : The book is deleted from the database
    - rate a book        : Input : Book's title, note                    | Output : The rate is added to the matrix of all notes
    - read a book        : Input : name, book number                     | Output : The book is linked to the user in the database
    - unread a book      : Input : name, book number                     | Output : Unliked the book from the user
    - recommand a book
    """)
    elif command=="add a reader": add_reader()
    elif command=="remove a reader":
        remove_client()
        matrix=compute_matrix()
    elif command=="view a reader": view_a_reader()
    elif command=="edit a reader": edit_reader()
    elif command=="display books": display_books() 
    elif command=="add a book":add_book()
    elif command=="edit a book":edit_book()
    elif command=="delete a book":
        remove_books()
        matrix=compute_matrix()
    elif command=="rate a book": 
        rate_a_book()
        matrix=compute_matrix()
    elif command=="read a book": read_book_input()
    elif command=="unread a book": 
        unread_book()
        matrix=compute_matrix()
    elif command=="recommand a book": recommand_book(matrix)
    else: print("command not found, try again and use the 'help' command")