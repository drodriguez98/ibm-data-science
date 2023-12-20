name = "Michael Jackson"

# Print the first element in the string

print(name[0])

# Print the element on index 6 in the string

print(name[6])

# Print the last element in the string

print(name[-1])

# Print the first element in the string

print(name[-15])

# Find the length of string

len("Michael Jackson")

# Take the slice on variable name with only index 0 to index 3

name[0:4]

# Take the slice on variable name with only index 8 to index 11

name[8:12]

# Get every second element. The elments on index 1, 3, 5 ...

name[::2]

# Get every second element in the range from index 0 to index 4

name[0:5:2]

# Concatenate two strings

statement = name + "is the best"
statement

# Print the string for 3 times

3 * "Michael Jackson"

# Concatenate strings

name = "Michael Jackson"
name = name + " is the best"
name

# New line escape sequence

print(" Michael Jackson \n is the best" )

# Tab escape sequence

print(" Michael Jackson \t is the best" )

# Include back slash in string

print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )

# Convert all the characters in string to upper case

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Convert all the characters in string to lower case
a = "MICHAEL JACKSON IS THE BEST"
print("Before lower:", a)
b = a.lower()
print("After lower:", b)

# Replace a segment of the string

a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b

# Replace the old substring with the new target substring by removing some punctuations

a = "Hello! Michael Jackson has: 12 characters."
print(a)
b = a.replace('!','').replace(':','').replace('.','')
print(b)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output

name = "Michael Jackson"
name.find('el')

# Find the substring in the string

name.find('Jack')

# Split the substring into list

name = "Michael Jackson"
split_string = (name.split())
split_string


# EXERCISE 1. Search for the word "Jackson" in the string "Michael Jackson is the best" using RegEx.

import re

s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string.
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")


# EXERCISE 2. Search for any digit character (0-9) using \d special sequence.
    
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

# EXERCISE 3. Search for any character that is not a word using \W special sequence.
    
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)    