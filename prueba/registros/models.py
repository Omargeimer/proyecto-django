from django.db import models
from ckeditor.fields import RichTextField
#Crear un modelo para administrar los cursos almacenando los datos que consideres necesarios "usa almenos 5 tipos de datos diferentes" (debes incluir una fecha de creación).

# Create your models here.
class Alumnos(models.Model):#define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12,verbose_name="Mat") #Texto corto, el verbose name es para la vista de admin
    nombre = models.TextField()#Texto largo
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Actualizado") #Fecha y tiempo

    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self) -> str:
        return self.nombre
        #Indica que se mostrará el nombre como valor en la tabla

#Identificar los cambios: python manage.py makemigrations registros 
#Aplicar los cambios: python manage.py migrate registros 
# Crear superusuario: python manage.py createsuperuser
    

class Comentario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumnos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self) -> str:
        return self.coment
    

class ComentarioContacto(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    usuario = models.TextField(verbose_name="Usuario")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.mensaje