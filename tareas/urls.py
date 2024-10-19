# tareas/urls.py

from django.urls import path
from .views import listar_tareas, crear_tarea, editar_tarea, eliminar_tarea

urlpatterns = [
    path('', listar_tareas, name='listar_tareas'),  # Ruta para listar tareas
    path('crear/', crear_tarea, name='crear_tarea'),  # Ruta para crear una tarea
    path('editar/<int:pk>/', editar_tarea, name='editar_tarea'),  # Ruta para editar una tarea
    path('eliminar/<int:pk>/', eliminar_tarea, name='eliminar_tarea'),  # Ruta para eliminar una tarea
]
