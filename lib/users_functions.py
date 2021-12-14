from ect.handle_data import *
from lib.books_functions import get_book

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                   users functions                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def readers():
    return list_readers()

def get_reader(name):
    for user in list_readers():
        if type(name)==str:
            if user["name"] == name:
                return user
        elif type(name)==int:
            if user["index"] == name:
                return user
        else:
            raise Exception("bad argument for get reader")

def get_readings(name):
    for user in list_readings():
        if user["name"]==name:
            return user["readings"]

def update_reader(old_name,**kargs):
    """
    user args are : name,gender, age, favorite
    """
    try:
        test = True
        if "name" in kargs.keys():
            test = get_reader(kargs["name"])
        user = get_reader(old_name)
        if not user and test:
            raise Exception("user not found or new name already taken")
        for key,value in kargs.items():
            if key in user.keys():
                user[key] = str(value)
        user.pop("index")
        new_line = ",".join(user.values()) + "\n"
        overide_line("readers.txt",old_name,new_line)
        temp = get_readings(old_name)
        new_line = user["name"] + "," + ",".join(temp) + ("," if len(temp) > 0 else "") + "\n"
        overide_line("booksread.txt",old_name,new_line)

    except FileNotFoundError:
        # do some shit to say to the user that the file doen't seems to exist
        print("File not found while trying to update a user")

def remove_reader(name):
    user = get_reader(name)
    if user:
        overide_line("readers.txt",name,"")
        overide_line("booksread.txt",name,"")
        overide_line("notes.txt",user["index"],"")
    else:
        print("user not found")

def add_reader(name,gender,age,favorite):
    """
    you must specify name,gender,age,favorite
    """
    new_line = f"{name},{gender},{age},{favorite}"
    try:
        if not get_reader(name):
            append_line("readers.txt",new_line)
            append_line("booksread.txt",name)
            append_line("notes.txt","0"*21)
        else:
            raise Exception("User already exist or your name was already use")
    except FileNotFoundError:
        # do some shit with tkinder to confirm creation of the file
        append_line("readers.txt",new_line)
        append_line("booksread.txt",name + ",") # this file doesn't interfere with the order so we can write in it even if it already exist
        append_line("notes.txt","0"*21) # this file interfere so fuuuuuuuuucccckkkkkk i guess

def read_book(user_name,book_name):
    temp = list()
    for book_read_index,book_read_name in get_readings(user_name).items():
        if book_read_name == book_name:
            raise Exception("Book already read")
        else:
            temp.append(str(book_read_index))
    else:
        temp.append(str(get_book(book_name)["index"]))
        new_line = f"{user_name}," + ",".join(temp) + ",\n"
        overide_line("booksread.txt",user_name,new_line)

def unread_book(user_name,book_name):
    temp = list()
    for book_read_index,book_read_name in get_readings(user_name).items():
        if book_read_name != book_name:
            temp.append(str(book_read_index))
    else:
        new_line = f"{user_name}," + ",".join(temp) + ",\n"
        overide_line("booksread.txt",user_name,new_line)

