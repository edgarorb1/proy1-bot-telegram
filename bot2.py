import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler,Filters
from telegram import  InlineKeyboardMarkup, InlineKeyboardButton, ChatAction

INPUT_TEXT = 0

def start(update, context):
    update.message.reply_text("Hola aaa ")

def qr_command_handler(update, context):
    update.message.reply_text("texto ")
    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    return filename

def send_qr(filename, chat):
    chat.send_action(action=ChatAction.UPLOAD_PHOTO)
    chat.send_photo(photo=open(filename, 'rb'))
    os.unlink(filename)


def input_text(update, context):
    text= update.message.text
    filename=generate_qr(text)
    chat = update.messsage.chat    
    send_qr(filename,chat)
    return ConversationHandler.END

if __name__ == '__main__':
    
    updater = Updater('5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('qr',qr_command_handler)],
    states={INPUT_TEXT: [MessageHandler(Filters.text, input_text)]},
    fallbacks=[]))

    updater.start_polling()
    updater.idle()