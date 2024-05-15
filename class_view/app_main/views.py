from django.shortcuts import render
#from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

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

class ReviewListView(TemplateView):
    template_name = "app_main/pages/review_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = ReviewModel.objects.all()
        context["review_template"] = review
        return context

class SingleReviewView(TemplateView):
    template_name = "app_main/pages/single_review.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]    #Parameter from dynamic url path
        selected_review = ReviewModel.objects.get(pk=review_id)  #pk is the primary key (id field on database)
        context["review_template"] = selected_review
        return context
