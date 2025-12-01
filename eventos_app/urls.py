# eventos_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_evento, name='registro_evento'),
    path('lista/', views.lista_eventos, name='lista_eventos'), # <--- ¡Nueva línea!
]