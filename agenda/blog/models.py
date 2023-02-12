from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):   
   description = models.CharField(max_length=200)
   cost = models.PositiveSmallIntegerField()
   date = models.DateTimeField(default=timezone.now)
   start = models.DateTimeField(default=timezone.now)
   end = models.DateTimeField(default=timezone.now)