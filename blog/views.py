from django.shortcuts import render
from .models import Campo

# Create your views here.

def muestraDatos(request):
    consulta = Campo.objects.all()
    listaSuma = calculaSuma(consulta)
    contexto = zip(consulta, listaSuma)
    return render(request, 'blog/index.html', {'contexto': contexto})

def calculaSuma(lista):
    listaSuma = []
    for i in lista:
        listaSuma.append(i.var1 + i.var3 + i.var4)
    return listaSuma