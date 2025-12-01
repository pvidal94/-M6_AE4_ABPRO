from django import forms
from .models import Evento, Participante
from datetime import date

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha <= date.today():
            raise forms.ValidationError("La fecha del evento debe ser futura.")
        return fecha

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and len(nombre) > 100:
            raise forms.ValidationError("El nombre del evento no debe superar los 100 caracteres.")
        return nombre

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre', 'correo_electronico']

ParticipanteFormSet = forms.inlineformset_factory(
    Evento, 
    Participante, 
    form=ParticipanteForm, 
    extra=1, 
    can_delete=False
)