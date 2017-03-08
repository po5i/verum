from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    context = {}
    return render(request, 'jrv/index.html', context)

def resultados(request):
    context = {}
    return render(request, 'jrv/resultados.html', context)

def opendata(request):
    data = {
        'some_var_1': 'foo',
        'some_var_2': 'bar',
    }
    return JsonResponse(data)