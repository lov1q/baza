from bottle import post, request
import re
from datetime import datetime

@post('/home')
def my_form():
    # Получение данных из формы
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')

    # Проверка заполненности полей формы
    if not mail or not question or not username:
        return "Error: Please fill in all fields."

    # Проверка формата адреса электронной почты
    if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        return "Error: Invalid email address format."

    # Получение текущей даты в сокращенном формате
    access_date = datetime.now().strftime("%Y-%m-%d")

    # Формирование результирующего сообщения с обращением по имени и датой
    result_message = f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {access_date}"

    return result_message
