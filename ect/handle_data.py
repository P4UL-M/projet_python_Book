from ect.globals import PATH

def list_readers():
    with open(PATH / "readers.txt", "r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            line = line.replace("\n","")
            user = dict()
            user["name"], user["gender"], user["age"], user["favorite"] = line.split(",")
            user["index"] = i
            yield user

def overide_value(file,index_book:int,index_user:int,new_value:str):
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

def overide_column(file,index:int,new_value:str):
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for line in lines:
                new_line = line.replace("\n","").split(" ")
                new_line[int(index)-1] = str(new_value)
                new_line = " ".join(new_line) + "\n"
                file.write(new_line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)

def overide_value(file,index_book:int,index_user:int,new_value:str):
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
    try:
        with open(PATH / file, "a", encoding="utf-8") as file:
            file.write(new_line)
    except FileNotFoundError:
        print("error while appending value")

def append_column(file,new_value):
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for line in lines:
                new_line = line.replace("\n","") + str(new_value) + "\n"
                file.write(new_line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)

def list_books():
    with open(PATH / "books.txt","r", encoding="utf-8") as file, open(PATH / "books_extended.txt","r", encoding="utf-8") as file_extended:
        a,b = file.readlines(),file_extended.readlines() # put the object directly in the zip don't work but i don't know why
        for i,line in enumerate(zip(a,b),1):
            line,line_extended  = line[0].replace("\n",""),line[1].replace("\n","").split(",,")[1]
            book = dict()
            book["name"], book["style"] = (line,line_extended)
            book["index"] = i
            yield book

def get_note_in_file(user,book):
    with open(PATH / "notes.txt","r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            if i == user["index"]:
                data = line.replace("\n","").split(" ")
                print(book["index"]-1)
                return data[book["index"]-1]

def list_readings():
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
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for line in lines:
                new_line = line.replace("," + str(book["index"]) + ",",",").replace("," + str(book["index"]),"")
                file.write(new_line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)