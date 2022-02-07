import telegram
import datetime

# Stuur een bericht naar 'https://t.me/botfather' om een bot aan te maken en een token te verkrijgen
# Stuur een bericht naar 'https://t.me/get_id_bot' om je user id te verkrijgen

# Insert token here
token = ''

# Insert user_id here
user_id = ''

# If user desires to not use telegram integration
def sendMsg(message):
    curr_time = datetime.datetime.now().strftime('%d-%b [%X]')
    try:
        bot = telegram.Bot(token=token)
        bot.send_message(text="Op voorraad! \n" + message, chat_id=user_id)
        print(f'{curr_time} - Telegram message sent!  ')
    except:
        # If user desires to not use telegram integration
        pass

