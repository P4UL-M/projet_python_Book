import tkinter.messagebox as msg

from ect.handle_data import *
from ect.globals import MATRIX,update_size

def verify_data():
    """
    this function test to access each book and reader, if it can't it trow a fatal error to stop the program from running
    """
    l = list_readers()
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
        msg.showerror("ERROR IN FILE USER OR FILE MISSING", "ERROR IN FILE USER OR FILE MISSING !\n Check that all your file exist and respect the format given in the readme.md")
        raise RuntimeError("ERROR IN FILE USER OR FILE MISSING")
    
    l = list_books()
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
        msg.showerror("ERROR IN FILE BOOK OR FILE MISSING", "ERROR IN FILE BOOK OR FILE MISSING !\n Check that all your file exist and respect the format given in the readme.md")
        raise RuntimeError("ERROR IN FILE BOOK OR FILE MISSING")

def generate_matrix():
    """
    this function genrerate the matrix of the ratio of similarity between two user
    """
    global MATRIX
    l_readers = [i for i in list_readers()]
    update_size(len(l_readers))
    for reader in list_readers():
        for target in list_readers():
            a = list()
            b = list()
            for book in list_books():
                a.append(int(get_value(reader,book)))
                b.append(int(get_value(target,book)))

            s1 = sum([ai*bi for ai,bi in zip(a,b)])
            s2 = sum([i**2 for i in a])**(1/2)
            s3 = sum([i**2 for i in b])**(1/2)
            MATRIX[reader["index"]-1][target["index"]-1] = s1/(s2*s3) if s3!=0 and s2!=0 else 0