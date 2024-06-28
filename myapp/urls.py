from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('administrador/', views.administrador, name='administrador'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('reservar_cita/', views.reservar_cita, name='reservar_cita'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('lista_citas/', views.lista_citas, name='lista_citas'),
    path('cita/nueva/', views.crear_cita, name='crear_cita'),
    path('cita/<int:pk>/editar/', views.editar_cita, name='editar_cita'),
    path('cita/<int:pk>/eliminar/', views.eliminar_cita, name='eliminar_cita'),
]
