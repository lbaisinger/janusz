from flask import Flask, render_template
from weather_module import *

app = Flask('FullCalendar Demo')


@app.route('/')
def home():
    # return render_template('index.html')
    return "Home"


@app.route('/dashboard')
def dashboard():
    weather_data = get_weather_data('01219', 'de', get_api_key())
    # return render_template('calendar.html')


if __name__ == '__main__':
    app.run()
