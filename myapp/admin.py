from django.contrib import admin
from .models import Barbero
from .models import Usuario
from .models import Cita
from .models import TipoCorte
from .models import Comentario


# Register your models here
admin.site.register(Barbero)
admin.site.register(Usuario)
admin.site.register(TipoCorte)
admin.site.register(Comentario)