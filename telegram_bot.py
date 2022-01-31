import telegram

# Stuur een bericht naar 'https://t.me/botfather' om een bot aan te maken en een token te verkrijgen
# Stuur een bericht naar 'https://t.me/get_id_bot' om je user id te verkrijgen

# Insert token here
token = ''

# Insert user_id here
user_id = ''

bot = telegram.Bot(token=token)


def sendMsg(message):
    bot.send_message(text="Op voorraad! \n" + message, chat_id=user_id)
