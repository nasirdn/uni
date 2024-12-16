from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import requests
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    """
    Определяет маршрут для главной страницы приложения.

    :return: Основной интерфейс, в котором пользователи могут выбрать валюту
            для мониторинга.
    """
    return render_template('index.html')

# Словарь для отслеживания подключенных клиентов и их выбранных валют
observers = {}

def get_currency_rates():
    """
    Извлекает текущие курсы валют.

    Отправляет запрос GET к конечной точке API Центрального банка России,
    которая предоставляет ежедневные данные о валюте в формате JSON.

    :return: Обработанный JSON-ответ, содержащий информацию о валютах.
    """
    return requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

def currency_updater():
    """
    Постоянно проверяет наличие обновлений курсов валют и уведомляет
    подключенных клиентов.

    Функция проверяет, доступна ли выбранная валюта в полученных данных.
    Если валюта найдена, отправляется событие обновления с текущим и
    предыдущим курсами выбранной валюты.

    Приостанавливается на 5 секунд, прежде чем повторить процесс,
    позволяя выполнять периодические обновления.
    """
    while True:
        # Получение актуальных курсов валют
        data = get_currency_rates()
        for sid, (currency_code) in observers.items(): # Перебор всех подключенных клиентов
            if currency_code in data['Valute']:
                currency_info = data['Valute'][currency_code] # Получение информации о валюте
                socketio.emit('update', {
                    'currency_code': currency_code,
                    'current_rate': currency_info['Value'],
                    'previous_rate': currency_info['Previous']
                }, room=sid) # Отправка обновления конкретному клиенту
        time.sleep(5) # Задержка перед следующим обновлением

@socketio.on('connect')
def handle_connect():
    """
    Обрабатывает новое подключение клиента через WebSocket.

    При подключении клиента отправляет сообщение о успешном соединении
    и уникальный идентификатор клиента.
    """
    sid = request.sid # Получение уникального идентификатора клиента
    emit('connected', {'message': 'Connected', 'id': sid}) # Уведомление клиента о подключении

@socketio.on('select_currency')
def handle_select_currency(data):
    """
    Обрабатывает запрос клиента на выбор валюты.

    Сохраняет выбранный код валюты в словаре observers и отправляет
    уведомление клиенту о том, что валюта выбрана.

    :param data: Данные, содержащие код выбранной валюты.
    """
    currency_code = data.get('currency_code')
    observers[request.sid] = currency_code
    print(f"Клиент {request.sid} подключился и выбрал валюту: {currency_code}")
    emit('currency_selected', {'message': f'You selected {currency_code}', 'id': request.sid}) # Уведомление клиента

@socketio.on('disconnect')
def handle_disconnect():
    """
    Обрабатывает отключение клиента.

    Удаляет клиента из словаря observers и выводит сообщение о
    его отключении в консоль.
    """
    sid = request.sid # Получение уникального идентификатора клиента
    if sid in observers: # Проверка, есть ли клиент в словаре
        print(f"Клиент {sid} отключился") # Логирование отключения клиента
        del observers[sid] # Удаление клиента из словаря

if __name__ == "__main__":
    # Запуск потока для обновления курсов валют в фоновом режиме
    threading.Thread(target=currency_updater, daemon=True).start()
    # Запуск приложения с использованием SocketIO
    socketio.run(app, host='localhost', port=5000, allow_unsafe_werkzeug=True)