import os
from pathlib import Path

PATH = Path("data/").resolve()

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
    if not os.path.isfile(PATH / "{file_name}.txt"):
        print("no {file_name}.txt found, a new one has been created")
        # create a new readers.txt file
        with open(PATH / "{file_name}.txt", "w") as f:
            pass