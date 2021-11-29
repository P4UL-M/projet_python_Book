from ect.globals import PATH
from ect.en_cour.others_functions import *

def add_client(name, gender, age, reading_style):  
    all_lines_books=get_all_lines("books.txt") ;          
    new_age=0
    if age <18:new_age=1
    elif age <=25:new_age=2
    else:new_age=3
    
    re_write_book("readers.txt", f"{name}, {gender}, {new_age}, {reading_style}", mode="a")
    re_write_book("booksread.txt", f"{name}, ", mode="a")
    re_write_book("notes.txt", "0"*(len(all_lines_books)), mode="a")
    return "user successfully registered"
    
def remove_client(name):
    all_lines_readers=get_all_lines("readers.txt"); all_lines_notes=get_all_lines("notes.txt"); all_lines_booksread=get_all_lines("booksread.txt")
    number_client=get_number_line("readers.txt", name)
        
    re_write_book("readers.txt", "".join(all_lines_readers[:number_client])+"".join(all_lines_readers[number_client+1:])) 
    re_write_book("notes.txt", "".join(all_lines_notes[:number_client])+"".join(all_lines_notes[number_client+1:]))   
    re_write_book("booksread.txt", "".join(all_lines_booksread[:number_client])+"".join(all_lines_booksread[number_client+1:]))          
    return "user successfully registered"

def View_a_reader(name):
    output="Name : "+name
    all_lines=get_all_lines("readers.txt")
    number_line=get_number_line("readers.txt", name)
    sep_line=all_lines[number_line].split(", ")
    if sep_line[1] == "1": output+=" | Gender : Male | "
    elif sep_line[1] == "2": output+=" | Gender : Female | "
    else: output+=" | Gender : Unknow | "
    
    if sep_line[2]=="1": output+="Age : Between 0 and 17 | "
    elif sep_line[2]=="2": output+="Age : Between 18 and 25 | "
    else: output+="Age : Above 25 | "
    output+="Favorite reading style : " + get_reading_style_with_number(sep_line[3][:-1])
    return output

def update_client(original_name, *args):
    """args = name, gender, age, reading_style"""
    all_lines_readers=get_all_lines("readers.txt");all_lines_booksread=get_all_lines("booksread.txt")
    number_line_user=get_number_line("readers.txt", original_name)
    args=list(args);lst=all_lines_readers[number_line_user].split(", ")    
    for i in range(4):
        if args[i]==None: args[i]=lst[i]
    name, gender, age, reading_style=args
    if int(age) <18:new_age=1
    elif int(age) <=25:new_age=2
    else:new_age=3
    re_write_book("readers.txt", "".join(all_lines_readers[:number_line_user])+f"{name}, {gender}, {new_age}, {reading_style}"+"".join(all_lines_readers[number_line_user+1:])+"\n")
    if name != original_name:
        re_write_book("booksread.txt", "".join(all_lines_booksread[:number_line_user])+name+", "+", ".join(all_lines_booksread[number_line_user].split(", ")[1:])+"".join(all_lines_booksread[number_line_user+1:]))