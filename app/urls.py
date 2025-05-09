

from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.horario_atual, name='horario_atual')
]
