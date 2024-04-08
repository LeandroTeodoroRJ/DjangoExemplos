#from django.forms import Form, ModelForm
from django import forms
from django.contrib.auth.models import User  #Model padrão User do Django


class RegisterForm(forms.ModelForm):  #Classe do formulario
    class Meta:         #Classe para passagem de dados
        model = User    #Aponta o form para o model
        fields = [      #Campos atrelados. Para usar todos os campos fields = '__all__'
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
