from django.contrib import admin

# Register your models here.
from .models import *

class ActaAdmin(admin.ModelAdmin):
    list_display = ('junta','timestamp','flagged')

admin.site.register(Acta, ActaAdmin)