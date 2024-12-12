from own_my_key import key
from getweatherdata import get_weather_data

if __name__ == '__main__':
    city = input('Введите город на английском: ')
    get_weather_data(city, key)
