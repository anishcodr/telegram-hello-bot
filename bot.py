import telebot
import os

TOKEN = os.environ.get("8234337661:AAHF2YQWwpnmZ6pvoaaEoRYgTlahGOBTafM")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "Hello, I’m active on TG now")

print("Bot running...")
bot.polling(non_stop=True)

