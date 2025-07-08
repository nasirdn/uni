import functools
import sys
from typing import Union, TextIO
import json
import sqlite3
from datetime import datetime
from collections import Counter

FILE = 'logdata.json'
DB_FILE = 'logs.db'

def trace(func=None, *, handle=sys.stdout):

    if func is None:
        return lambda func: trace(func, handle=handle)

    if handle == 'fp':
        log_data = []

    elif handle == 'db':
        conn = sqlite3.connect(DB_FILE)
        cur = conn.cursor()
        try:
            cur.execute('CREATE TABLE logs (datetime TEXT, func_name TEXT, params TEXT, result TEXT)')
        except sqlite3.OperationalError as e:
            print(f"Ошибка создания таблицы в БД: {e}")

    @functools.wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)

        log_entry = {
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'func_name': f'{func.__name__}()',
            'params': args,
            'result': result
        }

        if handle == sys.stdout:
            print(log_entry)
        elif handle == 'logdata':
            with open(FILE, 'a') as fp:
                json.dump([log_entry], fp, indent=2)
                fp.write('\n')
        elif handle == 'fp':
            log_data.append(log_entry)
        elif handle == 'db':
            try:
                conn = sqlite3.connect(DB_FILE)
                cur = conn.cursor()
                cur.execute('INSERT INTO logs VALUES (?, ?, ?, ?)',
                            (log_entry['datetime'],
                             log_entry['func_name'],
                             json.dumps(log_entry['params']),
                             str(log_entry['result'])))
                conn.commit()
                conn.close()
            except sqlite3.OperationalError as e:
                print(f"Ошибка добавления данных в таблицу: {e}")

        return result

    if handle == 'fp':
        def save_to_file():
            with open(FILE, 'a') as fp:
                for log_entry in log_data:
                    json.dump([log_entry], fp, indent=2)
                    fp.write('\n')

        inner.save_to_file = save_to_file

    return inner


def sql3_util_printer():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT * FROM logs')
    log = cur.fetchall()

    if not log:
        print("В базе данных нет записей")
    else:
        for row in log:
            print({
                'datetime': row[0],
                'func_name': row[1],
                'params': json.loads(row[2]) if row[2] else None,
                'result': row[3]
            })
    conn.close()

@trace
def f1(args: Union[list, tuple]) -> int:
    return sum(args)

@trace(handle='fp')
def f2(text: str) -> str:
    return text[::-1]

@trace(handle='db')
def f3(data: list) -> dict:
    counter = Counter(data)
    return dict(counter)


f1([1, 2, 3, 4, 5, 6])
f2('DORIAN')
f3([1, 2, 3, 1, 2, 3, 4, 5])

print("\nЛоги из БД:")
sql3_util_printer()

f2.save_to_file()
