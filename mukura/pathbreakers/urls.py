from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
 url(r'^$', views.init),
 url(r'^(.*)/$', views.getPathbreakerImage ), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


