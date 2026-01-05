import requests

TOKEN = "8553327134:AAGr9CxyCUmToszfhBjs-B18BvvopbbsqyI"

CHAT_ID = "-1003669160299"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": "🔥 TESTE DIRETO DO GITHUB 🔥"
    }
)
