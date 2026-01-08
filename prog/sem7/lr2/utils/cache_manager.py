import time
import threading
from typing import Any, Optional
import pickle


class CacheManager:
    def __init__(self, max_size=1000):
        self.cache = {}
        self.max_size = max_size
        self.lock = threading.RLock()

    def get(self, key: str) -> Optional[Any]:
        """Получение значения из кэша"""
        with self.lock:
            if key in self.cache:
                entry = self.cache[key]
                # Проверяем не истекло ли время жизни
                if entry['expiry'] > time.time():
                    return entry['value']
                else:
                    # Удаляем просроченную запись
                    del self.cache[key]
            return None

    def set(self, key: str, value: Any, ttl: int = 300):
        """Установка значения в кэш"""
        with self.lock:
            # Очищаем место если кэш переполнен
            if len(self.cache) >= self.max_size:
                self._evict_oldest()

            self.cache[key] = {
                'value': value,
                'expiry': time.time() + ttl,
                'created': time.time()
            }

    def delete(self, key: str):
        """Удаление значения из кэша"""
        with self.lock:
            if key in self.cache:
                del self.cache[key]

    def clear(self):
        """Очистка всего кэша"""
        with self.lock:
            self.cache.clear()

    def _evict_oldest(self):
        """Удаление самых старых записей (LRU)"""
        if not self.cache:
            return

        # Находим самую старую запись
        oldest_key = min(self.cache.keys(),
                         key=lambda k: self.cache[k]['created'])
        del self.cache[oldest_key]

    def get_stats(self):
        """Получение статистики кэша"""
        with self.lock:
            total_size = len(self.cache)
            expired_count = sum(1 for v in self.cache.values()
                                if v['expiry'] <= time.time())

            return {
                'total_entries': total_size,
                'expired_entries': expired_count,
                'max_size': self.max_size,
                'usage_percentage': (total_size / self.max_size) * 100
            }