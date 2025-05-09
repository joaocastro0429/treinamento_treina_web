from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
import datetime
from .forms import ClienteForm

# Create your views here.

def horario_atual(request):
    horario_atual = datetime.datetime.now()
    return render(request,'lista_horario.html',{'horario':horario_atual})

def form_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('horario_atual')
    form = ClienteForm()
    return render(request, 'form_cliente.html', context={'form': form})