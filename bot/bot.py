from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = f"Привет {update.message.chat.first_name}! Ты написал: {update.message.text}"
    logging.info(f"User: {update.message.chat.username}, "
                 f"Chat id: {update.message.chat.id}, "
                 f"Message: {update.message.text}")
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY)

    logging.info("Bot starting")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
