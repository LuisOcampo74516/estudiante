from django.db import models

# Create your models here.
class Estudiante(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombre = models.CharField(max_length=50)
 apellidos = models.CharField(max_length=50)
 edad = models.IntegerField()
 email = models.EmailField()