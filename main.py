import telebot 
from config import token
from random import randint
from logic import Pokemon
from logic import *

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['feed'])
def feed(message):
    if bot.send_message(message.chat.id, 'Твой покемон голоден'):
        bot.reply_to(message, "Молодец что покормил его, продолжай в том же темпе и ты повысишь ему уровень")

@bot.message_handler(commands=['lvl'])
def lvl(message):
    if bot.send_message(message.chat.id, 'Ваш покемон плотно покушал и поэтому вы повысили его уровень'):
        bot.reply_to(message, 'Вы повысили уровень покемона!')

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]

@bot.message_handler(commands=['help'])
def help(message):
    if message.from_user.username(message.chat.id, 'Нужна помощь'):
        bot.reply_to(meaage, 'Список всех команд: /lvl ; /info ; /feed ; /attack ; /go')

bot.infinity_polling(none_stop=True)

