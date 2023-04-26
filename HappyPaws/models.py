from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    nombre = models.CharField(max_length= 50,default="Sin Nombre")
    raza = models.CharField(max_length= 50,default="Perro")
    fecha = models.DateField(auto_now_add=True)
    tel= models.CharField(max_length=50)
    mail=models.EmailField(max_length=100)
    ciudad=models.CharField(max_length=50)
    estado=models.CharField(max_length=100, default="En adopción")
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="owner")
    imagen=models.ImageField(upload_to="images",null=True,blank=True)


    def __str__(self):
        return f"Identificación: {self.id} - Creado el: {self.fecha} - Nombre: {self.nombre} - Estado: {self.estado}"
    
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE,related_name="profile")
    imagen=models.ImageField(upload_to="profiles",null=True,blank=True)

        










# Create your models here.
