# First function example: Add 1 to a and store as b

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# Get a help on add function

help(add)

# Call the function add()

add(1)

# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

# Use mult() multiply two integers

Mult(2, 3)

# Use mult() multiply two floats

Mult(10.0, 3.14)

# Use mult() multiply two different type values together

Mult(2, "Michael Jackson ")

# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See the output

MJ()
MJ1()

# Define the function for combining strings

def con(a, b):
    return(a + b)

# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5

# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5

# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5

# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)

# Compare Two Strings Directly using in operator

string= "Michael Jackson is the best"

def check_string(text):

    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("Michael Jackson is the best")

# Compare two strings using == operator and function

def compareStrings(x, y):

    if x==y:

        return 1
    
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

check = compareStrings(string1, string2)

if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")

# Python Program to Count words in a String using Dictionary
    
def freq(string):

    words = []
    
    words = string.split() 
    
    Dict = {}
    
    for key in words:
        Dict[key] = words.count(key)

    print("The Frequency of words is:",Dict)
    
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

# Example for setting param with default value

def isGoodRating(rating=4): 

    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

# GLOBAL AND LOCAL VARIABLES.
        
# Example of global variable

artist = "Michael Jackson"

def printer1(artist):

    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)

# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)

# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)


# COLLECTIONS AND FUNCTIONS

def printAll(*args): 

    print("No of arguments:", len(args)) 

    for argument in args:

        print(argument)

printAll('Horsefeather','Adonis','Bone') # printAll with 3 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage') # printAll with 4 arguments


# PREDEFINED FUNCTIONS
        
# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# Use sum() to add every element in a list or tuple together

sum(album_ratings)

# Show the length of the list or tuple

len(album_ratings)