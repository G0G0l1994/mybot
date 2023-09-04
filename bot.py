import logging
from datetime import datetime
from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename="bot.log",level=logging.INFO,encoding='utf-8')


def greet_user(update,context):
    print('Бот начал работу /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')
def talk_to_me(update,context):
    user_text=update.message.text
    print(user_text)
    update.message.reply_text(user_text)   

def main():
    mybot=Updater(settings.API_KEY,use_context=True)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    date=datetime.now().strftime('%D-%M-%Y %H:%M')
    logging.info(f'Бот стартовал {date}')
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    mybot.start_polling()
    mybot.idle()

if __name__=="__main__":
    main()