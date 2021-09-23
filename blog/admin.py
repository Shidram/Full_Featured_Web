from django.contrib import admin
from django.db import models
from django.db.models import fields
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','author')

admin.site.register(Post, PostModelAdmin)