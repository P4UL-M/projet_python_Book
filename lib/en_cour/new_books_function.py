from ect.globals import PATH
from ect.en_cour.others_functions import *

def display_books():
    all_lines_books=get_all_lines("books.txt")
    string=""
    for i, line in enumerate(all_lines_books):
        string+=str(i+1)+". "+line
    return string

def add_book(book_name):
    all_lines_notes=get_all_lines("notes.txt")
        # the line[:-1] is to remove the \n
    re_write_book("books.txt", book_name, mode="a")
    final_notes=""
    for line in all_lines_notes:
        final_notes+= line[:-1]+"0"+"\n"
    re_write_book("notes", final_notes)   
    
def remove_books(book_number_to_remove):
    all_lines_books=get_all_lines("books.txt") ; all_lines_booksread=get_all_lines("booksread.txt") ; all_lines_notes=get_all_lines("notes.txt")
    
    if book_number_to_remove!= 0:    
        final_booksread, final_notes = "", ""
        
        for line in all_lines_booksread:
            for index, books_number in enumerate(line.split(", ")):
                # if its the name of an user
                if index==0:
                    final_booksread+=books_number+", "
                elif index != len(line.split(", "))-1:
                    if int(books_number)>book_number_to_remove:
                        final_booksread+=str(int(books_number)-1)+", "
                    elif int(books_number)!=book_number_to_remove:
                        final_booksread+=books_number+", "
            final_booksread+="\n"
            
        for line in all_lines_notes:
            final_notes+= line[:book_number_to_remove-1]+line[book_number_to_remove:]
        
        re_write_book("books.txt", "".join(all_lines_books[:book_number_to_remove-1])+"".join(all_lines_books[book_number_to_remove:]))
        re_write_book("booksread.txt", final_booksread)  
        re_write_book("notes.txt", final_notes)  
        return("Removed succesfully")
    else:
        return("Exit succesfully")

def edit_book(book_number_to_edit, new_title):
    all_lines_books=get_all_lines("books.txt")
    if new_title!= 0:
        re_write_book("books.txt", "".join(all_lines_books[:book_number_to_edit-1])+new_title+"\n"+"".join(all_lines_books[book_number_to_edit:])) 
    else:
        return("Exit succesfully")

def is_book_in_client(number_book, name):
    all_lines_booksread=get_all_lines("booksread.txt")
    client_number=get_number_line("readers.txt", name)
    if str(number_book) not in all_lines_booksread[client_number].split(", "):
        return False
    return True

def add_book_to_client(name, number_book):
    if not is_book_in_client(number_book, name):
        client_number=get_number_line("readers.txt", name)
        all_lines_booksread=get_all_lines("booksread.txt")
        
        re_write_book("booksread.txt", "".join(all_lines_booksread[:client_number]) + "".join(all_lines_booksread[client_number][:-1])+str(number_book)+", " + "".join(all_lines_booksread[client_number+1:]))
    else:
        return "book already registered"
    
def note_a_book(name, note, number_book):

    all_lines_notes=get_all_lines("notes.txt")
    client_number=get_number_line("readers.txt", name)
    
    if note !=0:
        final_notes="".join(all_lines_notes[:client_number])
        if number_book<len(all_lines_notes[client_number])-1: final_notes+=all_lines_notes[client_number][:number_book-1]+str(note)+all_lines_notes[client_number][number_book:]
        else: final_notes+=all_lines_notes[client_number][:number_book-1]+str(note)+"\n"
        final_notes+="".join(all_lines_notes[client_number+1:])
        re_write_book("notes.txt", final_notes)         
