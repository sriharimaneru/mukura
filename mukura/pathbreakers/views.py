from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.conf import settings
from pathbreakers.models import Pathbreaker
import constants
import os
import urllib
import json

# Create your views here.
def getPathbreakerImage(request, pathbreakerId):
  MEDIA_DIR = os.path.basename(os.path.dirname(os.path.abspath(__file__)));
  print request.build_absolute_uri("/")
  try:
    obj = Pathbreaker.objects.get(pk=pathbreakerId)
    print obj.image
    image_url = obj.image.url
    #image_url = "/pathbreakers/default-employer-profile.png"
    print "--------------------"
    print image_url
    if request.is_ajax:
      return HttpResponse(json.dumps({'image': image_url}))
  except:
    raise Http404("media does not exist")
  return HttpResponse('<img src=%s> </img>' %image_url)  

def init(request):
  value = os.system(" pwd")
  print value
  initTemplate = os.path.join(constants.BASE_DIR, "templates/pathbreakers.html")
  Categories = Pathbreaker.objects.order_by('category').values('category').distinct()
  return render(request , "pathbreakers.html", {'Categories': Categories})
