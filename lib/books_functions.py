from ect.handle_data import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                 books functions                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def books():
    return list_books()

def get_book(name):
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
    you must specify name,gender,age,favorite
    """
    new_line = f"{name},,{style}\n"
    try:
        if not get_book(name):
            append_line("books.txt",name + "\n")
            append_line("books_extended.txt",new_line)
            append_column("notes.txt",0)
        else:
            raise Exception("Book already exist or your name was already use")
    except FileNotFoundError:
        # do some shit with tkinder to confirm creation of the file
        append_line("readers.txt",new_line)
        append_line("booksread.txt",name + ",") # this file doesn't interfere with the order so we can write in it even if it already exist
        append_column("notes.txt","0") # this file interfere so fuuuuuuuuucccckkkkkk i guess

def update_book(old_name,**kargs):
    """
    user args are : name,gender, age, favorite
    """
    try:
        test = True
        if "name" in kargs.keys():
            test = get_book(kargs["name"])
        book = get_book(old_name)
        if not book and test:
            raise Exception("book not found or new name already taken")
        for key,value in kargs.items():
            if key in book.keys():
                book[key] = str(value)
        book.pop("index")
        new_line = ",,".join(book.values()) + "\n"
        overide_line("books_extended.txt",old_name,new_line)
        overide_line("books.txt",old_name,kargs["name"] + "\n")
    except FileNotFoundError:
        # do some shit to say to the user that the file doen't seems to exist
        print("File not found while trying to update a user")

def remove_book(name):
    book = get_book(name)
    overide_line("books_extended.txt",name,"")
    overide_line("books.txt",name,"")
    overide_column("notes.txt",str(book["index"]),None)
    delete_reading("booksread.txt",book)
    # make overide collumn à la place

def get_note(user,book):
    return get_note_in_file(user,book)

def note_book(book:dict,user:dict,note):
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
    temp = []
    for user in list_readers():
        val = int(get_note(user,get_book(name)))
        if val != 0:
            temp.append(val)
    return None if len(temp)==0 else round(sum(temp)/len(temp),2)