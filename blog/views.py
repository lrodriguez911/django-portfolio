from django.shortcuts import render
from .models import Post
# Create your views here.

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request):
    