from django.contrib import admin

# Register your models here.
from blogs_.models import BlogPost

admin.site.register(BlogPost)