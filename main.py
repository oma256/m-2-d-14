import telebot
from telebot import types
import globus_parse


token = '7194759653:AAHIBWsVCWJX6ydlVEiguv0DkDPPjSHMtGw'
bot = telebot.TeleBot(token=token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Добрый день!')
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton('Globus')
    btn2 = types.KeyboardButton('Народный')
    btn3 = types.KeyboardButton('Фрунзе')
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id=message.chat.id, 
                     text='Выберите магазин',
                     reply_markup=markup)


@bot.message_handler(func=lambda x: True)
def echo_all(message):
    if message.text == 'Globus':
        categories = globus_parse.get_categories()
        for category in categories:
            text = f'_{category["title"]}_\n' \
                   f'[-------------------]({category["image"]})'
            bot.send_message(chat_id=message.chat.id, 
                             text=text, 
                             parse_mode='Markdown')

bot.polling()
