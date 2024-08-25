import telebot
import setting
from random import choice

# Создание экземпляра бота с токеном из файла settings
bot = telebot.TeleBot(token=setting.BOT_TOKEN)

# Обработчик команды /coin
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    # Выбор случайной стороны монеты
    coin = choice(["ОРЕЛ", "РЕШКА"])
    # Отправка ответа пользователю
    bot.reply_to(message, coin)

# Запуск бота
if __name__ == "__main__":
    try:
        print("Бот запущен...")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
