# myapp/views.py
from django.shortcuts import render

def index(request):
    title = ("Bienvenido a Master Court Master Court - Maipu")
    return render(request, 'index.html',{
        "title" : title,
    })

def agendar(request):
    return render(request, 'agendar.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contactanos(request):
    return render(request, 'contactanos.html')
