import simplematrixbotlib as botlib


async def help_message(room, event, bot):
    match = botlib.MessageMatch(room, event, bot, bot.prefix)
    if not (match.command("help") and match.prefix()):
        return

    message = "# Matrix Madlib Bot\n"+(
       "https://github.com/krazykirby99999/matrix-madlib-bot\n")+(
       "A Bot for the Matrix protocol that generates madlibs.\n")+(
       "Commands:\n")+(
       "help - Display help message")

    await bot.api.send_markdown_message(room.room_id, message)


def setup_bot(bot: botlib.Bot):
    bot.listener.on_message_event(
        lambda room, event: (help_message(
            room, event, bot)))
