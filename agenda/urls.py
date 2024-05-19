from django.contrib import admin
from django.urls import path
from agenda.views import index, exibir_extrato

urlpatterns = [
    path('', index),
    path('extratos', exibir_extrato)
]