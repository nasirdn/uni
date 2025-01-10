import unittest
from unittest.mock import patch, MagicMock
import json
from main import CurrencyRates, ConcreteDecoratorJSON


class MyTestCase(unittest.TestCase):

    def test_json_decorator(self):
        currency_rates = CurrencyRates()
        currency_rates.rates = [
            {'AZN': {'name': 'Азербайджанский манат', 'value': '59.9498', 'nominal': 1}},
            {'GBP': {'name': 'Фунт стерлингов', 'value': '125.3855', 'nominal': 1}}
        ]
        json_decorator = ConcreteDecoratorJSON(currency_rates)
        json_result = json_decorator.get_rates(["R01035", "R01020A"])

        expected_json = json.dumps([
            {
                'AZN': {
                    'name': 'Азербайджанский манат',
                    'value': '59.9498',
                    'nominal': 1
                }
            },
            {
                'GBP': {
                    'name': 'Фунт стерлингов',
                    'value': '125.3855',
                    'nominal': 1
                }
            }
        ], ensure_ascii=False, indent=4)

        self.assertEqual(json_result, expected_json)

    @patch('requests.get')
    def test_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500

        mock_get.return_value = mock_response
        currency_rates = CurrencyRates()
        with self.assertRaises(Exception) as context:
            currency_rates.get_rates(["R01035"])

        self.assertEqual(str(context.exception), "Ошибка при получении данных.")


if __name__ == '__main__':
    unittest.main()
