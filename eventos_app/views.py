from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import EventoForm, ParticipanteFormSet
from django.contrib import messages
from .models import Evento

def registro_evento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)

        if evento_form.is_valid():
            evento = evento_form.save(commit=False)
            participante_formset = ParticipanteFormSet(request.POST, instance=evento)
            
            if participante_formset.is_valid():
                evento.save()
                participante_formset.save()
                messages.success(request, '🎉 Evento registrado con éxito y participantes guardados.')
                return redirect('registro_evento') 
            else:
                messages.error(request, 'Hubo un error con el registro de participantes. Por favor, revisa los datos.')
        else:
            messages.error(request, 'Hubo un error con el formulario del evento. Por favor, revisa los datos.')
            participante_formset = ParticipanteFormSet(instance=None)
            
    else:
        evento_form = EventoForm()
        participante_formset = ParticipanteFormSet(instance=None)

    context = {
        'evento_form': evento_form,
        'participante_formset': participante_formset,
    }
    return render(request, 'eventos_app/registro_evento.html', context)

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('fecha')
    context = {
        'eventos': eventos
    }
    return render(request, 'eventos_app/lista_eventos.html', context)