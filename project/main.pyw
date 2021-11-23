from users_functions import *
from books_functions import *

running=True

# TODO changer nom commande comme dans pres projet

while running:
    command=input("Enter a command : ")
    if command=="help":
        print("""Everythings that follow a 'Input' in the descriptions bellow will be asked in the command prompt. 
            Here is the list of all commands :
            - add client         : Input : Name, gender, age and reading style   | Output : A new client will be signed in
            - add book to client : Input : Client's name, book's title           | Output : Linked the client to the books in the database
            - remove client      : Input : Name                                  | Output : The client profil will be removed from the database
            - edit client        : Input : What you want to edit                 | Output : Edit the profile
            - add book           : Input : Title of the book                     | Output : Add the new book to the database
            - remove book        : Input : Title of the book                     | Output : Remove the book from the database
            - edit book          : Input : Book's old and new tile               | Output : Edit the tile of the book
            - display books      : Input :                                       | Output : Display all book's title and the number associated to it
            - view a reader      : Input : Name of the client                    | Output : Display the client's profile
            - end                : Input :                                       | Output : Close the file
            - note a book        : Input : Client's name, book's name, note      | Output : edit the matrix containing all notes""")
    elif command=="end":
        print("Goodbye !")
        running=False
    elif command=="add client":
        name=add_client()
        add_book_to_client(name=name)
    elif command=='remove client':
        remove_client()
    elif command=="edit client":
        update_client()
    elif command=='add book':
        add_book()
    elif command=="edit book":
        edit_book()
    elif command=="display books":
        display_books()
    elif command=="remove book":
        remove_books()
    elif command=="view a reader":
        View_a_reader()
    elif command=="add book to client":
        add_book_to_client()
    elif command=="note a book":
        note_a_book()
    else:
        print("command not found, please try again or use 'help' command")
    print()

