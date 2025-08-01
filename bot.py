import os
import requests
from fastapi import FastAPI, Request

BOT_TOKEN = "8234337661:AAHF2YQWwpnmZ6pvoaaEoRYgTlahGOBTafM"
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # Set this on Render dashboard

app = FastAPI()
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.on_event("startup")
async def set_webhook():
    if WEBHOOK_URL:
        url = f"{TELEGRAM_API}/setWebhook"
        data = {"url": WEBHOOK_URL}
        r = requests.post(url, data=data)
        print("Webhook set:", r.json())
    else:
        print("WEBHOOK_URL not set")

@app.post("/")
async def telegram_webhook(req: Request):
    data = await req.json()
    print("Received:", data)
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        msg_text = data["message"].get("text", "")

        reply = f"💬 You said: {msg_text}"
        requests.post(f"{TELEGRAM_API}/sendMessage", data={
            "chat_id": chat_id,
            "text": reply
        })

    return {"ok": True}
