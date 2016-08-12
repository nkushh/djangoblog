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