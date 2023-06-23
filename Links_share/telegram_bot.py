import telegram.ext

# Token from Botfather telegram (API)
Token = '5845532348:AAEg-aU7WnCNoz_aK1UnAhYWjP_rAzafkQ$'

# Updater obj will perform action with our bot 
updater = telegram.ext.Updater("5845532348:AAEg-aU7WnCNoz_aK1UnAhYWjP_rAzafkQs", use_context=True)

dispatcher = updater.dispatcher

def Start(update, context):
    update.message.reply_text("Hello Welcome to linker")

def Help(update, context):
    update.message.reply_text("""
    /Start -> Welcome to the channel 
   /Help -> This particular message 
   /Content -> About various playlist of linker
   /Instagram -> My instagram page
   /Linkedin -> My Linkedin page
   /Twitter -> My Twitter account
    """)

def Content(update, context):
    update.message.reply_text(" Linker will add more link in future")

def Instagram(update, context):
    update.message.reply_text(" My Instagram link : https://www.instagram.com/ ")

def Linkedin(update, context):
    update.message.reply_text(" My Linkedin page: https://www.linkedin.com/ ")

def Twitter(update, context):
    update.message.reply_text(" My Twitter page: https://twitter.com/")

dispatcher.add_handler(telegram.ext.CommandHandler('Start', Start))
dispatcher.add_handler(telegram.ext.CommandHandler('Content', Content))
dispatcher.add_handler(telegram.ext.CommandHandler('Instagram', Instagram))
dispatcher.add_handler(telegram.ext.CommandHandler('Linkedin', Linkedin))
dispatcher.add_handler(telegram.ext.CommandHandler('Twitter', Twitter))
dispatcher.add_handler(telegram.ext.CommandHandler('Help', Help))

updater.start_polling()
updater.idle()