from django.contrib import admin
from django.contrib.admin.sites import site
from .models import UploadedFile


class UploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

admin.site.register(UploadedFile, UploadAdmin)
