from django.db import models

# Create your models here.
class Destino(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    actividades = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    usuario_creador = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, related_name='destinos_creados')
    usuario_modificador = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, related_name='destinos_modificados')
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.nombre}"


class Paquete(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    destinos = models.ManyToManyField(Destino, related_name='paquetes')
    fecha = models.DateField()

    usuario_creador = models.ForeignKey('auth.User', on_delete=models.PROTECT, null=True, related_name='paquetes_creados')
    usuario_modificador = models.ForeignKey('auth.User', on_delete=models.PROTECT, null=True, related_name='paquetes_modificados')
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.fecha}"
    
    # Método para calcular la suma de los destinos incluidos en el paquete
    @property
    def precio_total(self):
        total = sum(destino.costo for destino in self.destinos.all())
        return total
    

class Reserva(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    usuario = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    paquete = models.ForeignKey(Paquete, on_delete=models.PROTECT)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Confirmada')

    def __str__(self):
        return f"Reserva de:{self.usuario.username} - {self.paquete.nombre} - {self.estado}"
    