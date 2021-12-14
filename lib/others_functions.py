from os import read
from ect.handle_data import *
from lib.books_functions import books
from lib.users_functions import readers, remove_reader

def verify_data():
    try:
        l = readers()
        def remove_corruption(index=None):
            try:
                i = index or 1
                while next(l):
                    i+=1
            except StopIteration:
                return True
            except Exception as e:
                return False
        if not remove_corruption():
            raise RuntimeError
    except RuntimeError:
        raise RuntimeError("ERROR IN FILE BOOK OR FILE MISSING")
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
                return False
        if not remove_corruption():
            raise RuntimeError
    except RuntimeError:
        raise RuntimeError("ERROR IN FILE BOOK OR FILE MISSING")

def restore_data():
    pass