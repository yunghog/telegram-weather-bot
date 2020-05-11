from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, ConversationHandler
import requests
import re
from selenium import webdriver
from random import randint
import json
import weather

def start(bot, update):
    chat_id = update.message.chat_id
    description="""
    Yo! What's up, Im Joey the Bot
    I can do some cool stuff
    """
    bot.send_message(chat_id=chat_id, text=description)

def pic(bot, update):
    print('pic called')
    url='https://picsum.photos/1080/1920'
    response=requests.get(url)
    driver=webdriver.Chrome()
    rurl=response.url
    driver.get(rurl)
    pic=driver.find_element_by_xpath('/html/body/img')
    src=pic.get_attribute('src')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=src)
    driver.close()

def read(bot, update):
    user_input = update.message.text
    if 'hi' in user_input:
        update.message.reply_text("Aye! What's up homie\nWhats yo name")

def weather_(bot, update):
    chat_id = update.message.chat_id
    city = update.message.text.split(' ')
    result=weather.tellWeather(city[-1])
    bot.send_message(chat_id=chat_id, text=result)


def main():
    key=open('config.json','r')
    key=json.load(key)
    print(key["telegram_bot_token"])
    updater = Updater(key["telegram_bot_token"])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('pic',pic))
    dp.add_handler(CommandHandler('weather',weather_))
    dp.add_handler(MessageHandler(Filters.text, read))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
