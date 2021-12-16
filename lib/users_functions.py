from os import read
from ect.handle_data import *
from lib.books_functions import books, get_book, get_global_rating, get_note

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                   users functions                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def readers():
    return list_readers()

def get_reader(name:str):
    for user in list_readers():
        if type(name)==str:
            if user["name"].upper() == name.upper():
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
    new_line = f"{name},{gender},{age},{favorite}\n"
    try:
        if not get_reader(name):
            append_line("readers.txt",new_line)
            append_line("booksread.txt",name + ",\n")
            nb = len([i for i in books()])
            append_line("notes.txt","0"*nb + "\n")
        else:
            raise Exception("User already exist or your name was already use")
    except FileNotFoundError:
        raise Exception("FATAL ERROR WHILE TYING TO ADD A READER PLEAZE CHECK YOUR SAVE FILE")

def read_book(user_name,book_name):
    temp = list()
    for book_read_index,book_read_name in get_readings(user_name).items():
        if book_read_name == book_name:
            raise Exception("Book already read")
        else:
            temp.append(str(book_read_index))
    else:
        temp.append(str(get_book(book_name)["index"]))
        new_line = f"{user_name}," + ",".join(temp) + "\n"
        overide_line("booksread.txt",user_name,new_line)

def unread_book(user_name,book_name):
    temp = list()
    for book_read_index,book_read_name in get_readings(user_name).items():
        if book_read_name != book_name:
            temp.append(str(book_read_index))
    else:
        new_line = f"{user_name}," + ",".join(temp) + "\n"
        overide_line("booksread.txt",user_name,new_line)

def generate_matrix():
    l_readers = [i for i in readers()]
    matrix = [[0 for i in l_readers] for i in l_readers]
    for reader in readers():
        for target in readers():
            a = list()
            b = list()
            for book in books():
                a.append(int(get_note(reader,book)))
                b.append(int(get_note(target,book)))

            s1 = sum([ai*bi for ai,bi in zip(a,b)])
            s2 = sum([i**2 for i in a])**(1/2)
            s3 = sum([i**2 for i in b])**(1/2)
            matrix[reader["index"]-1][target["index"]-1] = s1/(s2*s3) if s1!=0 and s2!=0 else 0
    return matrix

def recommand_books(user):
    similar_ratio = {}
    
    for i,ratio in enumerate(generate_matrix()[user["index"]-1]):
        if ratio>0 and get_reader(i+1)!=user:
            similar_ratio[get_reader(i+1)["name"]] = ratio
    
    list_recommandation = list()
    similar_ratio = dict(sorted(similar_ratio.items(), key=lambda item: -item[1])) # trie par odre de ressemblance décroissant
    for reader_name,ratio in similar_ratio.items():
        if ratio>0.35: # seulement si le use le ressemble au moins un minimum, 0.35 pour qu'il y est un minimum d'utilisateur ressemblant, comme il sont trier par ordre décroissant ceux à 0.40 par exemple ne seront affiché seulement si il n'y a vraiment aucun utilisateur plus ressemblant, en dessous de 0.35 la similarité est trop éloignée
            l = set(get_readings(reader_name)) - set(get_readings(user["name"]))
            for i in l:
                if int(get_note(get_reader(reader_name),get_book(int(i))))>2 and get_book(int(i)) not in list_recommandation: # si l'utilisateur qui nous ressemble n'a pas aimer le livre alors on est probable de pas l'aimer il ne faut donc pas l'afficher
                    list_recommandation.append(get_book(int(i)))
    else: #si la liste est pas assez complète on ajoute les livres qu'il a pas lu de son style préférer et en fonction des notes globale
        tmp = {}
        if len(list_recommandation)<10:
            for book in books():
                if len(list_recommandation)<10 and str(book["index"]) not in get_readings(user["name"]):
                    # 2 is the lesser average of a book note so we add 2 if there is no global rating and 2 if the user like the style of the book, like this a if we like fantasy a fantasy book of 3.1 is better than a normal book of 5 and an unnoted book will be either a 4 or a 2 if it has the good or not style.
                    tmp[book["name"]] = [(get_global_rating(book["name"]) or 2) + (2.5 if book["style"]==user["favorite"] else 0),book]

        tmp = dict(sorted(tmp.items(), key=lambda item: -item[1][0]))
        for elt in tmp.values():
            if len(list_recommandation)<10 and elt[1] not in list_recommandation:
                list_recommandation.append(elt[1])
    return list_recommandation