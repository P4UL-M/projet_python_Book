from path import PATH
from functions.others_functions import *
from math import sqrt

def display_books():
    """print the list of all books and its associated number (start from 1)
    will also return the maximum number"""
    for i, line in enumerate(get_all_lines("books.txt")):
        print(str(i+1)+". "+line, end="")
    print()
    return i+1

def add_book():
    """add a book to books.txt and a column to notes.txt"""
    book_name=input("Enter the book's name : ")
    if not is_registered("books.txt", book_name.lower()):
        all_lines_notes=get_all_lines("notes.txt")
        # add the book name to the end of the file
        re_write_file("books.txt", book_name, mode="a")
        final_notes=""
        # add a column to the note matrix
        for line in all_lines_notes:
            final_notes+= line[:-1]+" 0"+"\n"
        re_write_file("notes.txt", final_notes) 
    else: 
        print("Book already registered")  
    
def remove_books():
    """remove a book to the datebase, 
        - will remove the line of the book in books.txt
        - remove the column of the book from notes.txt
        - will remove the apparition of the book in booksread.txt and remove 1 from all the 
        number above the number of the book to delete, since books.txt lost 1 line
        """
    maxi=display_books()
    book_number_to_remove=ask_input("Enter the number assiociate to the book, 0 to exit: ", 0, maxi)
    if book_number_to_remove!= 0:   
        all_lines_booksread=get_all_lines("booksread.txt") ; all_lines_notes=get_all_lines("notes.txt") 
        final_booksread, final_notes = "", ""
        
        for line in all_lines_booksread:
            for index, books_number in enumerate(line.replace('\n', "").split(",")):
                # if its the name of an user
                if index==0:
                    final_booksread+=books_number
                else:
                    # if the number of the book is above book_number_to_remove we remove 1 from it since the files lost a line
                    if int(books_number)>book_number_to_remove:
                        final_booksread+=","+str(int(books_number)-1)
                    elif int(books_number)!=book_number_to_remove:
                        final_booksread+=","+books_number
            final_booksread+="\n"  
        for line in all_lines_notes:
            # remove the collumn number <book_number_to_remove> from notes.txt
            final_notes+= " ".join(
                line.replace("\n", "").split(" ")[:book_number_to_remove-1]+line.replace("\n", "").split(" ")[book_number_to_remove:]
                )+"\n"
        
        # since the number of books start at 1 we need to remove 1 from it to have the number of line
        re_write_line("books.txt", "", book_number_to_remove-1)
        re_write_file("booksread.txt", final_booksread)  
        re_write_file("notes.txt", final_notes)  

def edit_book():
    """change the name of a book"""
    maxi=display_books()
    book_number_to_edit=ask_input("Enter the number assiociate to the book : ", 1, maxi)
    new_title=input("Enter the new title of the book : ")
    # since the number of books start at 1 we need to remove 1 from it to have the number of line
    re_write_line("books.txt", new_title+"\n", book_number_to_edit-1)

def is_book_read(number_book:int, name:str):
    """return True if the book line <boonk_number> is read by the user <name> else False"""
    all_lines_booksread=get_all_lines("booksread.txt")
    client_number=get_number_line("readers.txt", name)
    if str(number_book) in all_lines_booksread[client_number].replace('\n', "").split(","):
        return True
    return False

def get_readings(name:str, number_client=None):
    """return a list of integers corresponding to the books that the user <name> as read
    if number_client is different from none it's because we already computed the number of line so we just passed it in parameter"""
    if number_client!=None or is_registered("readers.txt", name):
        all_lines_booksread=get_all_lines('booksread.txt')
        if number_client==None:
            number_client=get_number_line("booksread.txt", name)
        # return a list
        return all_lines_booksread[number_client].replace("\n", "").split(",")[1:]

def get_note(name:str, book:str):
    """return the note of the user <name> on the book <book>"""
    if is_registered("readers.txt", name):
        if is_registered("books.txt", book):
            number_reader=get_number_line("readers.txt", name)
            number_book=get_number_line('books.txt', book)
            all_lines_note=get_all_lines('notes.txt')
            return all_lines_note[number_reader].split(" ")[number_book]
        else:
            print("books not registered")
    else:
        print("user not registered")

def unread_book():
    """remove a book from booksread.txt on the line of the reader that the user will input"""
    name=input("Enter the reader's name : ").lower()
    if is_registered("readers.txt", name):
        maxi=display_books()
        book_number=ask_input("Enter the number assiociate to the book, 0 to exit: ", 0, maxi)
        if is_book_read(book_number, name):
            client_number=get_number_line("readers.txt", name)
            all_lines_booksread=get_all_lines("booksread.txt") ; all_lines_notes = get_all_lines("notes.txt")
            a=all_lines_booksread[client_number].replace("\n", "").split(",")
            a.remove(str(book_number))
            re_write_line("booksread.txt", ",".join(a)+"\n", client_number)
            
            re_write_line("notes.txt", " ".join(all_lines_notes[client_number].replace("\n", "").split(" ")[:book_number-1]+["0"]+all_lines_notes[client_number].replace("\n", "").split(" ")[book_number:])+"\n", client_number)
        else: print("book already not read")
    else: print("user not registered")

def read_book(name:str, book_number:int):
    """add the number of the book in parameter to the line of the user in parameter in booksread.txt"""
    if not is_book_read(book_number, name):
        client_number=get_number_line("readers.txt", name)
        all_lines_booksread=get_all_lines("booksread.txt")
        re_write_line("booksread.txt", "".join(all_lines_booksread[client_number].replace("\n", ""))+","+str(book_number)+"\n", client_number)
    
def rate_a_book(name=None, book_number=None):
    """add the note of the user in notes.txt
    if name and book_number are differents than None its because we already asked before so we dont need to do it here"""
    if not name : name=input("Enter your name : ").lower()
    if is_registered("readers.txt", name):
        if not book_number:
            maxi=display_books()
            book_number=ask_input("Enter the number assiociate to the book, 0 to exit: ", 0, maxi)
        if book_number != 0:
            # if the user didnt read the book we ask him if he want to and if he dont we exit
            if not is_book_read(book_number, name):
                choice=ask_input("It seems that you didnt read the book, enter 1 if you didnt and 2 if you did : ", 1, 2)
                if choice == 2:
                    read_book(name, book_number)
                else: return
                
            note=ask_input("Enter a note between 1 and 5 : ", 1, 5)
            all_lines_notes=get_all_lines("notes.txt")
            client_number=get_number_line("readers.txt", name)

            # we add all lines before the one of the user to final_notes, after we add the line till the note of the book
            # then we add the new note and finally we add the rest of the file
            final_notes="".join(all_lines_notes[:client_number])
            final_notes+=" ".join(all_lines_notes[client_number].split(" ")[:book_number-1])+" "+str(note)+" "+" ".join(all_lines_notes[client_number].split(" ")[book_number:])
            final_notes+="".join(all_lines_notes[client_number+1:])
            re_write_file("notes.txt", final_notes)         
        else:
            print("Successfully exit")
    else: 
        print("User not registered")
        
def read_book_input():
    """sometimes we want to call read_book and we already have our input so we needed to cut the function in two
    so if we want the user to input his name and the name of the book specifically for this function we just call ithis one 
    and if he already done it to note the book for example we call the other"""
    name=input("Enter your name : ").lower()
    if is_registered("readers.txt", name):
        maxi=display_books()
        book_number=ask_input("Enter the number assiociate to the book, 0 to exit: ", 0, maxi)
        if not is_book_read(book_number, name):
            read_book(name, book_number)
        else:
            print("Book already read")
        
    else: print("User not registered")        

def compute_matrix():
    """compute the matrix of similarity"""
    all_lines_readers=get_all_lines('readers.txt');all_lines_notes=get_all_lines("notes.txt")
    matrix=[[0 for _ in range(len(all_lines_readers))] for _ in range(len(all_lines_readers))]
    for i,line in enumerate(matrix):
        for y in range(len(line)):
            # we just apply the formula
            sum_both=0
            sum_a=0
            sum_b=0
            for c in range(len(all_lines_notes[0].replace("\n", "").split(" "))):
                a=all_lines_notes[i].replace("\n", "").split(" ")
                b=all_lines_notes[y].replace("\n", "").split(" ")
                sum_both+=int(a[c])*int(b[c])
                sum_a+=int(a[c])**2
                sum_b+=int(b[c])**2
            # the matrix is already initialize on 0 so we can just skip the initialization one of the sum = to 0
            # moreover we want to avoid the division by 0
            if sum_a!=0 and sum_b!=0:
                matrix[i][y]=round(sum_both/(sqrt(sum_a)*sqrt(sum_b)), 2)
    return matrix

def get_average_rate(book_number:int):
    """return the average note of all users on the book corresponding to <book_number>"""
    all_lines_notes=get_all_lines("notes.txt")
    c=0
    sum=0
    # n is the line splited by space without any \n
    # we just want the notes of book number (in column) so we create a new list with every book_number's element of each lines
    for note in [n[book_number] for n in [line.replace("\n", "").split(" ") for line in all_lines_notes]]:
        if note != "0":
            sum+=int(note)
            c+=1
    if c !=0:
        return sum/c
    else:
        return 0

def recommand_book(matrix:list):
    """recommand a book if possible then ask the user to read it and note it
    matrix is the matrix of similarity"""
    name = input("Enter your name : ").lower()
    if is_registered('readers.txt', name):
        # bool will be true if the user didnt read anything so if we need to recommand the best rated books
        bool=False
        if len(get_readings(name))> 0:
            number_client=get_number_line('readers.txt', name)
            final_set=set()
            # we try to compute the final set 1 time for every reader
            # it can fail if they both have read the sames books
            c=0
            # we will store all the user that failed to compute a set of book (if both readers have read the same books)
            banned=[]
            while final_set==set() and c < len(matrix[number_client])-1:
                # we take 1 random reader to initialize it so we can find the most similar user
                # we couldnt initialize it to the first reader since it may be the user itself
                other_client=[ i for i in range(len(matrix[number_client])) if i != number_client and i not in banned][0]
                # we get the most similar user that is not in banned
                for i, nbr in enumerate(matrix[number_client]):
                    if nbr > matrix[number_client][other_client] and i != number_client and i not in banned:
                        other_client=i
                set_client=set(get_readings("", number_client=number_client))
                set_other_client=set(get_readings(get_name(other_client, "readers.txt")))
                final_set=set_other_client-set_client
                banned.append(other_client)
                c+=1
        else:
            # creation of a list containing all books and its average note
            temp_list=[]
            for book in [line.replace("\n", "") for line in get_all_lines("books.txt")]:
                book_number=get_number_line("books.txt",book.lower())
                temp_list.append((book_number, round(get_average_rate(book_number), 2)))
            # we sort it
            final_list=sorted(temp_list, key=lambda item: item[1], reverse=True)
            # we will recommend only the 5 first book or less if their is less than 5 books
            if len(final_list)<5: final_set=set(tup[0] for tup in final_list)
            else: final_set=set(tup[0] for tup in final_list[:5])
            bool=True
        
        # we only recommand books if the user didnt read any books or if he does and if the most similar reader
        # that we computed before is similar enough
        if bool or (len(final_set)>0 and matrix[number_client][other_client]>0.3):
            all_lines_books=get_all_lines("books.txt")
            # printing of the book we will recommand
            for book in final_set:
                a=all_lines_books[int(book)-1]
                print(f"{book}. {a}")
            book_choice=-1
            # we ask the user to choose one or to exit with 0
            while book_choice not in final_set and book_choice != "0":
                book_choice=input("enter the number corresponding to the book you want to read, 0 to exit : ")
            
            if book_choice!= "0":
                read_book(name, int(book_choice))

                choice=ask_input('Enter 1 if you want to note it now and 2 if you dont : ', 1, 2)
                if choice == 1:
                    rate_a_book(name=name, book_number=int(book_choice))
                else:
                    print("Please note the book later !")
        else:
            print("We have no book to recommand, sorry")
    else:
        print("user not registered")