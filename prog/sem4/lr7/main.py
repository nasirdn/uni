import sqlite3
import datetime
from typing import List, Dict, Optional

def connect_to_db(path_to_db: str = "counter.db") -> sqlite3.Connection:
    conn = None
    try:
        print('Подключение к БД')
        conn = sqlite3.connect(path_to_db)
        print("Connection is established")
    except sqlite3.Error as e:
        print("Error:", e)
    return conn

def db_table_create(conn: sqlite3.Connection, query: str) -> None:
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print("Error creating table:", e)

def create_data(conn: sqlite3.Connection, data: List[Dict]) -> None:
    try:
        cur = conn.cursor()
        cur.executemany(
            "INSERT INTO counter VALUES(NULL, :value, :created)",
            data
        )
        conn.commit()
    except sqlite3.Error as e:
        print("Error inserting data:", e)

def read_data(conn: sqlite3.Connection, query: str) -> None:
    try:
        read_result = conn.execute(query)
        for _row in read_result:
            print(_row)
    except sqlite3.Error as e:
        print("Error reading data:", e)

def update_data(conn: sqlite3.Connection, query: str) -> None:
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print("Error updating data:", e)

def delete_data(conn: sqlite3.Connection, query: str) -> None:
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting data:", e)

class Counter:
    def __init__(self, db_conn: Optional[sqlite3.Connection] = None):
        self.count = 0
        self.conn = db_conn
        if self.conn:
            self._init_db()

    def _init_db(self) -> None:
        db_table_create(
            self.conn,
            "CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY AUTOINCREMENT, value INT, created DATETIME);"
        )

    def increment(self) -> None:
        self.count += 1
        self._save_to_db()

    def decrement(self) -> None:
        self.count -= 1
        self._save_to_db()

    def reset(self) -> None:
        self.count = 0
        self._save_to_db()

    def _save_to_db(self) -> None:
        if self.conn:
            data = [{"value": self.count, "created": datetime.datetime.now()}]
            create_data(self.conn, data)

    def get_history(self) -> None:
        if self.conn:
            print("History from database:")
            read_data(self.conn, "SELECT * FROM counter ORDER BY created DESC")


def main():
    # Подключение к реальной БД (не in-memory)
    conn = connect_to_db("counter.db")

    # Инициализация счетчика с подключением к БД
    counter = Counter(conn)

    # Тестирование методов счетчика
    print("Current count:", counter.count)
    counter.increment()
    print("After increment:", counter.count)
    counter.increment()
    print("After increment:", counter.count)
    counter.decrement()
    print("After decrement:", counter.count)
    counter.reset()
    print("After reset:", counter.count)

    # Просмотр истории изменений
    counter.get_history()

    # Дополнительные тесты с прямым доступом к БД
    input("\nPause. Press Enter to continue...")

    # Создание дополнительных данных
    test_data = [
        {"value": 10, "created": datetime.datetime.now() - datetime.timedelta(days=1)},
        {"value": 20, "created": datetime.datetime.now() - datetime.timedelta(hours=12)},
        {"value": 30, "created": datetime.datetime.now()}
    ]
    create_data(conn, test_data)

    # Чтение данных
    read_data(conn, "SELECT * FROM counter ORDER BY created DESC")

    # Обновление данных
    input("\nPause. Press Enter to update data...")
    cur_dt = datetime.datetime.now()
    update_data(conn, f"UPDATE counter SET value = 100 WHERE created < '{cur_dt}'")
    read_data(conn, "SELECT * FROM counter ORDER BY created DESC")

    # Удаление данных
    input("\nPause. Press Enter to delete some data...")
    delete_data(conn, "DELETE FROM counter WHERE value = 100")
    read_data(conn, "SELECT * FROM counter ORDER BY created DESC")

    conn.close()
    print("\nConnection closed")

if __name__ == '__main__':
    main()