# REST-сервис бонусной программы

## Описание
Это REST-сервис для просмотра текущего уровня бонусной программы с использованием FastAPI и JWT для аутентификации.

Запуск:

uvicorn main:app --reload

1. Получите токен:

curl -X POST "http://127.0.0.1:8000/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=user1&password=password1"

2. Используйте токен для получения информации о бонусах:

curl -X GET "http://127.0.0.1:8000/bonus" -H "Authorization: Bearer <your_token>"

Результат:

![](image_report/pic1.jpg)