from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.core import serializers
from django.http import Http404

def index(request):
    context = {}
    return render(request, 'jrv/index.html', context)

def contactenos(request):
    context = {}
    return render(request, 'jrv/contactenos.html', context)
	
def resultados(request):
    actas = Acta.objects.all()
    
    lasso = moreno = blancos = nulos = 0
    
    for acta in actas:
        lasso = lasso + acta.lasso
        moreno = moreno + acta.moreno
        blancos = blancos + acta.blancos
        nulos = nulos + acta.nulos
    
    context = {
        "actas": actas,
        "lasso": lasso,
        "moreno": moreno,
        "blancos": blancos,
        "nulos": nulos,
    }
    return render(request, 'jrv/resultados.html', context)

def acta(request, acta_id):
    try:
        acta = Acta.objects.get(id=acta_id)
        
        context = {
            "acta": acta,
        }
        return render(request, 'jrv/acta.html', context)
    except:
        raise Http404

def opendata(request):
    data = serializers.serialize("json", Acta.objects.all())
    return HttpResponse(data, content_type='application/json')


@csrf_protect
def register(request):
    
    # TODO: backend validation
    
    # TODO: reducir tamano de imagen
    
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
