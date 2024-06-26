from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('fechayhora/', views.fechayhora, name='fechayhora'),
    path('administrador/', views.administrador, name='administrador'),
    path('reservar/', views.reservar_cita, name='reservar_cita'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),  # Vista para la página de confirmación
]


