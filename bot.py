from cgitb import text
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

INPUT_TEXT = 0

def start(update, context):
    button1 = InlineKeyboardButton(
        text='si',url= None)
    #button2 = InlineKeyboardButton( text='no')
    update.message.reply_text(text='haz clic en un boton', reply_markup=InlineKeyboardButton([button1]))

if __name__ == '__main__':
    
    updater = Updater(token='5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler( CommandHandler('start',start))
    updater.start_polling()
    updater.idle()