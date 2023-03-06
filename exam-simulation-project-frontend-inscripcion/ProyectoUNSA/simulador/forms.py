from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Postulante, Examen_Postulante, Examen, Pregunta

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class Examen_PostulanteCreate(forms.ModelForm):
    class Meta:
        model = Examen_Postulante
        fields = '__all__'

class PostulanteForm(forms.ModelForm):
    class Meta:
        model = Postulante
        fields = (
            'Telefono',
            'DNI',
        )
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
class UserForm2(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class ExamenForm(forms.ModelForm):
    class Meta:
        model= Examen
        fields = ("__all__")
class Examen_PostulanteForm(forms.ModelForm):
    class Meta:
        model = Examen_Postulante
        fields = ['Escuela_id', 'Postulante_id']

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ("__all__")