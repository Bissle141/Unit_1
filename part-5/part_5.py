            
### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
     
 
def create_new_book():
    '''Will add a new book to the library'''
    title = str(input("What is the title of your book?\n"))
    author = str(input(f"Who wrote {title}?\n"))
    try:
        year = int(input("When was it published?\n"))
    except:
        year = int(input("Please use only numbers - "))
        
    try:
        pages = int(input(f"How many pages does {title} have?\n"))
    except:
        pages = int(input("Please use only numbers - "))
        
    try:
        rating = float(input(F"Out of 10, what would you rate {title}?\n"))
    except:
        rating = float(input("Please use only numbers. - "))  
        
    with open("library.txt", "a") as my_library:
        my_library.write(f"{title}, {author}, {year}, {pages}, {rating}\n")
    
    main()
    

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def txt_to_list(library_txt):
    '''will fetch all the book entries from the txt and return a list with nested dictionaries for every book entry'''
    lib_list = []
    with open(library_txt, "r") as my_library:
        file = my_library.readlines()
        
        for line in file:
            line = line.strip()
            
            book_line = line.split(', ')
            
            book = {
                "title": book_line[0],
                "author": book_line[1],
                "year": book_line[2],
                "pages": book_line[3],
                "rating": book_line[4]
            }
            
            lib_list.append(book)
    
    return (lib_list)


def readable(book_list):
    '''takes in the book-list and prints a readable rep to the console. should be called following txt_to_list function'''
    
    for i in range(len(book_list)):
        print(f"\n-----Book {i+1}-----")
        
        print(f'Title: {book_list[i]["title"]}\nAuthor: {book_list[i]["author"]}\nYear: {book_list[i]["year"]}\nPages: {book_list[i]["pages"]}\nRating: {book_list[i]["rating"]}')
    print('\n')

        


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

# delete a book, avg ratings, search for a book by title or author.

def del_book(lib, book_to_del):
    '''will delete a book from the lib'''
    
    with open(lib, "r") as fr:
        lines = fr.readlines()
        
        with open(lib, "w") as fw:
            for line in lines:
                
                if book_to_del not in line.lower():
                    fw.write(line)
    
    print("--- Book Deleted ---")
    
    
def avg_rate(lib):
    '''Will get the rating for all the books and avg it'''
    
    ratings = []
    
    for book in lib:
        ratings.append(float(book["rating"]))
    
    avg_rating = sum(ratings) / len(ratings)
    print("\nAvgerage Rating:", avg_rating)    
    return avg_rating
    
def search_lib(lib, title):
    '''Will seatch passed library.txt'''
    
    for book in lib:
        if title in book['title'].lower():
            print(f'\nTitle: {book["title"]}\nAuthor: {book["author"]}\nYear: {book["year"]}\nPages: {book["pages"]}\nRating: {book["rating"]}')
            return book
    
    print("\n--- BOOK NOT FOUND ---\n")
    main()
    




def main():
    '''Will initiate a command line menu which the user will be able to use to navigate the app'''
    main = True
    
    while main == True:
        answer = input("ACTION -- INPUT\nAdd a book -- add\nView book List -- list\nDelete a book -- del\nGet avgerage rating -- rate\nSearch by title -- sea\nExit -- exit\n")    
            
        if answer.lower() in "add":
            main = False
            create_new_book()
            
        elif answer.lower() in "list":
            main = False
            list = txt_to_list("library.txt")
            readable(list)
            
        elif answer.lower() in "del":
            main = False
            target = input("What is the name of the book you would like to delete?\n").lower()
            del_book("library.txt", target)
            
        elif answer.lower() in "rate":
            main = False
            list = txt_to_list("library.txt")
            avg_rate(list)
            
        elif answer.lower() in "sea":
            main = False
            title = input("What is the name of the book you are looking for?\n").lower()
            list = txt_to_list("library.txt")
            search_lib(list, title)
            
        elif answer.lower() in "exit":
            return exit
        
        else:
            print("\n--Please enter valid input--")


if __name__ == "__main__":
    main()