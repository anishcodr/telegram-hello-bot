from fastapi import FastAPI, Request
import telebot
import os

BOT_TOKEN = "8234337661:AAHF2YQWwpnmZ6pvoaaEoRYgTlahGOBTafM"
bot = telebot.TeleBot(BOT_TOKEN)
app = FastAPI()

@app.post("/")
async def webhook(request: Request):
    data = await request.json()
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return {"ok": True}

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, "✅ Hello, I'm active 24×7 via Render!")

# Optional: Just to keep it running cleanly (no need for @app.on_event)
@app.get("/")
def root():
    return {"status": "Bot is running."}
