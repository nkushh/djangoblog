from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Front-end
def allBlogs(request):
	posts = Post.objects.filter(published_on__lte=timezone.now()).order_by('-created_on')
	return render(request, 'blog/index.html', {'posts':posts})

def postDetails(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/blog_post.html', {'post':post})



# Dashboard
@login_required
def dashboard(request):
	posts = Post.objects.all()
	return render(request, 'blog/dashboard.html', {'posts':posts})

@login_required
def newPost(request):
	if request.method=="POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_details', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/new_post.html', {'form':form})

@login_required
def editPost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_on = timezone.now()
			post.save()
			return redirect('post_details', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/new_post.html', {'form':form})

@login_required
def post_details(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_details.html', {'post':post})

@login_required
def posts(request):
	posts = Post.objects.all()
	return render(request, 'blog/posts.html', {'posts':posts})

@login_required
def allDrafts(request):
	posts = Post.objects.filter(published_on__isnull=True).order_by('-created_on')
	return render(request, 'blog/posts.html', {'posts':posts})

@login_required
def allPublished(request):
	posts = Post.objects.filter(published_on__lte=timezone.now()).order_by('-created_on')
	return render(request, 'blog/posts.html', {'posts':posts})

@login_required
def publishPost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_details', pk=pk)

@login_required
def deletePost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('posts')

def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'blog/login.html')
    else:
        return render(request, 'blog/login.html')

def logUserOut(request):
	logout(request)
