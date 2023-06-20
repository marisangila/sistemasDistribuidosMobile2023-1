import requests
import os

    #tempo
lat = input("Digite a latitude: ")
lon =  input("Digite a longitude: ")
API_Key = "f13452c6778ffcf945b9bb3f91d6e076"

url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"

response = requests.get(url)

if response.status_code == 200:

    resultado = response.json()


    print (resultado)
else:
  print(response.status_code)
  print(response.reason)