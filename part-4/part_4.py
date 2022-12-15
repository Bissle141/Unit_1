library = [
    {"title": "Six of Crows",
     "author": "Leigh Bardugo",
     "year": 2015,
     "pages": 456, 
     "rating": 8.7},
    
    {"title": "A Game of Thrones",
     "author": "George R. R. Martin",
     "year": 1996,
     "pages": 694, 
     "rating": 3}
]

### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def create_new_book(lib):
#     title = str(input("What is the title of your book? - "))
#     author = input(f"Who wrote {title}? - ")
#     try:
#         year = input("When was it published? - ")
#     except:
#         year = input("Please use only numbers - ")
        
#     try:
#         pages = input(f"How many pages does {title} have? - ")
#     except:
#         pages = input("Please use only numbers - ")
        
#     try:
#         rating = input(F"Out of 10, what would you rate {title}? - ")
#     except:
#         rating = input("Please use only numbers. - ")
        
        
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "pages": pages,
#         "rating": rating
#     }

#     lib.append(book_dictionary)
#     return lib





### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book(lib):
#     title = str(input("What is the title of your book? - "))
#     author = str(input(f"Who wrote {title}? - "))
#     year = int(input("When was it published? - "))
#     pages = int(input(f"How many pages does {title} have? - "))
#     rating = float(input(F"Out of 10, what would you rate {title}? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "pages": pages,
#         "rating": rating
#     }

#     lib.append(book_dictionary)
#     return lib


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def create_new_book(lib):
#     title = str(input("What is the title of your book? - "))
#     author = str(input(f"Who wrote {title}? - "))
#     try:
#         year = int(input("When was it published? - "))
#     except:
#         year = int(input("Please use only numbers - "))
        
#     try:
#         pages = int(input(f"How many pages does {title} have? - "))
#     except:
#         pages = int(input("Please use only numbers - "))
        
#     try:
#         rating = float(input(F"Out of 10, what would you rate {title}? - "))
#     except:
#         rating = float(input("Please use only numbers. - "))
        
        
#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "pages": pages,
#         "rating": rating
#     }

#     lib.append(book_dictionary)
#     return lib


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def readable_lib(lib):
    '''Will take in library and return a readable version of it'''
    for book in lib:
        print("\nTitle:", book["title"])
        print("Author:", book["author"])
        print("Published:", book["year"])
        print("Page Count:", book["pages"])
        print("Rating:", book["rating"], "\n")       
    

def main(lib):
    '''Will start off by prompting the user for what they would like to do'''
    main = True
    while main == True:
        answer = input("Would you like to add a new book, if so, input 'new', or list them, then input 'list'. - ")
        if answer.lower() in "new":
            main = False
            create_new_book(lib)
        elif answer.lower() in "list":
            main = False
            readable_lib(lib)
        else:
            print("Please enter valid input. 'new' or 'list'")
        
 
def create_new_book(lib):
    '''Will add a new book to the library'''
    title = str(input("What is the title of your book? - "))
    author = str(input(f"Who wrote {title}? - "))
    try:
        year = int(input("When was it published? - "))
    except:
        year = int(input("Please use only numbers - "))
        
    try:
        pages = int(input(f"How many pages does {title} have? - "))
    except:
        pages = int(input("Please use only numbers - "))
        
    try:
        rating = float(input(F"Out of 10, what would you rate {title}? - "))
    except:
        rating = float(input("Please use only numbers. - "))
        
        
    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "pages": pages,
        "rating": rating
    }

    lib.append(book_dictionary)
    
    readable_lib(lib)





### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

# Please see above code^^^

main(library)