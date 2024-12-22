from telegram.ext import Updater, CommandHandler
from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_auth_project.settings')
django.setup()

User = get_user_model()


def start(update, context):
    token = context.args[0] if context.args else None
    if token:
        try:
            user = User.objects.get(telegram_token=token)
            user.telegram_id = update.effective_user.id
            user.telegram_username = update.effective_user.username
            user.telegram_token = None
            user.save()

            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Вы успешно авторизовались как {user.username}!"
            )
        except User.DoesNotExist:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неверный токен.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Токен отсутствует.")


def run_bot():
    updater = Updater(token=os.getenv('TELEGRAM_BOT_TOKEN'), use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run_bot()
