
import telebot
import config1 
from ethermine import Ethermine
import time
from loguru import logger

global currenthashrate

rigbot = telebot.TeleBot(config1.token)

logger.add("debug.log", format="{time} {level} {message}", level="INFO", rotation="1 MB")

@rigbot.message_handler(content_types='text')

def rig(message):
    ethermine = Ethermine() 
    stats = ethermine.miner_worker_current_stats("0x29d23ea65d0f8b311698c2423570d124173b6337", "scudaminer1")
    currenthashrate = stats.get('currentHashrate')
    hrinMHs = currenthashrate / 1000000
    rigbot.send_message(message.chat.id, text=f'RigscanBot On Air. Current Hashrate = {hrinMHs:.2f}MH/s. WatchDog on 140 MH/s')
    logger.info("On Air")
    while currenthashrate >= 140000000.00:
        logger.info(f"Current Hashrate = {hrinMHs:.2f}MH/s")
        time.sleep(30)
        stats = ethermine.miner_worker_current_stats("0x29d23ea65d0f8b311698c2423570d124173b6337", "scudaminer1")
        currenthashrate = stats.get('currentHashrate')

    rigbot.send_message(message.chat.id, text=f'scudaminer1 Low Hashrate = {hrinMHs:.2f}MH/s')
    rigbot.send_message(message.chat.id, text=f'Tap Start for begin Scanning')
    logger.info(f"Stop Scanning in Hashrate = {hrinMHs:.2f}MH/s")

if __name__ == '__main__': 

    rigbot.polling(none_stop=True) 