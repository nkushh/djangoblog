from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.allBlogs, name="index"),
	url(r'^post/(?P<pk>\d+)/$', views.postDetails, name="post-details"),
	url(r'^dashboard/$', views.dashboard, name="dashboard"),
	url(r'^post/(?P<pk>\d+)/detail/$', views.post_details, name="details"),
	url(r'^posts/$', views.posts, name="posts"),
	url(r'^posts/new/$', views.newPost, name="new-post"),
	url(r'^posts/(?P<pk>\d+)/edit/$', views.editPost, name="edit-post"),
]