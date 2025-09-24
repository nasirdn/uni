import unittest
from unittest.mock import patch
import json
from own_my_key import key
from getweatherdata import get_weather_data, get_offset


class MyTestCase(unittest.TestCase):

    def test_utc_offset(self):
        self.assertEqual(get_offset(3600), 'UTC+1')
        self.assertEqual(get_offset(-7200), 'UTC-2')

    @patch('requests.get')
    def test_getweatherdata(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_response = {
            'name': 'London',
            'sys': {
                'country': 'GB'
            },
            'coord': {
                'lon': -0.1257,
                'lat': 51.5085
            },
            'timezone': 3600,
            'main': {
                'temp': -0.54,
                'feels_like': -0.54
            }
        }

        mock_get.return_value.json.return_value = mock_response

        api_key = key
        result = get_weather_data('London', api_key)

        expected_data = {
            'name': 'London',
            'country': 'GB',
            'coord': {
                'lon': -0.1257,
                'lat': 51.5085
            },
            'timezone': 'UTC+1',
            'temperature': -0.54,
            'feels_like': -0.54
        }

        self.assertEqual(json.loads(result), expected_data)

    @patch('requests.get')
    def test_invalid_city(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_response = {
            'cod': '404',
            'message': 'city not found'
        }

        mock_get.return_value.json.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            get_weather_data('InvalidCity', key)

        self.assertEqual(str(context.exception), "Invalid city or API")

    @patch('requests.get')
    def test_invalid_API(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_response = {
            'cod': '401',
            'message': 'Invalid API key'
        }

        mock_get.return_value.json.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            get_weather_data('InvalidCity', '123')

        self.assertEqual(str(context.exception), "Invalid city or API")


if __name__ == '__main__':
    unittest.main()
