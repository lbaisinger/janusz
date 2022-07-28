from flask import Flask, render_template, request
from weather_module import *
import os

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('home.html')


@app.route('/base')
def base():
    return render_template('base.html')

# , methods=['POST']
@app.route('/')
def bootstrap():
    # zip_code = request.form['zipCode']
    zip_code = '01219'
    # country_code = request.form['countryCode']
    country_code = 'de'
    api_key = get_api_key()
    weather_data = get_weather_data(zip_code, country_code, api_key)
    temperature_kelvin = "{0:.2f}".format(weather_data['main']['temp'])
    temperature_feels_like_kelvin = '{0:.2f}'.format(weather_data['main']['feels_like'])
    temperature = float(temperature_kelvin) - 273.15
    temperature_feels_like = float(temperature_feels_like_kelvin) - 273.15
    return render_template('bootstrap.html',
                           temperature="{:.1f}".format(temperature))


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))

