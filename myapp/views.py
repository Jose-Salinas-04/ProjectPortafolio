from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import models
# Create your views here.

def index(request):
    return render(request, "index.html")

def fechayhora(request):
    return render(request, "fechayhora.html")

def form_contacto(request):
    return render(request, "form_contacto.html")

def contactanos(request):
    return render(request, "contactanos.html")