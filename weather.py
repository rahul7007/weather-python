import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=f196e1c1651f97563f531c7f465d8252&q='
city = input("Enter City Name : ")
url = api_address+city
json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']
print(formatted_data)