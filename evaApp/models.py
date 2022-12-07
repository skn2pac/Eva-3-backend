from django.db import models
from evaApp.choices import salas

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    fono = models.CharField(max_length=15)
    nivelAcademico = models.CharField(max_length=50)
    anos_exp = models.IntegerField()
    especialidad = models.CharField(max_length=50)

    class Meta:
        verbose_name='Docente'
        verbose_name_plural='Docentes'
        db_table='docente'
        ordering=['apellido']
    
    #creamos el formato para mostrar el nombre del docente en el apartado de registrar al alumno
    #pasandole los valores de nombre y apellido para luego utilizar el str y dar forma

    def nombre_docente(self):
        return "{} {}".format(self.nombre,self.apellido)

    def __str__(self):
        return self.nombre_docente()

class Alumno(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    fono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    ex_liceo = models.CharField(max_length=20)
    carrera = models.CharField(max_length=20)

    class Meta:
        verbose_name='Alumno'
        verbose_name_plural='Alumnos'
        db_table='alumno'
        ordering=['apellido']

    def nombre_alumno(self):
        return "{} {}".format(self.nombre,self.apellido)
    
    def __str__(self):
        return self.nombre_alumno()


class Seccion(models.Model):
    cod_seccion = models.CharField(max_length=8)
    alumnos_asignados = models.ManyToManyField(Alumno)
    docente_cargo = models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Seccion'
        verbose_name_plural='Secciones'
        db_table='seccion'
        ordering=['cod_seccion']


    # def __str__(self):
    #     return self.cod_seccion


class Sala(models.Model):
    cod_sala = models.CharField(max_length=5,choices=salas)
    cod_seccion = models.ForeignKey(Seccion,null=True,blank=True,on_delete=models.CASCADE)
    #docente_cargo = models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Sala'
        verbose_name_plural='Salas'
        db_table='sala'
        ordering=['cod_sala']

class DirectorC(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    rut = models.CharField(max_length=20)
    seccion_cargo = models.ManyToManyField(Seccion)

    def nombre_director(self):
        return "{} {}".format(self.nombre,self.apellido)
    
    def __str__(self):
        return self.nombre_director()

    class Meta:
        verbose_name='Director de Carrera'
        verbose_name_plural='Directores de carrera'
        db_table='director_carrera'
        ordering=['apellido']