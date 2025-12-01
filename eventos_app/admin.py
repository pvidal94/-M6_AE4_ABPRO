from django.contrib import admin
from .models import Evento, Participante

# Mostrar el evento y sus participantes en la misma página de edición
class ParticipanteInline(admin.TabularInline):
    model = Participante
    extra = 1

class EventoAdmin(admin.ModelAdmin):
    inlines = [ParticipanteInline]
    list_display = ('nombre', 'fecha', 'ubicacion')
    search_fields = ('nombre', 'ubicacion')

admin.site.register(Evento, EventoAdmin)
admin.site.register(Participante)