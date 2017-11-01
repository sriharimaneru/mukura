#from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import os
# Create your models here.

class Pathbreaker(models.Model):
  BASEDIR = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
  pathbreaker_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  batch = models.CharField(max_length=5)
  department = models.CharField(max_length=30)
  category = models.CharField(max_length=30)
  sub_category = models.CharField(max_length=30)
  profile_url = models.TextField(default='')
  url_type = models.CharField(max_length = 20, default = '')
  image = models.ImageField(upload_to = 'pathbreakers', default='pathbreakers/default-employer-profile.png')
  description = models.TextField(default='')
  interview_status = models.BooleanField(default=False)
 
  def getImage(_self_):
    return _self_.image;
