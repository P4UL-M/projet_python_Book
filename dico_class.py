mydico = {}

def add_func(func):
    mydico[func.__name__] = func

mydico["__add_fund__"] = add_func

@mydico["__add_fund__"]
def __init__(self,name,rating):
    self["name"] = name
    self["rating"] = rating

#mydico.__class__.__call__ = __init__

def book(name,rating):
    _dico = mydico.copy()
    _dico["__init__"](_dico,name,rating)
    return _dico.copy()

a = book("test1",4)
b = book("test2",3)
print(a["name"],a["rating"])
print(b["name"],b["rating"])
