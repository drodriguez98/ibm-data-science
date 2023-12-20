# Condition Equal

a = 5
a == 6

# Greater than Sign

i = 6
i > 5

# Inequality Sign

i = 2
i != 6

# Use Equality sign to compare the strings

"ACDC" == "Michael Jackson"

# Use Inequality sign to compare the strings

"ACDC" != "Michael Jackson"

# Compare characters

'B' > 'A'
'BA' > 'AB'

# If statement example

age = 19

if age > 18:
    
    print("you can enter" )

print("move on")

# Else statement example

age = 18

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")

# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")

# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")

# Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")