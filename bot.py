import telebot
import os
from flask import Flask
import threading

# Get the token from environment variable
TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "Hello, I’m active on TG now")

# Simple Flask server to keep alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

# Start Flask server in background, bot in main thread
if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    print("Bot running...")
    bot.polling(non_stop=True)
