# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('fechayhora/', views.fechayhora),
    path('form_contacto/', views.form_contacto),
    path('contactanos/', views.contactanos)
]