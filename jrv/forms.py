from django import forms
from .models import *

class ActaForm(forms.ModelForm):
    class Meta:
        model = Acta
        fields = (
            'provincia',
            'provincia',
            'circunscripcion',
            'zona',
            'canton',
            'junta',
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