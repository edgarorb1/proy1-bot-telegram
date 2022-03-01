import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler,Filters
from telegram import  ChatAction
from PIL import Image
INPUT_TEXT = 0
INPUT_TEXT2 = 0
INPUT_TEXT3 = 0
text2 = ''
text3 = ''
text4 = ''
text5 = ''
text6 = ''
text7 = ''
text8 = ''
nombre=''
firma=''
fecha=''
alerta=''
alerta2=''
alerta3=''
alerta4=''
alerta5=''
alerta6=''
alerta7=''
inpuf_final = ''
salto = '\n'
def start(update, context):
    update.message.reply_text("Cuestionario de validación para ingreso seguro")
    update.message.reply_text("Istrucciones\nResponda las siguientes 7 preguntas con SI o NO")
    update.message.reply_text("Accede a las preguntas \n/1\n/2\n/3\n/4\n/5\n/6\n/7")
    
def pregunta1(update, context):
    update.message.reply_text("¿Tiene fiebre?")
    return INPUT_TEXT

def pregunta2(update, context):
    update.message.reply_text("¿Tiene tos?")
    return INPUT_TEXT
def pregunta3(update, context):
    update.message.reply_text("¿Siiente dolor de cabeza?")
    return INPUT_TEXT
def pregunta4(update, context):
    update.message.reply_text("¿Tienes Malestar general: dolor muscular y/o de articulaciones?")
    return INPUT_TEXT
def pregunta5(update, context):
    update.message.reply_text("¿Tiene tos y/o estornudos?")
    return INPUT_TEXT
def pregunta6(update, context):
    update.message.reply_text("¿Tiene catarro?")
    return INPUT_TEXT
def pregunta7(update, context):
    update.message.reply_text("¿Ha estado en contacto con algun paciente 'caso sospechoso' o diagnositicado con covid-19?")
    return INPUT_TEXT
    


def generate_qr(text1):
    filename =  'qr.jpg'
    img = qrcode.make(text1)
    img.save(filename)
    return filename

def send_qr(filename, chat):
    chat.send_action(ChatAction.UPLOAD_PHOTO,timeout=None)
    chat.send_photo(photo=open(filename, 'rb'))
    os.unlink(filename)


def input_text(update, context):
    global text2
    global nombre
    global firma
    global alerta
    text2 ="¿Tiene fiebre? "+update.message.text 
    chat = update.message.chat   
    nombre = "Nombre: "+ update.message.chat.first_name +   update.message.chat.last_name
    firma =  "Firma: "+ str(update.message.chat.id)
    if text2 == "¿Tiene fiebre? Si" or text2 == "¿Tiene fiebre? si" 	or text2 == "¿Tiene fiebre? SI":
        alerta="ALERTA1!!!!!!!"
    else:
        alerta=""
    print(nombre)
    print(firma)
    return ConversationHandler.END

def input_text2(update, context):
    global text3
    global alerta2
    text3 ="¿Tiene tos? "+update.message.text 
    chat = update.message.chat      
    print(text3)
    if text3 == "¿Tiene tos? Si" or text3 == "¿Tiene tos? si" 	or text3 == "¿Tiene tos? SI":
        alerta2="ALERTA2!!!!!!!"
    else:
        alerta2=""
    return ConversationHandler.END
def input_text3(update, context):
    global text4
    global alerta3
    text4 ="¿Siiente dolor de cabeza? "+update.message.text 
    chat = update.message.chat      
    print(text4)
    if text4 == "¿Siiente dolor de cabeza? Si" or text4 == "¿Siiente dolor de cabeza? si" 	or text4 == "¿Siiente dolor de cabeza? SI":
        alerta3="ALERTA3!!!!!!!"
    else:
        alerta3=""
    return ConversationHandler.END
def input_text4(update, context):
    global text5
    global alerta4
    text5 ="¿Tienes Malestar general: dolor muscular y/o de articulaciones? "+update.message.text 
    chat = update.message.chat  
    if text5 == "¿Tienes Malestar general: dolor muscular y/o de articulaciones? Si" or text5 == "¿Tienes Malestar general: dolor muscular y/o de articulaciones? si" 	or text5 == "¿Tienes Malestar general: dolor muscular y/o de articulaciones? SI":
        alerta4="ALERTA4!!!!!!!"
    else:
        alerta4=""    
    print(text5)
    return ConversationHandler.END
def input_text5(update, context):
    global text6
    global alerta5
    text6 ="¿Tiene tos y/o estornudos? "+update.message.text 
    chat = update.message.chat      
    print(text6)
    if text6 == "¿Tiene tos y/o estornudos? Si" or text6 == "¿Tiene tos y/o estornudos? si" 	or text6 == "¿Tiene tos y/o estornudos? SI":
        alerta5="ALERTA5!!!!!!!"
    else:
        alerta5=""
    return ConversationHandler.END
def input_text6(update, context):
    global text7
    global alerta6
    text7 ="¿Tiene catarro? "+update.message.text 
    chat = update.message.chat      
    print(text7)
    if text7 == "¿Tiene catarro? Si" or text7 == "¿Tiene catarro? si" 	or text7 == "¿Tiene catarro? SI":
        alerta6="ALERTA6!!!!!!!"
    else:
        alerta6=""
    return ConversationHandler.END
def input_text7(update, context):
    global alerta7
    global text2
    global text3
    global text4
    global text5
    global text6
    global text7
    global text8
    global nombre
    global firma
    text8 ="¿Ha estado en contacto con algun paciente 'caso sospechoso' o diagnositicado con covid-19? "
    if text8+update.message.text == "¿Ha estado en contacto con algun paciente 'caso sospechoso' o diagnositicado con covid-19? Si" or text8+update.message.text == "¿Ha estado en contacto con algun paciente 'caso sospechoso' o diagnositicado con covid-19? si" 	or text8+update.message.text == "¿Ha estado en contacto con algun paciente 'caso sospechoso' o diagnositicado con covid-19? SI":
        alerta7="ALERTA7!!!!!!!"
    else:
        alerta7=""
    text = text2+salto+text3+salto+text4+salto+text5+salto+text6+salto+text7+salto+text8 + " " +update.message.text+salto+salto+salto+nombre+salto+firma+salto+salto+alerta+alerta2+alerta3+alerta4+alerta5+alerta6+alerta7
    filename=generate_qr(text)
    chat = update.message.chat 
   
    send_qr(filename, chat)     
    print(text8)
    return ConversationHandler.END

if __name__ == '__main__':
    
    updater = Updater('5246990550:AAEdax6SS8kbL385Ttift8HvfArdLhX6W8w', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('1',pregunta1)],
    states={INPUT_TEXT: [MessageHandler(Filters.text, input_text)]},
    fallbacks=[]))
    
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('2',pregunta2)],
    states={INPUT_TEXT2: [MessageHandler(Filters.text, input_text2)]},
    fallbacks=[]))

    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('3',pregunta3)],
    states={INPUT_TEXT3: [MessageHandler(Filters.text, input_text3)]},
    fallbacks=[]))

    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('4',pregunta4)],
    states={INPUT_TEXT3: [MessageHandler(Filters.text, input_text4)]},
    fallbacks=[]))

    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('5',pregunta5)],
    states={INPUT_TEXT3: [MessageHandler(Filters.text, input_text5)]},
    fallbacks=[]))

    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('6',pregunta6)],
    states={INPUT_TEXT3: [MessageHandler(Filters.text, input_text6)]},
    fallbacks=[]))

    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('7',pregunta7)],
    states={INPUT_TEXT3: [MessageHandler(Filters.text, input_text7)]},
    fallbacks=[]))

    updater.start_polling()
    updater.idle()