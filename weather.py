from dotenv import load_dotenv
from pprint import pprint
import requests
import os
load_dotenv()

def get_city(city='Kigali city'):
    request_url= f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_Key")}&q={city}&units=metric'
    weather_app=requests.get(request_url).json()
    #print(weather_app)
    return weather_app

if __name__=="__main__":
    print("\nGet our conditions")
    city=input("\nPut the city name: ")
    #empty spaces
    if not bool(city.strip()):
        city="Kigali"
    weather_app=get_city(city)
    print("\n")
    pprint(weather_app)    