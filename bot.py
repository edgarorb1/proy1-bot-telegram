from tracemalloc import start
from turtle import update
from telegram.ext import Updater, CommandHandler
def start(update, context):
    update.message.reply_text('hola')
if __name__ == '__main__':
    
    updater = Updater(token='5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler()
    updater.start_polling(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()