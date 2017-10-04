#from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pathbreaker(models.Model):
  pathbreaker_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  batch = models.CharField(max_length=5)
  department = models.CharField(max_length=30)
  category = models.CharField(max_length=30)
  sub_category = models.CharField(max_length=30)
  profile_url = models.TextField()
 # image = models.ImageField()
  
