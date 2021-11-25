from ect.globals import PATH

def list_readers():
    with open(PATH / "readers.txt", "r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            line.replace("\n","")
            user = dict()
            user["name"], user["gender"], user["age"], user["favorite"] = line.split(",")
            user["index"] = i
            yield user

def overide_line(file,name:str,new_line:str):
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for index,line in enumerate(lines,1):
                if line.split(",")[0].replace("\n","") == name or str(index)==name:
                    if index==len(lines):
                        new_line= new_line.replace("\n","")
                    file.write(new_line)
                    new_line = -1
                else:
                    if (index+1==len(lines) and new_line=="") or index==len(lines): # remove the last \n if we remove the last user
                        line = line.replace("\n","")
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
                    new_line = list(line)
                    new_line[int(index)-1] = str(new_value)
                    new_line = "".join(new_line)
                    file.write(new_line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Error while trying to write data :",e)

def append_reader(file,new_line:str):
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            if file.readlines():
                file.write("\n")
            file.write(new_line)
    except FileNotFoundError:
        open(PATH / file,"a")
        append_reader(file,new_line)

def list_books():
    with open(PATH / "books.txt","r", encoding="utf-8") as file, open(PATH / "books_extended.txt","r", encoding="utf-8") as file_extended:
        a,b = file.readlines(),file_extended.readlines() # put the object directly in the zip don't work but i don't know why
        for i,line in enumerate(zip(a,b),1):
            line,line_extended  = line[0].replace("\n",""),line[1].replace("\n","").split(",")[1]
            book = dict()
            book["name"], book["style"] = (line,line_extended)
            book["index"] = i
            yield book

def get_note(user,book):
    with open(PATH / "notes.txt","r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            if i == user["index"]:
                data = list(line.replace("\n",""))
                return data[book["index"]-1]
