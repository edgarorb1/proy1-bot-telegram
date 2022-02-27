from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton 

INPUT_TEXT = 0

def start(update, context):
    button1 = InlineKeyboardButton(
        text='sobre el autor',
        url='https://lugofev.com'
    )
    
    update.message.reply_text(
        text='haz clic en un boton',
        reply_markup=InlineKeyboardMarkup([
            [button1]
            ])
    )

if __name__ == '__main__':
    
    updater = Updater('5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler( CommandHandler('start', start))
    updater.start_polling()
    updater.idle()