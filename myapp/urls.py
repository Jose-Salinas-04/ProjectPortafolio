# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('agendar', views.agendar),
    path('nosotros/', views.nosotros),
    path('contactanos/', views.contactanos)
]