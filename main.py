import os

# from BeatstarsBot import Beatstars_Bot
import telebot
from flask import Flask, request

BOT_TOKEN = "5411402973:AAGhVaeouBYSFIAGOHshoBBMak3poZ5HxKI"
BOT_URL = "https://beatstarsbot.herokuapp.com/"

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello")


@server.route('/' + BOT_TOKEN, methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=BOT_URL)
    return "!", 200


if __name__ == "__main__":
    server.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

# print('Введите логин: ')
# username = input()
#
# print('Введите пароль: ')
# password = input()
#
# BS_bot = Beatstars_Bot(username, password)
# BS_bot.start_bot()
