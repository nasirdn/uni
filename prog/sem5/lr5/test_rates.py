import unittest
from unittest.mock import patch, MagicMock
from main import CurrencyRates


class MyTestCase(unittest.TestCase):
    def test_singleton(self):
        instance1 = CurrencyRates()
        instance2 = CurrencyRates()
        self.assertIs(instance1, instance2)

    @patch('requests.get')
    def test_getrates(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = '''
        <ValCurs Date="11.01.2025" name="Foreign Currency Market">
            <Valute ID="R01010">
                <NumCode>036</NumCode>
                <CharCode>AUD</CharCode>
                <Nominal>1</Nominal>
                <Name>Австралийский доллар</Name>
                <Value>63,1259</Value>
                <VunitRate>63,1259</VunitRate>
            </Valute>
            <Valute ID="R01020A">
                <NumCode>944</NumCode>
                <CharCode>AZN</CharCode>
                <Nominal>1</Nominal>
                <Name>Азербайджанский манат</Name>
                <Value>59,9498</Value>
                <VunitRate>59,9498</VunitRate>
            </Valute>
        </ValCurs>
        '''

        mock_get.return_value = mock_response
        currency_rates = CurrencyRates()
        result = currency_rates.get_rates(["R01010", "R01020A", "R1234"])

        expected_data = [{
            'AUD': ('Австралийский доллар', ('63', '1259'), 1)},
            {'AZN': ('Азербайджанский манат', ('59', '9498'), 1)},
            {'R1234': None}
        ]
        self.assertEqual(result, expected_data)

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
