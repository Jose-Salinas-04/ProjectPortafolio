from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View

def index(request):
    title = ("Bienvenido a Master Court Master Court - Maipu")
    return render(request, 'index.html',{
        "title" : title,
    })

def agendar(request):
    return render(request, 'agendar.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def fechayhora(request):
    return render(request, 'fechayhora.html')

def administrador(request):
    return render(request, 'administrador.html')



@csrf_exempt
def reservar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data['nombre']
            apellido = data['apellido']
            email = data['email']
            telefono = data['telefono']
            edad = data['edad']
            observaciones = data['observaciones']
            profesional = data['profesional']
            servicio = data['servicio']
            fecha = data['fecha']
            hora = data['hora']

            # Validar los datos aquí

            # Enviar el correo electrónico
            subject = 'Detalles de su reserva'
            message = f"""
            Estimado {nombre} {apellido},

            Gracias por su reserva. Aquí están los detalles de su reserva:

            Profesional: {profesional}
            Servicio: {servicio}
            Fecha: {fecha}
            Hora: {hora}

            Si tiene alguna pregunta, no dude en contactarnos.

            Saludos,
            El equipo de Master Court
            """
            try:
                send_mail(subject, message, 'folioporta228@gmail.com', [email])
                return JsonResponse({'status': 'success'})
            except BadHeaderError:
                return JsonResponse({'status': 'fail', 'error': 'Invalid header found.'})
            except Exception as e:
                logger.error(f"Error sending email: {str(e)}")
                return JsonResponse({'status': 'fail', 'error': str(e)})

        except KeyError as e:
            return JsonResponse({'status': 'fail', 'error': f'Missing key: {e}'})
        except Exception as e:
            return JsonResponse({'status': 'fail', 'error': str(e)})

    return JsonResponse({'status': 'fail'})


