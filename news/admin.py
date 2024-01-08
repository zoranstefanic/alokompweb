from django.contrib import admin
from .models import *

admin.autodiscover()
admin.site.enable_nav_sidebar=False

class FileInline(admin.StackedInline):
    model = File
    extra = 1

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, FileInline]
    prepopulated_fields = {"slug": ["title"]}
    list_display = ['title','created','published','user']
