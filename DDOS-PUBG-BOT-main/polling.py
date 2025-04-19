import telebot

bot = telebot.TeleBot("7143587146:AAEhsSJycaIrjhfXUrG7B9hjQ0sJRmxbOtk")

# Delete existing webhook to switch to polling
bot.remove_webhook()

# Now start polling
bot.polling()
