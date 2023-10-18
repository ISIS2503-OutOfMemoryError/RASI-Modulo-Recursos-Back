from django.urls import path
from . import views  # Importa tus vistas

urlpatterns = [
    # Ruta para crear una sede (POST)
    path('crear_equipo/', views.equipo_create),
    # Ruta para actualizar una sede (PUT)
    #path('put_equipo/', views.equipo_update),
]