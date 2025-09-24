'''Закаблукова Анастасия Эдуардовна 2 курс, ИВТ-1.1'''
'''Комплект 2. Задание 2.2'''

import requests
from bs4 import BeautifulSoup

# URL для получения погоды
location = 'London'
url = f'https://wttr.in/{location}'

try:
    # Получение данных с сайта
    response = requests.get(url)
    response.raise_for_status()  # Проверка на ошибки

    # Парсинг HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлечение информации о погоде
    weather_info = soup.find('div', class_='weather')
    if weather_info:
        print(weather_info.text.strip())
    else:
        print("Не удалось найти информацию о погоде.")

except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка при запросе: {e}")
