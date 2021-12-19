from ect.handle_data import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                 books functions                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def books():
    """
    this function return a generator with all book store in a dictionary
    """
    return list_books()

def get_book(name):
    """
    this function return the dictionary of a book by its name or index
    """
    for book in list_books():
        if type(name)==str:
            if book["name"] == name:
                return book
        elif type(name)==int:
            if book["index"] == name:
                return book
        else:
            raise Exception("bad argument for get book")

def add_book(name,style):
    """
    this function allow add a book
    you must specify name,style
    """
    new_line = f"{name},,{style}\n"
    try:
        if not get_book(name):
            append_line("books.txt",name + "\n")
            append_line("books_extended.txt",new_line)
            append_column("notes.txt",0)
        else:
            raise UserWarning
    except FileNotFoundError:
        raise Exception("FATAL ERROR WHILE TYING TO ADD A READER PLEAZE CHECK YOUR SAVE FILE")

def update_book(old_name,**kargs):
    """
    this function allow to update a parameter of a book
    user args are : name,style
    """
    try:
        test = False
        if "name" in kargs.keys():
            test = get_book(kargs["name"]) and kargs["name"]!=old_name
        book = get_book(old_name)
        if not book or test:
            raise UserWarning #this is an exception we choose to say to the app if the book title is already used (cannot create custum exeption without class)
        for key,value in kargs.items():
            if key in book.keys():
                book[key] = str(value)
        index = book["index"]
        book.pop("index")
        new_line = ",,".join(book.values()) + "\n"
        overide_line("books_extended.txt",index,new_line) # cannot use name because of "," detector which is there a ",,", more easy to use index than correct all
        overide_line("books.txt",old_name,kargs["name"] + "\n")
    except FileNotFoundError:
        print("File not found while trying to update a user")

def remove_book(name):
    """
    this function remove a user by his name
    """
    book = get_book(name)
    if book:
        overide_line("books_extended.txt",book["index"],"")
        overide_line("books.txt",book["index"],"")
        overide_column("notes.txt",str(book["index"]),None)
        delete_reading("booksread.txt",book)
    else:
        print("book not found")

def get_note(user,book):
    """
    this function give the note for a user and a book
    """
    return get_value(user,book)

def note_book(book:dict,user:dict,note):
    """
    this function note a book for a user and a book
    """
    try:
        if type(book)!=dict or type(user)!=dict or not book or not user:
            raise Exception("Bad argument, must send book and user")
        if "name" not in book.keys() or "name" not in user.keys():
            raise Exception("Bad argument, must send book and user")
        overide_value("notes.txt",book["index"],user["index"],note)
    except FileNotFoundError:
        # do some shit to say to the user that the file doen't seems to exist
        print("File not found while trying to update a user")

def get_global_rating(name):
    """
    this give the average rating of a book by its name
    """
    temp = []
    for user in list_readers():
        val = int(get_note(user,get_book(name)))
        if val != 0:
            temp.append(val)
    return None if len(temp)==0 else round(sum(temp)/len(temp),2)