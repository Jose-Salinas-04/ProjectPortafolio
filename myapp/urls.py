from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('index', views.index),
    path('agendar', views.agendar),
    path('nosotros', views.nosotros),
    path('contactanos', views.contactanos)
]
=======
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('fechayhora/', views.fechayhora, name='fechayhora'),
    path('reservar/', views.reservar, name='reservar'),  # Asegúrate de que esta línea exista
]
>>>>>>> 88b85e65360820a310cc0a09da08f61f526105b1
