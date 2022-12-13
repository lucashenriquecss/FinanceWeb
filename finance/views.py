from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import auth, messages
# Create your views here.
import csv
import io
from datetime import datetime
from django.contrib.auth.decorators import login_required



def save_data(data):
    #salvar os dados no banco
    aux = []
    for item in data:
        bancoorigem = item.get('bancoorigem')
        agenciaorigem = item.get('agenciaorigem')
        contaorigem = item.get('contaorigem')
        bancodestino = item.get('bancodestino')
        agenciadestino = item.get('agenciadestino')
        contadestino = item.get('contadestino')
        valor = item.get('valor')
        data = item.get('data')
        obj = Transacao(
            bancoorigem=bancoorigem,
            agenciaorigem=agenciaorigem,
            contaorigem=contaorigem,
            bancodestino=bancodestino,
            agenciadestino=agenciadestino,
            contadestino=contadestino,
            valor=valor,
            data=data
        )
        aux.append(obj)
    Transacao.objects.bulk_create(aux)


@login_required(login_url='login')
def importcsv(request):
  
    dados = Transacao.objects.all()
    
 
    if request.method == 'POST' and request.FILES['myfile']:
        myfile =  request.FILES['myfile']
       #lendo o arquivo
        file = myfile.read().decode('utf-8')
        re = csv.DictReader(io.StringIO(file))
        #gerando uma lista
        data = [line for line in re]
        save_data(data)
        return redirect('importcsv')
    return render(request,'pages/dashboard/importarcsv.html',{'dados':dados})

    
@login_required(login_url='login')
def historic(request):
    dados = Transacao.objects.order_by('data').distinct('data')
    return render(request,'pages/dashboard/historic.html',{'dados':dados})


@login_required(login_url='login')
def detail_transacoes(request,id):
    infos = Transacao.objects.get(pk=id)
    return render(request,'pages/dashboard/detail-transacao.html',{'infos':infos})





#USERS
@login_required(login_url='login')
def detailUser(request, id):
    info = get_object_or_404(User,pk=id)
    return render(request,'pages/dashboard/profile.html',{'info':info})

@login_required(login_url='login')
def removeUser(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('users_list')
    
@login_required(login_url='login')    
def users_list(request):
    users = User.objects.all()
    return render(request, 'pages/dashboard/users.html',{'users':users})

