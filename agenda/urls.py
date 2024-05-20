from django.contrib import admin
from django.urls import path
from agenda.views import Exibir_Extratos, Exibir_Extrato, Home

urlpatterns = [
    path('', Home),
    path('extratos', Exibir_Extratos, name="Exibir_Extratos"),
    path('extratos/<int:id>/', Exibir_Extrato, name="Exibir_Extrato")
]