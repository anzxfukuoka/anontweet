import config
import tweetbot
import telebot

bot = telebot.TeleBot(config.telegram_token)


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


bot.polling()
