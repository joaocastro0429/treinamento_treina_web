from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def horario_atual(request):
    horario = datetime.datetime.now()
    return render(request,'lista_horario.html',{'horario':horario})
