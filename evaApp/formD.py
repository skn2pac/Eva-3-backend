from django import forms
from evaApp.models import Docente


class FormDocente(forms.ModelForm):

    class Meta:
        model = Docente
        fields = '__all__'

    nombre = forms.CharField()
    apellido = forms.CharField()
    fono = forms.CharField(max_length=10)
    anos_exp = forms.IntegerField()
    nivelAcademico = forms.CharField()
    especialidad = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    fono.widget.attrs['class'] = 'form-control'
    nivelAcademico.widget.attrs['class'] = 'form-control'
    anos_exp.widget.attrs['class'] = 'form-control'
    especialidad.widget.attrs['class'] = 'form-control'

