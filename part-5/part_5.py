def main():
    '''Will start off by prompting the user for what they would like to do'''
    main = True
    while main == True:
        answer = input("Would you like to add a new book, if so, input 'y', if not, input 'n' - ")
        if answer in "y":
            main = False
            create_new_book()
        elif answer in "n":
            main = False
            return
        else:
            print("Please enter valid input. 'new' or 'list'")
            
### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
     
 
def create_new_book():
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
        
    with open("library.txt", "a") as my_library:
        my_library.write(f"{title}, {author}, {year}, {pages}, {rating}")
        my_library.close()
    

main()
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

with open("library.txt", "r") as my_library:
    file = my_library.readlines()

    for line in file:
        title, author, year, pages, rating = line.split(", ")
        
        book = {
            "title": title,
            "author": author,
            "year": year,
            "pages": pages,
            "rating": rating
        }
        
    print (book)


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!





