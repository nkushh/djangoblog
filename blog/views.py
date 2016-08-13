from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def allBlogs(request):
	posts = Post.objects.filter(published_on__lte=timezone.now()).order_by('created_on')
	return render(request, 'blog/index.html', {'posts':posts})

def postDetails(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/blog_post.html', {'post':post})
