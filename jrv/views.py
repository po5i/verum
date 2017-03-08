from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.core import serializers

def index(request):
    context = {}
    return render(request, 'jrv/index.html', context)

def resultados(request):
    context = {}
    return render(request, 'jrv/resultados.html', context)

def opendata(request):
    data = serializers.serialize("json", Acta.objects.all())
    return HttpResponse(data, content_type='application/json')


@csrf_protect
def register(request):
    
    # TODO: backend validation
    
    try:
        form = ActaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
            data = {
                'flag': 'ok',
            }
        else:
            data = {
                'flag': 'ko',
                'message': 'Form is not valid'
            }
    except Exception as e:
        data = {
            'flag': 'ko',
            'message': str(e)
        }
        
    return JsonResponse(data)