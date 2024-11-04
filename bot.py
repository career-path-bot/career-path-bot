from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я помогу тебе с профессиональной ориентацией. Давай начнем!")

# Основная функция для запуска бота
def main():
    # Укажи свой токен
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
