from .own_key import key
from .getweatherdata import get_weather_data

def main():
    city = input('Введите город на английском: ')
    get_weather_data(city, key)

if __name__ == '__main__':
    main()