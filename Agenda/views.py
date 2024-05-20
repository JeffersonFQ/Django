from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from agenda.models import Evento


def Home(request):
    return render(request=request, template_name="agenda/Home.html")

# Exibir todos os lançamentos
def Exibir_Extratos(request):
    # Buscar lançamentos por tipo
    extratos = Evento.objects.all()
    # Exibir em um template
    return render(request=request, context={"extratos":extratos}, template_name="agenda/exibir_extratos.html")
  
# Exibir UM único lançamento
def Exibir_Extrato(request, id):
    # Selecionar objeto na lista
    extrato = Evento.objects.get(id=id)
    # Renderizar Template
    return render(request=request, context={"extrato":extrato}, template_name="agenda/exibir_extrato.html")