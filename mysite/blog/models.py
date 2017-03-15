from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=50)
	text = models.TextField(default='text description')
	date_created = models.DateTimeField(default=timezone.now)
	date_published = models.DateTimeField(blank=True,null=True)
	
	def publish(self):
		self.date_published = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title
	
