import os
from ect.globals import PATH

def list_readers():
    with open(PATH / "readers.txt", "r", encoding="utf-8") as file:
        for i,line in enumerate(file.readlines(),1):
            line.replace("\n","")
            user = dict()
            user["name"], user["gender"], user["age"], user["favorite"] = line.split(",")
            user["index"] = i
            yield user

def overide_reader(file,name:str,new_line:str):
    try:
        with open(PATH / file, "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for index,line in enumerate(lines,1):
                print(index,line)
                if line.split(",")[0] == name or index==name:
                    if index==len(lines):
                        new_line= new_line.replace("\n","")
                    file.write(new_line)
                    new_line = -1
                else:
                    if (index+1==len(lines) and new_line=="") or index==len(lines): # remove the last \n if we remove the last user
                        print("yes sir")
                        line = line.replace("\n","")
                    file.write(line)
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
    