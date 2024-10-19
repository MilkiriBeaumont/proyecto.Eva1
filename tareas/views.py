from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tareas

def listar_tareas(request):
    """Lista todas las tareas en la base de datos."""
    try:
        tareas = Tareas.objects.all()  # Obtiene todas las tareas
    except Exception as e:
        print(f'Error al listar tareas: {e}')
        print(tareas)
        tareas = []  # En caso de error, asigna una lista vacía

    return render(request, 'vista.html', {'tareas': tareas})# Renderiza la plantilla con las tareas



def crear_tarea(request):
    """Crea una nueva tarea a partir de los datos del formulario."""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion', '')
        
        try:
            Tareas.objects.create(titulo=titulo, descripcion= descripcion)  # Crea la tarea
            messages.success(request, 'Tarea creada con éxito')  # Mensaje de éxito
            
        except Exception as e:
            print(f'Error al crear tarea: {e}')  # Manejo de errores
            messages.error(request, 'Error al crear la tarea')

        return redirect('listar_tareas')  # Redirige a la lista de tareas
    return render(request, 'crear.html')  # Renderiza la plantilla para crear una tarea

from .models import Tareas  # Asegúrate de que el nombre sea correcto

def editar_tarea(request, pk):
    """Edita una tarea existente."""
    tarea = get_object_or_404(Tareas, pk=pk)  # Obtiene la tarea por ID
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion', '')

        try:
            tarea.titulo = titulo  # Actualiza el título
            tarea.descripcion = descripcion  # Actualiza la descripción
            tarea.save()  # Guarda los cambios
            messages.success(request, 'Tarea actualizada con éxito')  # Mensaje de éxito
            return redirect('listar_tareas')  # Redirige a la lista de tareas
        except Exception as e:
            print(f'Error al actualizar tarea: {e}')  # Manejo de errores
            messages.error(request, 'Error al actualizar la tarea')

    return render(request, 'editar.html', {'tarea': tarea})  # Renderiza la plantilla para editar la tarea

def eliminar_tarea(request, pk):
    """Elimina una tarea existente."""
    try:
        tarea = get_object_or_404(Tareas, pk=pk)  # Obtiene la tarea por ID
        tarea.delete()  # Elimina la tarea
        messages.success(request, 'Tarea eliminada con éxito')  # Mensaje de éxito
    except Exception as e:
        print(f'Error al eliminar tarea: {e}')  # Manejo de errores
        messages.error(request, 'Error al eliminar la tarea')

    return redirect('listar_tareas')  # Redirige a la lista de tareas