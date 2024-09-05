from django.contrib import admin
from blog.models import BlogPost
# Register your models here.


@admin.register(BlogPost)
class blogpostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'timestamp', 'embedding')