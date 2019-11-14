from datetime import date

import requests

from app import BASE_URL
from app.db_commands import add_to_db, delete_from_db


def send_message(chat_id, text):
    url = BASE_URL + 'sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)

    return r.json()


def handle_command(message):
    chat_id = message['chat']['id']
    text = message['text']

    if text == '/subscribe':
        send_message(chat_id, 'Вы будете получать уведомления перед выходом новых серий "Рик и Морти"')
        add_to_db(chat_id)

    if text == '/unsubscribe':
        send_message(chat_id, 'Вы успешно отписались от уведомлений о новых сериях "Рик и Морти"')
        delete_from_db(chat_id)

    if text == '/when':
        days_left = 7 - date.today().weekday()

        if days_left:
            result_string = f'дней до выхода новой серии - {days_left}'
        else:
            result_string = 'Новая серия выходит сегодня'

        send_message(chat_id, result_string)
