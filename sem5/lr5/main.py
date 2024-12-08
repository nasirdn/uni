import requests
from xml.etree import ElementTree as ET
import time
import matplotlib.pyplot as plt

class SingletonMeta(type):
    """
    Метакласс для реализации шаблом Одиночка (Singleton) ля классов,
    использующих его как метакласс.

            Атрибуты:
        _instances (dict): Словарь для хранения экземпляров классов,
    использующих SingletomMetaкак метакласс.

            Методы:
        __call__(cls, *args, **kwargs): Метод, переопределяющий магический
    метод __call__ у классов-наследников.
    Проверяет, существуует ли экземпляр класса в словаре _instances.
    Если не существует, создает новый экземпляр класса и помещает его в словарь.
    В противном случае, возвращает экземпляр класса из словоря.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class CurrencyRates(metaclass=SingletonMeta):
    """
    Класс для получения и визуализации курсов валют из ЦБ РФ.
    Использует паттерн Одиночка (Singleton), чтобы гарантировать, что
    существует только один экземпляр CurrencyRates.
    Получает данные о курсах валют с API ЦБ РФ и предоставляет методы
    их извлечения и визуализации.

            Атрибуты:
    url (str): URL API ЦБ РФ для получения ежедневных курсов валют.
    rates (list): Список для хранения полученных курсов валют.
    last_request_time (float): Время последнего запроса к API для
    предотвращения частых вызовов.
    """

    def __init__(self):
        self.url = "http://www.cbr.ru/scripts/XML_daily.asp"
        self.rates = []
        self.last_request_time = 0

    def get_rates(self, codes_list):
        """
        Получает курсы валют для указанного списка идентификаторов валют.
        Делает запрос к API ЦБ РФ, чтобы получить текущий курс валют.
        Проверяет каждый идентификатор валюты в предоставленном списке,
        и если ID не найден, добавляет словарь с этим идентификатором и
        значением None.
        :param codes_list:(list) Список идентификаторов валют для получения курсов.
        :return: list: Список словарей, содержащих коды валют и соответствующие
        курсы или None, если не найдено.
        :exception: Если запрос к API не удался или если запросы выполняются
        слишком часто.
        """

        current_time = time.time()
        if current_time - self.last_request_time < 1:
            raise Exception("Слишком частый запрос. Пожалуйста, подождите.")

        response = requests.get(self.url)
        if response.status_code == 200:
            self.last_request_time = current_time
            root = ET.fromstring(response.content)
            self.rates = []

            found_codes = set()

            for item in root.findall('Valute'):
                v_id = item.get('ID')
                if v_id in codes_list:
                    code = item.find('CharCode').text
                    name = item.find('Name').text
                    value = item.find('Value').text.replace(',', '.')
                    nominal = int(item.find('Nominal').text)
                    whole, fractions = value.split('.')
                    self.rates.append({code: (name, (whole, fractions), nominal)})
                    found_codes.add(v_id)

            for code in codes_list:
                if code not in found_codes:
                    self.rates.append({code: None})

            return self.rates

        else:
            raise Exception("Ошибка при получении данных.")

    def visual_rates(self):
        """
        Визуализирует полученные курсы валют в виде столбчатой диаграммы.

        Фильтрует значения курсов, которые равны None, и
        создает столбчатую диаграмму с использованием Matplotlib.
        Диаграмма отображает действительные курсы валют в рублях.

        Диаграмма сохраняется как 'currencies.jpg' в текущем рабочем каталоге.
        """

        plt.figure(figsize=(10, 6))

        valid_rates = [rate for rate in self.rates if rate[list(rate.keys())[0]] is not None]
        list_rates = [list(rate.keys())[0] for rate in valid_rates]
        list_value = [float(rate[list(rate.keys())[0]][1][0]) for rate in valid_rates]

        plt.bar(list_rates, list_value, color='skyblue')
        plt.title('Курсы валют в рублях')
        plt.xlabel('Валюты')
        plt.ylabel('Курс (в рублях)')
        plt.grid(axis='y')
        plt.savefig('currencies.jpg')
        plt.close()

if __name__ == '__main__':
    currency_rates = CurrencyRates()
    result = currency_rates.get_rates(["R01035", "R01020A", "R01700J"]) #R01035
    print(result)
    currency_rates.visual_rates()