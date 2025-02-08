from flask import Flask, render_template, request
from weather import get_city
from waitress import serve
import os
app= Flask(__name__,)
@app.route('/')
@app.route("/index")
def index():
    #print(os.listdir("templates"))  # List files in the templates folder
    return render_template("index.html")
@app.route("/weather")
def get_weather():
    city=request.args.get('city')
    #empty spaces
    if not bool(city.strip()):
        city="Kigali"
    weather_app=get_city(city)
    #if not found
    if not weather_app["cod"]==200:
        return render_template("city_not_found.html")
    return render_template("weather.html",title=weather_app["name"],status=weather_app["weather"][0]["description"].capitalize(),
                           temp=f"{weather_app['main']['temp']:.1f}",
                           feels_like=f"{weather_app['main']['feels_like']:.1f}"
                           )
if __name__=="__main__":
    serve(app,host="0.0.0.0", port=8000)
