#Комплекс 1. Задание 1.4
# Закаблукова Анастасия Эдуардовна. 2 курс, ИВТ-1.1

def find_country(city_list, countries):
    city_country_map = {}

    '''Создаем словарь, где ключ - название города, значение - название страны'''
    for country, cities in countries.items():
        for city in cities:
            city_country_map[city] = country

    '''Проверяем для каждого города, в какой стране он находится'''
    result = {}
    for city in city_list:
        if city in city_country_map:
            result[city] = city_country_map[city]
        else:
            result[city] = "Unknown"

    return result

city_list = ['Saint Petersburg', 'Paris', 'Tokyo', 'Seoul'] #Список городов
countries = {
    'Russia': ['Moscow', 'Saint Petersburg'],
    'South Korea' : ['Seoul', 'Incheon'],
    'France': ['Paris', 'Nice'],
    'Japan': ['Tokyo', 'Osaka']
} #Словарь, где ключами являются названия стран, а значениями - список городов для каждой страны

result = find_country(city_list, countries)

# Выводим результат
for city, country in result.items():
    print(f"Город {city} находится в {country}.")