import requests
import ast

from src.utils.settings import LOGIN_URL, CONN_URL


key = None
username = None

def connect_to_server(email, password):
    global key, username
    json = {}
    json['username'] = email
    json['email'] = email
    json['password'] = password
    response = requests.post(LOGIN_URL, json = json)
    response_json = ast.literal_eval(response.text)
    if "key" in response_json:
        key = response_json['key']
        username = email
        return True, None
    else:
        return False, response_json
    

def send_score_to_server(points):
    global key, username
    if not key:
        return False
    json = {}
    headers = {}
    json["author"] = username
    json["points"] = points
    headers['Authorization'] = 'Token ' + str(key)
    response = requests.post(CONN_URL, json=json, headers=headers)
    response_json = ast.literal_eval(response.text)
    print(str(response_json))