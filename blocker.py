import telebot
import os

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id != (your_id):
        bot.send_message(message.from_user.id, 'bot not available')
    else:
        bot.send_message(message.from_user.id, '/lock')


@bot.message_handler(commands=['lock'])
def lock(message):
    winpath = os.environ["windir"]
    os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')

    bot.send_message(message.from_user.id, 'computer is locked')


bot.polling(non_stop=True)
