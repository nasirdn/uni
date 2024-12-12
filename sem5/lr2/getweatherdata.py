import json
import requests

def get_offset(tz):
    timezone = tz // 3600
    return f"UTC{'+' if timezone >= 0 else ''}{timezone}"


def get_weather_data(place, api_key=None):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric'
    res_data = requests.get(url).json()

    data = {
        'name': res_data['name'],
        'country': res_data['sys']['country'],
        'coord': {
            'lon': res_data['coord']['lon'],
            'lat': res_data['coord']['lat']
        },
        'timezone': get_offset(res_data['timezone']),
        'temperature': res_data['main']['temp'],
        'feels_like': res_data['main']['feels_like']
    }

    json_data = json.dumps(data, indent=4)
    print(json_data)


