from django.shortcuts import render
from django.http import HttpResponseRedirect
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


        #Information from the session, the try blobk is the case session
        #not open (not exist yet)
        request = self.request
        try:
            favorite_id = request.session["favorite_review"]
            if (int(favorite_id) == review_id):
                pass
                context["is_favorite"] = True
            else:
                context["is_favorite"] = False
            return context
        except KeyError as error:
            return context


class AddFavoriteView(View):
    def post(self, request):
        review_user_id = request.POST["review_id"]
        #fav_review = ReviewModel.objects.get(pk=review_user_id)
        request.session["favorite_review"] = review_user_id  #Save only primitive values on the session
        return HttpResponseRedirect("/reviews/" + review_user_id)

    def get(self, request):
        pass
