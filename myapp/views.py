# myapp/views.py
from django.shortcuts import render

def index(request):
    title = ("Bienvenido a Master Court Master Court - Maipu")
    return render(request, 'index.html',{
        "title" : title,
    })

def fechayhora(request):
    return render(request, 'fechayhora.html')

def form_contacto(request):
    return render(request, 'form_contacto.html')

def contactanos(request):
    return render(request, 'contactanos.html')
