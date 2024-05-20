from django.contrib import admin
from agenda.models import Tipo, Evento

# Register your models here.
admin.site.register(Evento)
admin.site.register(Tipo)
