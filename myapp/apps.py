from django.apps import AppConfig

# myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la página de inicio")

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
