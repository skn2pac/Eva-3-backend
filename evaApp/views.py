from django.shortcuts import render
from evaApp.models import Alumno, Docente, Sala, Seccion, DirectorC
from evaApp.forms import alumnoRegistro
from evaApp.formD import FormDocente
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


    ###############################

def index(request):
    return render(request, 'index.html')

def listadoDocente(request):
    docentes = Docente.objects.all()
    data = {'docentes': docentes}
    return render(request, 'evaApp/lista_docente.html', data)

def agregarDocente(request):
    form = FormDocente()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    data = {'form': form}
    return render(request, 'evaApp/registrarDocente.html', data)


def eliminarDocente(request, id):
    docente = Docente.objects.get(id = id)
    docente.delete()
    return redirect('/listaDocente/')

def actualizarDocente(request, id):
    docente = Docente.objects.get(id = id)
    form = FormDocente(instance = docente)
    if request.method == 'POST':
        form = FormDocente(request.POST, instance = docente)
        if form.is_valid():
            form.save()
    data = {'form': form}
    return render(request, 'evaApp/docente.html', data)

def sala(request):
    sal = Sala.objects.all()
    data = {'sala':sal}
    return render(request, 'evaApp/sala.html', data)

def seccion(request):
    sec = Seccion.objects.all()
    data= {'seccion':sec}
    return render(request, 'evaApp/seccion.html',data)

def directorC(request):
    d = DirectorC.objects.all()
    data = {'directorC':d}
    return render(request, 'evaApp/directorC.html',data)