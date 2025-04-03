import telebot
from telebot import types
import requests
import time
from bs4 import BeautifulSoup

bot=telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def hello(message):
    keyboard=types.InlineKeyboardMarkup()
    key_curs=types.InlineKeyboardButton(text='курс',callback_data='curs')
    keyboard.add(key_curs)
    bot.send_message(message.chat.id,'Здравствуйте, это бот для отслеживания курса юань к рублю',reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def call_all(call):
   
    if call.data=='curs':
        url='https://www.rbc.ru/quote/ticker/59066'
        headers={'user-agent':'Mozilla/5.0 '}

        req=requests.get(url,headers=headers)

        soup=BeautifulSoup(req.text,'html.parser')
        answer=soup.find('span',class_='chart__info__sum').text
        bot.send_message(call.message.chat.id,f'Цена: {answer}')
    











while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f'Ошибка: {e}')
        time.sleep(15)

