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



url = (f"{HOST}/clients/as-array")

payload = json.dumps([
    {
    "firstName": "Daniil2",
    "lastName": "Bukarev",
    "middleName": "Maksimovich",
    "sex": "MAN",
    "phoneNumber": "8777889843614922",
    "birthday": "2024-10-25T11:20:43.645Z",
    "active": True,
    "identifiers": [
        0
]
},
    {
    "firstName": "Daniil1",
    "lastName": "Bukarev",
    "middleName": "Maksimovich",
    "sex": "MAN",
    "phoneNumber": "8777889843614911",
    "birthday": "2024-10-25T11:20:43.645Z",
    "active": True,
    "identifiers": [
        0
]
}
])
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {token}'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
print(response.status_code)
