from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage

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


@csrf_protect
def register(request):
    """
    provincia = request.POST.get("provincia")
    parroquia = request.POST.get("parroquia")
    circunscripcion = request.POST.get("circunscripcion")
    zona = request.POST.get("zona")
    canton = request.POST.get("canton")
    junta = request.POST.get("junta")
    lasso = request.POST.get("lasso")
    moreno = request.POST.get("moreno")
    blancos = request.POST.get("blancos")
    nulos = request.POST.get("nulos")
    autor = request.POST.get("autor")
    useragent = request.POST.get("useragent")
    latitude = request.POST.get("latitude")
    longitude = request.POST.get("longitude")
    foto = request.FILES.get('file')
    """
    
    # TODO: backend validation
    
    try:
        """
        acta = Acta()
        acta.provincia = provincia
        acta.parroquia = parroquia
        acta.circunscripcion = circunscripcion
        acta.zona = zona
        acta.canton = canton
        acta.junta = junta
        acta.lasso = lasso
        acta.moreno = moreno
        acta.blancos = blancos
        acta.nulos = nulos
        acta.autor = autor
        acta.useragent = useragent
        acta.latitude = latitude
        acta.longitude = longitude
        #acta.foto = foto
        acta.save()
        """
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