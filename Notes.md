<span style="color: #e4cfff">

# Unit 1 Notes

</span>

<br>
<span style="color: #e4cfff">

## Directory

</span>

1. [Basic Python Operators](#operators)
    * [Basic Math Operators](#basic-math-operations)
    * [Augmented Assignment Operations](#augmented-assignment-operations)
    * [Comparison Operators](#comparison-operators)
    * [Boolean Operators](#boolean-operators)
1. [Simple Biolerplates](#boiler-plates)
    * [Functions](#function)
    * [For Loop](#for-loop)
    * [While Loop](#while-loop)
1. [Lists & Tuples](#lists--tuples)
    * [Zero Indexing](#zero-indexing)
    * [Indexing](#indexing)
        * [Getting a value with index](#getting-a-value-with-index)

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

### For Loop

</span>
The 'for loop' can iterate over lists, tuples, dictionaries, sets and strings.

    for item in obj:
        # Loop body... 

<br>
<span style="color: #d2afff">

### While Loop

</span>
A while loop will run continuious so long as the set condition is thruthy.

    while condition: 
        # While body...

Example:
    
    x = 0
    while x < y:
        print(x)
        x += 1  #will increment x to avoid an infinite loop

IMPORTANT, make sure there is some sort of incrementor happening or that after every iteration of the loop the condition is closer to becoming false. You do not want to accidentally make an infinite loop. 

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

#### Negative indexing

Using negative indexing is just like regular indexing but with very handy additional functionality.

|Index:|-4|-3|-2|-1|
|:-:|:-:|:-:|:-:|:-:|
|Value:|a|b|c|d|e|
