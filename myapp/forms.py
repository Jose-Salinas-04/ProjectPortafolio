
from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['usuario', 'barbero', 'tipo_corte', 'fecha_hora', 'duracion']


'''
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
'''