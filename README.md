# PROJECT PYTHON FIRST SEMESTER
by Paul MAIRESSE and Louis LE MEILLEUR

## REQUIREMENT
*all requirement are normally already installed on newer version of python*
- python 3.8 or higher (order in dictionary)
- PIL (image in tkinter)    ``python -m pip install PIL``
- Tkinter                   ``python -m pip install tkinter``
- PATH                      ``python -m pip install PATH``
- sys                       ``default installed in python``

## How to Use :

- execute the main file or the App.pyw
  
- the App is divised in 4 tab :
  - first the home page where you can see the recommandation of the user connected,the last books added, the last books read
  - second the search tab to search a user or a book
  - third to connect as/create a user, or see its information, edit it or delete it
  - fourth to add a book

- to see a book you just have to double click on it in the main page or the search tab
  - you can see all the info : title, global rating,style
  - read it
  - rate it
  - edit it
  - delete it
  - (you can also see the info of a user this way but to edit or delete it you need to connect with it in the third tab)

- to see a user you just have to double click on it in the main page or the search tab
  - you can see all the info : name, gender, age, favorite style


- Modify the data without the app can be dangerous :
  - a book in the readings list that don't exist anymore will crash the app
  - a name for a user with a coma in it (forbiden in the application) will crash the app
  - every book must have a column in the matrix or the app will crash
  - every user must have a row in the matrix or the app will crash
  - if books are not in the same order in the two file, the app migth crash
  - if users are not in the same order in the two file, the app migth also crash
  - error of format in the file migth crash the app or make it corrumpt data and crash


Note : For X reasons Tkinter may don't update correctly (principaly on Windows), This normally won't happen but if it's the case to correct this you can resize the window of 2 more pixels until the application is fully updated (what force_update do).


## formats of files :

```
_____________________
readers.txt :
_____________________
user_name,(1-3),(1-3),(1-9)

```


```
_____________________
books.txt :
_____________________
title

```


```
_____________________
books_extended.txt :
_____________________
title,(1-9)

```

```
_____________________
booksread.txt :
_____________________
user_name,(1-nbbook),(1-nbbook),(1-nbbook)
user_name

```

```
_____________________
notes.txt :
_____________________
0 0 ⎡...⎤ 0
0 0 ⎪...⎪ 0
⎡. . . .⎪ 0
⎣. . . .⎦ 0
0 0 0 0 0 0

```

## link :

github : https://github.com/P4UL-M/projet_python_Book

this README use markdown, please consider use a appropriate application to read it properly.