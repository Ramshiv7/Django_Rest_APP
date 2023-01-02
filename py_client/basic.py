import requests 

endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint)

print(get_response.text) # if its not a valid endpoint ( Non api request ) - then HTML is returned 

print("\n\n\n\n")

endpoint = "https://httpbin.org/anything"

#get_response = requests.get(endpoint)

get_response = requests.get(endpoint, json={'query':"hello world"})  # another way to query json data if data is sent, we will receive json data 


print(get_response.text) # if its valid endpoint - then JSON data is returned  ( JavaScript Object Notation ~ Python Dict )


print(get_response.json()) # Converts JSON into Usable Python Dictonary 

# client can consume API as long as it sends API requests

print(get_response.status_code) # Returns the API Response status 