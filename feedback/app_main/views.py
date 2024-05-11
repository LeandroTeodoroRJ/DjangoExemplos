from django.shortcuts import render
#from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import ReviewModel

# Create your views here.

def home(request):
    if (request.method == "POST"):       #After send the form
        form = ReviewForm(request.POST)
        if (form.is_valid()):
            #print(form.cleaned_data)     #Return a dictionary with data

            #Saving a simple Form
            #review = ReviewModel(
            #    user_name = form.cleaned_data['user_name'],
            #    review_text = form.cleaned_data['review_text'],
            #    rating = form.cleaned_data['rating'],
            #)
            #review.save()

            #Saving a model form
            form.save()

            return render(request, 'app_main/pages/thank_you.html')

    else:   #GET request
        form = ReviewForm()     #First time load form
        return render(request, 'app_main/pages/home.html', {
            "render_form": form
        })
