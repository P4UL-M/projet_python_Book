from others_functions import ask_input

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                 books functions                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def add_book():
    book_name=input("Enter the book's title you want to add : ")
    with open(f"books.txt", "r", encoding="utf-8") as books:
        # the line[:-1] is to remove the \n
        if book_name not in [line[:-1] for line in books.readlines()]:
            with open(f"books.txt", "a", encoding="utf-8") as books_write, open(f"notes.txt", "r", encoding="utf-8") as notes:
                books_write.write(f"{book_name}\n")
                final_notes=""
                for line in notes.readlines():
                    final_notes+= line[:-1]+"0"+"\n"
                with open(f"notes.txt", "w", encoding="utf-8") as notes_write:
                    notes_write.write(final_notes)    
        else:
            print("book already registered")

def remove_books():
    with open(f"books.txt", "r", encoding="utf-8") as books, open(f"booksread.txt", "r", encoding="utf-8") as booksread, open(f"notes.txt", "r", encoding="utf-8") as notes:
        all_lines_books=books.readlines()
        all_lines_booksread=booksread.readlines()
        all_lines_notes=notes.readlines()
        display_books()
        book_number_to_remove=ask_input("Enter the number related to the book's title you want to remove, 0 to exit :  ", int, 0, len(all_lines_books))
        if book_number_to_remove!= 0:    
            final_books=""    
            final_booksread=""
            final_notes=""
            
            for number_line, line in enumerate(all_lines_books):
                if number_line+1!=book_number_to_remove:
                    final_books+= line
            
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
                
            with open(f"books.txt", "w", encoding="utf-8") as books_write:
                books_write.write(final_books)
            with open(f"booksread.txt", "w", encoding="utf-8") as booksread_write:
                booksread_write.write(final_booksread)
            with open(f"notes.txt", "w", encoding="utf-8") as notes_write:
                    notes_write.write(final_notes)
        else:
            print("Exit succesfully")

def display_books():
    with open(f"books.txt", "r", encoding="utf-8") as books:
        for i, line in enumerate(books.readlines()):
            print(str(i+1)+". "+line, end="")
        print()
        return i

def edit_book():
    with open(f"books.txt", "r", encoding="utf-8") as books:
        all_lines_books=books.readlines()
        display_books()
        book_number_to_edit=ask_input("Enter the number related to the book's title you want to edit, 0 to exit :  ", int, 0, len(all_lines_books))
        new_title=input("Enter the new title of the book : ")
        if book_number_to_edit!= 0:
            final_books="" 
            for number_line, line in enumerate(all_lines_books):
                if number_line+1!=book_number_to_edit:
                    final_books+= line
                else:
                    final_books+=new_title+"\n"
            with open(f"books.txt", "w", encoding="utf-8") as books_write:
                books_write.write(final_books)
        else:
            print("Exit succesfully")

def note_a_book():
    name=input("What is your name ? ")
    with open(f"booksread.txt", "r", encoding="utf-8") as booksread, open(f"books.txt", "r", encoding="utf-8") as books, open(f"readers.txt", "r", encoding="utf-8") as readers :
        all_lines_booksread=booksread.readlines()
        maximum_number_book=len(books.readlines())
        if name in [line.split(", ")[0] for line in all_lines_booksread]:
            client_number=-1
            for index, clients_name in enumerate([line.split(", ")[0] for line in readers.readlines()]):
                if clients_name == name:
                    client_number=int(index)
            
            display_books()
            number_book=ask_input("Enter the number of the book you want to note, 0 to exit : ", int, 0, maximum_number_book)
            while number_book!=0:
                if number_book not in all_lines_booksread[client_number].split(", "):
                    choice=ask_input("The book is not in your read list, enter 1 if you read it or 0 if you didn't :", int, 0, 1)
                    if choice==1:
                        add_book_to_client(name=name, book=number_book, maximum_number_book=maximum_number_book)
                    else:
                        number_book=ask_input("Enter the number of the book you want to note, 0 to exit : ", int, 0, maximum_number_book)
                        continue
                with open(f"notes.txt", "r", encoding="utf-8") as notes:
                    final_notes=""
                    note=ask_input("Note it between 1 and 5 : ",int, 1, 5)
                    for number_line, line in enumerate(notes.readlines()):
                        if number_line==client_number: 
                            if number_book<len(line)-1:
                                final_notes+=line[:number_book-1]+str(note)+line[number_book:]
                            else:
                                final_notes+=line[:number_book-1]+str(note)+"\n"
                        else:
                            final_notes+=line
                            
                    with open(f"notes.txt", "w", encoding="utf-8") as notes_write:
                        notes_write.write(final_notes) 
                number_book=ask_input("Enter the number of the book you want to note, 0 to exit : ", int, 0, maximum_number_book)
        else:
            print("user not registered")
        
def add_book_to_client(name=None, book=None, maximum_number_book=None):
    if name==None:    
        name=input("What is your name ? ")
    
    with open(f"booksread.txt", "r", encoding="utf-8") as booksread:
        all_lines=booksread.readlines()
        boucle=True
        if name in [line.split(", ")[0] for line in all_lines]:
            # print all books and give the number of books
            if maximum_number_book==None:maximum_number_book=display_books()
            if book == None:
                book=ask_input("Enter 0 to stop\nWhat book have you read ? ", int, 0, maximum_number_book)
            else:
                boucle=False
            while book !=0:
                new_books_read=""
                for i, line in enumerate(all_lines):
                    if line.split(", ")[0]==name:
                        if str(book) not in line.split(", "):
                            all_lines[i]=line[:-1]+str(book)+", \n"
                            new_books_read+=line[:-1]+str(book)+", \n"
                        else: 
                            print("book already registered")
                            new_books_read+=line
                    else:
                        new_books_read+=line
                if boucle:
                    book=ask_input("Enter 0 to stop\nWhat book have you read ? ", int, 0, maximum_number_book)
                else:
                    book=0
                with open(f"booksread.txt", "w", encoding="utf-8") as booksread_write:
                    booksread_write.write(new_books_read)
                
        else:
            print("user not registered")