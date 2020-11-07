import requests
import json

url = "http://192.168.1.18:8080/pessoas"

response = requests.get(url)
teste = response.json()

print(teste[0]["endereco"])