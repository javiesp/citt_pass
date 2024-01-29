from django.db import models

# Create your models here.
class usuario_citt(models.model):
    fecha_ingreso = models.DateField()
    usaurio_uid = models.CharField(max_lenght=255)
    comentario = models.CharField(max_lenght=255)