from django.db import models

# Create your models here.

class Tareas(models.Model):
    titulo = models.CharField(max_length=200,default=False)
    descripcion = models.CharField(max_length=200,default=False)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.titulo,self.descripcion
    class Meta: db_table = 'tareas'