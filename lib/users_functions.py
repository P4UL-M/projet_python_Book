from ect.handle_data import *
from lib.books_functions import books, get_book, get_global_rating, get_note
from ect.globals import Matrix

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                   users functions                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def readers():
    """
    this function return a generator with all user store in a dictionary
    """
    return list_readers()

def get_reader(name:str):
    """
    this function return the dictionary of a user by its name
    """
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
    """
    this function return the readings of a user store in dictionaries
    """
    for user in list_readings():
        if user["name"].upper()==name.upper():
            return user["readings"]

def update_reader(old_name,**kargs):
    """
    this function allow to update a parameter of a user
    user args are : name,gender, age, favorite
    """
    try:
        test = False
        if "name" in kargs.keys():
            test = get_reader(kargs["name"]) and kargs["name"]!=old_name
        user = get_reader(old_name)
        if not user or test:
            raise UserWarning
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
        print("File not found while trying to update a user")

def remove_reader(name):
    """
    this function remove a user by his name
    """
    user = get_reader(name)
    if user:
        overide_line("readers.txt",name,"")
        overide_line("booksread.txt",name,"")
        overide_line("notes.txt",user["index"],"")
        generate_matrix()
    else:
        print("user not found")

def add_reader(name,gender,age,favorite):
    """
    this function allow add a reader
    you must specify name,gender,age,favorite
    """
    new_line = f"{name},{gender},{age},{favorite}\n"
    try:
        if not get_reader(name):
            append_line("readers.txt",new_line)
            append_line("booksread.txt",name + ",\n")
            nb = len([i for i in books()])
            l = ["0"]*nb
            append_line("notes.txt"," ".join(l) + "\n")
            generate_matrix()
        else:
            raise UserWarning
    except FileNotFoundError:
        raise Exception("FATAL ERROR WHILE TYING TO ADD A READER PLEAZE CHECK YOUR SAVE FILE")

def read_book(user_name,book_name):
    """
    this function allow to read a book by the user name and the book name
    """
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
    """
    this function allow to un-read a book by the user name and the book name
    """
    temp = list()
    for book_read_index,book_read_name in get_readings(user_name).items():
        if book_read_name != book_name:
            temp.append(str(book_read_index))
    else:
        new_line = f"{user_name}," + ",".join(temp) + "\n"
        overide_line("booksread.txt",user_name,new_line)

def recommand_books(user):
    """
    this function return book recommanded for a user
    """
    similar_ratio = {}
    
    for i,ratio in enumerate(Matrix[user["index"]-1]):
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
                if len(list_recommandation)<10 and str(book["index"]) not in get_readings(user["name"]) and book not in list_recommandation:
                    # 2 is the lesser average of a book note so we add 2 if there is no global rating and 2 if the user like the style of the book, like this a if we like fantasy a fantasy book of 3.1 is better than a normal book of 5 and an unnoted book will be either a 4 or a 2 if it has the good or not style.
                    weight = (get_global_rating(book["name"]) or 2) + (2.5 if book["style"]==user["favorite"] else 0)
                    tmp[book["name"]] = weight
        tmp = dict(sorted(tmp.items(), key=lambda item: -item[1])) # we sort them by their weight
        for book_name in tmp.keys(): # and add them to the end of the recommandation list if there are not in it already
            if len(list_recommandation)<10 and get_book(book_name) not in list_recommandation:
                list_recommandation.append(get_book(book_name))
    return list_recommandation