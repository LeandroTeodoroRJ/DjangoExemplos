from django.shortcuts import render
#from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import ReviewModel

# Create your views here.
class ReviewView(View):
    def get(self, request):  #To GET request
        form = ReviewForm()     #First time load form
        return render(request, 'app_main/pages/home.html', {
            "render_form": form
        })

    def post(self, request): #To POST request
        form = ReviewForm(request.POST)
        if (form.is_valid()):
            form.save()
            return render(request, 'app_main/pages/thank_you.html')
        else:
            return render(request, 'app_main/pages/home.html', {
                "render_form": form
            })

class ThankYouView(TemplateView):  #Render template for GET request
    template_name = "app_main/pages/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Great job!"
        return context

class ReviewListView(ListView):
    template_name = "app_main/pages/review_list.html"
    model = ReviewModel
    context_object_name = "review_template"

    # Return items rating grather than 3
#    def get_queryset(self):
#        base_query = super().get_queryset()
#        data = base_query.filter(rating__gt=3)
#        return data


class SingleReviewView(DetailView):
    template_name = "app_main/pages/single_review.html"
    model = ReviewModel
    context_object_name = "review_template"  #If you not insert this line
                                             #django automactily uses
                                             #the model name with lower case.
