from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem



root_logger= logging.getLogger()
root_logger.setLevel(logging.INFO)
handler = logging.FileHandler('bot1.log', 'w', 'utf-8')
handler.setFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
root_logger.addHandler(handler)

planets = {
    'mercury': ephem.Mercury(),
    'venus': ephem.Venus(),
    'mars': ephem.Mars(),
    'jupiter': ephem.Jupiter(),
    'saturn': ephem.Saturn(),
    'uranus': ephem.Uranus(),
    'neptune': ephem.Neptune()
            }


def greet_user(bot, update):
    greet_text = "Вызван /start"
    logging.info(greet_text)
    update.message.reply_text(greet_text)


def get_constellation(bot, update):
    logging.info(update.message.text)

    command, planet = update.message.text.strip().split(' ')

    planet = ephem.star(planet, "2016/07/07")
    print(planet)

    print(ephem.constellation(planet))

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал {}".format(update.message.chat.username, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    my_bot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info("Бот запускается")

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    dp.add_handler(CommandHandler("planet", get_constellation))

    my_bot.start_polling()
    my_bot.idle()


main()