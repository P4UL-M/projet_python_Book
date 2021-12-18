from path import PATH
from functions.others_functions import *

def add_reader():  
    """add a reader to the database, so to readers.txt, booksread.txt and notes.txt"""
    name=input("Enter your name : ").lower()
    if not is_registered("readers.txt", name):
        gender=ask_input("Enter '1' if you are a male, '2' if you are a female and '3' if you don't want to tell : ", 1, 3)      
        age=ask_input("How old are you ? ", 0, 125)
        new_age=0
        if age <18:new_age=1
        elif age <=25:new_age=2
        else:new_age=3
        string_reading_style="""Enter the number corresponding to your prefered reading style \n1. sci-fi \n2. Biography \n3. Horror \n4. Romance \n5. Fable \n6. History \n7. Comedy\n"""    
        reading_style=ask_input(string_reading_style, 1, 7)
        
        all_lines_books=get_all_lines("books.txt") ;          
        
        temp="0 "*(len(all_lines_books))
        re_write_file("readers.txt", f"{name},{gender},{new_age},{reading_style}", mode="a")
        re_write_file("booksread.txt", f"{name}", mode="a")
        # we remove the last space because we dont want our line to end with a space
        re_write_file("notes.txt", temp[:-1], mode="a")
    else: print("User already registered")
    
def remove_client():
    """remove a client to the database"""
    name=input("enter your name : ").lower()
    if is_registered("readers.txt", name):
        number_client=get_number_line("readers.txt", name)
        # overwrite the lines from the files
        re_write_line("readers.txt", "", number_client)
        re_write_line("notes.txt", "", number_client)
        re_write_line("booksread.txt", "", number_client)         
    else:
        print("user already not registered")

def get_dico_reader(name):
    """return a dictionnarie for the user <name>"""
    if is_registered("readers.txt", name):
        all_lines=get_all_lines("readers.txt")
        number_line=get_number_line("readers.txt", name)
        sep_line=all_lines[number_line].replace("\n", "").split(",")
        dico={
            "name":name,
            "gender":sep_line[1],
            "age":sep_line[2],
            "reading_style":sep_line[3]
        }
        return dico

def view_a_reader():
    """print all the informations about a user"""
    name=input("Enter the name of the reader : ").lower()
    if is_registered("readers.txt", name):
        dico=get_dico_reader(name)
        
        if dico["age"] == "1": age_print="Younger than 19"
        elif dico["age"] == "2": age_print="Between 18 and 25"
        else:age_print="Older than 25"
        gender=dico["gender"]
        reading_style=get_reading_style(dico["reading_style"])
        print(f"Name : {name} | gender : {gender}| age : {age_print} | reading_style : {reading_style}")
    else: print("user not registered")

def edit_reader():
    """edit the informations of a reader in term of what the user want to modify"""
    original_name=input("Enter the name of the client : ").lower()
    if is_registered("readers.txt", original_name):
        all_lines_booksread=get_all_lines("booksread.txt")
        number_line_user=get_number_line("readers.txt", original_name)
        
        dico_client=get_dico_reader(original_name)
        
        choice=-1
        # ask the user what to modify first and then how
        while choice != 0:
            choice=ask_input("What do you want to modify ? 1. name | 2. age | 3. gender | 4. reading style | 0 to stop : ", 0, 4)
            if choice==1: dico_client['name']=input("Enter the new name : ")
            elif choice==2:
                age=ask_input("How old are you ? ", 0, 125)
                if age <18:new_age=1
                elif age <=25:new_age=2
                else:new_age=3
                dico_client["age"]=new_age
            elif choice==3:  dico_client["gender"]=ask_input("Enter '1' if you are a male, '2' if you are a female and '3' if you don't want to tell : ", 1, 3) 
            elif choice==4: 
                string_reading_style="""Enter the number corresponding to your prefered reading style \n1. sci-fi \n2. Biography \n3. Horror \n4. Romance \n5. Fable \n6. History \n7. Comedy\n"""    
                dico_client["reading_style"]=ask_input(string_reading_style, 1, 7)
            
        name = dico_client['name'] ; age=dico_client['age'] ; gender=dico_client['gender'];reading_style=dico_client['reading_style']
        re_write_line("readers.txt", f"{name},{gender},{age},{reading_style}\n",number_line_user)
        # if the name has changed we need to modify it in booksread.txt
        if name != original_name:
            re_write_line("booksread.txt", name+",".join(all_lines_booksread[number_line_user].split(",")[1:]),number_line_user)
    else: print("User not registered")