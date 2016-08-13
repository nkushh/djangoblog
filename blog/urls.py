from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.allBlogs, name="index"),
	url(r'^post/(?P<pk>\d+)/$', views.postDetails, name="post-details"),
	url(r'^dashboard/$', views.dashboard, name="dashboard"),
]