import os
from path import PATH

def ask_input(display_string:str, minimum:int, maximum:int):
    """will ask the user to input using display_string
    until the input can be converted in int and is compromised between minimum and maximum"""
    string_wrong_input="Wrong input, please try again."
    input_=""
    while True:
        if input_ !="":
            print(string_wrong_input)
        input_=input(display_string)
        try:
            input_=int(input_)
        except:
            continue
        if minimum <= input_ <= maximum:
            break
    print()
    return input_

def get_reading_style(number:int):
    """return the reading style corresponding to its number in readers.txt"""
    if number=="1": return "sci-fi"
    elif number=="2": return "Biography"
    elif number=="3": return "Horror"
    elif number=="4": return "Romance"
    elif number=="5": return "Fable"
    elif number=="6": return "History"
    elif number=="7": return "Comedy" 

def verif_is_file(file_name:str):
    """return True if the file exist else create the an empty file <file_name>.txt"""
    if not os.path.isfile(PATH/file_name):
        print("no {file_name}.txt found, a new one has been created")
        # create a new readers.txt file
        with open(PATH/file_name, "w") as f:
            pass
    else:
        return True
    
def init_notes():
    """initialize the file notes.txt with only 0 considering the number of books and the number of users"""
    with open(PATH/"notes.txt", "w") as notes_write:
        all_lines_books=get_all_lines("books.txt") ; all_lines_readers=get_all_lines("readers.txt") ;
        for _ in range(len(all_lines_readers)):
            a="0 "*len(all_lines_books) 
            # we remove the last space because we don't want our line to finish with a space
            notes_write.write(a[:-1])
            notes_write.write("\n")
    
def get_all_lines(name_file:str):
    """return a list containing all the lines of a file"""
    with open(PATH/name_file, "r", encoding="utf-8") as f:
        all_files=f.readlines()
        return all_files
    
def get_name(number_line:int, filename:str):
    """return the first element of a file by spliting it by ,
    So it will return the name of the user of the <number_line> line in readers.txt or booksread.txt"""
    return get_all_lines(filename)[number_line].replace("\n", "").split(",")[0]

def re_write_file(file_name, new_str, mode="w"):
    """overwrite the file <file_name> with <new_str> if mode is w else
    add new_str + \n at the end of the file <file_name>"""
    with open(PATH/file_name, mode, encoding="utf-8") as f:
        f.write(new_str)
        if mode=="a":
            f.write("\n")
            
def re_write_line(file_name:str, new_line:str, number_line:int):
    """overwrite only one line of the file <new_file>"""
    all_lines=get_all_lines(file_name)
    re_write_file(file_name, "".join(all_lines[:number_line])+new_line+"".join(all_lines[number_line+1:]))
        
def get_number_line(file_name:str, id:str):
    """return the number of line of the <id> (first element in the line => name of reader in readers.txt and booksread.txt) 
    from the file <file_name>"""
    with open(PATH/file_name, "r", encoding="utf-8") as f:
        number=-1
        for number_of_line, line in enumerate(f.readlines()):
            if line.replace("\n","").split(",")[0].lower()==id:
                number=number_of_line
    return number

def is_registered(file_name:str, name:str):
    """return True if <name> is the first element of a line in <file_name>
    else return False"""
    all_lines=get_all_lines(file_name)
    if file_name!="books.txt":
        if name not in [line.replace("\n", "").split(",")[0].lower() for line in all_lines]:
            return False
    # books.txt is only composed of the name of the books so we don't need to do a .split()
    elif name not in [e.replace("\n", "").lower() for e in all_lines]:    
        return False
    return True