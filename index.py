from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '81111469126:AAGVtZd8Mt5h6Baq9JlpCAbMsuFywAXQp8tA'
TELEGRAM_CHAT_ID = '778547754'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    msg = data.get("message", {}).get("text", "")
    if msg:
        send_telegram(f"User said: {msg}")
    return "ok"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)
