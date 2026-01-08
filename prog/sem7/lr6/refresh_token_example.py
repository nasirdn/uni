"""
Пример использования refresh token для обновления access token
Некоторые провайдеры (Google, Microsoft) поддерживают refresh tokens
GitHub не выдает refresh tokens в стандартном OAuth flow
"""

from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
import os
import json
from datetime import datetime, timedelta

# Для примера будем использовать Google OAuth
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = "http://localhost:8000/google-callback"
GOOGLE_AUTHORIZATION_BASE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid"
]


class TokenManager:
    """Менеджер для работы с OAuth токенами"""

    def __init__(self, token_file='token.json'):
        self.token_file = token_file
        self.token = self.load_token()

    def load_token(self):
        """Загрузка токена из файла"""
        try:
            with open(self.token_file, 'r') as f:
                token = json.load(f)
                print(f"✓ Токен загружен из {self.token_file}")
                return token
        except FileNotFoundError:
            print(f"✗ Файл {self.token_file} не найден")
            return None

    def save_token(self, token):
        """Сохранение токена в файл"""
        with open(self.token_file, 'w') as f:
            json.dump(token, f, indent=2)
        print(f"✓ Токен сохранен в {self.token_file}")
        self.token = token

    def is_token_expired(self):
        """Проверка истечения срока действия токена"""
        if not self.token:
            return True

        # Проверяем expires_at если есть
        expires_at = self.token.get('expires_at')
        if expires_at:
            return datetime.now().timestamp() > expires_at

        # Или проверяем expires_in
        expires_in = self.token.get('expires_in')
        if expires_in and 'created_at' in self.token:
            created_at = self.token['created_at']
            expire_time = created_at + expires_in
            return datetime.now().timestamp() > expire_time

        return False  # Если нет информации о времени

    def refresh_access_token(self):
        """Обновление access token с помощью refresh token"""
        if not self.token or 'refresh_token' not in self.token:
            print("✗ Refresh token не найден")
            return False

        print("♻️  Обновление access token...")

        try:
            # Создаем сессию для обновления токена
            extra = {
                'client_id': GOOGLE_CLIENT_ID,
                'client_secret': GOOGLE_CLIENT_SECRET
            }

            oauth = OAuth2Session(
                client_id=GOOGLE_CLIENT_ID,
                token=self.token
            )

            # Обновляем токен
            new_token = oauth.refresh_token(
                GOOGLE_TOKEN_URL,
                refresh_token=self.token['refresh_token'],
                **extra
            )

            # Добавляем время создания
            new_token['created_at'] = datetime.now().timestamp()

            # Сохраняем новый токен
            self.save_token(new_token)

            print("✅ Access token успешно обновлен!")
            return True

        except Exception as e:
            print(f"✗ Ошибка при обновлении токена: {e}")
            return False

    def get_valid_token(self):
        """Получение валидного токена (обновляет если нужно)"""
        if self.is_token_expired():
            print("⚠️  Токен истек, пытаемся обновить...")
            if self.refresh_access_token():
                return self.token
            else:
                print("✗ Не удалось обновить токен, требуется новая авторизация")
                return None
        else:
            print("✓ Токен действителен")
            return self.token

        def google_oauth_with_refresh():
            """Полный пример OAuth с Google с поддержкой refresh token"""

            print("=" * 60)
            print("Google OAuth 2.0 с Refresh Token")
            print("=" * 60)

            # Инициализация менеджера токенов
            token_manager = TokenManager('google_token.json')

            # Проверяем, есть ли валидный токен
            token = token_manager.get_valid_token()

            if token:
                # Используем существующий токен
                oauth = OAuth2Session(
                    client_id=GOOGLE_CLIENT_ID,
                    token=token
                )
            else:
                # Нужна новая авторизация
                print("\n1. Начало новой авторизации...")

                oauth = OAuth2Session(
                    client_id=GOOGLE_CLIENT_ID,
                    redirect_uri=GOOGLE_REDIRECT_URI,
                    scope=GOOGLE_SCOPE
                )

                # Генерация URL для авторизации
                authorization_url, state = oauth.authorization_url(
                    GOOGLE_AUTHORIZATION_BASE_URL,
                    access_type="offline",  # Важно: запрашиваем refresh token
                    prompt="consent"  # Всегда запрашиваем разрешение
                )

                print(f"\n2. Откройте в браузере: {authorization_url}")
                print("\n3. После авторизации Google перенаправит вас")
                redirect_response = input("\n4. Вставьте полный URL перенаправления: ")

                # Обмен кода на токен
                print("\n5. Получение токена...")
                token = oauth.fetch_token(
                    GOOGLE_TOKEN_URL,
                    authorization_response=redirect_response,
                    client_secret=GOOGLE_CLIENT_SECRET,
                    include_client_id=True
                )

                # Сохраняем время создания
                token['created_at'] = datetime.now().timestamp()
                token_manager.save_token(token)

            # Используем токен для запроса данных
            print("\n6. Запрос данных пользователя...")
            try:
                response = oauth.get("https://www.googleapis.com/oauth2/v2/userinfo")

                if response.status_code == 200:
                    user_data = response.json()
                    print(f"\nДанные пользователя:")
                    print(f"   Имя: {user_data.get('name', 'N/A')}")
                    print(f"   Email: {user_data.get('email', 'N/A')}")
                    print(f"   Картинка: {user_data.get('picture', 'N/A')}")
                else:
                    print(f"✗ Ошибка: {response.status_code}")

            except TokenExpiredError:
                print("Токен истек во время запроса")
                if token_manager.refresh_access_token():
                    # Повторяем запрос с новым токеном
                    oauth = OAuth2Session(
                        client_id=GOOGLE_CLIENT_ID,
                        token=token_manager.token
                    )
                    response = oauth.get("https://www.googleapis.com/oauth2/v2/userinfo")
                    if response.status_code == 200:
                        user_data = response.json()
                        print(f"\ Данные пользователя (после обновления токена):")
                        print(f"   Имя: {user_data.get('name', 'N/A')}")

            except Exception as e:
                print(f"✗ Ошибка при запросе данных: {e}")

        if name == "__main__":
            # Установите переменные окружения для Google OAuth
            # export GOOGLE_CLIENT_ID="your_id"
            # export GOOGLE_CLIENT_SECRET="your_secret"

            if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
                print(" Установите переменные окружения GOOGLE_CLIENT_ID и GOOGLE_CLIENT_SECRET")
                print("\nПример регистрации приложения в Google:")
                print("1. Перейдите на https://console.cloud.google.com/")
                print("2. Создайте новый проект")
                print("3. В APIs & Services → Credentials создайте OAuth 2.0 Client ID")
                print("4. Добавьте Redirect URI: http://localhost:8000/google-callback")
            else:
                google_oauth_with_refresh()