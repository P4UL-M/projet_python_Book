from ect.handle_data import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                   users functions                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def get_reader(name):
    for user in list_readers():
        if user["name"] == name:
            return user

def get_readings(name):
    for user in list_readings():
        if user["name"] ==name:
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
    except FileNotFoundError:
        # do some shit to say to the user that the file doen't seems to exist
        print("File not found while trying to update a user")

def remove_reader(name):
    user = get_reader(name)
    overide_line("readers.txt",name,"")
    overide_line("booksread.txt",name,"")
    overide_line("notes.txt",str(user["index"]),"")

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
    for book_read_index,book_read_name in get_readings(user_name):
        if book_read_name == book_name:
            raise Exception("Book already read")
        else:
            temp.append(book_read_index)
    #inprogress

def unread_book():
    pass
