# eventos_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    # 1. Redirigir la raíz (/) a la lista de eventos
    path('', RedirectView.as_view(pattern_name='lista_eventos'), name='home'), # <--- ¡Nueva línea!

    path('admin/', admin.site.urls),
    
    # 2. Incluir las URLs de la aplicación (Mantenemos el include, pero lo movemos al final)
    path('', include('eventos_app.urls')),
]