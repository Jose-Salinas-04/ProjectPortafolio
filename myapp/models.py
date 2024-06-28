from django.db import models

# Create your models here.
def __str__(self):
        return self.nombre  

class Localizacion(models.Model):
        pais = models.CharField(max_length=100)
        region = models.CharField(max_length=100)
        comuna = models.CharField(max_length=100)

class Comentario(models.Model):
        descripcion = models.CharField(max_length=250)
        valorizacion = models.DecimalField(max_digits=2, decimal_places=1)

class HorarioTrabajo(models.Model):
        barbero = models.ForeignKey('Barbero', on_delete=models.CASCADE)
        dia_semana = models.IntegerField()
        horario_inicio = models.TimeField()
        horario_fin = models.TimeField()

class TipoCorte(models.Model):
        descripcion = models.CharField(max_length=50)

        def __str__(self):
                return self.descripcion

class Barbero(models.Model):
        nombre = models.CharField(max_length=50)

        def __str__(self):
                return self.nombre



class Usuario(models.Model):
        nombre = models.CharField(max_length=50)
        correo = models.EmailField(unique=True)
        telefono = models.CharField(max_length=15)
        comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)


        
class Meta:
        unique_together = ('barbero', 'fecha_hora')

class Barberia(models.Model):
        nombre = models.CharField(max_length=50)
        direccion = models.CharField(max_length=250)
        telefono = models.CharField(max_length=15)
        correo = models.EmailField(unique=True)
        valorizacion = models.DecimalField(max_digits=2, decimal_places=1)
        barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)


class Cita(models.Model):
        nombre_cliente = models.CharField(max_length=100, default='Nombre Predeterminado')
        apellido_cliente = models.CharField(max_length=100, default='Apellido Predeterminado')
        email_cliente = models.EmailField(default='default@example.com')
        telefono_cliente = models.CharField(max_length=15, default='0000000000')
        edad_cliente = models.IntegerField(default=0)
        observaciones = models.TextField(blank=True, null=True)
        fecha_cita = models.DateField(default='2000-01-01')
        hora_cita = models.TimeField(default='12:00')
        barbero = models.CharField(max_length=100, default='Barbero Predeterminado')

        def __str__(self):
                return f"{self.nombre_cliente} {self.apellido_cliente} - {self. fecha_cita} {self.hora_cita}"



