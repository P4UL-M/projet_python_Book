from lib.others_functions import get_reading_style_with_number, ask_input
from ect.globals import PATH
from ect.handle_data import *

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                   users functions                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#region rewrited
def add_client():
    name=input("What is your name ? ")
    
    with open(PATH / "readers.txt", "r", encoding="utf-8") as readers:
        if name not in [line.split(", ")[0] for line in readers.readlines()]:
            gender=ask_input("Enter '1' if you are a male, '2' if you are a female and '3' if you don't want to tell : ", int, 1, 3)
                
            age=ask_input("How old are you ? ", int, 0, 125)
            new_age=0
            if age <18:new_age=1
            elif age <=25:new_age=2
            else:new_age=3
            
            string_reading_style="""Enter the number corresponding to your prefered reading style \n1. sci-fi \n2. Biography \n3. Horror \n4. Romance \n5. Fable \n6. History \n7. Comedy\n"""    
            reading_style=ask_input(string_reading_style, int, 1, 7)
            
            with open(PATH / "readers.txt", "a", encoding="utf-8") as readers_write:
                readers_write.write(f"{name}, {gender}, {new_age}, {reading_style}\n")
            with open(PATH / "booksread.txt", "a", encoding="utf-8") as readers_write:
                readers_write.write(f"{name}, \n")
        else:
            print("user already registered")
    return name
      
def remove_client():
    name=input("What is the name of the client you want to remove ? ")
    
    with open(PATH / "readers.txt", "r", encoding="utf-8") as readers, open( PATH / "booksread.txt", "r") as booksread, open(PATH / "notes.txt", "r") as notes:
        all_lines_readers=readers.readlines()
        if name in [line.split(", ")[0] for line in all_lines_readers]:
            final_readers=""
            final_booksread=""
            final_notes=""
            number_client=-1
            
            for number_of_line, line in enumerate(all_lines_readers):
                if line.split(", ")[0]!=name:
                    final_readers+=line
                else:
                    number_client=number_of_line+1
            
            print(number_client)
            for number_of_line, line in enumerate(notes.readlines()):
                print(number_of_line)
                if number_of_line+1 != number_client:
                    print("sdg")
                    final_notes+=line
                    
            for number_of_line, line in enumerate(booksread.readlines()):
                if number_of_line+1 != number_client:
                    final_booksread+=line
                    
            with open(PATH / "readers.txt", "w", encoding="utf-8") as readers_write:
                readers_write.write(final_readers)
            with open(PATH / "notes.txt", "w", encoding="utf-8") as notes_write:
                notes_write.write(final_notes)
            with open(PATH / "booksread.txt", "w", encoding="utf-8") as booksread_write:
                booksread_write.write(final_booksread)
        else:
            print("user not registered")
                  
def View_a_reader():
    name=input("What is your name ? ")
    
    with open(PATH / "readers.txt", "r", encoding="utf-8") as readers:
        all_lines=readers.readlines()
        if name in [line.split(", ")[0] for line in all_lines]:
            for line in all_lines:
                sep_line=line.split(", ")
                if sep_line[0]==name: 
                    print("Name :", name)
                    if sep_line[1] == "1": print("Gender : Male")
                    elif sep_line[1] == "2": print("Gender : Female")
                    else: print("Gender : Unknow")
                    if sep_line[2]=="1": print("Age : Between 0 and 17")
                    elif sep_line[2]=="2": print("Age : Between 18 and 25")
                    else: print("Age : Above 25")
                    print("Favorite reading style :",get_reading_style_with_number(sep_line[3][:-1]))
            
        else:
            print("user not registered")
            
def update_client():
    original_name=input("What is the name of the client ? ")
    
    with open(PATH / "readers.txt", "r", encoding="utf-8") as readers:
        all_lines=readers.readlines()
        liste_names=[line.split(", ")[0] for line in all_lines]
        if original_name in liste_names:
            for line in all_lines:
                if line.split(", ")[0]==original_name:
                    name, gender, age, reading_style=line.split(", ")
                    
            choice_string="What do you want to modify ? \n1. name \n2. gender \n3. age \n4. reading_style \n5. end and return to the menu\n"
            choice = ask_input(choice_string, int, 1, 5)
            while choice != 5:
                if choice == 1:
                    name=input("What is your name ? ")
                elif choice == 2:
                    gender=ask_input("Enter '1' if you are a male, '2' if you are a female and '3' if you don't want to tell.", int, 1, 3)
                elif choice == 3: 
                    age=ask_input("How old are you ? ", int, 0, 125)
                elif choice == 4: 
                    string_reading_style="""Enter the number corresponding to your prefered reading style \n1. sci-fi \n2. Biography \n3. Horror \n4. Romance \n5. Fable \n6. History \n7. Comedy\n"""    
                    reading_style=ask_input(string_reading_style, int, 1, 7)
                choice = ask_input(choice_string, int, 1, 5)
            
            final_readers=""    
            for line in all_lines:
                if line.split(", ")[0]!=original_name:
                    final_readers+= line
                else:
                    final_readers+=f"{name}, {gender}, {age}, {reading_style}"
            with open(PATH / "readers.txt", "w", encoding="utf-8") as readers_write:
                readers_write.write(final_readers)
                
            if name != original_name:
                with open(PATH / "booksread.txt", "r", encoding="utf-8") as booksread:
                    final_booksread=""    
                    all_lines_booksread=booksread.readlines()
                    for line in all_lines_booksread:
                        if line.split(", ")[0]!=original_name:
                            final_booksread+=line
                        else:
                            # we remove the \n
                            rest_of_line=", ".join(line.split(", ")[1:])[:-1]
                            final_booksread=final_booksread+name + rest_of_line + ", " + "\n"
                    with open(PATH / "booksread.txt", "w", encoding="utf-8") as booksread_write:
                        booksread_write.write(final_booksread)
        else:
            print("user not found")
#endregion

def get_reader(name):
    for user in list_readers():
        if user["name"] == name:
            return user

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
        new_line = ",".join(user.values()) + "\n"
        overide_reader("readers.txt",old_name,new_line)
    except FileNotFoundError:
        # do some shit to say to the user that the file doen't seems to exist
        print("File not found while trying to update a user")

def remove_reader(name):
    user = get_reader(name)
    overide_reader("readers.txt",name,"")
    overide_reader("booksread.txt",name,"")
    overide_reader("booksread.txt",str(user["index"]),"")

def add_reader(name,gender,age,favorite):
    """
    you must specify name,gender,age,favorite
    """
    new_line = f"{name},{gender},{age},{favorite}"
    try:
        if not get_reader(name):
            append_reader("readers.txt",new_line)
            append_reader("booksread.txt",name)
            append_reader("notes.txt","0"*21)
        else:
            raise Exception("User already exist or your name was already use")
    except FileNotFoundError:
        # do some shit with tkinder to confirm creation of the file
        append_reader("readers.txt",new_line)
        append_reader("booksread.txt",name + ",") # this file doesn't interfere with the order so we can write in it even if it already exist
        append_reader("notes.txt","0"*21) # this file interfere so fuuuuuuuuucccckkkkkk i guess
