import requests
import pip._vendor.requests 

BASE_URL = "http://127.0.0.1:5000/"


response = requests.get(BASE_URL + "/Mayday_Parade")
print(response.text)

response = requests.get(BASE_URL + "/Blue_Öyster_Cult")
print(response.text)

response = requests.get(BASE_URL + "/Britney_Spears")
print(response.text)

response = requests.get(BASE_URL + "/Aerosmith")
print(response.text)