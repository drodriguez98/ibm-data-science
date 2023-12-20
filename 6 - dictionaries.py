# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

# Access to the value by the key

Dict["key1"]

# Access to the value by the key

Dict[(0, 1)]

# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}

release_year_dict

# Get value by keys

release_year_dict['Thriller'] 

# Get all the keys in dictionary

release_year_dict.keys() 

# Get all the values in dictionary

release_year_dict.values() 

# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict

# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict

# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict

# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 

# EXERCISE. The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively:

# a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.

album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}

# b) Use the dictionary to find the total sales of Thriller:

album_sales_dict["Thriller"]

# c) Find the names of the albums from the dictionary using the method keys():

album_sales_dict.keys()

# d) Find the values of the recording sales from the dictionary using the method values:

album_sales_dict.values()

