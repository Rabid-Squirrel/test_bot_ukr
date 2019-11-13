
# -*- coding: utf-8 -*-
import config
import telebot
import time
import os

from telebot import types

bot = telebot.TeleBot(config.token)
# getMe
user = bot.get_me()
print("BEGIN!!!")

@bot.message_handler(commands = ['start'])
def url(message):
    bot.send_message(message.from_user.id, "Поддерживаемые команды: /start /help")

    keyboard  = types.InlineKeyboardMarkup()#resize_keyboard=True)#resize_keyboard=True)#
    keyboard1 = types.InlineKeyboardButton(text='Выведите тарифы',callback_data="text1")
    keyboard2 = types.InlineKeyboardButton('Показать мои данные',callback_data="text2")
    keyboard.add(keyboard1,keyboard2)
    chat_id = message.from_user.id
    msg=bot.send_message(chat_id, "Приветсвуем тебя, наш гость. Для помощи нажми /help", reply_markup=keyboard )
    print('start')
    #bot.callback_query_handler(selector)
    #bot.register_next_step_handler(msg, selector)
    #bot.answer_callback_query(call_id, text="Дата выбрана")
    #bot.register_next_step_handler(msg,selector)


@bot.callback_query_handler(func=lambda c:True)
def selector(c):
    cid = c.message.chat.id
    #keyboard = types.InlineKeyboardMarkup()
    print('11111')
    if c.data == "text1":
        print('2222')
        #bot.send_message(cid, "Нажали 1-ю кнопку")#), reply_markup=keyboard)
        bot.send_message(cid, "50000-месяц\n20000-неделя\n5000-день")
    elif c.data == "text2":
        print('333')
        #bot.send_message(cid, "Нажали 2-ю кнопку")
        bot.send_message(cid, cid)
    # if m.text == 'Выведите тарифы':
    #     bot.send_message(m.from_user.id, "50000-месяц\n20000-неделя\n5000-день")
    # elif m.text == 'Показать мои данные':
    #     bot.send_message(m.from_user.id, m.chat.id)

@bot.message_handler(commands=['help'])
def url(message):
    bot.send_message(message.from_user.id, "Поддерживаемые команды: /start /help")
    bot.send_message(message.from_user.id, "Начните приветсвие со следующих слов:")
    bot.send_message(message.from_user.id, '"привет","прив","здравствуйте","здравствуй","здорово","здарова","хай","hello","hi"')
    bot.send_message(message.from_user.id, "Или задайте следующий вопрос:")
    bot.send_message(message.from_user.id, "можете связать с оператором?")
    bot.send_message(message.from_user.id, "Или просто напишите что-нибудь.")
    bot.send_message(message.from_user.id, "Хорошего Вам дня.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):


    if message.text.strip().lower().split()[0] in ['привет','прив','здравствуйте',"здравствуй","здорово","здарова","хай","hello","hi"]:
        bot.send_message(message.from_user.id, "Доброго времени суток, чем могу помочь?")
    elif message.text == "можете связать с оператором?":
        bot.send_message(message.from_user.id, "На текущий момент все операторы заняты")
    else:
        bot.reply_to(message, message.text)





if __name__ == '__main__':
     bot.polling(none_stop=True)
