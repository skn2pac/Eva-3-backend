"""evaluacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from evaApp.views import renderIndex, alumnoData,alumnoRegistrationView,eliminarAlumno,actualizarAlumno,agregarDocente,eliminarDocente,listadoDocente,sala, seccion, directorC,actualizarDocente
from apiapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('alumnos', views.AlumnoVS)
router.register('docentes',views.DocenteVS)
router.register('salas',views.SalaVS)
router.register('secciones',views.SeccionVS)
router.register('directorc', views.DirectorCVS)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', renderIndex, name='index'),
    # path('alumnos/', alumnoData, name='alumnos'),
    # path('registrar/', alumnoRegistrationView, name='registrar'),
    # path('eliminarAlumno/<int:id>',eliminarAlumno),
    # path('actualizarAlumno/<int:id>',actualizarAlumno),
    # path('registrarDocente/', agregarDocente, name='docentes'),
    # path('listaDocente/', listadoDocente, name='listaDocente'),
    # path('eliminarDocente/<int:id>',eliminarDocente),
    # path('actualizarDocente/<int:id>',actualizarDocente),
    # path('salas/',sala, name='sala'),
    # path('seccion/',seccion, name='seccion'),
    # path('directorC/',directorC,name='directorC'),
    # ###############################################
    # path('alumnoapi/', views.AlumnoL.as_view()),
    # path('alumnoapi/<int:pk>', views.AlumnoD.as_view()),

    path('', include(router.urls))
    
]
