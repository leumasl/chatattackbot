from telegram.ext import Updater
updater = Updater(token='403985840:AAEPQBb3UhfJchCIYbg3Ed9i0ztl4fjIZiA')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
