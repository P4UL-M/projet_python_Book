from ect.globals import PATH

def list_readers():
    try:
        with open(PATH / "readers.txt", "r", encoding="utf-8") as file:
            line = file.readline().replace("\n","")
            while line:
                user = dict()
                user["name"], user["gender"], user["age"], user["favorite"] = line.split(",")
                yield user
                line = file.readline().replace("\n","")
    except Exception as e:
        print("Exeception occured while trying to read data :",e)

def overide_reader(name:str,new_line:str):
    try:
        with open(PATH / "readers.txt", "r+", encoding="utf-8") as file:
            lines = file.readlines() # this is not memory efficient but otherwise we need some libraries
            file.seek(0)
            for index,line in enumerate(lines,1):
                if line.split(",")[0] == name:
                    if index==len(lines):
                        new_line= new_line.replace("\n","")
                    print("new",new_line)
                    file.write(new_line)
                else:
                    print("old",line.replace("\n",""))
                    if index+1==len(lines) and new_line=="": # remove the last \n if we remove the last user
                        line = line.replace("\n","")
                    file.write(line)
            file.truncate() # remove all data that wasn't overide
    except Exception as e:
        print("Exeception occured while trying to write data :",e)