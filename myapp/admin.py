from django.contrib import admin
from .models import Barbero
from .models import Usuario
from .models import Cita
from .models import TipoCorte

# Register your models here
admin.site.register(Barbero)
admin.site.register(Usuario)
admin.site.register(Cita)
admin.site.register(TipoCorte)

