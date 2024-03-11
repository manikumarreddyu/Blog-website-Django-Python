from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)
     author = models.ForeignKey(User, on_delete=models.CASCADE)

     """ 
     auto_now=true -- changes the date every time the post is updated
     auto_now_add = true -- adds date at the time of post creation , can't be updated.
     default=timezone.now -- can update date whenever wanted.  """

     def __str__(self):
          return self.title

     def get_absolute_url(self):
          return reverse('post-detail', kwargs={'pk': self.pk})  # as url of the post-detail expects pk attribute


