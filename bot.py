#-*- coding: utf-8 -*-
import telebot
from telebot import *

import config
'''import keyboards
from keyboards import *'''

#bot = telebot.TeleBot(config.token)
bot = telebot.TeleBot('1211157363:AAEDjDXkQDj8v5mYuKJnUOGJuHLQbjD-57A')
markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
itembtn1 = types.KeyboardButton('1 курс')
itembtn2 = types.KeyboardButton('2 курс')
itembtn3 = types.KeyboardButton('3 курс')
itembtn4 = types.KeyboardButton('4 курс')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
#menu_remove=types.ReplyKeyboardRemove()

help_message = (
    'sdfsdf\n'+
    'sdfsfs\n'+
    '/start\n'+
    '/help sdf\n'+
    '\n'
)


@bot.message_handler(commands=['start'])
def start_message(message):
#    bot.send_message(message.chat.id, 'Привет, '+ message.from_user.first_name)
    bot.reply_to(message, 'v 0,1'+ str(message.from_user.first_name), reply_markup=markup)
#   menu_remove=types.ReplyKeyboardRemove()

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(content_types=['text'])
def inline(message):
##1 kurs
    if message.text == '1 курс':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Архітектура ПК', callback_data='Number11')
        but_2 = types.InlineKeyboardButton(text='Вступ до спеціальності', callback_data='Number12')
        but_3 = types.InlineKeyboardButton(text='Початок програмування', callback_data='Number13')
        but_4 = types.InlineKeyboardButton(text='Початок програмування4', callback_data='Number14')
        key.add(but_1, but_2, but_3)
        key.add(but_4)
        bot.send_message(message.chat.id, 'Виберіть предмет', reply_markup=key)

##2 kurs
    elif message.text == '2 курс':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Архітектура ПК', callback_data='Number21')
        but_2 = types.InlineKeyboardButton(text='Вступ до спеціальності', callback_data='Number22')
        but_3 = types.InlineKeyboardButton(text='Початок програмування', callback_data='Number23')
        but_4 = types.InlineKeyboardButton(text='Початок програмування4', callback_data='Number24')
        key.add(but_1, but_2, but_3)
        key.add(but_4)
        bot.send_message(message.chat.id, 'Виберіть предмет', reply_markup=key)

##3 kurs
    elif message.text == '3 курс':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Архітектура ПК', callback_data='Number31')
        but_2 = types.InlineKeyboardButton(text='Вступ до спеціальності', callback_data='Number32')
        but_3 = types.InlineKeyboardButton(text='Початок програмування', callback_data='Number33')
        but_4 = types.InlineKeyboardButton(text='Початок програмування4', callback_data='Number34')
        key.add(but_1, but_2, but_3)
        key.add(but_4)
        bot.send_message(message.chat.id, 'Виберіть предмет', reply_markup=key)

##4 kurs
    elif message.text == '4 курс':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Архітектура ПК', callback_data='Number41')
        but_2 = types.InlineKeyboardButton(text='Вступ до спеціальності', callback_data='Number42')
        but_3 = types.InlineKeyboardButton(text='Початок програмування', callback_data='Number43')
        but_4 = types.InlineKeyboardButton(text='Початок програмування4', callback_data='Number44')
        key.add(but_1, but_2, but_3)
        key.add(but_4)
        bot.send_message(message.chat.id, 'Виберіть предмет', reply_markup=key)
    else :
        bot.send_message(message.chat.id, 'Я не розумію тебе (')
@bot.callback_query_handler(func=lambda c:True)
def inlin(c):

#### 1 kurs 
    if c.data == 'Number11':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1C0nwRYRiDfML161MPvhwb_Fof4aVkVuY')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1HjzBiii6cX1YE-YgMhbQoiNWO4mdmIVH')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1bC0p0s79f_ItTV2Jb84Me_DmbrLPbb3K')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1_pEh7FqXMNyDWcHDhFoXZS8wX-V2_xbT')
    if c.data == 'Number12':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkM1pUcUgtU2lzYUE')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkbHJha0gxUmQ2T00')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkXzJPNVNoRldtVG8')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkN1Fzdk9pSTJQZnc')
    if c.data == 'Number13':
        bot.send_message(c.message.chat.id, 'Меню так меню!!')
    if c.data == 'Number14':
    	bot.send_message(c.message.chat.id, 'Меню так меню!!', reply_markup=markup)


#### 2 kurs
    if c.data == 'Number21':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1C0nwRYRiDfML161MPvhwb_Fof4aVkVuY')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1HjzBiii6cX1YE-YgMhbQoiNWO4mdmIVH')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1bC0p0s79f_ItTV2Jb84Me_DmbrLPbb3K')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1_pEh7FqXMNyDWcHDhFoXZS8wX-V2_xbT')
    if c.data == 'Number22':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkM1pUcUgtU2lzYUE')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkbHJha0gxUmQ2T00')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkXzJPNVNoRldtVG8')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkN1Fzdk9pSTJQZnc')
    if c.data == 'Number23':
        bot.send_message(c.message.chat.id, 'Меню так меню!!')
    if c.data == 'Number24':
    	bot.send_message(c.message.chat.id, 'Меню так меню!!', reply_markup=markup)
    

#### 3 kurs
    if c.data == 'Number31':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1C0nwRYRiDfML161MPvhwb_Fof4aVkVuY')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1HjzBiii6cX1YE-YgMhbQoiNWO4mdmIVH')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1bC0p0s79f_ItTV2Jb84Me_DmbrLPbb3K')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1_pEh7FqXMNyDWcHDhFoXZS8wX-V2_xbT')
    if c.data == 'Number32':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkM1pUcUgtU2lzYUE')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkbHJha0gxUmQ2T00')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkXzJPNVNoRldtVG8')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkN1Fzdk9pSTJQZnc')
    if c.data == 'Number33':
        bot.send_message(c.message.chat.id, 'Меню так меню!!')
    if c.data == 'Number34':
    	bot.send_message(c.message.chat.id, 'Меню так меню!!', reply_markup=markup)


#### 4 kurs
    if c.data == 'Number41':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1C0nwRYRiDfML161MPvhwb_Fof4aVkVuY')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1HjzBiii6cX1YE-YgMhbQoiNWO4mdmIVH')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1bC0p0s79f_ItTV2Jb84Me_DmbrLPbb3K')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=1_pEh7FqXMNyDWcHDhFoXZS8wX-V2_xbT')
    if c.data == 'Number42':
        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkM1pUcUgtU2lzYUE')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkbHJha0gxUmQ2T00')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkXzJPNVNoRldtVG8')
#        bot.send_message(c.message.chat.id, 'https://drive.google.com/uc?export=download&id=0B698oYkUaQVkN1Fzdk9pSTJQZnc')
    if c.data == 'Number43':
        bot.send_message(c.message.chat.id, 'Меню так меню!!')
    if c.data == 'Number44':
    	bot.send_message(c.message.chat.id, 'Меню так меню!!', reply_markup=markup)







if __name__ == '__main__':
    bot.polling(none_stop=True)
#https://drive.google.com/uc?export=download&id=<Идентификатор файла>
