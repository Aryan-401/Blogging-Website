from django.shortcuts import render
from datetime import date
from .models import Post

all_posts = [

]


# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]  # [-3:] doesnt work cuz Django is a bitch
    return render(request, "blog/index.html", {
        "posts": latest_posts
    }
                  )


def posts(request):
    return render(request, "blog/all-posts.html", { "all_posts": all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
