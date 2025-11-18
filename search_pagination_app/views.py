from django.shortcuts import render
from django.db.models import Q
from .models import Post
from .functions import *


RPP = 10  # Results Per Page


def post(request, pk):
    current_post = Post.objects.get(id=pk)
    context = {"post": current_post, "page": "post"}

    return render(request, "search_pagination_app/post.html", context)


def posts(request):
    all_posts = Post.objects.all()
    new_queryset = pagination(request, all_posts, RPP)
    context = {"posts": new_queryset}  # search_url is none, showing nothing in pagination url

    return render(request, "search_pagination_app/posts.html", context)


def search(request):
    search_query = request.GET.get("q", "")
    search_url = f"&q={search_query}"

    search_results_queryset = Post.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(post__icontains=search_query)
    )

    new_queryset = pagination(request, search_results_queryset, RPP)
    context = {"posts": new_queryset, "search_query": search_query, "search_url": search_url}

    return render(request, "search_pagination_app/posts.html", context)
