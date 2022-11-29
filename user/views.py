from django.shortcuts import render, redirect
from django.contrib import auth, messages
# Create your views here.
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'pages/dashboard/dashboard.html')
# Usuario


def login(request):
    return render(request, 'pages/user/login.html')


def registro(request):
    """CADASTRA UMA NOVA PESSOA NO SISTEMA"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']

        if campo_vazio(nome):  # verificação para evitar campos em branco ou com espaços
            messages.error(request, 'O nome não pode ficar em branco.')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, ' O e-mail não pode ficar em branco')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Está conta ja existe, tente outra!')
            # verificando email se ja esta criado ou nao
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.warning(request, 'Está conta ja existe, tente outra!')
            # verificando nome se ja esta criado ou nao
            return redirect('cadastro')

        user = User.objects.create_user(
            username=nome, email=email)
        user.save()
        messages.success(request, 'Conta criada com sucesso!')
        return redirect('login')
    else:
        return render(request, 'pages/user/cadastro.html')


def campo_vazio(campo):
    return not campo.strip()
