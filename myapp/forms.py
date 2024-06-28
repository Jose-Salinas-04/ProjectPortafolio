from django import forms
from .models import Cita

from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_cliente', 'apellido_cliente', 'email_cliente', 'telefono_cliente', 'edad_cliente', 'observaciones', 'fecha_cita', 'hora_cita', 'barbero']

