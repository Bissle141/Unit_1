            
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
        my_library.write(f"\n{title}, {author}, {year}, {pages}, {rating}")
        my_library.close()
    
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
        
        for i in range(len(lib_list)):
            print(f"-----Book {i+1}-----")
            
            print(f'Title: {lib_list[i]["title"]}\nAuthor: {lib_list[i]["author"]}\nYear: {lib_list[i]["year"]}\nPages: {lib_list[i]["pages"]}\nRating: {lib_list[i]["rating"]} \n')
    
    main()
    return (lib_list)

        


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

# delete a book, avg ratings, search for a book by title or author.


def main():
    '''Will start off by prompting the user for what they would like to do'''
    main = True
    while main == True:
        answer = input("Add a new book, input 'new', \nView library, input 'list', \nExit, input 'exit'\n")    
            
        if answer.lower() in "new":
            main = False
            create_new_book()
        elif answer.lower() in "list":
            main = False
            txt_to_list("library.txt")
        elif answer.lower() in "exit":
            return exit
        else:
            print("\n--Please enter valid input--")


if __name__ == "__main__":
    main()