import os
from ect.globals import PATH

def ask_input(display_string, type, minimum, maximum):
    string_wrong_input="Wrong input, please try again."
    finish=False
    input_=""
    while not finish:
        if input_ !="":
            print(string_wrong_input)
        input_=input(display_string)
        try:
            input_=type(input_)
        except:
            continue
        if minimum <= input_ <= maximum:
            finish=True
    print()
    return input_

def get_reading_style_with_number(number):
    if number=="1": return "sci-fi"
    elif number=="2": return "Biography"
    elif number=="3": return "Horror"
    elif number=="4": return "Romance"
    elif number=="5": return "Fable"
    elif number=="6": return "History"
    elif number=="7": return "Comedy" 

def verif_is_file(file_name):
    if not os.path.isfile(PATH/file_name):
        print("no {file_name}.txt found, a new one has been created")
        # create a new readers.txt file
        with open(PATH/file_name, "w") as f:
            pass

def re_write_book(name_file, new_str, mode="w"):
    with open(PATH/name_file, mode, encoding="utf-8") as f:
        f.write(new_str)
        if mode=="a":
            f.write("\n")
            
def get_all_lines(name_file):
    with open(PATH/name_file, "r", encoding="utf-8") as f:
        all_files=f.readlines()
        return all_files
        
def get_number_line(name_file, id):
    with open(PATH/name_file, "r", encoding="utf-8") as f:
        number=-1
        for number_of_line, line in enumerate(f.readlines()):
            if line.split(", ")[0]==id:
                number=number_of_line
    return number

def init_notes():
    with open(PATH/"notes.txt", "w") as notes_write:
        all_lines_books=get_all_lines("books.txt");all_lines_readers=get_all_lines("readers.txt");
        for _ in range(len(all_lines_readers)):
            notes_write.write("0"*(len(all_lines_books)))
            notes_write.write("\n")

def verif_is_not_registered(file_name, name):
    all_lines_reader=get_all_lines(file_name)
    if name not in [line.split(", ")[0] for line in all_lines_reader]:
        return True
    else:
        return False