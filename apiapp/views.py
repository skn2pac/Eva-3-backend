# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
from apiapp.models import Alumno, Docente, Sala, Seccion, DirectorC
from apiapp.serializers import AlumnoSerializer, DocenteSerializer, SalaSerializer, SeccionSerializer, DirectorCSerializer
# from rest_framework.views import APIView
# from django.http import Http404

from rest_framework import generics, mixins
from rest_framework import viewsets

# Create your views here.

###################################################### ALUMNOS ######################################################

class AlumnoVS(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoL(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer


    def get(self,request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class AlumnoD(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)


###################################################### DOCENTES ######################################################

class DocenteVS(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class DocenteL(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


    def get(self,request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class DocenteD(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)


###################################################### SALAS ######################################################

class SalaVS(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class SalaL(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

###################################################### SECCIONES ######################################################

class SeccionVS(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class SeccionL(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer
    
###################################################### DIRECTORC ######################################################

class DirectorCVS(viewsets.ModelViewSet):
    queryset = DirectorC.objects.all()
    serializer_class = DirectorCSerializer