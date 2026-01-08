import requests
import json
import time
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from utils.cache_manager import CacheManager

logger = logging.getLogger(__name__)


class CurrencyService:
    def __init__(self):
        self.cache = CacheManager()
        self.api_endpoints = {
            'ecb': 'https://api.exchangerate-api.com/v4/latest/',
            'open_exchange': 'https://openexchangerates.org/api/latest.json',
            'currency_api': 'https://freecurrencyapi.net/api/v2/latest'
        }
        self.api_keys = self._load_api_keys()
        self.currencies = self._load_currencies()

    def _load_api_keys(self) -> Dict:
        """Загрузка API ключей из окружения или файла"""
        # В реальном приложении используйте os.environ или секреты
        return {
            'open_exchange': 'your_api_key_here',  # Получите на openexchangerates.org
            'currency_api': 'your_api_key_here'  # Получите на freecurrencyapi.net
        }

    def _load_currencies(self) -> Dict:
        """Загрузка списка валют"""
        currencies = {
            'USD': 'United States Dollar',
            'EUR': 'Euro',
            'GBP': 'British Pound',
            'JPY': 'Japanese Yen',
            'CAD': 'Canadian Dollar',
            'AUD': 'Australian Dollar',
            'CHF': 'Swiss Franc',
            'CNY': 'Chinese Yuan',
            'RUB': 'Russian Ruble',
            'INR': 'Indian Rupee',
            'BRL': 'Brazilian Real',
            'MXN': 'Mexican Peso',
            'KRW': 'South Korean Won',
            'TRY': 'Turkish Lira',
            'ZAR': 'South African Rand',
            'SGD': 'Singapore Dollar',
            'NZD': 'New Zealand Dollar',
            'HKD': 'Hong Kong Dollar',
            'NOK': 'Norwegian Krone',
            'SEK': 'Swedish Krona',
            'DKK': 'Danish Krone',
            'PLN': 'Polish Zloty',
            'CZK': 'Czech Koruna',
            'HUF': 'Hungarian Forint',
            'RON': 'Romanian Leu',
            'IDR': 'Indonesian Rupiah',
            'THB': 'Thai Baht',
            'MYR': 'Malaysian Ringgit',
            'PHP': 'Philippine Peso',
        }
        return currencies

    def get_available_currencies(self) -> Dict:
        """Получение списка доступных валют"""
        return self.currencies

    def get_exchange_rates(self, base_currency: str = 'USD',
                           symbols: Optional[List[str]] = None) -> Dict:
        """
        Получение курсов валют
        """
        cache_key = f"rates_{base_currency}"

        # Проверка кэша
        cached_data = self.cache.get(cache_key)
        if cached_data:
            logger.info(f"Cache hit for {base_currency}")

            # Фильтрация по symbols если нужно
            if symbols:
                filtered_rates = {k: v for k, v in cached_data['rates'].items()
                                  if k in symbols}
                return filtered_rates
            return cached_data['rates']

        logger.info(f"Cache miss for {base_currency}, fetching from API")

        try:
            # Используем несколько источников для надежности
            rates = self._fetch_from_multiple_sources(base_currency)

            if not rates:
                raise Exception("Could not fetch exchange rates from any source")

            # Сохраняем в кэш на 1 час
            cache_data = {
                'rates': rates,
                'timestamp': datetime.now().isoformat(),
                'base': base_currency
            }
            self.cache.set(cache_key, cache_data, ttl=3600)

            # Фильтрация по symbols если нужно
            if symbols:
                filtered_rates = {k: v for k, v in rates.items() if k in symbols}
                return filtered_rates

            return rates

        except Exception as e:
            logger.error(f"Error fetching rates: {e}")
            # Возвращаем запасные данные если API недоступен
            return self._get_fallback_rates(base_currency)

        def _fetch_from_multiple_sources(self, base_currency: str) -> Dict:
            """Получение данных из нескольких источников"""
            rates = {}
            sources_used = []

            # 1. ECB API (бесплатный, не требует API ключа)
            try:
                response = requests.get(f"{self.api_endpoints['ecb']}{base_currency}",
                                        timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    rates.update(data.get('rates', {}))
                    sources_used.append('ecb')
                    logger.info(f"Successfully fetched from ECB API")
            except Exception as e:
                logger.warning(f"ECB API failed: {e}")

            # 2. Open Exchange Rates (требует API ключ)
            if self.api_keys.get('open_exchange'):
                try:
                    response = requests.get(
                        f"{self.api_endpoints['open_exchange']}",
                        params={'app_id': self.api_keys['open_exchange'],
                                'base': base_currency},
                        timeout=5
                    )
                    if response.status_code == 200:
                        data = response.json()
                        rates.update(data.get('rates', {}))
                        sources_used.append('open_exchange')
                        logger.info(f"Successfully fetched from Open Exchange")
                except Exception as e:
                    logger.warning(f"Open Exchange API failed: {e}")

            # Усредняем значения если получили из нескольких источников
            if len(sources_used) > 1:
                # В реальном приложении можно добавить логику усреднения
                pass

            return rates

        def _get_fallback_rates(self, base_currency: str) -> Dict:
            """Запасные данные на случай недоступности API"""
            # Статические курсы (для демонстрации)
            fallback_rates = {
                'USD': 1.0,
                'EUR': 0.85,
                'GBP': 0.73,
                'JPY': 110.0,
                'CAD': 1.25,
                'AUD': 1.35,
                'CHF': 0.92,
                'CNY': 6.45,
                'RUB': 75.0,
                'INR': 74.0,
            }

            # Конвертируем если нужна другая базовая валюта
            if base_currency != 'USD' and base_currency in fallback_rates:
                base_rate = fallback_rates[base_currency]
                converted_rates = {}
                for currency, rate in fallback_rates.items():
                    converted_rates[currency] = rate / base_rate
                return converted_rates

            return fallback_rates

        def health_check(self) -> Dict:
            """Проверка работоспособности сервиса"""
            try:
                rates = self.get_exchange_rates('USD', ['EUR', 'GBP'])
                return {
                    'status': 'healthy',
                    'sources_available': len(rates) > 0,
                    'cache_enabled': True
                }
            except Exception as e:
                return {
                    'status': 'unhealthy',
                    'error': str(e)
                }