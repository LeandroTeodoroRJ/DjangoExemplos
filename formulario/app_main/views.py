from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def home(request):
    form = RegisterForm()
    return render(request, 'app_main/pages/home.html', {
        'form': form,  #Passando o form para o html
    })
