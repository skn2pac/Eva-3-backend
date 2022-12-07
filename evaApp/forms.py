from django import forms
from evaApp.models import Alumno

class alumnoRegistro(forms.ModelForm):
    
    class Meta:
        model = Alumno
        fields = '__all__'
        
    nombre = forms.CharField()
    apellido = forms.CharField()
    fono = forms.CharField(max_length=10)
    email = forms.CharField()
    direccion = forms.CharField()
    ex_liceo = forms.CharField(required=False)
    carrera = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    fono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    ex_liceo.widget.attrs['class'] = 'form-control'
    carrera.widget.attrs['class'] = 'form-control'



