import os
import threading
import fnmatch
import time


class ParallelFileSearcher:
    def __init__(self, pattern, search_path, num_threads=4):
        self.pattern = pattern
        self.search_path = search_path
        self.num_threads = num_threads
        self.found = False
        self.found_lock = threading.Lock()
        self.found_file = None
        self.threads = []
        self.stop_event = threading.Event()

    def search_in_chunk(self, file_chunk, thread_id):
        """Поиск файла в своем фрагменте"""
        print(f"[Поток {thread_id}] Начинаю поиск в {len(file_chunk)} файлах...")

        for filename in file_chunk:
            # Проверяем, не нашли ли уже файл в другом потоке
            if self.stop_event.is_set():
                print(f"[Поток {thread_id}] Поиск прерван - файл уже найден")
                return

            # Проверяем соответствие паттерну
            if fnmatch.fnmatch(filename, self.pattern):
                with self.found_lock:
                    if not self.found:  # Двойная проверка
                        self.found = True
                        self.found_file = os.path.join(self.search_path, filename)
                        self.stop_event.set()  # Сигнализируем всем потокам остановиться
                        print(f"[Поток {thread_id}] Найден файл: {filename}")
                        return

        print(f"[Поток {thread_id}] Поиск завершен, файл не найден")

    def split_files(self, all_files):
        """Разделение файлов на чанки для потоков"""
        chunk_size = len(all_files) // self.num_threads
        chunks = []

        for i in range(self.num_threads):
            start = i * chunk_size
            # Для последнего потока берем все оставшиеся файлы
            end = start + chunk_size if i < self.num_threads - 1 else len(all_files)
            chunks.append(all_files[start:end])

        return chunks

    def search(self):
        """Основной метод поиска"""
        # Получаем список всех файлов в директории
        try:
            all_files = os.listdir(self.search_path)
        except FileNotFoundError:
            print(f"Директория {self.search_path} не найдена")
            return None

        print(f"Найдено {len(all_files)} файлов для поиска")

        # Разделяем файлы между потоками
        file_chunks = self.split_files(all_files)

        # Создаем и запускаем потоки
        for i in range(self.num_threads):
            thread = threading.Thread(
                target=self.search_in_chunk,
                args=(file_chunks[i], i + 1)
            )
            self.threads.append(thread)
            thread.start()

        # Ожидаем завершения всех потоков
        for thread in self.threads:
            thread.join()

        # Выводим результат
        if self.found:
            print(f"\n[Результат] Файл найден: {self.found_file}")
            return self.found_file
        else:
            print(f"\n[Результат] Файл с паттерном '{self.pattern}' не найден")
            return None


def create_test_files(directory, num_files=20):
    """Создание тестовых файлов для демонстрации"""
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Создаем тестовые файлы
    for i in range(num_files):
        filename = f"test_file_{i}.txt" if i != 5 else "target_file.txt"
        with open(os.path.join(directory, filename), 'w') as f:
            f.write(f"Содержимое файла {filename}")

    print(f"Создано {num_files} тестовых файлов в {directory}")


def main_search():
    # Настройки поиска
    search_directory = "./test_search"
    file_pattern = "target*.txt"  # Ищем файлы, начинающиеся с "target"
    num_threads = 4

    # Создаем тестовые файлы
    create_test_files(search_directory)

    print("\n" + "=" * 50)
    print(f"Начинаем параллельный поиск файла с паттерном '{file_pattern}'")
    print("=" * 50 + "\n")

    # Создаем и запускаем поиск
    searcher = ParallelFileSearcher(file_pattern, search_directory, num_threads)
    start_time = time.time()
    result = searcher.search()
    elapsed_time = time.time() - start_time

    print(f"\nВремя поиска: {elapsed_time:.3f} секунд")

    # Дополнительный тест: поиск несуществующего файла
    print("\n" + "=" * 50)
    print("Тест 2: Поиск несуществующего файла")
    print("=" * 50 + "\n")

    searcher2 = ParallelFileSearcher("nonexistent*.txt", search_directory, 2)
    result2 = searcher2.search()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("=" * 60)
    main_search()