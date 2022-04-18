from asyncio.log import logger
import Constants as keys
from telegram.ext import *
import Responses as R

# Initialize the bot
print("Initializing bot...        OK...     bot initialized and started")

#create bot start command
def start_command(update, context):
    update.message.reply_text("Bot started Type something to get started")

#help command
def help_command(update, context):
    update.message.reply_text("This is my help options use it to interact with me!")

#create a handle message function to reply to the user
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)


#error function
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    print(f"Update {update} caused error {context.error}")


# Create the main function that will be called when the bot is started
def main():
    updater = Updater(keys.BOT_TOKEN, use_context=True)
    dspatcher  = updater.dispatcher

    dspatcher.add_handler(CommandHandler('start', start_command))
    dspatcher.add_handler(CommandHandler('help', help_command))

    dspatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dspatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
