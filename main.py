import os
import requests
import csv
import io

TELEGRAM_TOKEN = os.getenv("8553327134:AAGr9CxyCUmToszfhBjs-B18BvvopbbsqyI")
CHAT_ID = os.getenv("-1003669160299")

SHEET_URL = "https://docs.google.com/spreadsheets/d/1w6wh_QL0_yf-phUJOChBrPSnxkU477QteaTr6TihsI8/edit?usp=sharing/export?format=csv"

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "disable_web_page_preview": False
    }
    requests.post(url, json=payload)

def main():
    response = requests.get(SHEET_URL)
    data = csv.DictReader(io.StringIO(response.text))

    for row in data:
        if row["status"].lower() == "pendente":
            message = f'{row["mensagem"]}\n\n👉 {row["link"]}'
            send_message(message)
            break

if __name__ == "__main__":
    main()
