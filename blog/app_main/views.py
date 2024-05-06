from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from .models import Post


# Create your views here.


def starting_page(request):
    #Ordena pela data de forma descendente e retorna os 3 primeiros
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'app_main/pages/index.html', {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'app_main/pages/all-posts.html', {
        "all_posts_template": all_posts
    })

def post_detail(request, slug):
    try:
        single_post = Post.objects.get(slug=slug)
        return render(request, 'app_main/pages/post-detail.html', {
            "single_post_template": single_post,
            "post_tags": single_post.tags.all()  #Retorna a lista de tags
            })
    except:
        #Return page not found - 404 error
        response_data = render_to_string("global/404.html")
        return HttpResponseNotFound(response_data)
