from django import forms
from .models import *

class ActaForm(forms.ModelForm):
    class Meta:
        model = Acta
        fields = (
            'provincia',
            'parroquia',
            'circunscripcion',
            'zona',
            'canton',
            'junta',
            'genero',
            'lasso',
            'moreno',
            'blancos',
            'nulos',
            'foto',
            'autor',
            'useragent',
            'latitude',
            'longitude'
        )
