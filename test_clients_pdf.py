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
print(response.text.split("\"")[3])

print(response.status_code)

def test_clients_pdf():
  url = (f"{HOST}/clients/pdf"
   #      f"?sortBy=<string>"
    #     f"&sortOrder=<string>"
    #     f"&startBirthdayDate=<string>"
    #     f"&endBirthdayDate=<string>"
    #     f"&searchText=<string>"
         f"&sex=WOMAN"
       #  f"&page=<integer>"
    #     f"&pageSize=<integer>"
         #f"&active=<boolean>"
         )

  payload = json.dumps({ })
  headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  print(response.text)
  print(response.status_code)