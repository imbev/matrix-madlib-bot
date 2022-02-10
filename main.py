import os
import simplematrixbotlib as botlib
import madlib_bot


if __name__ == '__main__':
    HOMESERVER = os.environ.get('HOMESERVER')
    USERNAME = os.environ.get('USERNAME')
    TOKEN = os.environ.get('TOKEN')
    creds = botlib.Creds(
        HOMESERVER, USERNAME, access_token=TOKEN)
    bot = botlib.Bot(creds)

    madlib_bot.setup_bot(bot)
    bot.run()
