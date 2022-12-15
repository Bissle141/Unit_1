##### Quick note: This is not a regular readme. This .md file is meant to be used as a quick ref to look back on the topics covered during this units project. 

<br></br>
<span style="color: #e4cfff">

# Unit 1 Notes

</span>

<br>
<span style="color: #e4cfff">

## Directory

</span>

- [Unit 1 Notes](#unit-1-notes)
  - [Directory](#directory)
  - [Operators](#operators)
    - [Basic Math Operations](#basic-math-operations)
    - [Augmented Assignment Operations](#augmented-assignment-operations)
      - [(most of these names I just made up and I was not creative)](#most-of-these-names-i-just-made-up-and-i-was-not-creative)
    - [Comparison Operators](#comparison-operators)
    - [Boolean Operators](#boolean-operators)
      - [And, Or, and Not](#and-or-and-not)
  - [Boiler Plates](#boiler-plates)
    - [Function](#function)
    - [If/Elif/Else](#ifelifelse)
    - [For Loop](#for-loop)
    - [While Loop](#while-loop)
    - [Exceptions](#exceptions)
  - [Lists \& Tuples](#lists--tuples)
    - [Zero Indexing](#zero-indexing)
    - [Indexing](#indexing)
      - [Getting a value with index](#getting-a-value-with-index)
  - [Type Conversion](#type-conversion)
  - [Input function](#input-function)

<br>

---
<br>
<span style="color: #e4cfff">

## Operators

</span>
<br>

<span style="color: #d2afff">

### Basic Math Operations

</span>


| Type | Operator | Example
| :-: | :-: | :-: |
| Exponent | ** | 2 ** 2 = 4
| Modulus | % | 3 % 2 = 1 |
| Integer Division | // | 22 // 8 = 2 |
| division | / | 3 / 3 = 1 |
| Multiplication | * | 5 * 5 = 25 |
| Subtraction | - | 5 - 3 = 2 |
| Addition | + | 10 + 2 = 12 |

<br>
<br>
<span style="color: #d2afff">

### Augmented Assignment Operations

</span>

#### (most of these names I just made up and I was not creative)
| Type | Operator | Example & Break Down
| :-: | :-: | :-: |
| Plus equal | += | 'x += 1' &harr; 'x = x + 1' |
| Minus Equal | -= | 'x -= 1' &harr; 'x = x - 1'  |
| Multiply Equal | *= | 'x *= 1' &harr; 'x = x * 1'  |
| Devide Equal | /= | 'x /= 1' &harr; 'x = x / 1'  |
| Remainder Equl | %= | 'x %= 1' &harr; 'x = x % 1'  |

<br>
<br>
<span style="color: #d2afff">

### Comparison Operators

</span>

| Operator | Meaning |
|:-:|:-:|
| < | Less than |
| <= | Less than or equal to|
| > | Greater than |
| >= | Greater than or equal to |
| == | Equal to |
| != | Not equal to|

<br>
<br>

<span style="color: #d2afff">

### Boolean Operators

</span>

#### And, Or, and Not

These three operators can evaluate an expression and return only true or false.

Example Table:
| Example | Output |
| :-: | :-: |
|True <i>and</i> True | True |
|True <i>and</i> False | False |
|  |  |
|True <i>or</i> True | True |
|True <i>or</i> False | True |
|False <i>or</i> False | False |
|False <i>or</i> False | False |
|  |  |
| <i>not</i> False | True |
| <i>not</i> True | False |

<br>

---
<br>
<span style="color: #e4cfff">

## Boiler Plates

</span>
<span style="color: #d2afff">

### Function

</span>


    def func_name(param1, param2...):
        ## Function body...

<br>
<span style="color: #d2afff">

### If/Elif/Else

</span>
If statments are condition based and will first check if any pased condition is true. if it is they will enact the code within them, if not they will either move onto the next check in the if/elif/else sequence or simply move on in the code.
<br></br>

Syntax:

    if {condition}:
        # runs if the if condition is true
    elif {condition}:
        # runs if the elif contion is true
    elif {condition}:
        # runs if the second elif contion is true
    else:
        # will only run if all of the above catches are false. 




<br>
<span style="color: #d2afff">

### For Loop

</span>
The 'for loop' can iterate over lists, tuples, dictionaries, sets and strings.
<br></br>
Syntax:

    for item in obj:
        # Loop body... 

<br>
<span style="color: #d2afff">

### While Loop

</span>
A while loop will run continuious so long as the set condition is thruthy.
<br></br>
Syntax:

    while condition: 
        # While body...

Example:
    
    x = 0
    while x <br y:
        print(x)
        x += 1  #will increment x to avoid an infinite loop

IMPORTANT, make sure there is some sort of incrementor happening or that after every iteration of the loop the condition is closer to becoming false. You do not want to accidentally make an infinite loop. 

<br>
<span style="color: #d2afff">

### Exceptions

</span>

An Exception is an Event that happens while a pogram is being executed. It is also called a "run time error". When it occurs, Python generates an exception that can be "handled" with some additional logic, which avoids code breaking.

There are up to four parts of an exception: The try, except, else, and finally. 
<br></br>

Syntax:

    try:
       # The code you wish to enact but could produce an exception
    except:
        # The exception handler, will only fire if there is an exception/error
    else:
        # An else statment that will only fire if there is no exception/error
    finally:
        # Code which will fire everytime after all previous blocks have run.

Example:
(Taken from GeeksforGeeks.org)

    def divide(x, y):
        try:
            # Floor Division : Gives only Fractional Part as Answer
            result = x // y
        except ZeroDivisionError:
            print("Sorry ! You are dividing by zero ")
        else:
            print("Yeah ! Your answer is :", result)
        finally: 
            # this block is always executed regardless of exception generation. 
            print('This is always executed')  
 
    # Look at parameters and note the working of Program
    divide(3, 2)
    divide(3, 0)




<br>

---
<br>
<span style="color: #e4cfff">

## Lists & Tuples

</span>

List &rarr; A list is a mutable, ordered collection of data. Mutable meaning it can be changed and altered after its declaration, and ordered meaning its stored data will maintain a consistant order.

Tuple &rarr; A tuple is like a list but, it is immutable and ordered. Meaning its values cannot be changed after decleration and it's order will remain consistant.

<br>

### Zero Indexing
Remeber when idexing we begin at the 0 index and move up.
|Index:|0|1|2|3|4|...|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Value:|a|b|c|d|e|...|

<br>

### Indexing

#### Getting a value with index

    my_list = ['a', 'b', 'c', 'd']
    my_list[3] -> 'd'

    my_tuple = ('a', 'b', 'c', 'd')
    my_tuple[0] -> 'a'

<br>
<span style="color: #e4cfff">


## Type Conversion

</span>
Type conversion can be used in certain cases to convered one data type to another. A string to a integer, an integer to a float and so on. 
For the most part it is stright forward enough, however you need to pay attention to the data-type you are trying to convert. 
Take strings for example, they are quite flexible so long as you pay attention to what you are converting, a string like "34" will have no problem being converted to an integer or a float, but if you try to convert somthing like "hello" to an integer/float, it's not gonna work. So just keep this in mind when converting.
<br></br>

Syntax:

    num = 2.74
    num = int(num) ==> num = 2
    num = str(num) ==> num = "2"
    
<br>

---

<br>
<span style="color: #e4cfff">


## Input function

</span>
The input function will utilize the terminal and request the user input soe sort of value. By default the users input will be a string, but you can utilize type conversion on an input to change that.

<br></br>
Syntax:
        
    input("A string to prompt user. \n")