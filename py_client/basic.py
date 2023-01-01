import requests 

endpoint = "https://www.github.com"

#requests.get()

get_response = requests.get(endpoint)

print(get_response.text)
# if improper api end point - then HTML will be returned 
# if End point is proper - then JSON Data is returned 

# Application Programming Inteface 

# REST API -> Web API 

# API - Application progamming interface 

# Request and Response 

# Get, POST, PUT,  

# CRUD - Create,Read, Update, Delete


# Added Readme file