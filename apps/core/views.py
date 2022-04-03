


from django.contrib import messages

from django.shortcuts import render

from .models import listbanks

# Create your views here.
def home(request):
    template_name = 'base.html'
    return render(request, template_name, {})

def listagem(request):
    template_name = 'listagem.html'
    bancos = listbanks.objects.all()
    context = {'bancos': bancos}

    return render(request, template_name, context)

def consulta(request):
    template_name = 'consulta.html'
    search = request.GET.get('search')
    if search=='':
        search = 0
        messages.warning(request, 'Digite um Numero!')

    bancos = listbanks.objects.filter(cod_compensacao=search)
    print(bancos)

    if search in bancos:
        messages.error(request, 'Banco não Encontrado!')
        print(bancos)
    
    context = {'bancos': bancos}

    return render(request, template_name, context)