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


@bot.message_handler(commands=['whatdoes'])
def handle(message):
    ticker = yf.Ticker(get_message_text_without_command(message))
    bot.send_message(message.chat.id, ticker.info['longBusinessSummary'])


@bot.message_handler(commands=['performance'])
def handle(message):
	#Work in progress
    ticker = yf.Ticker(get_message_text_without_command(message))
    bot.send_message(message.chat.id, ticker.history(period="max"))


@bot.message_handler(commands=['price'])
def handle(message):
    ticker = yf.Ticker(get_message_text_without_command(message))
    price = ticker.info['regularMarketPrice']
    open = ticker.info['regularMarketOpen']
    increase = (float(price) - float(open)) / float(open) * float(100)
    dayHigh = ticker.info['dayHigh']
    fiftyTwoWeekLow = ticker.info['fiftyTwoWeekLow']
    fiftyTwoWeekHigh = ticker.info['fiftyTwoWeekHigh']
    dayLow = ticker.info['dayLow']
    prevClose = ticker.info['regularMarketPreviousClose']
    fiftyDayAverage = ticker.info['fiftyDayAverage']
    twoHundredDayAverage = ticker.info['twoHundredDayAverage']
    bot.send_message(message.chat.id, 'Current price of {}: {}\nPrevious close: {}\nOpened today at: {}\nIncrease since open: {}%\nDay low: {}\nDay high: {}\n52 weeks low: {}\n52 weeks high: {}\n200 days average: {}'.format(get_message_text_without_command(message), price, prevClose,open,increase, dayLow, dayHigh,fiftyTwoWeekLow, fiftyTwoWeekHigh, twoHundredDayAverage))


bot.polling()


# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# - interval: True/False (default False) - The interval between polling requests
#           Note: Editing this parameter harms the bot's response time
# - timeout: integer (default 20) - Timeout in seconds for long polling.

#tb.polling(none_stop=False, interval=0, timeout=20)
