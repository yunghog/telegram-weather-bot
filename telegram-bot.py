from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
from selenium import webdriver
from random import randint

def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='hello my nigger')

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

def dp_(bot, update):
    print("dp called")
    url='https://picsum.photos/500'
    response=requests.get(url)
    driver=webdriver.Chrome()
    driver.get(response.url)
    pic=driver.find_element_by_xpath('/html/body/img')
    src=pic.get_attribute('src')
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=src)
    driver.close()

def reply(bot, update):
    user_input = update.message.text
    if 'hi' in user_input:
        update.message.reply_text("Aye! What's up homie")



def main():
    updater = Updater('1230910993:AAECpkgUiUn0tNB6_UzUh5LpmSZEpZQ_ub8')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('dp',dp_))
    dp.add_handler(CommandHandler('pic',pic))
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
