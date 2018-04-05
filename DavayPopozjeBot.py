
import telebot
token = '501248582:AAEYt5VQlFmTLX5qj1erECajOD0Z76uAaI4'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except KeyboardInterrupt:
        exit()
