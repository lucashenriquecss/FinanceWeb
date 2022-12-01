
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth




@login_required(login_url='login')
def dashboard(request):
    """#verificar se usuario esta logado"""
    if request.user.is_authenticated:           
        return render(request, 'pages/dashboard/dashboard.html',)   
    else:
        return redirect('login')
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
           
    return render(request, 'pages/user/login.html')


@login_required(login_url='login')
def registro(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name,email,password)
        user.save()
        messages.success(request, 'Conta criada com sucesso!')
        redirect('users_list')
    return render(request, 'pages/user/cadastro.html')


def logout(request): 
    auth.logout(request)#saida do usuario
    return redirect('login')   
