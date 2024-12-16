import unittest
from lr3.AppOpenWeather.getweatherdata import get_offset

class TestWeatherData(unittest.TestCase):
    def test_utc_offset(self):
        self.assertEqual(get_offset(3600), 'UTC+1')
        self.assertEqual(get_offset(-7200), 'UTC-2')

if __name__ == '__main__':
    unittest.main()
