import requests
import json



def test_auto():
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

  print(response.text.split("\"")[3])
  print(response.status_code)