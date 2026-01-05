import os
import requests

TOKEN = os.environ["8553327134:AAGr9CxyCUmToszfhBjs-B18BvvopbbsqyI
"]
CHAT_ID = os.environ["-1003669160299"]

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": "✅ TESTE COM SECRETS FUNCIONANDO!"
    }
)
