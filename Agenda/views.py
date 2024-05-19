from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from agenda.models import extratos

# Criação de Views
def index(request):
    return HttpResponse("Olá Mundo!")
  

def exibir_extrato(request):
    # Selecionar objeto na lista
    extrato = extratos[0]
    # # Encontrar template
    # template = loader.get_template("agenda/exibir_extrto.html")
    # # Renderizar template
    # rendered_template = template.render(context={"extrato":extrato}, request=request)
    # # Retorna o valor pra API
    # return HttpResponse(rendered_template)
    return render(request=request, context={"extrato":extrato}, template_name="agenda/exibir_extrato.html")