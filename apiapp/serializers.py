from rest_framework import serializers
from apiapp.models import Alumno,Docente,Sala,Seccion,DirectorC


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'
    

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

    cod_seccion = serializers.SlugRelatedField(read_only=False,queryset=Seccion.objects.all(),slug_field='cod_seccion')

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ('__all__')

    # con el slugrelatedfield nos permite ingresar un manytomany en el html usando un property en el model, el slugfield se nombra por el campo en base de datos, se asigna
    # el queryset para permitir ingresar los datos

    alumnos_asignados = serializers.SlugRelatedField(many=True,queryset=Alumno.objects.all(),slug_field="nombre_apellido")
    
    docente_cargo = serializers.SlugRelatedField(read_only=False,queryset=Docente.objects.all(),slug_field='nombre_apellido')

class DirectorCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorC
        fields = '__all__'

    seccion_cargo = serializers.SlugRelatedField(many=True,queryset=Seccion.objects.all(),slug_field='cod_seccion')
    