from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def home(request):
#    return render(request, 'app_main/pages/home.html')
#    if request.POST:
#        form = RegisterForm(request.POST)
#    else:
    form = RegisterForm()
    return render(request, 'app_main/pages/home.html', {
        'form': form,  #Passando o form para o html
    })
