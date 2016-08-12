from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def allBlogs(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', {'posts':posts})
