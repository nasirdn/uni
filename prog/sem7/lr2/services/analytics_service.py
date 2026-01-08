import sqlite3
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import io
import base64

logger = logging.getLogger(__name__)


class AnalyticsService:
    def __init__(self, db_path='conversions.db'):
        self.db_path = db_path
        self._init_database()

    def _init_database(self):
        """Инициализация базы данных"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Таблица истории конвертаций
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    from_currency TEXT NOT NULL,
                    to_currency TEXT NOT NULL,
                    result_amount REAL NOT NULL,
                    exchange_rate REAL NOT NULL,
                    timestamp DATETIME NOT NULL,
                    user_ip TEXT,
                    user_agent TEXT
                )
            ''')

            # Таблица запросов курсов
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rate_requests (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    base_currency TEXT NOT NULL,
                    target_currency TEXT NOT NULL,
                    rate REAL NOT NULL,
                    timestamp DATETIME NOT NULL
                )
            ''')

            # Индексы для ускорения запросов
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_conversions_timestamp ON conversions(timestamp)')
            cursor.execute(
                'CREATE INDEX IF NOT EXISTS idx_conversions_currency_pair ON conversions(from_currency, to_currency)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_rate_requests_timestamp ON rate_requests(timestamp)')

            conn.commit()
            conn.close()

            logger.info("Database initialized successfully")

        except Exception as e:
            logger.error(f"Database initialization error: {e}")

    def log_conversion(self, conversion_data: Dict):
        """
        Логирование операции конвертации
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO conversions 
                (amount, from_currency, to_currency, result_amount, exchange_rate, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                conversion_data['amount'],
                conversion_data['from'],
                conversion_data['to'],
                conversion_data['result']['to_amount'],
                conversion_data['result']['exchange_rate'],
                conversion_data['timestamp']
            ))

            conn.commit()
            conn.close()

        except Exception as e:
            logger.error(f"Error logging conversion: {e}")

    def get_conversion_statistics(self) -> Dict:
        """
        Получение статистики по конвертациям
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Самые популярные валютные пары
            cursor.execute('''
                SELECT from_currency, to_currency, COUNT(*) as count
                FROM conversions
                GROUP BY from_currency, to_currency
                ORDER BY count DESC
                LIMIT 10
            ''')
            popular_pairs = cursor.fetchall()

            # Общее количество конвертаций
            cursor.execute('SELECT COUNT(*) FROM conversions')
            total_conversions = cursor.fetchone()[0]

            # Конвертации за последние 24 часа
            cursor.execute('''
                SELECT COUNT(*) FROM conversions 
                WHERE timestamp > datetime('now', '-1 day')
            ''')
            last_24h = cursor.fetchone()[0]

            # Самые крупные конвертации
            cursor.execute('''
                            SELECT from_currency, to_currency, amount, result_amount
                            FROM conversions
                            ORDER BY amount DESC
                            LIMIT 5
                        ''')
            largest_conversions = cursor.fetchall()

            conn.close()

            return {
                'total_conversions': total_conversions,
                'last_24h_conversions': last_24h,
                'popular_currency_pairs': [
                    {
                        'from': pair[0],
                        'to': pair[1],
                        'count': pair[2]
                    }
                    for pair in popular_pairs
                ],
                'largest_conversions': [
                    {
                        'from': conv[0],
                        'to': conv[1],
                        'amount': conv[2],
                        'result': conv[3]
                    }
                    for conv in largest_conversions
                ],
                'timestamp': datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"Error getting statistics: {e}")
            return {'error': str(e)}

        def get_rate_history(self, base_currency: str, target_currency: str,
                             days: int = 30) -> Dict:
            """
            Получение истории курсов валют
            В реальном приложении здесь был бы запрос к историческим данным API
            """
            # Для демонстрации генерируем синтетические данные
            import random
            from datetime import datetime, timedelta

            history = []
            start_date = datetime.now() - timedelta(days=days)

            # Базовый курс (для демонстрации)
            base_rate = random.uniform(0.8, 0.9) if target_currency == 'EUR' else random.uniform(100, 120)

            for i in range(days):
                date = start_date + timedelta(days=i)

                # Добавляем некоторую случайность к курсу
                fluctuation = random.uniform(-0.02, 0.02)
                rate = base_rate * (1 + fluctuation)

                history.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'rate': round(rate, 4),
                    'base': base_currency,
                    'target': target_currency
                })

            # Генерация графика (опционально)
            chart_image = self._generate_rate_chart(history, base_currency, target_currency)

            return {
                'base_currency': base_currency,
                'target_currency': target_currency,
                'period_days': days,
                'history': history,
                'chart_image': chart_image,
                'statistics': self._calculate_history_stats(history)
            }

        def _generate_rate_chart(self, history: List[Dict],
                                 base_currency: str, target_currency: str) -> Optional[str]:
            """
            Генерация графика изменения курса
            """
            try:
                dates = [item['date'] for item in history]
                rates = [item['rate'] for item in history]

                plt.figure(figsize=(10, 6))
                plt.plot(dates, rates, marker='o', linestyle='-', linewidth=2, markersize=4)
                plt.title(f'Exchange Rate: {base_currency} to {target_currency}')
                plt.xlabel('Date')
                plt.ylabel(f'Rate ({target_currency} per {base_currency})')
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                plt.tight_layout()

                # Сохраняем в буфер
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)

                # Конвертируем в base64
                img_str = base64.b64encode(buf.read()).decode('utf-8')
                plt.close()

                return f"data:image/png;base64,{img_str}"

            except Exception as e:
                logger.error(f"Error generating chart: {e}")
                return None

            def _calculate_history_stats(self, history: List[Dict]) -> Dict:
                """Расчет статистики по истории"""
                if not history:
                    return {}

                rates = [item['rate'] for item in history]

                return {
                    'min_rate': min(rates),
                    'max_rate': max(rates),
                    'average_rate': sum(rates) / len(rates),
                    'current_rate': rates[-1],
                    'change_percentage': ((rates[-1] - rates[0]) / rates[0]) * 100
                }

            def health_check(self) -> Dict:
                """Проверка работоспособности сервиса"""
                try:
                    conn = sqlite3.connect(self.db_path)
                    cursor = conn.cursor()
                    cursor.execute('SELECT COUNT(*) FROM conversions')
                    count = cursor.fetchone()[0]
                    conn.close()

                    return {
                        'status': 'healthy',
                        'database_connected': True,
                        'total_records': count
                    }
                except Exception as e:
                    return {
                        'status': 'unhealthy',
                        'error': str(e)
                    }