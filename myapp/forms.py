from django.forms import ModelForm
from django import forms
from .models import Cita, Usuario


''''
class ReservaForm(forms.ModelForm):
    usuario_nombre = forms.CharField(max_length=50)
    usuario_correo = forms.EmailField()
    usuario_telefono = forms.CharField(max_length=15)

    class Meta:
        model = Cita
        fields = ['barbero', 'tipo_corte', 'fecha_hora', 'duracion']


    def save(self, commit=True):
        usuario_data = {
            'nombre': self.cleaned_data.pop('usuario_nombre'),
            'correo': self.cleaned_data.pop('usuario_correo'),
            'telefono': self.cleaned_data.pop('usuario_telefono')
        }
        usuario, created = Usuario.objects.get_or_create(correo=usuario_data['correo'], defaults=usuario_data)
        cita = super().save(commit=False)
        cita.usuario = usuario
        if commit:
            cita.save()
        return cita


class CitaForm(ModelForm):
    class Meta:
        model = Cita
        fields = ["tipo_corte", "fecha_hora", "duracion"]
        '''