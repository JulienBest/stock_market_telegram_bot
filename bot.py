import telebot
import yfinance as yf
import time
import re
from private import bot_token


bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def handle(message):
	bot.send_message(message.chat.id, 'Welcome to the stock market bot! Type /help to see what commands are available at the moment!')
