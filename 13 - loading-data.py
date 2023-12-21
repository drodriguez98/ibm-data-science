# pip install xlrd

import requests
import pandas as pd

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

# Download CSV file
            
csv_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
download_file(csv_url, 'TopSellingAlbums.csv')

# Download Excel file

xlsx_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
download_file(xlsx_url, 'TopSellingAlbums.xlsx')

# Read CSV file

df_csv = pd.read_csv('TopSellingAlbums.csv')
print(df_csv.head())

# Read Excel file

df_xlsx = pd.read_excel('TopSellingAlbums.xlsx')
print(df_xlsx.head())

# Read data from CSV file

df = pd.read_csv("TopSellingAlbums.csv")

# Read data from Excel File and print the first five rows

df = pd.read_excel("TopSellingAlbums.xlsx")
df.head()

# Access to the column Length

x = df[['Length']]
x

# Get the column as a series

x = df['Length']
x

# Get the column as a dataframe

x = df[['Artist']]
type(x)

# Access to multiple columns

y = df[['Artist','Length','Genre']]
y

# Access the value on the first row and the first column

df.iloc[0, 0]

# Access the value on the first row and the third column

df.iloc[0,2]

# Slicing the dataframe

df.iloc[0:2, 0:3]

# Slicing the dataframe using name

df.loc[0:2, 'Artist':'Released']