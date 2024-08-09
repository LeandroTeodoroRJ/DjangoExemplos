from django.contrib.auth.models import User
from django.contrib.auth import forms

# Register your models here.
class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        #Adicionando os fields default mais os fields adicionais
        fields = forms.UserCreationForm.Meta.fields + ('email','first_name','last_name',)

    #Adiciona a classe boostrap em todos os campos do formulário
#    def __init__(self, *args, **kwargs): # Adiciona
#        super().__init__(*args, **kwargs)
#        for field_name, field in self.fields.items():
#            field.widget.attrs['class'] = 'form-control'
