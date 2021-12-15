from ect.handle_data import *
from lib.books_functions import books
from lib.users_functions import readers

def verify_data():
    """
    this function test to access each book and reader, if it can't it trow a fatal error to stop the program from running
    """
    try:
        l = readers()
        def detect_corruption(index=None):
            try:
                i = index or 1
                while next(l):
                    i+=1
            except StopIteration:
                return True
            except:
                return False
        if not detect_corruption():
            raise RuntimeError
    except RuntimeError:
        raise RuntimeError("ERROR IN FILE BOOK OR FILE MISSING")
    try:
        l = books()
        def detect_corruption(index=None):
            try:
                i = index or 0
                while next(l):
                    i+=1
            except StopIteration:
                return True
            except:
                return False
        if not detect_corruption():
            raise RuntimeError
    except RuntimeError:
        raise RuntimeError("ERROR IN FILE BOOK OR FILE MISSING")