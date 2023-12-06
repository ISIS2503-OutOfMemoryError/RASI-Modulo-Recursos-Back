from django.urls import path
from . import views  # Importa tus vistas

urlpatterns = [
    # Ruta para crear una sede (POST)
    path('crear_sede/', views.sede_create, name='crear_sede'),
    # Ruta para actualizar una sede (PUT)
    path('put_sede/', views.sede_update, name='actualizar_sede'),
]