from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views import View

from .models import Post
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = "app_main/pages/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts" #Variable name in html file

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]  #Only 3 posts
        return data


class AllPostsView(ListView):
    template_name = "app_main/pages/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts_template" #Variable name in html file

class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "single_post_template": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "app_main/pages/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) #To don't save in database now
            comment.post = post
            comment.save()  #Yes, save now.
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        else:
            post = Post.objects.get(slug=slug)
            context = {
                "single_post_template": post,
                "post_tags": post.tags.all(),
                "comment_form": comment_form,
                "comments": post.comments.all().order_by("-id")
            }
            return render(reuqest, "app_main/pages/post-detail.html", context)



#def post_detail(request, slug):
#    try:
#        single_post = Post.objects.get(slug=slug)
#        return render(request, 'app_main/pages/post-detail.html', {
#            "single_post_template": single_post,
#            "post_tags": single_post.tags.all()  #Retorna a lista de tags
#            })
#    except:
        #Return page not found - 404 error
#        response_data = render_to_string("global/404.html")
#        return HttpResponseNotFound(response_data)
