import telebot
import yfinance as yf
import time
import re
from private import bot_token


bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def handle(message):
	bot.send_message(message.chat.id, 'Welcome to the stock market bot! Type /help to see what commands are available at the moment!')



@bot.message_handler(commands=['help'])
def handle(message):
	bot.send_message(message.chat.id, 'The following commands are available at the moment:\n\n \
/price - Shows the current price and some historical prices \n\
/performance - Shows the performance of a stock for different time periods \n\
/whatdoes - Shows the general information about a company')


def get_message_text_without_command(msg):
	return re.sub('\/[a-z]+\s', '', msg.text)
