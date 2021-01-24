from django.shortcuts import render
from .models import Post, PostView, Comment, Like


# def post_list(request):
#     qs = Post.objects.filter(status='p')
#     context = {
#         "object_list": qs
#     }
#     return render(request, "blog/post_list.html", context)


# Create your views here.
