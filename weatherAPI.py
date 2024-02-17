import requests

api_key = "1e68aec1676454b5e769a80b0d0f182b"
input_By_User = input("Enter City: ")
data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={input_By_User}&units=imperial&APPID={api_key}")



if data.json()['cod']=='404':
    print("City not found")
else:
    weather = data.json()['weather'][0]['main']
    temperature = data.json()['main']['temp']
    print(f"The weather in {input_By_User} is : {weather}")
    print(f"The temperature in {input_By_User} is : {temperature} F ")