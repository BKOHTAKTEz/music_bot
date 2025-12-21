print("1. START")
import telebot
print("2. TELEBOT OK")
bot = telebot.TeleBot("8333965893:AAGkgqCIs9dr52WF95aVdD2l6_Fm-RNjfbU")
print("3. BOT OK")

@bot.message_handler(commands=['start'])
def start(message):
    print("4. /start ПОЛУЧЕН!")
    bot.reply_to(message, "✅ БОТ РАБОТАЕТ!")

@bot.message_handler(commands=['test'])
def test(message):
    print("5. /test ПОЛУЧЕН!")
    bot.reply_to(message, "🔥 ТЕСТ OK!")

print("6. ПОЛЛИНГ...")
bot.polling()
