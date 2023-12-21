# pip install randomuser

from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_list = r.generate_users(10)

name = r.get_full_name()

# Get all users with full names and their email addresses
    
for user in some_list:

    print (user.get_full_name()," ",user.get_email())

# Generate photos of the random 10 users

for user in some_list:

    print (user.get_picture())

# Generate a table with information about the users
    
def get_users():

    users =[]
     
    for user in RandomUser.generate_users(10):

        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

get_users()

df1 = pd.DataFrame(get_users())  

# API

import requests
import json

# Obtain the fruityvice API data using requests and retrieve results

data = requests.get("https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

# Convert json data into pandas data frame

pd.DataFrame(results)

# Normalize json result

df2 = pd.json_normalize(results)

# Extract information from the dataframe

cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])