import telebot

bot = telebot.TeleBot('YOUR TOKEN HERE')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'ЕЩЩЩЩКЕРЕЕЕЕЕЕ')

@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, 'ПАУПАУПАУПАУПАУ')

bot.polling()