my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_books = [
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "rating": 4.32,
        "pages": 374
    },
    {
        "title": "Six of Crows",
        "author": "Leigh Bardugo",
        "year": 2015,
        "rating": 4.5,
        "pages": 465
    }
]


# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(book):
    ''' will take a given book dictionary, parse it and return a readable output to the console '''
    book_string = f'{book["title"]} was written by {book["author"]} and published in {book["year"]}. It has {book["pages"]} pages, and has a rating of {book["rating"]}'
    
    
    
    return (book_string)
    
    
print(book_parser(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title(book):
    '''Will return the books title'''
    return book["title"]

def book_author(book):
    '''Will return the books author'''
    return book["author"]

def book_year(book):
    '''Will return the year the book was published'''
    return book["year"]

def book_pages(book):
    '''Will return the bookks number of pages'''
    return book["pages"]

def book_rating(book):
    '''Will return the books rating'''
    return book["rating"]

# print(book_author(my_book), book_pages(my_book), book_rating(my_book), book_title(my_book), book_year(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def readable_lib(lib):
    '''Will take in library and return a readable version of it'''
    
    print("\nLIBRARY:")
    for entry in lib:
        print("-----")

        for key in entry:
            print(key, ":", entry[key])
        
# readable_lib(my_books)

def change_book_rating(lib, book_title, new_rating):
    '''will take in a book and new rating var and alter the books rating '''
    for entry in lib:
        if entry["title"] == book_title:
            entry["rating"] = new_rating
        else:
            pass
    readable_lib(lib)

# change_book_rating(my_books, "Six of Crows", 10)


def delete_book(lib, book_title):
    '''takes in an id and lib and will delete the accociated book from the lib.'''
    
    for entry in lib:
        if entry["title"] == book_title:
            lib.remove(entry)
        else:
            pass
    readable_lib(lib)
    
    
delete_book(my_books, "The Hunger Games")



