from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre_apellido = models.CharField(max_length=35)
    direccion = models.CharField(max_length=15)
    fono = models.CharField(max_length=15)
    nivelAcademico = models.CharField(max_length=50)
    anios_exp = models.IntegerField()
    especialidad = models.CharField(max_length=50)

    class Meta:
        verbose_name='Docente Api'
        verbose_name_plural='Docentes Api'
        db_table='docente_api'
        ordering=['nombre_apellido']
    
    #creamos el formato para mostrar el nombre del docente en el apartado de registrar al alumno
    #pasandole los valores de nombre y apellido para luego utilizar el str y dar forma

    def nombre_docente(self):
        return "{}".format(self.nombre_apellido)

    def __str__(self):
        return self.nombre_docente()


class Alumno(models.Model):
    jornadas = (('Diurno','Diurno'), ('Vespertino','Vespertino'))

    nombre_apellido = models.CharField(max_length=35)
    jornada = models.CharField(max_length=11,choices=jornadas)
    email = models.CharField(max_length=20)
    fono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    ex_liceo = models.CharField(max_length=20)
    carrera = models.CharField(max_length=20)

    class Meta:
        verbose_name='Alumno Api'
        verbose_name_plural='Alumnos Api'
        db_table='alumno_api'
        ordering=['nombre_apellido']

    def nombre_alumno(self):
        return "{}".format(self.nombre_apellido)
    
    def __str__(self):
        return self.nombre_alumno()



class Seccion(models.Model):
    cod_seccion = models.CharField(max_length=8)
    alumnos_asignados = models.ManyToManyField(Alumno)
    docente_cargo = models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Seccion Api'
        verbose_name_plural='Secciones Api'
        db_table='seccion_api'
        ordering=['cod_seccion']


    def codigo(self):
        return "{}".format(self.cod_seccion)
    
    def __str__(self):
        return self.codigo()
    



class Sala(models.Model):
    salas = ( ('Ñ401','Ñ401'), ('Ñ402','Ñ402'),('Ñ403','Ñ403'),('Ñ404','Ñ404'),('Ñ405','Ñ405'),('Ñeica','Ñeica'))
    cod_sala = models.CharField(max_length=5,choices=salas)
    cod_seccion = models.ForeignKey(Seccion,null=True,blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Sala Api'
        verbose_name_plural='Salas Api'
        db_table='sala_api'
        ordering=['cod_sala']

class DirectorC(models.Model):
    nombre_apellido = models.CharField(max_length=20)
    rut = models.CharField(max_length=20)
    seccion_cargo = models.ManyToManyField(Seccion)

    def nombre_director(self):
        return "{}".format(self.nombre_apellido)
    
    def __str__(self):
        return self.nombre_director()

    class Meta:
        verbose_name='Director de Carrera Api'
        verbose_name_plural='Directores de carrera Api'
        db_table='director_carrera_api'
        ordering=['nombre_apellido']