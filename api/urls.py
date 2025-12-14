from django.urls import path, include
from rest_framework import routers, viewsets
from rest_framework.routers import DefaultRouter
from .views import DestinoViewSet, PaqueteViewSet, ReservaViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = DefaultRouter()
router.register(r'destinos', DestinoViewSet)
router.register(r'paquetes', PaqueteViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]