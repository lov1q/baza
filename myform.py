from bottle import post, request
import re
from datetime import datetime

@post('/home')
def my_form():
    # Ïîëó÷åíèå äàííûõ èç ôîðìû
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')

    # Ïðîâåðêà çàïîëíåííîñòè ïîëåé ôîðìû
    if not mail or not question or not username:
        return "Error: Please fill in all fields."

    # Ïðîâåðêà ôîðìàòà àäðåñà ýëåêòðîííîé ïî÷òû
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail):
        return "Error: Invalid email address format."

    # Ïîëó÷åíèå òåêóùåé äàòû â ñîêðàùåííîì ôîðìàòå
    access_date = datetime.now().strftime("%Y-%m-%d")

    # Ôîðìèðîâàíèå ðåçóëüòèðóþùåãî ñîîáùåíèÿ ñ îáðàùåíèåì ïî èìåíè è äàòîé
    result_message = f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date: {access_date}"

    return result_message
