import requests
import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_data(zip_code, country_code, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}".format(zip_code, country_code,
                                                                                         api_key)
    r = requests.get(api_url)
    # print(api_url)
    return r.json()
