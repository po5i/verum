from __future__ import unicode_literals

from django.db import models

def get_image_path(self,filename):
    filename = time.strftime("%Y%m%d-%H%M%S") + filename
    return os.path.join("actas", filename)

# Create your models here.
class Acta(models.Model):
    provincia = models.CharField(max_length=200)
    parroquia = models.CharField(max_length=200,blank=True,null=True)
    circunscripcion = models.CharField(max_length=200,blank=True,null=True)
    zona = models.CharField(max_length=200,blank=True,null=True)
    canton = models.CharField(max_length=200)
    junta = models.CharField(max_length=200)
    
    lasso = models.IntegerField()
    moreno = models.IntegerField()
    blancos = models.IntegerField()
    nulos = models.IntegerField()
    zona = models.CharField(max_length=200,blank=True,null=True)
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