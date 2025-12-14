from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .serializers import DestinoSerializer, PaqueteSerializer, ReservaSerializer
from .models import Destino, Paquete, Reserva


# Create your views here.

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    
    def get_permissions(self):
        #si la accion es get, cualquier usuario puede ver la lista o detalle
        if self.action == 'list' or self.action == 'retrieve':
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [permissions.IsAdminUser]
        return [permission() for permission in permissions_classes]

    def perform_create(self, serializer):
        print("Usuario que crea el destino:", self.request.user)
        serializer.save(usuario_creador=self.request.user)

    def perform_update(self, serializer):
        print("Usuario que modifica el destino:", self.request.user)
        serializer.save(usuario_modificador=self.request.user)


class PaqueteViewSet(viewsets.ModelViewSet):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer
    #se define los permisos permitidos, y se bloquea put y patch
    http_method_names = ['get', 'post', 'delete']
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [permissions.IsAdminUser]
        return [permission() for permission in permissions_classes]
    
    def perform_create(self, serializer):
        print("Usuario que crea el paquete:", self.request.user)
        serializer.save(usuario_creador=self.request.user)


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    #el usuario autenticado solo puede ver sus reservas y el admin ve todas
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Reserva.objects.all()
        else:
            return Reserva.objects.filter(usuario=user)
        
    def perform_create(self, serializer):
        print("Usuario que crea la reserva:", self.request.user)
        serializer.save(usuario=self.request.user)