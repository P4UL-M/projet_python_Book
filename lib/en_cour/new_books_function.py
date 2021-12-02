from ect.globals import PATH
from lib.new_others_functions import *

def add_book(book_name, gender):
    if not is_registered("books.txt", book_name):
        all_lines_notes=get_all_lines("notes.txt")
            # the line[:-1] is to remove the \n
        re_write_book("books.txt", book_name+","+gender, mode="a")
        final_notes=""
        for line in all_lines_notes:
            final_notes+= line[:-1]+"0"+"\n"
        re_write_book("notes", final_notes)   
    
def remove_books(book_name):
    if is_registered("books.txt", book_name):
        all_lines_books=get_all_lines("books.txt") ; all_lines_booksread=get_all_lines("booksread.txt") ; all_lines_notes=get_all_lines("notes.txt")
        book_number_to_remove=get_number_line('books.txt', book_name)
        if book_number_to_remove!= 0:    
            final_booksread, final_notes = "", ""
            
            for line in all_lines_booksread:
                for index, books_number in enumerate(line.split(",")):
                    # if its the name of an user
                    if index==0:
                        final_booksread+=books_number+","
                    elif index != len(line.split(","))-1:
                        if int(books_number)>book_number_to_remove:
                            final_booksread+=str(int(books_number)-1)+","
                        elif int(books_number)!=book_number_to_remove:
                            final_booksread+=books_number+","
                final_booksread+="\n"
                
            for line in all_lines_notes:
                final_notes+= line[:book_number_to_remove]+line[book_number_to_remove+1:]
            
            re_write_book("books.txt", "".join(all_lines_books[:book_number_to_remove])+"".join(all_lines_books[book_number_to_remove+1:]))
            re_write_book("booksread.txt", final_booksread)  
            re_write_book("notes.txt", final_notes)  

def edit_book(book_name, new_title, new_gender):
    if is_registered("books.txt", book_name):
        book_number_to_edit=get_number_line('books.txt', book_name)
        all_lines_books=get_all_lines("books.txt")
        re_write_book("books.txt", "".join(all_lines_books[:book_number_to_edit])+new_title+","+new_gender+"\n"+"".join(all_lines_books[book_number_to_edit+1:])) 

def is_book_read(number_book, name):
    all_lines_booksread=get_all_lines("booksread.txt")
    client_number=get_number_line("readers.txt", name)
    if str(number_book) not in all_lines_booksread[client_number].split(","):
        return False
    return True

def get_readings(name):
    if is_registered("readers.txt", name):
        all_lines_booksread=get_all_lines('booksread.txt')
        number_reader=get_number_line("booksread.txt", name)
        # return a list
        return all_lines_booksread[number_reader].split(",")[1:-1]

def get_note(name, book):
    if is_registered("books.txt", book) and is_registered("readers.txt", name):
        number_reader=get_number_line("readers.txt", name)
        number_book=get_number_line('books.txt', book)
        all_lines_note=get_all_lines('notes.txt')
        return all_lines_note[number_reader][number_book]

def unread_book(name, book_name):
    if is_registered("books.txt", book_name) and is_registered("readers.txt", name):
        number_book=get_number_line('books.txt', book_name)
        if is_book_read(number_book, name):
            client_number=get_number_line("readers.txt", name)
            all_lines_booksread=get_all_lines("booksread.txt")
            a=all_lines_booksread[client_number].split(",")
            a.remove(str(number_book))
            re_write_book("booksread.txt", "".join(all_lines_booksread[:client_number]) + ",".join(a) + "".join(all_lines_booksread[client_number+1:]))

def read_book(name, book_name):
    if is_registered("books.txt", book_name) and is_registered("readers.txt", name):
        number_book=get_number_line('books.txt', book_name)
        if not is_book_read(number_book, name):
            client_number=get_number_line("readers.txt", name)
            all_lines_booksread=get_all_lines("booksread.txt")
            
            re_write_book("booksread.txt", "".join(all_lines_booksread[:client_number]) + "".join(all_lines_booksread[client_number][:-1])+str(number_book)+","+"\n" + "".join(all_lines_booksread[client_number+1:]))
    
def note_a_book(name, note, book_name):
    if is_registered("books.txt", book_name):
        number_book=get_number_line('books.txt', book_name)
        all_lines_notes=get_all_lines("notes.txt")
        client_number=get_number_line("readers.txt", name)

        final_notes="".join(all_lines_notes[:client_number])
        final_notes+=all_lines_notes[client_number][:number_book]+str(note)+all_lines_notes[client_number][number_book+1:]
        final_notes+="".join(all_lines_notes[client_number+1:])
        re_write_book("notes.txt", final_notes)         
        