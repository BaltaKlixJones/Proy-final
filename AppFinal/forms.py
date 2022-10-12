from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AutoFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()

class MotoFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()

class AvionFormulario(forms.Form):
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()

class CamionFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo=forms.CharField(max_length=50)
    color=forms.CharField(max_length=50)
    año=forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)

    class Meta: 
        model= User 
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    username= forms.CharField(label="nombre de usuario")
    email = forms.EmailField(label="Modificar Email")
    descripcion = forms.CharField()
    link = forms.URLField()
    password1 = forms.CharField(label= 'Nueva Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)
    first_name= forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label= "Modificar Apellido")

    class Meta: 
        model= User 
        fields = ['username','descripcion','email','link','first_name', 'last_name', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")


class BlogForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")


