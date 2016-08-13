from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def allBlogs(request):
	posts = Post.objects.filter(published_on__lte=timezone.now()).order_by('created_on')
	return render(request, 'blog/index.html', {'posts':posts})

def postDetails(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/blog_post.html', {'post':post})

def dashboard(request):
	posts = Post.objects.all()
	return render(request, 'blog/dashboard.html', {'posts':posts})

def newPost(request):
	if method.request=="POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_on = timezone.now()
			post.save()
			return redirect('post_details', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/new_post.html', {'form':form})

def post_details(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_details.html', {'post':post})


def posts(request):
	posts = Post.objects.all()
	return render(request, 'blog/posts.html', {'posts':posts})
