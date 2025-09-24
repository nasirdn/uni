import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Настройки
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your_email@example.com'
password = 'your_password'

# Создание сообщения
sender_email = 'your_email@example.com'
receiver_email = 'receiver@example.com'
subject = 'Тестовое письмо'
body = 'Это тело тестового письма, отправленного через Python!'

# Создание объекта сообщения
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Добавление текста к сообщению
msg.attach(MIMEText(body, 'plain'))

try:
    # Подключение к SMTP-серверу
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Начало TLS шифрования
    server.login(username, password)  # Вход на сервер

    # Отправка письма
    server.send_message(msg)
    print("Письмо успешно отправлено!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    server.quit()  # Закрытие соединения
