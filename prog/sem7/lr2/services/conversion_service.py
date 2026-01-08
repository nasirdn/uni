import logging
from typing import Dict
from datetime import datetime

logger = logging.getLogger(__name__)


class ConversionService:
    def __init__(self, currency_service=None):
        self.currency_service = currency_service

    def convert(self, amount: float, from_currency: str, to_currency: str) -> Dict:
        """
        Конвертация суммы из одной валюты в другую
        """
        try:
            # Получаем курсы валют
            if self.currency_service:
                rates = self.currency_service.get_exchange_rates(from_currency)
            else:
                # Используем локальный экземпляр если не передан
                from services.currency_service import CurrencyService
                currency_service = CurrencyService()
                rates = currency_service.get_exchange_rates(from_currency)

            # Проверяем наличие целевой валюты в курсах
            if to_currency not in rates:
                raise ValueError(f"Currency {to_currency} not available")

            # Получаем курс конвертации
            rate = rates[to_currency]

            # Вычисляем результат
            converted_amount = amount * rate

            # Форматируем результат
            return {
                'from_amount': amount,
                'from_currency': from_currency,
                'to_amount': round(converted_amount, 2),
                'to_currency': to_currency,
                'exchange_rate': round(rate, 6),
                'timestamp': datetime.now().isoformat(),
                'calculation': f"{amount} {from_currency} × {rate} = {converted_amount:.2f} {to_currency}"
            }

        except ValueError as e:
            raise e
        except Exception as e:
            logger.error(f"Conversion error: {e}")
            raise Exception(f"Conversion failed: {str(e)}")

    def health_check(self) -> Dict:
        """Проверка работоспособности сервиса"""
        try:
            # Тестовая конвертация
            result = self.convert(100, 'USD', 'EUR')
            return {
                'status': 'healthy',
                'test_conversion_successful': 'to_amount' in result
            }
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e)
            }