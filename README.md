A tiny Python client for sending notifications to a remote Telegram bot service
(Notifier API).

The library is designed to talk to a FastAPI service that exposes a `/notify`
endpoint and forwards messages to Telegram recipients by their nickname.

## Installation
From local source (during development):
```bash
   pip install -e .
```
From GitHub:
```bash
   pip install git+https://github.com/Yasaly/notifier_client.git
```

## Configuration
`notifier_client` reads its configuration from environment variables
(optionally via `.env` using `python-dotenv`):

`NOTIFIER_API_URL` – URL of the notifier API endpoint
(e.g. http://localhost:8000/notify or http://192.168.0.167:8000/notify)

NOTIFIER_API_SECRET – shared secret, must match NOTIFIER_API_SECRET on
the server side.

Example `/env`:
```
NOTIFIER_API_URL=http://192.168.0.167:8000/notify
NOTIFIER_API_SECRET=your_very_secret_string
```

## Usage
```
from dotenv import load_dotenv
from notifier_client import message

load_dotenv()  # optional, if you use a .env file

# "admin" is a nickname that is registered on the notifier server
message("admin", "✅ Task from external project has finished!")
```
If something goes wrong (bad URL, wrong secret, server error, etc.),
message() will raise `NotifierError`.

## API contract
The client expects a server that accepts:
* `POST /notify`
* JSON body:
```
{
  "secret": "<NOTIFIER_API_SECRET>",
  "nickname": "<recipient_nickname>",
  "text": "<message text>"
}

```
and responds with {"status": "ok"} on success.

## Requirements
* Python 3.8+
* `requests`
* `python-dotenv`