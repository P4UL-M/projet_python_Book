from ect.handle_data import *
from lib.books_functions import books, get_book, get_super_notes

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

def recommand_books(user):
    similar_ratio = {}
    for reader in readers():
        if reader!= user:
            a = list()
            b = list()
            for book in books():
                a.append(int(get_super_notes(user,book)))
                b.append(int(get_super_notes(reader,book)))

            s1 = sum([ai*bi for ai,bi in zip(a,b)])
            s2 = sum([i**2 for i in a])**(1/2)
            s3 = sum([i**2 for i in b])**(1/2)
            if s1!=0 and s2!=0:
                similar_ratio[reader["name"]] = s1/(s2*s3)
    
    list_recommandation = list()
    similar_ratio = dict(sorted(similar_ratio.items(), key=lambda item: item[1])) # trie par odre de ressemblance
    for reader_name,ratio in similar_ratio.items():
        if ratio>0.35: # seulement si le use le ressemble au moins un minimum
            l = set(get_readings(reader_name)) - set(get_readings(user["name"]))
            for i in l:
                list_recommandation.append(get_book(int(i)))
    else: #si la liste est pas assez complète on ajoute les livres qu'il a pas lu de son style préférer
        if len(list_recommandation)<10:
            for book in books():
                if len(list_recommandation)<10 and book["style"]==user["favorite"] and str(book["index"]) not in get_readings(user["name"]):
                    list_recommandation.append(book)
    
    return list_recommandation
