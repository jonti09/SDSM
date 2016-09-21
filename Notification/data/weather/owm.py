import pyowm


def get_weather():
    try:
        owm = pyowm.OWM('7e9465e06a4071881e4eeba3e4027967')
        forecast = owm.weather_at_place('Gujarat,in').get_weather()
        temp = forecast.get_temperature('celsius')
        return str(temp['temp_max'])

    except:
        pass
