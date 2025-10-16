from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SimpleRegistrationForm, SimpleLoginForm

def simple_register(request):
    """Простая регистрация"""
    if request.method == 'POST':
        form = SimpleRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Создается запись в БД
            login(request, user)  # Автоматический вход
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')  # На главную страницу
    else:
        form = SimpleRegistrationForm()
    data={'css_file': 'users/style_login_register.css',
          'form': form,}
    return render(request, 'users/simple_register.html', data,)

def simple_login(request):
    """Простой вход"""
    if request.method == 'POST':
        form = SimpleLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'С возвращением, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Неверный логин или пароль')
    else:
        form = SimpleLoginForm()
    data={'css_file': 'users/style_login_register.css',
          'form': form,}
    return render(request, 'users/simple_login.html', data)

def simple_logout(request):
    """Выход"""
    logout(request)
    messages.info(request, 'Вы вышли из системы')
    return redirect('home')