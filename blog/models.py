from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# My Blog App Models
class Post(models.Model):
	author = models.ForeignKey('auth.user')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_on = models.DateTimeField(default=timezone.now)
	published_on = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_on = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text