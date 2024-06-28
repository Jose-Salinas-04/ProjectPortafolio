from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from .forms import CitaForm
from .models import Cita

def index(request):
    title = "Bienvenido a Master Court Master Court - Maipu"
    return render(request, 'index.html', {"title": title})

def nosotros(request):
    return render(request, 'nosotros.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def administrador(request):
    return render(request, 'administrador.html')

def confirmacion(request):
    return render(request, 'confirmacion.html')


def reservar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
    else:
        form = CitaForm()
    return render(request, 'reservar_cita.html', {'form': form})

def confirmacion(request):
    return render(request, 'confirmacion.html')

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'lista_citas.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'crear_cita.html', {'form': form})

def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'editar_cita.html', {'form': form})

def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')
    return render(request, 'eliminar_cita.html', {'cita': cita})
