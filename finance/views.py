from django.shortcuts import render,redirect 
from .models import *
# Create your views here.
import csv
import io
from datetime import datetime
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



def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile =  request.FILES['myfile']
       #lendo o arquivo
        file = myfile.read().decode('utf-8')
        re = csv.DictReader(io.StringIO(file))
        #gerando uma lista
        data = [line for line in re]
        save_data(data)
        print(data)
        return redirect('index')
    return render(request,'index.html')
