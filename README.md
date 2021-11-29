# PROJECT PYTHON FIRST SEMESTER

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

- create a script to make all our menu and generate all menus possibles
- create dictionary creation methode for books and for users
- create save and load methods for books and users, can be store in the disctionnary
- faire bouton suivant/ précédent (à voir)
- fenetre accessible dans menu pour préférence
- possibilité d'ajouter des commentaires sur la page des détails d'un livres, associé au rating (à voir)
- ranger les rating dans un fichier texte et créée un générateur type SQL pour chercher les valeurs via requete
- edit user dans une fenetre à part pour plus simple zone entré et peut etre ouvert du menu ou de l'app ez

# In progress
- Tab "for you"
    * Liste recommendation, préférer des amis, nouveauté, et livre déjà lu non noté style menu déroulant à la apple music
    - Cliquer sur un livre ouvres les détail dans une nouvelles fenêtre : ceci permet de tout traiter dans un script tier.
    - les gallery affiche le titre des livres sur un fond rattaché à une couleur rattaché au genre du livre
-Tab "search"
    - (in progress) style of the tab
    - get actual data
    - search and give result
- Tab "User"
    * connection and disconnection
    - edit profile and delete
    - button disconnect
    - Style of the tab
    - corriger bug user already exist but recreate


# Finished
