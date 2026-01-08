from requests_oauthlib import OAuth2Session
import os
from flask import Flask, request, redirect
import json

# Конфигурация
CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID", "your_client_id_here")
CLIENT_SECRET = os.environ.get("GITHUB_CLIENT_SECRET", "your_client_secret_here")
REDIRECT_URI = "http://localhost:8000/callback"
AUTHORIZATION_BASE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
SCOPE = ["read:user", "user:email"]  # Права доступа

# Инициализация Flask для обработки callback
app = Flask(__name__)

def github_oauth_flow():
    """Основной поток OAuth 2.0 Authorization Code"""

    print("=" * 60)
    print("OAuth 2.0 Authorization Code Flow с GitHub")
    print("=" * 60)

    # Создаем OAuth сессию
    oauth = OAuth2Session(
        client_id=CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE
    )

    # Генерируем URL для авторизации
    authorization_url, state = oauth.authorization_url(
        AUTHORIZATION_BASE_URL,
        state="random_state_string"  # Защита от CSRF
    )

    print("\n1. URL для авторизации:")
    print(f"   {authorization_url}")
    print(f"\n   State параметр: {state}")

    print("\n2. Откройте этот URL в браузере и авторизуйтесь в GitHub")
    print("3. После авторизации GitHub перенаправит вас на callback URL")

    return oauth, state


def exchange_code_for_token(oauth, authorization_response):
    """Обмен authorization code на access token"""

    print("\n4. Обмен кода на токен...")

    token = oauth.fetch_token(
        TOKEN_URL,
        authorization_response=authorization_response,
        client_secret=CLIENT_SECRET,
        include_client_id=True
    )

    print(" Токен успешно получен!")
    print(f"\n   Access Token: {token.get('access_token', '')[:20]}...")
    print(f"   Token Type: {token.get('token_type', 'N/A')}")
    print(f"   Scope: {token.get('scope', 'N/A')}")

    if 'refresh_token' in token:
        print(f"   Refresh Token: {token.get('refresh_token', '')[:20]}...")

    return token


def get_user_info(oauth):
    """Получение информации о пользователе с использованием access token"""

    print("\n5. Получение информации о пользователе...")

    try:
        # Запрос к защищенному ресурсу
        response = oauth.get("https://api.github.com/user")

        if response.status_code == 200:
            user_data = response.json()

            print("✓ Данные пользователя получены!")
            print(f"\n   Имя: {user_data.get('name', 'N/A')}")
            print(f"   Логин: {user_data.get('login', 'N/A')}")
            print(f"   Email: {user_data.get('email', 'N/A')}")
            print(f"   Компания: {user_data.get('company', 'N/A')}")
            print(f"   Блог: {user_data.get('blog', 'N/A')}")
            print(f"   Локация: {user_data.get('location', 'N/A')}")
            print(f"   Публичные репозитории: {user_data.get('public_repos', 'N/A')}")
            print(f"   Подписчики: {user_data.get('followers', 'N/A')}")
            print(f"   Подписки: {user_data.get('following', 'N/A')}")

            # Дополнительный запрос для получения email
            email_response = oauth.get("https://api.github.com/user/emails")
            if email_response.status_code == 200:
                emails = email_response.json()
                primary_email = next((e for e in emails if e['primary']), None)
                if primary_email:
                    print(f"   Основной email: {primary_email['email']}")

            return user_data
        else:
            print(f"✗ Ошибка: {response.status_code}")
            print(f"   Ответ: {response.text}")

    except Exception as e:
        print(f" Ошибка при запросе данных: {e}")

    return None

    def manual_flow():
        """Ручной поток OAuth (без веб-сервера)"""

        print("\n" + "=" * 60)
        print("Ручной поток OAuth")
        print("=" * 60)

        # Инициализация OAuth
        oauth = OAuth2Session(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        )

        # Генерация URL для авторизации
        authorization_url, state = oauth.authorization_url(
            AUTHORIZATION_BASE_URL,
            state="manual_flow_state"
        )

        print(f"\n1. Откройте в браузере: {authorization_url}")
        print("\n2. После авторизации GitHub перенаправит вас на:")
        print(f"   {REDIRECT_URI}")
        print("\n3. Скопируйте ПОЛНЫЙ URL из адресной строки браузера")
        print("   (он будет выглядеть примерно так: http://localhost:8000/callback?code=XXX&state=YYY)")

        # Получение callback URL от пользователя
        redirect_response = input("\n4. Вставьте полный URL перенаправления: ")

        # Обмен кода на токен
        token = exchange_code_for_token(oauth, redirect_response)

        # Получение данных пользователя
        user_data = get_user_info(oauth)

        return token, user_data

    # Flask endpoints для автоматического потока
    @app.route('/')
    def home():
        """Домашняя страница с ссылкой для авторизации"""

        oauth = OAuth2Session(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        )

        authorization_url, state = oauth.authorization_url(
            AUTHORIZATION_BASE_URL,
            state="flask_flow_state"
        )

        return f'''
        <html>
            <head>
                <title>OAuth 2.0 с GitHub</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .container {{ max-width: 800px; margin: 0 auto; }}
                    .btn {{ 
                        display: inline-block;
                        padding: 12px 24px;
                        background-color: #24292e;
                        color: white;
                        text-decoration: none;
                        border-radius: 6px;
                        font-weight: bold;
                    }}
                    .btn:hover {{ background-color: #444d56; }}
                    .info {{ background-color: #f6f8fa; padding: 15px; border-radius: 6px; margin: 20px 0; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1> OAuth 2.0 Authorization Code Flow</h1>
                    <div class="info">
                        <p><strong>Провайдер:</strong> GitHub</p>
                        <p><strong>Redirect URI:</strong> {REDIRECT_URI}</p>
                        <p><strong>Scopes:</strong> {', '.join(SCOPE)}</p>
                    </div>
                    <a href="{authorization_url}" class="btn">Авторизоваться через GitHub</a>
                    <p><small>После авторизации вы будете перенаправлены обратно на эту страницу</small></p>
                </div>
            </body>
        </html>
        '''

    @app.route('/callback')
    def callback():
        """Обработка callback от GitHub"""

        # Получаем код авторизации из URL
        authorization_response = request.url

        # Создаем OAuth сессию
        oauth = OAuth2Session(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI
        )

        try:
            # Обмен кода на токен
            token = oauth.fetch_token(
                TOKEN_URL,
                authorization_response=authorization_response,
                client_secret=CLIENT_SECRET
            )

            # Получаем информацию о пользователе
            user_response = oauth.get("https://api.github.com/user")
            user_data = user_response.json() if user_response.status_code == 200 else {}

            return f'''
            <html>
                <head>
                    <title>Успешная авторизация!</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 40px; }}
                        .container {{ max-width: 800px; margin: 0 auto; }}
                        .success {{ background-color: #d1f7c4; padding: 20px; border-radius: 6px; }}
                        .token-info {{ background-color: #f0f0f0; padding: 15px; border-radius: 6px; margin: 20px 0; }}
                    .user-info {{ background-color: #e6f7ff; padding: 20px; border-radius: 6px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Успешная авторизация!</h1>
                    
                    <div class="success">
                        <h2>Access Token получен</h2>
                        <div class="token-info">
                            <p><strong>Token Type:</strong> {token.get('token_type', 'N/A')}</p>
                            <p><strong>Scope:</strong> {token.get('scope', 'N/A')}</p>
                            <p><strong>Access Token (первые 20 символов):</strong> {token.get('access_token', '')[:20]}...</p>
                        </div>
                    </div>
                    
                    <div class="user-info">
                        <h2>Информация о пользователе</h2>
                        <p><strong>Имя:</strong> {user_data.get('name', 'N/A')}</p>
                        <p><strong>Логин:</strong> {user_data.get('login', 'N/A')}</p>
                        <p><strong>Email:</strong> {user_data.get('email', 'N/A')}</p>
                        <p><strong>Компания:</strong> {user_data.get('company', 'N/A')}</p>
                        <p><strong>Блог:</strong> {user_data.get('blog', 'N/A')}</p>
                        <p><strong>Публичные репозитории:</strong> {user_data.get('public_repos', 'N/A')}</p>
                    </div>
                    
                    <p><a href="/">Вернуться на главную</a></p>
                </div>
            </body>
        </html>
        '''

        except Exception as e:
            return f'''
        <html>
            <body>
                <h1>Ошибка авторизации</h1>
                <p>{str(e)}</p>
                <p><a href="/">Попробовать снова</a></p>
            </body>
        </html>
        '''

def main():
    """Основная функция"""

    print("Выберите режим работы:")
    print("1. Ручной поток (ввод URL вручную)")
    print("2. Автоматический поток (Flask веб-сервер)")
    print("3. Демонстрация Client Credentials Flow")

    choice = input("\nВведите номер (1-3): ").strip()

    if choice == "1":
        # Ручной поток
        token, user_data = manual_flow()

        # Сохранение токена в файл
        if token:
            with open('token.json', 'w') as f:
                json.dump(token, f, indent=2)
            print(f"\n✓ Токен сохранен в token.json")

    elif choice == "2":
        # Автоматический поток с Flask
        print("\nЗапуск Flask сервера на http://localhost:8000")
        print("Откройте браузер и перейдите по указанному адресу")
        app.run(host='localhost', port=8000, debug=False)

    elif choice == "3":
        # Client Credentials Flow (если поддерживается провайдером)
        demonstrate_client_credentials()

    else:
        print("Неверный выбор")

def demonstrate_client_credentials():
    """Демонстрация Client Credentials Flow"""

    print("\n" + "=" * 60)
    print("Client Credentials Flow")
    print("=" * 60)

    print("\nПримечание: GitHub не поддерживает Client Credentials Flow")
    print("Этот поток обычно используется для машин-машинной аутентификации")
    print("\nПример для другого провайдера (например, Auth0):")
    print("""
    from oauthlib.oauth2 import BackendApplicationClient
    from requests_oauthlib import OAuth2Session
    
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)
    
    token = oauth.fetch_token(
        token_url=TOKEN_URL,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope=SCOPE
    )
    """)

if __name__ == "__main__":
    main()
