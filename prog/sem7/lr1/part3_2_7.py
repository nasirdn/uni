import threading
import time
import random


def server_task(barrier):
    print("[Сервер] Готовлюсь к приему запросов...")
    time.sleep(random.uniform(1, 3))  # Имитация подготовки сервера
    print("[Сервер] Готов к приему запросов!")
    barrier.wait()  # Ожидаем клиента

    # Сервер готов обрабатывать запросы
    print("[Сервер] Обрабатываю запросы...")
    for i in range(3):
        time.sleep(0.5)
        print(f"[Сервер] Обработан запрос {i + 1}")

    print("[Сервер] Завершил работу.")


def client_task(barrier):
    print("[Клиент] Ожидаю готовности сервера...")
    barrier.wait()  # Ожидаем готовности сервера

    # Клиент отправляет запросы
    print("[Клиент] Сервер готов! Отправляю запросы...")
    for i in range(3):
        time.sleep(0.3)
        print(f"[Клиент] Отправлен запрос {i + 1}")

    print("[Клиент] Все запросы отправлены.")


def main_barrier():
    # Создаем барьер на 2 потока (сервер и клиент)
    barrier = threading.Barrier(2)

    # Создаем и запускаем потоки
    server_thread = threading.Thread(target=server_task, args=(barrier,))
    client_thread = threading.Thread(target=client_task, args=(barrier,))

    server_thread.start()
    time.sleep(0.1)  # Небольшая задержка для порядка вывода
    client_thread.start()

    # Ожидаем завершения потоков
    server_thread.join()
    client_thread.join()

    print("\n[Система] Все операции завершены.")


if __name__ == "__main__":
    main_barrier()