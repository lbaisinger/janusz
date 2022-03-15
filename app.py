from flask import Flask, render_template, request
from weather_module import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard', methods=['POST'])
def dashboard():
    zip_code = request.form['zipCode']
    country_code = request.form['countryCode']
    api_key = get_api_key()
    weather_data = get_weather_data(zip_code, country_code, api_key)
    temperature = "{0:.2f}".format(weather_data['main']['temp'])
    temperature_feels_like = '{0:.2f}'.format(weather_data['main']['feels_like'])
    # todo add icon
    return render_template('dashboard.html',
                           temperature=temperature,
                           temperature_feels_like=temperature_feels_like)


if __name__ == '__main__':
    app.run()
