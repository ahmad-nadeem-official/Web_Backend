import requests

url = 'http://127.0.0.1:5000/subscribe'
data = {
    'email': 'test@example.com'
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
