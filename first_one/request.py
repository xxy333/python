
import requests

data = {"name": "John", "age": 30}  # Data, která chcete poslat na server
response = requests.post('http://localhost:5000/save_data', json=data)  # Provolání endpointu s POST požadavkem
print(response.text)  # Vytiskne odpověď z serveru
