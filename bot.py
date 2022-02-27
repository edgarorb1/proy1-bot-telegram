from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyMarkup

def start(update, context):
    update.message.reply_text('hola')
    button1 = InlineKeyboardButton( text='si')
    button2 = InlineKeyboardButton( text='no')
    update.message.reply_text('haz clic en un boton', ReplyMarkup=InlineKeyboardButton([button1],[button2]))

if __name__ == '__main__':
    
    updater = Updater(token='5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler( CommandHandler('start',start))
    updater.start_polling()
    updater.idle()