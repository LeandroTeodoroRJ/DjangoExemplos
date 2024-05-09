from django.shortcuts import render
#from django.http import HttpResponseRedirect

from .forms import ReviewForm

# Create your views here.

def home(request):
    if (request.method == "POST"):       #After send the form
        form = ReviewForm(request.POST)
        if (form.is_valid()):
            print(form.cleaned_data)     #Return a dictionary with data
            return render(request, 'app_main/pages/thank_you.html')

    else:   #GET request
        form = ReviewForm()     #First time load form
        return render(request, 'app_main/pages/home.html', {
            "render_form": form
        })
