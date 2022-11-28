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
from django.urls import path
from evaApp.views import renderIndex
from evaApp.views import alumnoData
from evaApp.views import alumnoRegistrationView
from evaApp.views import eliminarAlumno
from evaApp.views import actualizarAlumno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', renderIndex, name='index'),
    path('alumnos/', alumnoData, name='alumnos'),
    path('registrar/', alumnoRegistrationView, name='registrar'),
    path('eliminarAlumno/<int:id>',eliminarAlumno),
    path('actualizarAlumno/<int:id>',actualizarAlumno)
]