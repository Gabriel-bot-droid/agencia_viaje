import requests
import random

# pedir JWT token
url = "http://localhost:8000/api/token/"
payload = {
    "username": "admin",
    "password": "admin123"
}
response = requests.post(url, json=payload)
creds = response.json()

headers = {

}

url = "http://localhost:8000/api/destinos/"

for i in range(11):
    #ip = f"192.168.{random.randint(0, 255)}.{i}"
    #headers["X-Forwarded-For"] = ip
    #headers["REMOTE_ADDR"] = ip
    
    response = requests.get(url) #, headers=headers
    print(response.status_code)
