import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com')

#print the response text (the content of the requested file):
print(x.text)