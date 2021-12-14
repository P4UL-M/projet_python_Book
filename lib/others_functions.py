from os import read
from ect.handle_data import *
from lib.books_functions import books
from lib.users_functions import readers, remove_reader

def verify_data():
    try:
        l = readers()
        def remove_corruption(index=None):
            try:
                i = index or 0
                while next(l):
                    i+=1
            except StopIteration:
                return True
            except Exception as e:
                print(e)
                remove_reader(i)
                remove_corruption(i)
        if not remove_corruption():
            print("ERROR IN FILE USER")
    except:
        raise Exception("FATAL ERROR FILE MISSING")
    try:
        l = books()
        def remove_corruption(index=None):
            try:
                i = index or 0
                while next(l):
                    i+=1
            except StopIteration:
                return True
            except:
                remove_reader(i)
                remove_corruption(i)
        if not remove_corruption():
            print("ERROR IN FILE BOOK")
    except:
        raise Exception("FATAL ERROR FILE MISSING")

def restore_data():
    pass