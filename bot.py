import telebot
import sqlite3
import os
from datetime import datetime
from telebot import types
from dotenv import load_dotenv
import os
import subprocess

# ИНИЦИАЛИЗАЦИЯ БАЗЫ ДАННЫХ
subprocess.run(['python', 'music_init.py'], check=True)
print("✅ База данных инициализирована!")

# ДАЛЬШЕ ВАШ BOT КОД
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
db_path = 'music.db'

# ========================================
# ✅ АДМИН ID (ЗАМЕНИТЕ НА ВАШ!)
# ========================================
ADMIN_ID = 1961723672  # ← @userinfobot → /start → ВСТАВЬТЕ СВОЙ ID!

# ========================================
# 📊 ОТЧЕТЫ - УЛУЧШЕННАЯ ФУНКЦИЯ
# ========================================
def send_report(user_id, user_name, action, button_text="", status="✅ УСПЕШНО", artist=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report_text = f"""
📊 *ОТЧЕТ БОТА*

🆔 ID: `{user_id}`
👤 Имя: {user_name}
⏰ Время: `{timestamp}`
🔘 Кнопка: `{button_text}`
📝 Действие: `{action}`
📈 Статус: {status}
"""
    
    if artist:
        report_text += f"\n🎸 Артист: `{artist}`"
    
    try:
        bot.send_message(ADMIN_ID, report_text, parse_mode='Markdown')
    except:
        print(f"❌ Отчет не отправлен: {action}")

# ========================================
# INLINE КНОПКИ
# ========================================
def main_inline_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(types.InlineKeyboardButton("🎸 ROCK", callback_data="genre_rock"),
               types.InlineKeyboardButton("🎤 POP", callback_data="genre_pop"),
               types.InlineKeyboardButton("🤘 METAL", callback_data="genre_metal"))
    markup.add(types.InlineKeyboardButton("🔥 DISCO", callback_data="genre_disco"),
               types.InlineKeyboardButton("🎤 HIP-HOP", callback_data="genre_hiphop"),
               types.InlineKeyboardButton("⚡️ EDM", callback_data="genre_edm"))
    markup.add(types.InlineKeyboardButton("💎 R&B", callback_data="genre_rnb"),
               types.InlineKeyboardButton("👑 LEGENDS", callback_data="genre_legends"),
               types.InlineKeyboardButton("🌀 PSY", callback_data="genre_psy"))
    markup.add(types.InlineKeyboardButton("🇯🇲 REGGAE", callback_data="genre_reggae"),
               types.InlineKeyboardButton("⛓️ PUNK", callback_data="genre_punk"),
               types.InlineKeyboardButton("🌈 INDIE", callback_data="genre_indie"))
    return markup

def artist_inline_keyboard(artists):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for i in range(0, len(artists), 2):
        if i + 1 < len(artists):
            artist1 = artists[i].replace(' ', '_').replace('\'', '').replace('.', '').replace('&', '')
            artist2 = artists[i+1].replace(' ', '_').replace('\'', '').replace('.', '').replace('&', '')
            markup.add(types.InlineKeyboardButton(artists[i], callback_data=f"artist_{artist1}"),
                       types.InlineKeyboardButton(artists[i+1], callback_data=f"artist_{artist2}"))
        else:
            artist = artists[i].replace(' ', '_').replace('\'', '').replace('.', '').replace('&', '')
            markup.add(types.InlineKeyboardButton(artists[i], callback_data=f"artist_{artist}"))
    markup.add(types.InlineKeyboardButton("🔙 ГЛАВНОЕ МЕНЮ", callback_data="main_menu"))
    return markup

# ========================================
# БАЗА АРТИСТОВ
# ========================================
genre_artists = {
    "rock": ["AC/DC", "Queen", "Nirvana", "Deep Purple", "Guns N' Roses", "Led Zeppelin", "Aerosmith", "The Rolling Stones"],
    "pop": ["Madonna", "Michael Jackson", "The Beatles", "Taylor Swift", "Britney Spears", "Elvis Presley", "ABBA", "Rihanna"],
    "metal": ["Metallica", "Iron Maiden", "Rammstein", "Slipknot", "Ozzy Osbourne", "Judas Priest", "Black Sabbath", "Slayer"],
    "disco": ["Bee Gees", "ABBA", "Donna Summer", "Boney M", "Village People", "Earth Wind & Fire", "Chic", "Gloria Gaynor"],
    "hiphop": ["Eminem", "Drake", "Kanye West", "Tupac Shakur", "Snoop Dogg", "The Notorious B.I.G.", "Nas", "50 Cent"],
    "edm": ["David Guetta", "Daft Punk", "Avicii", "Calvin Harris", "Marshmello", "Martin Garrix", "Skrillex", "Deadmau5"],
    "rnb": ["Beyoncé", "The Weeknd", "Alicia Keys", "SZA", "Usher", "Chris Brown", "Frank Ocean", "H.E.R."],
    "legends": ["Queen", "The Beatles", "Michael Jackson", "Metallica", "Eminem", "Madonna", "Led Zeppelin", "Pink Floyd"],
    "psy": ["Pink Floyd", "The Doors", "Jimi Hendrix", "Grateful Dead", "Jefferson Airplane", "Cream", "The Who"],
    "reggae": ["Bob Marley", "Peter Tosh", "Steel Pulse", "UB40", "Jimmy Cliff", "Toots and the Maytals"],
    "punk": ["Green Day", "The Clash", "Sex Pistols", "The Ramones", "The Offspring", "Blink-182"],
    "indie": ["Arctic Monkeys", "Tame Impala", "The Strokes", "Radiohead", "The Killers", "Franz Ferdinand"]
}

genre_titles = {
    "rock": "🤘 ROCK ЛЕГЕНДЫ", "pop": "⭐ POP ИКОНЫ", "metal": "🔥 METAL БОГИ",
    "disco": "🕺 DISCO ХИТЫ", "hiphop": "🎤 HIP-HOP ЛЕГЕНДЫ", "edm": "⚡️ EDM ЗВЁЗДЫ",
    "rnb": "💎 R&B ДИВЫ", "legends": "👑 ТОП ЛЕГЕНДЫ", "psy": "🌀 PSYCHEDELIC",
    "reggae": "🇯🇲 REGGAE", "punk": "⛓️ PUNK", "indie": "🌈 INDIE"
}

# ========================================
# СТАРТ + ОТЧЕТ
# ========================================
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name or "Неизвестно"
    
    send_report(user_id, user_name, "ЗАПУСК БОТА", "/start", "✅ УСПЕШНО")
    
    bot.send_message(message.chat.id, 
                    "🎵 *Звуки Времени*\n\n"
                    "🎸 12 жанров • 144 легенды!\n"
                    "👇 Выберите жанр или напишите имя:", 
                    reply_markup=main_inline_keyboard(), parse_mode='Markdown')

# ========================================
# ЖАНРЫ + ПОЛНЫЙ ОТЧЕТ
# ========================================
@bot.callback_query_handler(func=lambda call: call.data.startswith("genre_"))
def genre_callback(call):
    user_id = call.from_user.id
    user_name = call.from_user.first_name or "Неизвестно"
    genre = call.data.replace("genre_", "")
    button_text = call.data
    
    send_report(user_id, user_name, f"ОТКРЫТ ЖАНР", button_text, "✅ УСПЕШНО", genre)
    
    artists = genre_artists.get(genre, [])
    title = genre_titles.get(genre, "Жанр")
    
    bot.edit_message_text(f"{title}\n\n👇 Выберите артиста:", 
                         call.message.chat.id, 
                         call.message.message_id, 
                         reply_markup=artist_inline_keyboard(artists))

# ========================================
# АРТИСТЫ + ПОЛНЫЙ ОТЧЕТ
# ========================================
@bot.callback_query_handler(func=lambda call: call.data.startswith("artist_"))
def artist_callback(call):
    user_id = call.from_user.id
    user_name = call.from_user.first_name or "Неизвестно"
    artist = call.data.replace("artist_", "").replace("_", " ")
    button_text = call.data
    info = get_artist_info(artist)
    
    success = "✅ УСПЕШНО" if info else "❌ НЕ НАЙДЕН"
    
    send_report(user_id, user_name, f"ЗАПРОС АРТИСТА", button_text, success, artist)
    
    if info:
        back_only_keyboard = types.InlineKeyboardMarkup()
        back_only_keyboard.add(types.InlineKeyboardButton("🔙 ГЛАВНОЕ МЕНЮ", callback_data="main_menu"))
        
        bot.edit_message_text(info, 
                            call.message.chat.id, 
                            call.message.message_id, 
                            reply_markup=back_only_keyboard,
                            parse_mode='Markdown')
    else:
        bot.answer_callback_query(call.id, "❌ Артист не найден!")

# ========================================
# ГЛАВНОЕ МЕНЮ + ОТЧЕТ
# ========================================
@bot.callback_query_handler(func=lambda call: call.data == "main_menu")
def back_to_main(call):
    user_id = call.from_user.id
    user_name = call.from_user.first_name or "Неизвестно"
    
    send_report(user_id, user_name, "ВОЗВРАТ В МЕНЮ", "🔙 ГЛАВНОЕ МЕНЮ", "✅ УСПЕШНО")
    
    bot.edit_message_text("🎵 *Звуки Времени*\n\n"
                         "🎸 12 жанров • 144 легенды!\n"
                         "👇 Выберите жанр или напишите имя:", 
                        call.message.chat.id, 
                        call.message.message_id, 
                        reply_markup=main_inline_keyboard(), 
                        parse_mode='Markdown')

# ========================================
# ПОИСК + ОТЧЕТ
# ========================================
@bot.message_handler(content_types=['text'])
def search_artist(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name or "Неизвестно"
    text = message.text.strip()
    info = get_artist_info(text)
    
    success = "✅ НАЙДЕН" if info else "❌ НЕ НАЙДЕН"
    
    send_report(user_id, user_name, "ТЕКСТОВЫЙ ПОИСК", text, success, text)
    
    if info:
        back_only_keyboard = types.InlineKeyboardMarkup()
        back_only_keyboard.add(types.InlineKeyboardButton("🔙 ГЛАВНОЕ МЕНЮ", callback_data="main_menu"))
        
        bot.send_message(message.chat.id, info, 
                        reply_markup=back_only_keyboard,
                        parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, 
                        "❌ Артист не найден!\n\n"
                        "🎵 Напишите имя или используйте кнопки ниже:", 
                        reply_markup=main_inline_keyboard())

# ========================================
# БАЗА ДАННЫХ
# ========================================
def get_artist_info(name):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT years, genre, hits, facts FROM artists WHERE UPPER(name) LIKE ?", (f'%{name.upper()}%',))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            years, genre, hits, facts = result
            return f"🎸 *{name.title()}*\n\n📅 {years}\n🎵 {genre}\n🔥 Топ хит: `{hits}`\n💡 {facts}"
    except Exception as e:
        print(f"Ошибка БД: {e}")
    return None

if __name__ == '__main__':
    print("🚀 🎵 ЗВУКИ ВРЕМЕНИ - ПОЛНАЯ ОТЧЕТНОСТЬ!")
    print(f"✅ Отчеты → ID: {ADMIN_ID}")
    print("✅ ВСЕ кнопки отслеживаются!")
    bot.polling(none_stop=True)
