import telegram.ext

with open('TOKEN.txt', 'r') as f:
    token = f.read()

def start(update, context):
    update.message.reply_text('Hello! Welcome to Xprints!')

def help(update, context):
    update.message.reply_text('''
    The following commands are available:
    
    /start -> Start Xprints
    /help -> Contact Xprints
    /print -> Print  some documents
    /scan -> Scan some documents
    ''')

def print(update, context):
    update.message.reply_text('Upload a document')

def scan(update, context):
    update.message.reply_text('Scan some documents')

def handler_message(update, context):
    update.message.reply_text(f'You said {update.message.text},'
                              f'this is not a valid Xprints command '
                              f' please select a valid command from the help menu -> /help')


updater = telegram.ext.Updater(token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('help', help))
disp.add_handler(telegram.ext.CommandHandler('scan', scan))
disp.add_handler(telegram.ext.CommandHandler('print', print))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handler_message))

updater.start_polling()
updater.idle()