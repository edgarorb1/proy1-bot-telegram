import os
from fileinput import filename
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler,Filters
from telegram import Chat, InlineKeyboardMarkup, InlineKeyboardButton, ChatAction

INPUT_TEXT = 0

def start(update, context):
    update.message.reply_text("Hola ")

def qr_command_handler(update, context):
    update.message.reply_text("texto ")
    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    return filename

def send_qr(filename, chat):
    chat.send_action(action=ChatAction.UPLOAD_PHOTO,timeout=None)
    chat.send_photo(photo=open(filename,'rb'))
    os.unlink(filename)


def input_text(update, context):
    text= update.message.text
    print(text)
    chat = update.messsage.chat
    filename=generate_qr(text)

    send_qr(filename,chat)
    return ConversationHandler.END

 #   button1 = InlineKeyboardButton(
  #      text='sobre el autor',
   #     url='https://lugofev.com'
   # )
    
  #  update.message.reply_text(
   ##    reply_markup=InlineKeyboardMarkup([
     #       [button1]
      #      ])
    #)

if __name__ == '__main__':
    
    updater = Updater('5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler( CommandHandler('start', start))

    dp.add_handler(entry_points=[CommandHandler('qr',qr_command_handler)]),
    states={INPUT_TEXT: [MessageHaandler(Filters.text,input_text)]},
    fallbacks=[]

    updater.start_polling()
    updater.idle()