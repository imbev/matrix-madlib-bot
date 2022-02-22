import os
import simplematrixbotlib as botlib
from dotenv import load_dotenv
import madlib_bot


def main():
    load_dotenv()
    HOMESERVER = os.environ.get('HOMESERVER')
    USERNAME = os.environ.get('BOT_USERNAME')
    PASSWORD = os.environ.get('PASSWORD')
    TOKEN = os.environ.get('TOKEN')
    PREFIX = os.environ.get('PREFIX')

    creds = botlib.Creds(
        HOMESERVER, USERNAME, password=PASSWORD, access_token=TOKEN)
    bot = botlib.Bot(creds)

    madlib_bot.setup_bot(bot)
    bot.run()


if __name__ == '__main__':
    main()
