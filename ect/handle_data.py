from ect.globals import PATH,Matrix,update_size

"""
this file like the function of the app with the data saved
"""

def list_readers():
    """
    this function return a dictionary of every user in the file
    """
    with open(PATH / "readers.txt", "r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            line = line.replace("\n","")
            user = dict()
            user["name"], user["gender"], user["age"], user["favorite"] = line.split(",")
            user["index"] = i
            yield user

def overide_line(file,name:str,new_line:str):
    """
    this function overide a line in a file with a new file by the name of the first element or its index
    """
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for index,line in enumerate(lines,1):
                if line.split(",")[0].replace("\n","") == name or index==name:
                    file.write(new_line)
                else: # si rien de tout
                    file.write(line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)

def overide_column(file,index:int,new_value:str):
    """
    this overide a column in a matrix by a new value
    """
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for line in lines:
                new_line = line.replace("\n","").split(" ")
                if new_value != None:
                    new_line[int(index)-1] = str(new_value)
                else:
                    del new_line[int(index)-1]
                new_line = " ".join(new_line) + "\n"
                file.write(new_line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)

def overide_value(file,index_book:int,index_user:int,new_value:str):
    """
    this function overide a single value in a matrix
    """
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for i,line in enumerate(lines,1):
                if i==index_user:
                    new_line = line.replace("\n","").split(" ")
                    new_line[int(index_book)-1] = str(new_value)
                    new_line = " ".join(new_line) + "\n"
                    file.write(new_line)
                else:
                    file.write(line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)

def append_line(file,new_line:str):
    """
    this function add a new line at the end of a file
    """
    try:
        with open(PATH / file, "a", encoding="utf-8") as file:
            file.write(new_line)
    except FileNotFoundError:
        print("error while appending value")

def append_column(file,new_value):
    """
    this function add a column to the end of a file, matrix
    """
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for line in lines:
                new_line = " ".join(line.replace("\n","").split(" ") + [str(new_value)]) + "\n"
                file.write(new_line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)

def list_books():
    """
    this function return dictionary for each books saved
    """
    with open(PATH / "books.txt","r", encoding="utf-8") as file, open(PATH / "books_extended.txt","r", encoding="utf-8") as file_extended:
        a,b = file.readlines(),file_extended.readlines() # put the object directly in the zip don't work but i don't know why
        for i,line in enumerate(zip(a,b),1):
            line,line_extended  = line[0].replace("\n",""),line[1].replace("\n","").split(",,")[1]
            book = dict()
            book["name"], book["style"] = (line,line_extended)
            book["index"] = i
            yield book

def get_value(user,book):
    """
    this function return the value of a case in a matrix
    """
    with open(PATH / "notes.txt","r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            if i == user["index"]:
                data = line.replace("\n","").split(" ")
                return data[book["index"]-1]

def list_readings():
    """
    this return all readings of all user
    """
    with open(PATH / "booksread.txt", "r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            line = line.replace("\n","")
            user = dict()
            user["name"] = line.split(",")[0]
            user["readings"] = {elt:"name" for elt in line.split(",")[1:] if elt !=""}
            for book in list_books():
                if str(book["index"]) in user["readings"]:
                    user["readings"][str(book["index"])] = book["name"]
            user["index"] = i
            yield user

def delete_reading(file,book:dict):
    """
    this function search and delete all index of a book in a file
    """
    with open(PATH / file, "r+", encoding="utf-8") as file:
        lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
        file.seek(0)
        for line in lines:
            l = line.replace("\n","").split(",")
            index = 1
            for elt in l[1:]:
                if elt=="":
                    break
                if elt==str(book["index"]):
                    del l[index]
                else:
                    if int(elt)>book["index"]:
                        l[index] = str(int(elt) -1)
                    index += 1
            new_line = ",".join(l) + "\n"
            file.write(new_line)
        file.truncate() # remove all data that wasn't overide

def generate_matrix():
    """
    this function return the matrix of the ratio of similarity between two user
    """
    global Matrix
    l_readers = [i for i in list_readers()]
    update_size(len(l_readers))
    for reader in list_readers():
        for target in list_readers():
            a = list()
            b = list()
            for book in list_books():
                a.append(int(get_value(reader,book)))
                b.append(int(get_value(target,book)))

            s1 = sum([ai*bi for ai,bi in zip(a,b)])
            s2 = sum([i**2 for i in a])**(1/2)
            s3 = sum([i**2 for i in b])**(1/2)
            Matrix[reader["index"]-1][target["index"]-1] = s1/(s2*s3) if s3!=0 and s2!=0 else 0