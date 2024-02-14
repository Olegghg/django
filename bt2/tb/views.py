from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib.auth import login, authenticate
from functools import wraps
from django.shortcuts import redirect

def login_required(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        if 'user_id' in request.session:
            return f(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrap


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    context = {'error': None}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(name=username)
            if check_password(password, user.password):
                # Устанавливаем ID пользователя в сессии
                request.session['user_id'] = user.id
                return redirect('home')  # Перенаправление на главную страницу
            else:
                # Неверный пароль
                context['error'] = "Пароль не верный"
        except User.DoesNotExist:
            # Пользователь не найден
            context['error'] = "Пользователь не найден"

    return render(request, 'login.html', context)
@login_required
def home(request):
    user_id = request.session.get('user_id')  # Получение ID пользователя из сессии
    user = User.objects.get(id=user_id)  # Получение объекта пользователя по ID
    context = {'user_name': user.name}
    return render(request, 'home.html', context)

@login_required
def user_logout(request):
    del request.session['user_id']
    return redirect('login')
