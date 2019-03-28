import config
import tweetbot
import telebot
from flask import Flask, request

bot = telebot.TeleBot(config.telegram_token)

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	#bot.reply_to(message, "https://twitter.com/penayongbumi")
	bot.send_message(message.chat.id, "отправь мне что-нибудь и я это твитну.")


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id,
	"""
	/start - перезагрузить бота
	/help - список команд
	/sendmsg - отправить анонимное сообщение пользователю twitter(пользователь должен фоловить бота)
	""")

@bot.message_handler(commands=['sendmsg'])
def send_msg_to_twuser(message):
        mesg = message.text.replace('/sendmsg ', '').split(' ', maxsplit=1)
        if(len(mesg) != 2):
                bot.send_message(message.chat.id, "/sendmsg [имя_пользователя] [сообщение]\n пример: \n /sendmsg pathetic_bread привет!")
        else:
                username = mesg[0]
                text = mesg[1]
                bot.send_message(message.chat.id, tweetbot.sendmsgtouser(username, text))


@bot.message_handler(func=lambda message: True)
def send_tweet(message):
	bot.send_message(message.chat.id, tweetbot.sendtweet(message.text))


@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://anontweet.herokuapp.com/' + config.token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    pass

#bot.polling()
