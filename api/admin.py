from django.contrib import admin
from api.models import Destino, Paquete, Reserva

# Register your models here.
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'costo', 'usuario_creador', 'usuario_modificador', 'fecha_modificacion')
    search_fields = ('nombre', 'descripcion', 'actividades')
    list_filter = ('costo',)

class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'usuario_creador', 'usuario_modificador', 'fecha_modificacion')
    search_fields = ('nombre',)
    list_filter = ('fecha',)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'paquete', 'fecha_reserva', 'estado')
    search_fields = ('usuario__username', 'paquete__nombre')
    list_filter = ('estado',)

admin.site.register(Destino, DestinoAdmin)
admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(Reserva, ReservaAdmin)