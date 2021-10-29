
import telebot
from telebot import types #директория types в библиотеке telebot для кнопок
import config1 #токен
import ethermine
from ethermine import Ethermine
import time

global currenthashrate

rigbot = telebot.TeleBot(config1.token)

@rigbot.message_handler(content_types='text')

def rig(message):
    ethermine = Ethermine() 
    stats = ethermine.miner_worker_current_stats("0x29d23ea65d0f8b311698c2423570d124173b6337", "3070")
    currenthashrate = stats.get('currentHashrate')
    while currenthashrate != 8888888.888888888:
        print(currenthashrate)
        time.sleep(300)
        stats = ethermine.miner_worker_current_stats("0x29d23ea65d0f8b311698c2423570d124173b6337", "3070")
        currenthashrate = stats.get('currentHashrate')

    rigbot.send_message(message.chat.id, text='!!!!!!!!!!')

if __name__ == '__main__': #если выполняется непосредственно тело модуля, то цикл повторяется бесконечно (для исключения
    #зависания при импорте модуля) Устойчивое выражение
    rigbot.polling(none_stop=True) #Цикл непрерывной проверки входящих условий