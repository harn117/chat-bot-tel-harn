import telebot

# Create a bot
bot = telebot.TeleBot("7303366791:AAGT9q5V832Ah8lSUDLygL5lnMRV_w-vKBI")

""" # Set the bot's name
bot.setName("HarnBot") """

# set funcionality
@bot.message_handler(commands=['start'])
def start(message):
    bot.sendMessage(message, "Hello, I'm HarnBot!")

@bot.message_handler(func=lambda message: True)
def echoall(message):
    bot.sendMessage(message, message.text)
if __name__ == '__main__':
    bot.polling(none_stop=True) 