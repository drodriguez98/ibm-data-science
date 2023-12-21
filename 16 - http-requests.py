import requests
import os 
from PIL import Image

url = 'https://www.ibm.com/'
r = requests.get(url)

# Information about the request

print(r.status_code)

print(r.request.headers)

print(r.request.body)

# Information about the request using the attribute headers

header = r.headers
print(r.headers)

header['date']

header['Content-Type']

r.encoding

# Display the HTML in the body

r.text[0:100]

# Load other types of data (image)

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r=requests.get(url)

print(r.headers)

r.headers['Content-Type']

path=os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)  

# Get Request with URL Parameters 

url_get='http://httpbin.org/get'

payload={"name":"Joseph","ID":"123"}

r=requests.get(url_get,params=payload)

r.url

print("request body:", r.request.body)

print(r.status_code)

print(r.text)

r.headers['Content-Type']

r.json()

r.json()['args']

# Post requests

url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

r_post.json()['form']