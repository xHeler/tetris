import requests
import ast


url = 'http://127.0.0.1:8000/api/v1/dj-rest-auth/login/'
url2 = 'http://127.0.0.1:8000/api/v1/'

json = {
    'username': "andrzej@mail.com",
    'email': 'andrzej@mail.com',
    'password': 'bartosz1235',
}

response = requests.post(url, json = json)
key = ast.literal_eval(response.text)
print()

# add number

json2 = {
    'author': 'andrzej@mail.com',
    'points': 10
}

headers = {}
headers['Authorization'] = 'Token ' + str(key['key'])
print(headers)

response = requests.post(url2, json = json2, headers=headers)
print(response.text)


# edit number