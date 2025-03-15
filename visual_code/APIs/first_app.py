import requests



data_send = {
    "name": "Vladimir",
    "email": "vlavon@gmail.com"
}


forward_url = ("http://localhost:8081/v1/send-data")
response = requests.post(forward_url, json=data_send)







