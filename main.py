import os
import requests

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

mensagem = "✅ Teste automático funcionando!"

url = f"https://api.telegram.org/bot{token}/sendMessage"

requests.post(url, json={
    "chat_id": chat_id,
    "text": mensagem
})
