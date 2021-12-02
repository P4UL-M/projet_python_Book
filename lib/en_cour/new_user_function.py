from ect.globals import PATH
from lib.en_cour.new_others_functions import *

def add_reader(name, gender, age, reading_style):  
    if not is_registered("readers.txt", name):
        all_lines_books=get_all_lines("books.txt") ;          
        
        re_write_book("readers.txt", f"{name},{gender},{age},{reading_style}", mode="a")
        re_write_book("booksread.txt", f"{name},", mode="a")
        re_write_book("notes.txt", "0"*(len(all_lines_books)), mode="a")
    
def remove_client(name):
    if is_registered("readers.txt", name):
        all_lines_readers=get_all_lines("readers.txt"); all_lines_notes=get_all_lines("notes.txt"); all_lines_booksread=get_all_lines("booksread.txt")
        number_client=get_number_line("readers.txt", name)
        print(number_client)
        print(all_lines_notes)
        print("-------")
        print("".join(all_lines_notes[:number_client]))
        print("------------")
        print("".join(all_lines_notes[number_client+1:]))
        re_write_book("readers.txt", "".join(all_lines_readers[:number_client])+"".join(all_lines_readers[number_client+1:])) 
        re_write_book("notes.txt", "".join(all_lines_notes[:number_client])+"".join(all_lines_notes[number_client+1:]))   
        re_write_book("booksread.txt", "".join(all_lines_booksread[:number_client])+"".join(all_lines_booksread[number_client+1:]))          

def View_a_reader(name):
    if is_registered("readers.txt", name):
        all_lines=get_all_lines("readers.txt")
        number_line=get_number_line("readers.txt", name)
        sep_line=all_lines[number_line].split(",")
        dico={
            "name":name,
            "gender":sep_line[1],
            "age":sep_line[2],
            "reading_style":sep_line[3][:-1]
        }
        return dico

def update_client(original_name, **kwargs):
    """args = name, gender, age, reading_style"""
    if is_registered("readers.txt", original_name):
        all_lines_readers=get_all_lines("readers.txt");all_lines_booksread=get_all_lines("booksread.txt")
        number_line_user=get_number_line("readers.txt", original_name)
        
        dico_client=View_a_reader(original_name)
        
        if int(kwargs['age']) <18:kwargs['age']=1
        elif int(kwargs['age']) <=25:kwargs['age']=2
        else:kwargs['age']=3
        
        for key, value in kwargs.items():
            dico_client[key]=value
            
        name = dico_client['name'] ; age=dico_client['age'] ; gender=dico_client['gender'];reading_style=dico_client['reading_style']
        re_write_book("readers.txt", "".join(all_lines_readers[:number_line_user])+f"{name},{gender},{age},{reading_style}"+"".join(all_lines_readers[number_line_user+1:]))
        if name != original_name:
            re_write_book("booksread.txt", "".join(all_lines_booksread[:number_line_user])+name+","+",".join(all_lines_booksread[number_line_user].split(",")[1:])+"".join(all_lines_booksread[number_line_user+1:]))