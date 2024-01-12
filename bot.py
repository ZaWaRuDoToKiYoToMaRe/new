from config import token
#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot



bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi")
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=['random'])
def random_handler(message):
    n = random.randint(1,100)
    bot.reply_to(message, f'случайное число - {n}')

@bot.message_handler(commands=['quote'])
def quote_message(message):
    bot.reply_to(message, "Мудрая цитата")
    bot.send_message(message.chat.id, 'Зажиточно жить — надо фарм любить')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    string = 'Ты сказал: ' + message.text
    bot.reply_to(message, string)


bot.infinity_polling()