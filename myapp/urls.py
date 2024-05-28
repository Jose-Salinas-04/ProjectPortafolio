from django.urls import path
from . import views
#Se traspasan las urls desde urls de mysite

urlpatterns = [
    path("", views.index),
    path("fechayhora/", views.fechayhora),
    path("form_contacto/", views.form_contacto),
    path("contactanos/", views.contactanos)
]