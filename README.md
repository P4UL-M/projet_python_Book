# PROJECT PYTHON FIRST SEMESTER

# How to Use

- execute the main file or the App.pyw
  
- the App is divised in 4 tab :
  - first the home page where you can see the recommandation of the user connected,the last books added, the last books read by the user
  - second the search tab to search a user or a book
  - third to connect as/create a user, or see its infos, edit it or delete it
  - fourth to add a book

- to see a book you just have to double click on it in the main page or the search tab
  - you can see all the info : title, global rating,style
  - read it
  - rate it
  - edit it
  - delete it
  - (you can also see the info of a user this way but to edit or delete it you need to connect with it)

## Instructions :

### Key Dates :
- Release date: 08/11/2021
- Project presentation date: 10/11/2021 
- Follow-up date 1: Week of 15/11/2021 
- Follow-up date 2: Week of 06/12/2021 
- Submission date: 19/12/2021 at 23:59 
- Date of defense : Week of 03/01/2022

### Final Output: A .zip archive containing :
- The project code containing the . py and . txt files
- The report in . pdf
- A README.txt file listing the programs and how to use them in practice. This file should contain all the instructions needed to run the program; it is very important to explain to the user how to use the tool.

### Code Organization :
- Implementing the requested features: move forward as best as possible but NOT off topic
- The quality of the code provided: organization in functions, comments, significant variable names, respect of file names.
- Ease of use of the user interface
- CLASS ARE FORBIDEN

## Objectifs :

### 3 Choices of functionalities
1. Reader Profiles
2. Visit the book depository
3. Recommendation

### Part 1 :
- add a reader
- display a reader information
- Edit a reader information
- Delete a reader

### Part 2 :
- Display the list of book saved (titles)
- Add a book
- Modify the title of a book
- Delete a book

### Part 3 :
- rate a book (reader)
- suggest books to reader

## Part 1 : Details

### User Construction :

- The pseudonym
- The gender
    * MAN.
    * WOMAN
    * NO MATTER WHAT
- Age
    * <= 18 years old
    * Between 18 and 25 years old
    * \> 25 years old
- The reading style
    * sci-fi
    * Biography
    * Horror
    * Romance
    * Fable
    * History
    * Comedy
- The list of books read among those present in the depository

All must be save in files in 2 distinct files : booksread.txt and readers.txt with the two forms :
- ``pseudonym, gender_number, age_number, reading_style_number``
- ``pseudonym, Number_book_read_1, number_book_read_2, ...``

### functionnalities :

- create and add a reader
- search reader (with name like in google + advanced arg or via a list) and wiev its details
- edit a reader and modify the file concern
- delete a reader

We can maybe make an account system like any other where we put edit of our profile and deletion, and then the other functionnalities.

## Part 2 :

### functionnalities :

- add a book (title) and save it at the end of the file, only if not already save
- Edit a book title, we can make a inspect menu of the menu with global rating and put a modify option here (maybe with admin account)
- Delete a book, we can also put it in the inspect menu

## Part 3 :

### recommendation calculation :

reader give note to book they read so we can make a matrix of rating between user and books (maybe store the rating in a db (optionnal)). A user can rate a book only if he has read it and if the book exist.

With this matrix we can make a "similarity" matix which give a % of similarity between to users :
- The Cosine Similarity : if we take book_n <=> a_n and b_n which are rating of respectivelly both users then we have :

![formula Cosine Similarity](https://render.githubusercontent.com/render/math?math=E=\frac{Sum(a_i%20\times%20b_i)}{\sqrt{Sum(a_i^2)}%20\times%20\sqrt{Sum(b_i^2)}}) ![formula Cosine Similarity](https://render.githubusercontent.com/render/math?math=\color{white}E=\frac{Sum(a_i%20\times%20b_i)}{\sqrt{Sum(a_i^2)}%20\times%20\sqrt{Sum(b_i^2)}})

With that we can find similar user to our user and recommend him book that user like him read and like.

We can also add to our calcul a bonus if it's the favorite categories of our user, bonus of global notes of the book and bonus for each similar user with loved this books and then take the first 5 higher recommended book. They must be book the user hasn't read before.

### functionnalities :

- recommendation of lecture to the reader which can decide to read it and then rate it

# ideas

# In progress
- Finir l'UI et retravailler les zones baclées/moches

# Finished