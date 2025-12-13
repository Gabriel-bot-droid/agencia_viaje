from rest_framework import serializers
from .models import Destino, Paquete, Reserva

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'nombre', 'descripcion', 'actividades', 'costo', 'usuario_creador', 'usuario_modificador', 'fecha_modificacion']


class PaqueteSerializer(serializers.ModelSerializer):
    destino = DestinoSerializer(many=True, read_only=True)
    #Como es relacion ManyToMany se usa PrimaryKeyRelatedField y many=True
    destinos_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Destino.objects.all(),source='destino', write_only=True) #Para escribir los id de los destinos al crear o actualizar un paquete
    
    class Meta:
        model = Paquete
        fields = ['id', 'nombre', 'destino', 'destinos_id', 'fecha', 'usuario_creador', 'usuario_modificador', 'fecha_modificacion', 'precio_total']


class ReservaSerializer(serializers.ModelSerializer):
    # Se muestra el nombre del usuario y del paquete
    nombre_usuario = serializers.CharField(source='usuario.username', read_only=True)
    nombre_paquete = serializers.CharField(source='paquete.nombre', read_only=True)

    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'nombre_usuario', 'paquete', 'nombre_paquete', 'fecha_reserva', 'estado']