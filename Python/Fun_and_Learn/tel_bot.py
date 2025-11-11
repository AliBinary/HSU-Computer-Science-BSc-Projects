from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5497579687:AAEIP96DNd_TsCMs_ajCCQjBa9fTLixJgCU",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the Ali's Bot.Please write\
     /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/youtube - To get my youtube URL
	/number - To get my Phone number
	/gmail - To get my gmail
	/telegram - To get my telegram ID""")


def gmail(update: Update, context: CallbackContext):
    update.message.reply_text("my Gmail ==> \
     acount.ali.gh@gmail.com)")


def youtube(update: Update, context: CallbackContext):
    update.message.reply_text("my Youtube Link =>\
	https://www.youtube.com/channel/UC6GQxwifkc4xlOOlsARGnCA/featured")


def number(update: Update, context: CallbackContext):
    update.message.reply_text("my phone number => \
     +98 9152609984")


def telegram(update: Update, context: CallbackContext):
    update.message.reply_text("my telegram id => \
     @Third_FanTasTic")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('number', number))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail))
updater.dispatcher.add_handler(CommandHandler('telegram', telegram))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
