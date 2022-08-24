import telebot
from telebot import types
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    photo = open('picture.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Сайт')
    getId = types.KeyboardButton('Напиши мой АЙДИ!')
    SendPic = types.KeyboardButton('Отправь фотку!')
    markup.add(website,getId,SendPic)
    mess = f'Вiтання, <b> { message.from_user.first_name} {message.from_user.last_name} </b>'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_message(message):
    if message.text == "Напиши привет!":
        bot.send_message(message.chat.id, "Привет!", parse_mode='html')
    elif message.text == "Напиши мой АЙДИ!":
        bot.send_message(message.chat.id, f'Твой АЙДИ - {message.from_user.id}', parse_mode='html')
    elif message.text == "Отправь фотку!":
        photo = open('picture.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Сайт":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("На сайтик", url="vk.com"))
        mess = 'Переходи по ссылке ниже, дружище!'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Я тобi не разумiю", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, какое говно-фотка!')



bot.polling(none_stop=True)
