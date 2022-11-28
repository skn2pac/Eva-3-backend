from django.shortcuts import render
from evaApp.models import Alumno
from evaApp.forms import alumnoRegistro
from django.shortcuts import redirect

# Create your views here.

def renderIndex(request):
    return render(request, 'evaApp/index.html')

def alumnoData(request):
    alumnos = Alumno.objects.all()
    data = {'alumnos': alumnos}
    return render(request, 'evaApp/alumnos.html',data)


def alumnoRegistrationView(request):
    form = alumnoRegistro()

    if request.method == 'POST':
        form = alumnoRegistro(request.POST)
        if form.is_valid():
            form.save()
    data = {'form':form}
    return render(request, 'evaApp/registrarAlumno.html', data)


def eliminarAlumno(request,id):
    alumnos = Alumno.objects.get(id = id)
    alumnos.delete()
    return redirect('/alumnos/')

def actualizarAlumno(request,id):
    alumno = Alumno.objects.get(id = id)
    form = alumnoRegistro(instance = alumno)
    if request.method == 'POST':
        form = alumnoRegistro(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
    data = {'form':form}
    return render(request,'evaApp/registrarAlumno.html',data)

