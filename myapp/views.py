# ProjectPortafolio/myapp/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def fechayhora(request):
    return render(request, 'fechayhora.html') 

