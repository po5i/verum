from __future__ import unicode_literals
import time
import os
from django.db import models
from django.utils.crypto import get_random_string

def get_image_path(self, filename):
    #filename = time.strftime("%Y%m%d-%H%M%S") + filename
    random = get_random_string()
    filename = time.strftime("%Y%m%d-%H%M%S") + "-" + random
    return os.path.join("actas", filename)

# Create your models here.
class Acta(models.Model):
    provincia = models.CharField(max_length=200)
    parroquia = models.CharField(max_length=200,blank=True,null=True)
    circunscripcion = models.CharField(max_length=200,blank=True,null=True)
    zona = models.CharField(max_length=200,blank=True,null=True)
    canton = models.CharField(max_length=200)
    junta = models.CharField(max_length=200)
    genero = models.CharField(max_length=10,blank=True,null=True)
    
    lasso = models.IntegerField()
    moreno = models.IntegerField()
    blancos = models.IntegerField()
    nulos = models.IntegerField()
    foto = models.ImageField(upload_to=get_image_path)
    
    # metadata
    autor = models.CharField(max_length=200,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    useragent = models.CharField(max_length=200,blank=True,null=True)
    latitude = models.CharField(max_length=50,blank=True,null=True)
    longitude = models.CharField(max_length=50,blank=True,null=True)
    
    # flags
    flagged = models.BooleanField(default=False)
    verified1 = models.BooleanField(default=False)
    verified2 = models.BooleanField(default=False)
    notes = models.TextField(blank=True,null=True)