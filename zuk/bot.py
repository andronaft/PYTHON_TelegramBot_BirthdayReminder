# coding=utf-8
import telebot
import config
import connection
import random
import pymysql
import schedule
import time

from telebot import types



bot = telebot.TeleBot(config.TOKEN)




# def job():
#     print("I'm working...")
#
# bot.send_message(247576938, schedule.every(1).minutes.do(job))
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

#d add

@bot.message_handler(commands=['start'])
def welcome(message):
    cur = connection.connection().cursor()
    data = {'chat_id': cgi.escape(123, True),'mobile': cgi.escape(123, True),'date': cgi.escape('29.01.2019', True),'description': cgi.escape('des', True)}
    cur.execute("""INSERT INTO `rememberbot.remember` (`chat_id`,`mobile`,`date`,`description`) VALUES ({name},{mobile},{date},{decription})""", data)
    cur.execute("SELECT * FROM remember")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2} {3}".format(row[0], row[1], row[2], row[3]))
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    print (message.chat.id)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь вам не забывать о важных датах связаных с людьми.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def contact(message):

    bot.send_message(message.chat.id, message.contact)
    bot.send_contact(message.chat.id,message.contact.phone_number,message.contact.first_name,message.contact.last_name,message.contact.user_id)

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message)
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                                  reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)