
import requests

import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('INHYDL08743\\prismtest', 'prismtest')

api_url = "https://localhost:888/api/identity"
token_url = 'https://localhost:888/token'

headers =  {"Content-Type":"application/json"}
auth_headers =  {
                 'Authorization': 'UserName: "INHYDL08743\\prismtest", Password: "prismtest"'
                }

# first getting user guid
user_response = requests.post(api_url, auth = basic, verify = False)
user_guid_json = user_response.json()
print('UserGuid: ', user_guid_json.get('UserGuid'))

# getting token
input_token_data = { "username" : user_guid_json.get('UserGuid')
                     ,"grant_type" : "password"
                     ,"client_id"  : "prism-api"
                     ,"client_secret": "12c40d7162f452117bf5f71b112fdc96"
                   }
token_response = requests.get(token_url, data=input_token_data, headers= headers, verify=False)
print(token_response.json())
