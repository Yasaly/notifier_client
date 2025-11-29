import os

from dotenv import load_dotenv
import requests

load_dotenv()

NOTIFIER_API_URL = os.getenv("NOTIFIER_API_URL", "http://localhost:8000/notify").strip()
NOTIFIER_API_SECRET = os.getenv("NOTIFIER_API_SECRET", "").strip()


class NotifierError(Exception):
    pass


def message(recipient_id: str, text: str) -> None:
    """
    Отправить уведомление через удалённый сервер с ботом.

    Требует:
      - NOTIFIER_API_URL      (адрес сервера, например)
      - NOTIFIER_API_SECRET   (совпадает с серверным NOTIFIER_API_SECRET)
    """
    if not NOTIFIER_API_URL:
        raise NotifierError("NOTIFIER_API_URL не настроен")
    if not NOTIFIER_API_SECRET:
        raise NotifierError("NOTIFIER_API_SECRET не настроен")

    payload = {
        "secret": NOTIFIER_API_SECRET,
        "recipient_id": recipient_id,
        "text": text,
    }

    resp = requests.post(NOTIFIER_API_URL, json=payload, timeout=10)
    if not resp.ok:
        raise NotifierError(
            f"Ошибка уведомления: HTTP {resp.status_code}, {resp.text}"
        )
