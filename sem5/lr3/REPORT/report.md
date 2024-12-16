# Закаблукова Анастасия Эдуардовна ИВТ-1.1
## Лабораторная работа №3. Создание своего пакета. Публикация на pypi.

Преобразовать (выполните рефакторинг) вашего существующего проекта для работы с open weather посредством API к виду, 
возможному для публикации в PyPI.

1. Создана структура:

lr3/  
│  
├── ZakWeather/  
│   ├── [\__init\__.py](ZakWeather/\__init\__.py)  
│   ├── [main.py](../lr3/ZakWeather/main.py)  
│   ├── [getweatherdata.py](../lr3/ZakWeather/getweatherdata.py)  
│   └── [owm_my_key.py](ZakWeather/owm_my_key.py)  
│  
├── tests/  
│   └── [test_weather.py](../tests/test_weather.py)  
│  
├── [setup.py](../setup.py)  
├── [setup.cfg](../setup.cfg)  
├── [README.md](../README.md)  
└── [requirements.txt](../requirements.txt)  

2. Создать аккаунт в PyPi и создать API-токен.
3. Устанавливаем библиотеки `setuptools` и `twine`.
```
pip3 install setuptools
```
```
python -m pip install twine
```
4. Развёрнуть пакет запустив setup.py
```
python setup.py sdist
```
В результате создались две директории: `dist` и `ZakWeather.egg-info`

5. С помощью twine развёрнуть пакет на PyPI
```
twine upload dist/*
```
![](image_report/pic1.jpg)