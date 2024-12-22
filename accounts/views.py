from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


@login_required
def home(request):
    return render(request, 'home.html')


def telegram_login(request):
    if not request.user.is_authenticated:
        return redirect('login')

    token = str(uuid.uuid4())
    user = request.user
    user.telegram_token = token
    user.save()

    telegram_bot_url = f"https://t.me/MyDjango_Auth_bot?start={token}"
    return redirect(telegram_bot_url)
