import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler,Filters
from telegram import  ChatAction
from PIL import Image
INPUT_TEXT = 0
INPUT_TEXT2 = 0
inpuf_final = ''
def start(update, context):
    update.message.reply_text("Cuestionario de validación para ingreso seguro\nIstrucciones")
    update.message.reply_text("Responda a cada una de las siguientes preguntas con SI o NO")
    
def qr_command_handler(update, context):
    update.message.reply_text("texto ")
    return INPUT_TEXT
    
def qr_command_handler(update, context):
    update.message.reply_text("texto ")
    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    return filename

def send_qr(filename, chat):
    chat.send_action(ChatAction.UPLOAD_PHOTO,timeout=None)
    chat.send_photo(photo=open(filename, 'rb'))
    os.unlink(filename)


def input_text(update, context):
    global inpuf_final
    inpuf_final = update.message.text
    chat = update.message.chat      
    print(inpuf_final)
    return ConversationHandler.END
def input_text2(update, context):
    global inpuf_final
    text = update.message.text + ' . '+ inpuf_final
    print(inpuf_final)
    filename=generate_qr(text)
    chat = update.message.chat   
    send_qr(filename, chat)
    return ConversationHandler.END

if __name__ == '__main__':
    
    updater = Updater('5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('qr',qr_command_handler)],
    states={INPUT_TEXT: [MessageHandler(Filters.text, input_text)]},
   
    fallbacks=[]))
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('qr1',qr_command_handler)],
    states={INPUT_TEXT2: [MessageHandler(Filters.text, input_text2)]},
   
    fallbacks=[]))

    updater.start_polling()
    updater.idle()