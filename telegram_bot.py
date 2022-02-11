import telegram
import datetime

# Stuur een bericht naar 'https://t.me/botfather' om een bot aan te maken en een token te verkrijgen
# Stuur een bericht naar 'https://t.me/get_id_bot' om je user id te verkrijgen

# Insert token here
token = ''

# Insert user_id here
user_id = ''


# Controleert de verbinding met de bot en de gebruiker
# Zal de gebruiker erop wijzen dat de verbinding is mislukt of is gelukt. Zal ongeacht status verder gaan
def check_creds():
    # Variabel die bepaalt of handler.py berichten moet versturen
    valid = False

    # Controleer bot token
    try:
        bot = telegram.Bot(token=token)
        botinfo = bot.getMe()

        # Controleer user id
        try:
            bot.send_message(text="Stock-watcher is begonnen", chat_id=user_id)
            print(f"Telegram bot {botinfo['username']} verbonden met gebruiker {user_id}")
            valid = True
        except:
            print("Gebruiker niet gevonden. Applicatie zal verder gaan zonder Telegram bot")
    except:
        print("Bot niet gevonden. Applicatie zal verder gaan zonder Telegram bot")

    return valid


def sendMsg(message):
    curr_time = datetime.datetime.now().strftime('%d-%b [%X]')

    try:
        bot = telegram.Bot(token=token)
        bot.send_message(text="Op voorraad! \n" + message, chat_id=user_id)
    except:
        print(f'{curr_time} - Telegram bericht verzenden MISLUKT, controleer gegevens en internetverbinding.')
