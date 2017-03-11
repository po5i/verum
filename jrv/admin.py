from django.contrib import admin

# Register your models here.
from .models import *

class ActaAdmin(admin.ModelAdmin):
    list_display = ('junta','timestamp','flagged','verified1','verified2')

admin.site.register(Acta, ActaAdmin)