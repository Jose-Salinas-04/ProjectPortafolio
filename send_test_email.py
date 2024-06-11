# -*- coding: utf-8 -*-
import os
import django
from django.core.mail import send_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

try:
    send_mail(
        'Prueba de Envío de Correo',
        'Este es un correo de prueba con caracteres especiales: ñ, á, é, í, ó, ú.',
        'folioporta228@gmail.com',
        ['destinatario@ejemplo.com'],
        fail_silently=False,
    )
    print("Correo enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar el correo: {e}")
