import requests
import json

# Авторизация
HOST="http://192.168.25.137:9777/api/v1"

url = f"{HOST}/auth/token"

payload = json.dumps({
  "username": "admin",
  "password": "123"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

token=response.text.split("\"")[3]


url = (f"{HOST}/clients/by-identifier-id?identifierId=35")

payload = { }
headers = {
  'Accept': '*/*',
  'Authorization': f'Bearer {token}'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
print(response.status_code)
