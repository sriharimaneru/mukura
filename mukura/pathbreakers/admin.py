from django.contrib import admin
from . import models


class PathbreakerAdmin(admin.ModelAdmin):
  list_display = ['pathbreaker_id', 'name']
  ordering = ['pathbreaker_id']

# Register your models here.
admin.site.register(models.Pathbreaker, PathbreakerAdmin)
