import json
import requests


def get_offset(tz):
    timezone = tz // 3600
    return f"UTC{'+' if timezone >= 0 else ''}{timezone}"


def get_weather_data(place, api_key=None):

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric')
    if response.status_code == 200:
        res_data = response.json()

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
        return (json_data)
    else:
        raise ValueError("Invalid city or API")


