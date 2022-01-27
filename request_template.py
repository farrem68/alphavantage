import requests
import json

base_url = "http://0.0.0.0:8000/api/v1/"


def authenticate(username,password):
    data = {
        "username": username,
        "password": password
    }
    response = json.loads(requests.request("POST", base_url+"api-token-auth/", data=data).text)

    return response

def get_prices(token):
    base_url+"get-prices/"
    headers = {
        "Authorization" : "token "+str(token),
        "content-type":"application/json" 
    }
    response = requests.request("GET",url=base_url+"quotes/", headers=headers)

    return response.text

def post_prices(token):
    base_url+"get-prices/"
    headers = {
        "Authorization" : "token "+token,
        "content-type":"application/json" 
    }
    response = requests.request("POST",url=base_url+"quotes/", headers=headers)
    
    return response.text 

token = authenticate("username","password")["token"]
get_prices(token)
post_prices(token)

